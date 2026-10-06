# AGENTS.md — News Intelligence Engine

## Objective and scope

Build a personal evidence-first editorial opportunity engine, not a headline
aggregator. Human editor decides and publishes. Current authorization is **Phase 0
only**. Do not implement real collection or later phases without user approval.

This is an independent Git repository. Run all commands from this directory.
Never stage, modify, pull, commit or push the parent AWS evidence repository.
Never reuse its origin or backup remote for this project.

## Architecture and module ownership

- `engine/`: Python source/provider contracts, configuration validation and cache identity.
- `apps/api/`: future small TypeScript Cloudflare Worker boundary.
- `apps/dashboard/`: future React/Vite browser interface.
- `contracts/`: TypeScript wire contracts; keep semantics aligned with Python.
- `config/`: versioned source categories/tiers, audience, scan budgets and weights.
- `migrations/`: immutable reviewed SQL migrations; D1/SQLite compatible.
- `prompts/`: versioned AI prompt rules.
- `tests/fixtures/`: clearly synthetic, nonpublishable examples using `.invalid` URLs.
- `scripts/check_foundation.py`: offline checks and optional Git handoff-change guard.
- `.github/workflows/ci.yml`: tests and contract checks only; no collection schedule.

Read ARCHITECTURE.md, DECISIONS.md and HANDOFF.md before changing a feature.
Do not have two agents modify the same feature concurrently. Record feature
ownership and current task in HANDOFF.md; use separate branches if needed.

## Coding conventions

Python 3.12+, standard library for foundation, typed dataclasses and Protocols;
TypeScript strict mode. Use UUIDs at application boundaries and UTC ISO timestamps.
Prefer explicit statuses and structured errors. Keep I/O outside core logic.
Add dependencies only for a demonstrated need; pin and lock before runtime use.
Use small commits with `feat:`, `fix:`, `test:` or `docs:` prefixes.

## Commands

```powershell
git status --short
git pull --ff-only origin main
python scripts/check_foundation.py
python -m unittest discover -s tests -v
npm install --ignore-scripts
npm run typecheck
```

Pull only when origin exists, the working tree is safe, and the tracked branch is
confirmed. Initial bootstrap has no remote until the user supplies the separate
repository URL. Stop and report sync conflicts; never force push, hard reset or
discard another agent's work. Stage explicit project paths only. Test stable work,
commit, push to origin and verify the remote commit. Do not claim push success
without confirmation. Phase 0 may be committed locally while remote is pending.

## Invariants: do not casually change

1. Facts, attributed claims, interpretation and possible consequences remain distinct.
2. Every angle/statement has inspectable evidence support; references alone do not prove truth.
3. Unavailable social/search/performance metrics are `not_measured` and null, never zero.
4. Source category and tier are independent; neither guarantees confidence.
5. Audience geography, topics and language are configurable; no fixed regional bias.
6. Scheduled and manual scans share idempotency, budgets and overlap protection.
7. Models are replaceable behind AIProvider; never silently use a paid fallback.
8. Cache identity includes content, audience, provider/model, prompt and schema versions.
9. Marfeel is optional and independent; no credential scraping or insecure login automation.
10. Never bypass paywalls, authentication, robots restrictions or technical controls.
11. Never commit keys, credentials, cookies, tokens, private keys or `.env` files.
12. No automatically published articles, invented sources, fabricated measurements,
    or guarantees that an angle is globally unique.
13. Migrations already deployed must not be rewritten; append a new migration.
14. Feedback remains append-only; preserve recommendation/score history.

## Mandatory handoff before stopping

Every coding agent must update HANDOFF.md with these exact sections:
CURRENT STATUS, LAST COMPLETED TASK, FILES CHANGED, WHAT WORKS, KNOWN ISSUES,
NEXT TASK, TEST INSTRUCTIONS. Record test results, unavailable checks, ownership,
Git synchronization status and the next approval gate honestly.

Run `python scripts/check_foundation.py --handoff-base <starting-commit>` before
committing subsequent tasks. It rejects changed work without a changed HANDOFF.md.
CI enforces this on pull-request and push diffs after bootstrap. Update DECISIONS.md
for major architecture changes. A handoff must stand alone without chat history.
