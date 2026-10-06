# Phase 0 Alignment Review

Reviewed tree: `99533963972c9e303a9c947ab77998a98b1b14d7`  
Repository: https://github.com/osamaali-albawaba/news-intelligence-engine  
Date: 2026-10-06 | Review only; remote files unchanged

## Verified review

All 29 files were retrieved through GitHub at the reviewed tree. The original v1.0 attachment was read in full including tables. Offline snapshot checks passed: `python scripts/check_foundation.py`; `python -m unittest discover -s tests -v` — 18 tests passed. Tests were executed from the snapshot's project directory; an initial invocation from its parent failed Python import resolution and was corrected. No product code was changed to make tests pass.

TypeScript checking and current GitHub Actions status were not independently rerun in this review. HANDOFF reports a successful earlier CI run; that is historical evidence, not a claim about the current run. No live source/provider/cloud/CMS/Marfeel capability was tested. Repository metadata now reports public visibility with connector read access and no push permission, superseding HANDOFF's historical private-repo description.

## File and decision disposition

| Area | Disposition | Rationale/action |
| --- | --- | --- |
| Independent repository and parent-repo isolation | KEEP | No news-engine work should modify or reuse the AWS evidence repository. |
| Python typed adapter/provider interfaces | KEEP + extend | Useful boundaries; add effective config, section and optional-angle/story semantics. |
| Four statement kinds and passage references | KEEP + strengthen | Good provenance baseline; summary and Why Now need their own support, and references do not prove entailment. |
| Nullable metrics and scoring history | KEEP | Avoid fake zero; maintain snapshots and confidence separately. |
| Configurable categories/tiers/audience | KEEP | No fixed source cap or inferred geography. Add initial en/ar discovery and section profiles. |
| Cache key | KEEP + extend | Existing model/prompt/evidence/audience dimensions useful; add extraction/translation/behavior versions and separate score cache. |
| SQLite-compatible migration | KEEP + migrate | Strong foundation. Add document/cluster revisions, recommendations/impressions, optional angle, snapshots and action/article edges. |
| Source example | KEEP synthetic; ADD real dossier separately | `.invalid` example is not a live source. |
| Jobs/idempotency/lease model | KEEP + change scope | Global join cannot combine incompatible section/config scans. Local worker rather than remote dispatch. |
| `config/scan.json` scheduled.enabled=true | CHANGE | Explicit false during personal pilot; current execution_enabled=false prevents execution today but is an unsafe latent default. |
| `engine/config.py` requires both triggers true | CHANGE | Must permit manual enabled/scheduled disabled and capability-based execution policy. |
| 120-second runtime and numeric call budgets | REVIEW | Initial proposals; separate interactive UI from total scan time and measure actual constraints. |
| Supported-angle-required and confidence minimum 70 | CHANGE | Conflicts with useful story/no-angle and visible labeled rumor leads. Separate investigative visibility from evidence verification. |
| API ScanRequest only idempotencyKey | CHANGE | Add section/freshness/count/effective profile scope. |
| API Opportunity angle:string | CHANGE | Nullable best angle; explicit recommendation/score/impression IDs and temporal state. |
| Feedback enum and SQL angle-required references | CHANGE | Need detailed reasons, opening/exposure/selection and story-only publication linkage. |
| Document canonical URL unique with mutable content | CHANGE | Keep canonical identity, add immutable content versions. |
| Source failure fields | EXTEND | Track last failure/code/time and acquisition observations, not only last success. |
| SQL future performance table | KEEP boundary; defer filling | Add native metric/window/dimension/import identity before R3 usage. |
| Cloudflare Worker/D1 deployment | DEFER | Optional hosted runtime; not a local-first requirement. |
| GitHub Actions live processing/hourly cron | DEFER | CI is useful; scheduled news processing conflicts with manual pilot. |
| OAuth/remote cross-device runtime | DEFER | Loopback local session adequate for initial pilot; remote access needs separate decision. |
| React/Vite browser stack | KEEP proposal | UI not implemented; minimal view starts R1.1, not only after all backend layers. |
| 10–20 browser results | CHANGE | Up to ten per section by default, no padding. |
| Old technical phases 1–9 | REPLACE map, preserve history | Use five product releases and six R1 slices. |
| Synthetic fixtures/offline CI/handoff guard | KEEP + grow | Protect useful invariants; tests must evolve with intentional contract changes. |
| `package-lock.json` absent | ADD on actual dependency installation | Lock reproducible dependency set; do not claim locked runtime today. |
| README/ARCHITECTURE/DECISIONS/ROADMAP/HANDOFF/AGENTS | ALIGN before coding | Local-first/manual-only, current source of truth, accurate permissions/status and approved task. |

## Proposed decision updates

D001: GitHub remains code/config source of truth; original private intent and temporary public access are recorded separately. Public visibility is not a SaaS or credential-storage decision. Restoring private visibility is optional owner choice after connector access is arranged.

D002/D003: supersede remote pipeline + D1 as the pilot default with local Python worker + local API + local SQLite. Preserve Worker/D1 as future options, not mandatory dependencies.

D004: retain shared job semantics for future triggers, disable scheduled execution and key active scopes by compatible section/config rather than unconditional global joining.

D009: retain null/missing withholding but use a usable R1 base formula; do not require unmeasured future dimensions.

D013: strengthen append-only feedback and score snapshots with recommendation exposure, full config and optional-angle article linkage.

New records should explain why, what changes, migration implications, test evidence and rollback. Existing records are superseded rather than rewritten as if the old decision never occurred.

## Reuse versus rebuild verdict

Reuse is preferable because source/provider boundaries, evidence semantics, database checks and tests already work. Permission to rebuild removes a constraint; it does not supply a reason to discard these assets. If the implementer chooses a clean replacement, preserve tree/fixtures/test report and map every protected invariant to the replacement. No existing runtime database has been provided; do not claim no production data exists anywhere merely because repository files are synthetic.
