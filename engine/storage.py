"""Offline SQLite migration boundary, not a runtime DB or scan worker."""
from pathlib import Path
import sqlite3


def migrate(db: sqlite3.Connection, migration_dir: Path) -> None:
    if db.in_transaction:
        raise ValueError("Commit or rollback existing writes before migration")
    db.execute("PRAGMA foreign_keys=ON")
    exists = db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='schema_versions'").fetchone()
    applied = {row[0] for row in db.execute("SELECT version FROM schema_versions")} if exists else set()
    for path in sorted(migration_dir.glob("[0-9][0-9][0-9][0-9]_*.sql")):
        version = int(path.name.split("_",1)[0])
        if version not in applied:
            try:
                sql = path.read_text(encoding="utf-8")
                if version == 1:
                    sql = "BEGIN IMMEDIATE;\n" + sql + "\nCOMMIT;"
                db.executescript(sql)
            except sqlite3.Error:
                if db.in_transaction:
                    db.rollback()
                raise
            applied.add(version)
    if db.execute("PRAGMA foreign_key_check").fetchall():
        raise ValueError("Migration left invalid foreign keys")
