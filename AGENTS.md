# AGENTS.md ? News Intelligence Engine

## Objective, authority and current scope

Help the human editor discover strong evidence-supported stories and optional
angles. AI recommends; the journalist verifies, decides and publishes.
User approved planning v1.1 and **R1.0 Foundation Alignment only** on 2026-10-06.
Read all supplied docs/planning files, especially R1_EXECUTION_PLAN and
PHASE_0_ALIGNMENT. Their proposed/review-only language is historical; explicit
current user instructions govern scope. Do not start R1.1, live collection/AI,
scheduled scans, cloud provisioning or paid services without new authorization.

## Architecture and file boundaries

Pilot target: local Python modular monolith/API, one local worker, SQLite, browser
UI (React/TypeScript/Vite proposal). Device sleep accepted; no cloud uptime promise.
Current code is offline foundation only. Worker/D1/OAuth are deferred options.

- engine/contracts.py: typed evidence, adapters/providers and optional angles.
- engine/alignment.py: effective snapshot, section intent/scope and capability guard.
- engine/config.py, config/: sections/audience/sources, manual/scheduled and cost policy.
- engine/cache.py: separate analysis/scoring identities.
- engine/storage.py, migrations/: additive offline database evolution.
- contracts/api.ts, apps/api/boundary.ts: declarations, no running API.
- tests/fixtures/: nonpublishable .invalid synthetic examples and populated v1 data.
- docs/planning/: exactly nine original supplied files; do not casually edit.
- docs/baseline/: starting main archive, hash manifest; preserve for audit/rollback.
- docs/legacy/original-docs-file.txt: unchanged relocated user docs file.
- scripts/check_foundation.py, .github/workflows/ci.yml: offline checks/CI only.

## Workflow and commands

This checkout is C:/Projects/news-intelligence-engine, independent of the AWS
library. Never modify/reuse the AWS evidence repo, origin, backup, code or IDs.
GitHub is source of truth for code/config; runtime data stays local and ignored.
Read ARCHITECTURE, DECISIONS and HANDOFF first. One owner per feature; no concurrent
Codex/Antigravity changes to the same feature. Work on a dedicated reviewable branch.
Check status before synchronization. Preserve unrelated work and Git history; no
force push, hard reset or destructive conflict resolution. Fetch origin safely,
base new tasks on reviewed latest main; never merge/rebase uncommitted user work.

```powershell
python scripts/check_foundation.py
python -m unittest discover -s tests -v
python scripts/check_foundation.py --handoff-base <starting-commit>
npm ci --ignore-scripts
npm run typecheck
```

Python 3.12+, strict TypeScript, explicit statuses, UTC timestamps, application UUIDs
and short transactions. Add dependencies only when needed; pin/lock on installation.
Immutable deployed migrations are never rewritten. Use small feat/fix/test/docs
commits; stage intended paths, test, push dedicated branch to origin and verify SHA.

## Protected invariants

- Four claim types; summary/Why Now/risk/angles need relevant support or explicit
  system-observation basis. ID validation alone never establishes truth.
- Optional angle/story-only score/action/article links. Rumor visibility is distinct
  from verification; no numeric traffic score verifies a claim.
- Unknown social/search/usage/performance stays null/not_measured, never zero.
- Effective configuration, evidence versions, original scores and exposure ranks
  survive reload. Append-only events with idempotency; corrections are new events.
- Compatible section/config joining only; selected section does not run all others.
- Scheduled false, fail-closed capabilities; no paid or unknown-cost fallback.
- Source category/tier/permission/originality separate; no paywall/auth/robots bypass.
- en/ar discovery, English output; The Node taxonomy is unconfirmed. No fixed geography.
- Models replaceable, cache includes extraction/translation/behavior; weights change
  scoring cache without forcing identical AI analysis again.
- Marfeel independent R3 connector. No credentials/cookies/runtime/private data in Git.
- Rights-required deletion must honor source permissions and tombstones, not use
  immutable-history triggers as an excuse to retain forbidden material.

## Mandatory handoff

Before stopping, update HANDOFF.md with exact sections CURRENT STATUS, LAST
COMPLETED TASK, FILES CHANGED, WHAT WORKS, KNOWN ISSUES, NEXT TASK, TEST INSTRUCTIONS.
Record baseline/branch/owner, acceptance evidence, test results/skips, migration,
remaining gates and actual sync/CI status. Run the handoff diff guard. Update
DECISIONS for major changes; retain superseded decisions. Do not claim the entire
R1 release is complete from R1.0 tests. Stop at the next explicit approval gate.
