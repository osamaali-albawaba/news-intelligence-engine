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
