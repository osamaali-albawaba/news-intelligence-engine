"""Offline config, syntax, schema, secrets and handoff checks; no collection."""
import argparse
import hashlib
import zipfile
import ast
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from engine.config import validate_config  # noqa: E402
from engine.storage import migrate  # noqa: E402

HANDOFF_SECTIONS = (
    'CURRENT STATUS', 'LAST COMPLETED TASK', 'FILES CHANGED', 'WHAT WORKS',
    'KNOWN ISSUES', 'NEXT TASK', 'TEST INSTRUCTIONS',
)


def validate_handoff(text: str) -> None:
    for section in HANDOFF_SECTIONS:
        if f'## {section}\n' not in text:
            raise ValueError(f'Missing handoff section: {section}')
        body = text.split(f'## {section}\n', 1)[1].split('\n## ', 1)[0].strip()
        if not body:
            raise ValueError(f'Empty handoff section: {section}')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--handoff-base', help='Git commit before this task (include working tree changes)')
    parser.add_argument('--handoff-head', default=None, help='Optional committed head for CI diff')
    args = parser.parse_args()
    validate_config(ROOT / 'config')
    manifest = json.loads((ROOT / 'docs/baseline/manifest.json').read_text(encoding='utf-8'))
    files = list((ROOT / 'docs/planning').glob('*.md'))
    if len(files) != 9 or {p.name for p in files} != set(manifest['planning_sha256']):
        raise ValueError('Expected exactly nine approved planning Markdown files')
    for path in files:
        if hashlib.sha256(path.read_bytes()).hexdigest() != manifest['planning_sha256'][path.name]:
            raise ValueError('Approved planning bytes changed: ' + path.name)
    archive = ROOT / 'docs/baseline' / manifest['archive']
    if hashlib.sha256(archive.read_bytes()).hexdigest() != manifest['archive_sha256']:
        raise ValueError('Archived main baseline changed')
    validate_handoff((ROOT / 'HANDOFF.md').read_text(encoding='utf-8'))
    for path in ROOT.rglob('*.py'):
        if not any(part in {'.venv', 'node_modules'} for part in path.parts):
            ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    for path in [ROOT / 'package.json', ROOT / 'tsconfig.json',
                 *list((ROOT / 'tests/fixtures').glob('*.json'))]:
        json.loads(path.read_text(encoding='utf-8'))
    with sqlite3.connect(':memory:') as db:
        migrate(db, ROOT / 'migrations')
        assert db.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
        assert not db.execute('PRAGMA foreign_key_check').fetchall()
    # Obvious-secret screening, not a claim of comprehensive security auditing.
    patterns = [r'AKIA[0-9A-Z]{16}', r'ASIA[0-9A-Z]{16}',
                r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                r'gh[pousr]_[A-Za-z0-9]{30,}', r'AIza[A-Za-z0-9_-]{30,}']
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(p in {'.git', '.venv', 'node_modules', '__pycache__'} for p in path.parts):
            continue
        if path.name == '.env' or (path.name.startswith('.env.') and path.name != '.env.example'):
            continue  # ignored local configuration is not a source artifact
        if path.suffix == '.zip':
            with zipfile.ZipFile(path) as archive:
                content = '\n'.join(archive.read(name).decode('utf-8') for name in archive.namelist() if not name.endswith('/'))
        else:
            content = path.read_text(encoding='utf-8')
        if any(re.search(pattern, content) for pattern in patterns):
            raise ValueError(f'Possible secret detected in {path.relative_to(ROOT)}; value withheld')
    if args.handoff_base:
        command = ['git', 'diff', '--name-only', args.handoff_base]
        if args.handoff_head:
            command.append(args.handoff_head)
        names = subprocess.check_output(command, cwd=ROOT, text=True).splitlines()
        if not args.handoff_head:
            names += subprocess.check_output(
                ['git', 'ls-files', '--others', '--exclude-standard'], cwd=ROOT, text=True
            ).splitlines()
        if names and 'HANDOFF.md' not in names:
            raise ValueError('Changed work requires an updated HANDOFF.md')
    print('PASS: configuration, handoff, Python syntax, JSON, all migrations, approved baseline hashes, obvious-secret screening')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, sqlite3.Error, subprocess.CalledProcessError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
