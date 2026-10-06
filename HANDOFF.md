# Handoff

## CURRENT STATUS

Phase 0 foundation completed and validated. Phase 1 is not authorized. Owner:
Codex; no concurrent feature owner. Independent Git repository on branch master
under the AWS evidence workspace.
GitHub origin not configured: awaiting the user's separate repository URL.

## LAST COMPLETED TASK

Created architecture documentation, SQL schema, source and AI-provider contracts,
manual/scheduled scan contracts, configurable audience/source/scoring/budgets,
synthetic fixtures, tests, CI and handoff enforcement. All 18 offline tests passed.
Foundation checker passed configuration, handoff, Python syntax, JSON, SQLite
migration integrity and obvious-secret screening. No live service was contacted.

## FILES CHANGED

Initial project files: README.md, ARCHITECTURE.md, ROADMAP.md, AGENTS.md,
HANDOFF.md, DECISIONS.md, .env.example, .gitignore, .gitattributes, pyproject.toml, package.json,
tsconfig.json; engine/contracts.py, engine/cache.py, engine/config.py,
engine/__init__.py; config/*.json; contracts/api.ts; apps/api/boundary.ts;
apps/dashboard/README.md; prompts/README.md; migrations/0001_foundation.sql;
tests/test_foundation.py, tests/fixtures/synthetic_cluster.json;
scripts/check_foundation.py; .github/workflows/ci.yml.
No parent repository files or evidence records changed.

## WHAT WORKS

Offline Python contracts and configuration; schema intended for SQLite/D1;
synthetic evidence validation; nullable metrics; cache invalidation dimensions;
database constraints for overlap/idempotency, attribution and append-only feedback.
No real collectors, providers, endpoints or application UI are implemented.

## KNOWN ISSUES

- Node/npm were not found on PATH or common installation paths; local TypeScript
  typecheck could not run. CI is configured to run it, but CI has not executed.
  package-lock.json is not generated yet; create/review it when npm is available.
- No cloud deployment, D1 remote verification, credentials or live-source permission review.
- No separate GitHub origin yet; local commit does not establish GitHub synchronization.
- Free-tier timing/AI quotas are best effort and need measurement before live operation.
- Referential evidence validation does not assess factual truth or semantic entailment.

## NEXT TASK

Push the completed local foundation commit only to the separate origin when
supplied; never push it to the AWS evidence repository. Commit identity is available
with `git log -1 --format=%H` (not embedded here to avoid a self-referential hash).
Stop for explicit Phase 1 approval. After approval, implement permitted collectors
and shared scheduled/manual job execution; no AI or dashboard until later phases.
Recheck service quotas and access terms before enabling live use.

## TEST INSTRUCTIONS

From this project directory: `python scripts/check_foundation.py` and
`python -m unittest discover -s tests -v`. For TypeScript: install Node.js 22+
and run `npm install --ignore-scripts`, then `npm run typecheck`.
Before subsequent commits: `python scripts/check_foundation.py --handoff-base <starting-commit>`.
All Phase 0 tests use synthetic data and no external services.
