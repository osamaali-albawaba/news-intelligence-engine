# News Intelligence Engine

An evidence-first editorial opportunity engine: discover, understand, find optional
angles, score and recommend. The journalist verifies, chooses and publishes.

## Approved baseline and current authorization

Planning **v1.1** is the approved baseline by the owner's explicit request on
2026-10-06. All nine supplied files are preserved byte-for-byte in
[docs/planning](docs/planning/README.md). Their original "proposed"/"review only"
headers remain archival text; the current user approval establishes authority.
Only **R1.0 ? Foundation Alignment** is authorized and implemented here.
Read [R1_EXECUTION_PLAN](docs/planning/R1_EXECUTION_PLAN.md) and
[alignment checklist](docs/R1_0_ALIGNMENT_CHECKLIST.md).

R1 pilot design is local Python API + single local worker + SQLite + a browser UI
(proposed React/TypeScript/Vite). It is manual-only. Hosted Workers/D1, remote
processing, OAuth and scheduled scans are future options, not pilot requirements.
No launcher, API server, real collector, live AI provider, dashboard or dispatcher
is implemented or activated in R1.0. R1.1 requires a new explicit authorization.

## Offline checks

Requires Python 3.12+ and Git; no Python dependencies or credentials needed:

```powershell
python scripts/check_foundation.py
python -m unittest discover -s tests -v
python scripts/check_foundation.py --handoff-base 0900eaf
```

For TypeScript contracts, Node 22+ and npm:

```powershell
npm ci --ignore-scripts
npm run typecheck
```

CI only validates code/contracts; it has no live scan trigger. Runtime files never
belong in Git. Production use will eventually be a normal local browser workflow,
with the device awake; R1.0 does not claim that workflow already exists.

## Configuration

- `config/sections.json`: News, Business, The Node; 24/48/72-hour intent; up to ten.
  Section definitions remain pending, particularly The Node. en/ar discovery,
  English output; timezone proposal Asia/Amman remains owner-confirmable.
- `config/audience.json`: no fixed geographic/topic bias.
- `config/sources.example.json`: disabled synthetic source; category/tier/provenance
  separate; arbitrary registry size. No live-source permission dossier exists yet.
- `config/scan.json`: manual-on, scheduled-off, local runtime, execution and all
  live capability flags false. Foundation intent validation does not create jobs.
- `config/scoring.json`: provisional fixed story-compatible formula; missing
  weighted inputs withhold aggregate. Social/search are not measured, never zero.
- `.env.example`: local placeholders only; credentials stay server-side and ignored.

## History and migration

Original migration 0001 and Git history are retained. Additive migration 0002
preserves IDs and legacy rows, adds immutable versions/configuration, story-only
recommendations, exposure/events and article link edges. Unknown legacy settings
are marked incomplete; historical impressions are not fabricated.
`docs/baseline/` contains the archived starting main and hash manifest. The user's
previous file named `docs` is preserved unchanged at
`docs/legacy/original-docs-file.txt` to allow the requested directory.
No owner runtime database has been supplied or migrated by this task.

See [ARCHITECTURE](ARCHITECTURE.md), [ROADMAP](ROADMAP.md), [DECISIONS](DECISIONS.md),
[AGENTS](AGENTS.md) and [HANDOFF](HANDOFF.md) before continuing.
