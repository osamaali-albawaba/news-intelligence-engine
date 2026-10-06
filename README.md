# News Intelligence Engine

Find evidence-supported editorial opportunities a human editor might miss:
**discover → understand → find angles → score → recommend**.
The editor makes the final decision. The engine never publishes articles.

## Current status

Phase 0 only: repository foundation, configuration, database migration, Python
adapter/provider contracts, TypeScript browser/API contracts, synthetic fixtures,
offline tests, and agent handoff checks. **No live sources, AI calls, scheduler,
SCAN NOW endpoint, dashboard, or cloud deployment exists yet.**

Scheduled collection and manual SCAN NOW are designed to share one bounded,
idempotent job system. Missing metrics remain `not_measured` with `value: null`.
The audience is configurable and not geographically hardcoded.

## Run offline checks

Requires Python 3.12+ and Git. No Python packages or API keys are needed.

```powershell
python scripts/check_foundation.py
python -m unittest discover -s tests -v
```

Optional TypeScript contract check requires Node.js 22+ and npm:

```powershell
npm install --ignore-scripts
npm run typecheck
```

The first npm install generates `package-lock.json`; review and commit it before
adding runtime dependencies. CI also checks the TypeScript contracts. Production
usage will require only a browser; these tools are for development.

Do not run these commands from the parent AWS evidence repository. Enter this
project's directory first. Its Git history is independent.

## Configuration

- `config/audience.json`: regions, languages, interests, exclusions, output language.
  Empty lists mean unrestricted, not a default Middle East profile.
- `config/sources.example.json`: scalable source registry, category, tier,
  publisher provenance, permissions, polling and priority. Every example is disabled.
- `config/scan.json`: both triggers, budgets and cooldowns. Execution is disabled.
- `config/scoring.json`: all metric names, proposed weights, missing-data policy.
- `.env.example`: names only; copy to an ignored `.env` when deployment starts.

No credentials are needed for Phase 0. Do not configure paid services yet.

## Next phase

Phase 1 is blocked on explicit user approval. Then verify source permissions,
configure cloud resources, and implement collection. Refer to [ROADMAP.md](ROADMAP.md).
For cross-agent continuation read [AGENTS.md](AGENTS.md), [HANDOFF.md](HANDOFF.md),
[ARCHITECTURE.md](ARCHITECTURE.md), and [DECISIONS.md](DECISIONS.md).
