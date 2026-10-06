# Decisions

| ID | Date | Decision | Reason |
| --- | --- | --- | --- |
| D001 | 2026-10-06 | Independent private repository | News engine must not share evidence-library history, files or remotes. |
| D002 | 2026-10-06 | Python remote pipeline, small TypeScript API, React/Vite dashboard | Keep laptop-independent processing and browser use; avoid free Worker CPU limits for heavy tasks. |
| D003 | 2026-10-06 | D1 with SQLite-compatible migrations | Managed SQL persistence, portable local tests, bounded personal-project cost. |
| D004 | 2026-10-06 | Common queued job model for manual and scheduled scans | SCAN NOW is essential; idempotency and overlap control avoid duplicate spend. |
| D005 | 2026-10-06 | Categories, tiers and permissions are separate source attributes | Scales beyond initial source list without conflating content type with trust. |
| D006 | 2026-10-06 | Configurable, initially unrestricted audience | No permanent international/Middle East assumption. |
| D007 | 2026-10-06 | Four statement kinds plus passage references | Distinguish facts, claims, interpretation and conditional consequences. |
| D008 | 2026-10-06 | Provider protocol and explicit cache identity | Models can change; changed evidence/audience invalidates analysis. |
| D009 | 2026-10-06 | Missing values stay null; withhold scores with missing weighted inputs | Unknown social/search data must never masquerade as zero. |
| D010 | 2026-10-06 | Marfeel optional future connector | MVP remains useful without performance access. |
| D011 | 2026-10-06 | Foundation uses dependency-free Python tests, synthetic fixtures only | Phase 0 is fully testable without credentials or real collection. |
| D012 | 2026-10-06 | No live cron/dispatch/provider implementation in Phase 0 | Honor explicit scope and stop for Phase 1 approval. |
| D013 | 2026-10-06 | Append-only feedback and versioned score snapshots | Later learning must compare what was actually recommended with outcomes. |
| D014 | 2026-10-06 | CI validates handoff changes and offline contracts | Codex/Antigravity continuation must not rely on chat context. |


## v1.1 alignment decisions ? 2026-10-06

Original D001-D014 above are preserved as historical records. These updates
supersede their active assumptions; archived main and unchanged planning bytes
are identified in docs/baseline/manifest.json.

| ID | Decision / supersession | Why and migration impact |
| --- | --- | --- |
| D015 | v1.1 approved by direct user request; R1.0 only | Attachment headers retain their historical proposed wording; current approval authorizes alignment, not all releases. |
| D016 | Supersedes D002/D003: local Python API/worker and SQLite pilot | No mandatory cloud cost/company resources; Worker/D1 remain future options. Add 0002 without editing 0001. No runtime launcher in R1.0. |
| D017 | Supersedes D004/D012 trigger assumptions: manual-only, scheduled false | Compatible section/config scopes retain future shared-job semantics. No GitHub live dispatch or scheduler. |
| D018 | Extends D006: News/Business/The Node, en/ar acquisition and English output | All editorial section definitions require confirmation. No inferred generic technology taxonomy or geography. |
| D019 | Supersedes angle-required eligibility; extends D007/D009 | Zero angles and labeled rumor leads valid; story scores, events and manual URL edges work without angle. Null/verification semantics preserved. |
| D020 | Extends D008/D013: immutable versions/config/recommendation/impression lineage | Historical settings/exposure must not be invented. Migration preserves IDs and flags legacy config incomplete. Separate analysis and scoring cache. |
| D021 | Supersedes old 10-20 target/technical phase map | Up to ten per selected section; no padding. Five releases, six R1 slices; UI starts R1.1. |
| D022 | Archive baseline and preserve file named docs under docs/legacy | Needed to create docs/planning without losing unrelated user work; planning files copied byte-for-byte and hash checked. |
| D023 | Runtime/exports/backups ignored, loopback session planned | Git holds no newsroom runtime data. Actual privacy checked separately; no OAuth/hosting introduced. |

Evidence: offline config/migration/contract acceptance tests and TypeScript CI.
Rollback: review branch before merge; original Git tree and archive remain intact.
For a migrated owner DB, use a verified pre-migration backup; no destructive reverse
migration is provided, and no owner database was touched in this task.
