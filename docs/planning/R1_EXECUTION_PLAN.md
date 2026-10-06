# Release 1 Execution Plan — Make It Useful

Version 1.1 | Proposed implementation scope | 2026-10-06

## 1. Goal and authorization

Select News, Business or The Node → SCAN NOW → receive real grouped opportunities progressively → understand Why Now and an optional supported angle → inspect sources → record a decision and, when applicable, a published URL.

This document plans work; it does not claim live runtime implementation exists. Planning was authorized. Actual repository synchronization and live capability activation should be reflected in an explicit engineering task/handoff. No phase name authorizes recurring spend.

## 2. Scope

Manual selected-section scans; 24/48/72-hour freshness; up to ten results; source registry; bilingual acquisition and basic clustering; document/cluster history; cached evidence-linked intelligence; versioned relative scoring; compact dashboard/basic detail; structured feedback, selected/writing state/manual publication link; exposure/action logs; timezone-aware daily view; cost/source isolation and local recovery.

Deferred: research room, story/angle/question research, paid/restricted social dependence, SEO engine, writing editor, automated collection, Marfeel connector, CMS, multi-user login, Arabic output and hosted infrastructure. Do not activate hourly scheduling because an old configuration says enabled.

## 3. Dependency gates

| Gate | Needed before | Evidence | If unresolved |
| --- | --- | --- | --- |
| G01 Local environment | Runtime slice | OS, Python/Node availability, disk/RAM, startup constraints | Plan remains valid; launcher/AI capacity provisional. No hardware purchase assumed. |
| G02 Section profile | Section routing | News/Business rules; The Node definition | Implement first confirmed section; do not mislabel unknown scope. |
| G03 Source access | Live adapter | Reviewed source dossier and representative permitted content | Disabled source; smaller permitted batch. No bypass. |
| G04 Free AI capability | Useful intelligence | Account/project/model, billing disabled or verified free-only mode, request/limit test, data policy | Continue raw discovery slice; R1 intelligence cannot be called done. |
| G05 Baseline/editorial rubric | Utility evaluation | Comparable manual session notes and angle/usefulness rubric | Operability can be tested; business-success conclusion withheld. |
| G06 Backup destination | Pilot history reliance | Successful export and restored sample; owner-controlled destination | Local recovery possible; device-loss risk remains explicit. |

G04 is not solved by provider abstraction. Existing subscriptions do not prove API entitlement. If free API analysis is unavailable, a manual export/import using existing subscriptions can be designed as a separately labeled assisted experiment; it is not a transparent substitute for the intended integrated scan. A local model is another candidate only after hardware and editorial quality are tested.

## 4. Vertical slices

### R1.0 — Align and preserve the foundation

**Outcome:** one coherent local-first baseline with contracts that do not block future lineage.

Tasks: record main commit; archive baseline; keep typed evidence and null semantics; replace remote-first assumptions with local runtime boundaries; disable scheduled flag; add section/freshness/count request fields; make angle optional; specify recommendation/impression/config history; write additive schema migrations and v1-to-v1.1 tests. Update ARCHITECTURE, ROADMAP, DECISIONS, AGENTS and HANDOFF in a reviewable change. Retain old decisions as superseded records, not deleted history.

Acceptance: configuration explicitly accepts manual-on/scheduled-off; disabled capabilities do not create requests. Story-only recommendation and feedback persist. Immutable versions and effective config survive a synthetic reload. Existing data fixture migrates with unchanged original IDs; no remote service is called. No code from a parent evidence repository is touched.

Deliverable: alignment checklist, migrations/contracts and passing offline checks. Dependencies: supplied repo/docs. Estimate remains TBD after runtime inspection; no arbitrary deadlines.

### R1.1 — First real signal through a minimal usable screen

**Outcome:** choose the first confirmed section, trigger a local scan and inspect real permitted signals and sources.

Tasks: implement local launcher/API and durable single-worker job; create minimal dashboard tab/scan/progress/list; first source adapter and registry loading; source failure isolation, conditional requests, timeouts/backoff, item budgets; normalized URLs/times/languages; signal/document-version persistence. Grow the approved batch to include Arabic and English plus independent origins. Preserve source excerpts honestly when full body is unavailable.

Acceptance: UI works without developer tools; one source timeout does not abort others; progress is stored and visible; a replayed request does not re-collect unnecessarily; source cursor advances only after persistence; partial results remain visible. No score/angle is fabricated in this slice: raw candidates are explicitly 'not yet analyzed'.

Dependencies: R1.0, G01–G03. Integration demonstration: real scan → normalized rows → source link. This is genuinely vertical; do not postpone all UI until R1.4.

### R1.2 — Dedupe, event memory and temporal correctness

**Outcome:** repeated scans refine an event list rather than dump the same feed again.

Tasks: canonical URL/content dedupe; revision detection; entity aliases including bilingual fixtures; bounded basic event clustering; separate same-person/different-event cases; independent-origin counts; cluster revisions; NEW/SEEN/UPDATE behavior; settings/day rollover projection. Add a reviewable merge/split correction path internally without a complex admin console.

Acceptance: same content twice creates no new event card; unchanged existing card stays SEEN and remains visible; changed article at same URL produces a preserved version and meaningful update where justified; syndicated copies do not increase corroboration as independent origins; Arabic/English same event can group; same person at unrelated events stays separate. Midnight while asleep resets view at next startup without deleting saved/history rows.

Dependencies: R1.1. Demo: two repeated scans and one updated report; original source/evidence content still inspectable.

### R1.3 — Evidence-backed opportunity intelligence

**Outcome:** selected clusters become explainable editorial opportunities within a validated free budget.

Tasks: permitted body/excerpt selection; cheap shortlist; AIProvider registry and free-only policy; structured request/output and semantic evidence checks; summary/Why Now/risk labels; optional best angle/no-angle state; per-story and angle scores; cached analysis and separate scoring cache; usage reservations; immutable recommendations and impression capture.

Start with one bounded cluster call containing selected evidence and a capped output. Do not run a separate expensive agent for every score component. A valid model output is not treated as truthful solely because JSON parses. Allow one bounded repair retry where useful; do not recursively research failed candidates.

Acceptance: a real candidate produces an inspectable recommendation; important claims and Why Now use relevant passage/system-observation references. Zero-angle result works. Unknown evidence reference, unsupported inference and attributed-claim-without-speaker are rejected or withheld from trusted display. Quota failure leaves other/cached results visible. No paid provider fallback occurs. Score shows index/status/confidence and complete snapshot metadata.

Dependencies: R1.2, G04. Without G04, stop at a disclosed raw-discovery pilot; do not report full R1 usefulness achieved by synthetic AI fixtures.

### R1.4 — Full pilot decision workflow

**Outcome:** the complete three-section interface supports real editorial decisions.

Tasks: approved compact cards, sorted/paginated incremental results, basic story/evidence detail, settings defaults/one-scan overrides, verified section routing, structured feedback, saved views, selected angle/story, Mark as Writing and manual article URL link. Add exposure/open/action idempotency and stable recommendation rank history. Hide Deep Research until R2.

Acceptance: selected section does not run all others by default; browser stays interactive during the scan; preliminary and fully scored states differ; source links open originals; unmeasured metrics are not shown as zeros; unsupported sort options do not mislead; structured reasons persist; story-only publication linking works; settings saved/restored without code edits. A new scan keeps valid old cards until replaced, and retains SEEN history within the day.

Dependencies: R1.3 plus complete section definitions. Baseline user sessions may begin earlier; this slice improves the working interface rather than unveiling it for the first time.

### R1.5 — Repeated use, recovery and evidence of utility

**Outcome:** the pilot can be used repeatedly without manual database repair.

Tasks: crash/restart recovery, cancellation, source/provider error panels, budget exhaustion, stale/offline states, retention enforcement/tombstones, ignored runtime files, backup/export/restore, relevant CI and handoff, baseline/pilot session review. Run performance checks using a representative fixture and real measured scan sizes; record memory/DB growth and UI interaction behavior. No new 30-second scan SLA.

Acceptance: completed/partial scans and committed recommendations survive restart; stale ownership cannot duplicate final writes; queued work has an honest state; export restores IDs and action history; sources/models remain bounded; user completes three sessions and records useful and weak suggestions. Known gaps are in the release report.

Dependencies: R1.4, G05/G06. Three sessions establish initial usability, not a validated traffic model.

## 5. Processing budget and error matrix

Provisional starting limits, not provider entitlements: manual scans only; one active worker; per-source/item/document byte limits; bounded host concurrency; maximum candidate clusters per scan; maximum input/output tokens per call; per-scan/day call ceilings; bounded retries and daily manual cooldown. Carry forward existing numeric budgets only after measuring actual source volume and available quotas. Its 120-second total runtime limit and 15 calls/day are proposals, not a SLA or a confirmed optimum.

Enforce a budget ledger before every dispatch. Cached reads do not require AI. Smaller source/candidate batches should be the first response to quota pressure. Pricing/quota knowledge must be specific to project/model/tool; a token-only cap cannot bound unknown search/grounding charges. A paid mode requires approved monthly monetary cap, service list, fail-closed usage controls and concrete owner sign-off. No billing is activated during this task.

| Failure | Required behavior |
| --- | --- |
| Source timeout/HTTP/rate limit | Record sanitized source error, retry/backoff within bounds, preserve other sources. |
| Full text inaccessible | Use permitted snippet if sufficient; mark access limitation; never pretend body was read. |
| No source succeeded | Scan failed with reasons; keep cached cards visibly stale. |
| No relevant items | Successful empty scan with section/window summary. |
| One AI candidate fails | Candidate remains pending/failed analysis; continue other candidates within budget. |
| Quota exhausted | Stop new calls; show budget state and cached/unanalyzed candidates. |
| Malformed/unsupported AI output | Reject or bounded repair; no unvalidated claims displayed as verified. |
| Required score input missing | Nullable aggregate and reason; provisional ordering separate. |
| Disk full/database failure | Fail safely, do not advance cursor or claim completion; preserve earlier transactions. |
| Sleep/restart | Interrupted attempt state and safe resumption; no duplicate recommendations/events. |
| Request replay/overlap | Same scope joins/replays; different scope queues visibly. |
| Evidence expires/disappears | Retain permitted provenance/tombstone; mark inspection limitation. |

## 6. Release Definition of Done

All mandatory rows require evidence, not a checkbox based on code presence.

| ID | Mandatory acceptance criterion | Proof |
| --- | --- | --- |
| R1-D01 | Start locally and scan each configured section from a normal browser without editing code | User-flow demonstration |
| R1-D02 | Real approved Arabic/English sources, provenance and access limits recorded | Source dossiers and one real run |
| R1-D03 | One failing source does not fail the whole scan | Adapter timeout integration test |
| R1-D04 | Progressive committed results and visible incomplete states; responsive UI | Incremental scan demonstration |
| R1-D05 | URL/content duplicates collapse and syndication does not fake corroboration | Deterministic fixtures |
| R1-D06 | Bilingual same-event grouping and different-event separation work | Curated clustering fixtures |
| R1-D07 | Re-scan keeps SEEN cards without relabeling unchanged stories NEW | Repeat-scan test |
| R1-D08 | Same URL substantive update preserves versions and can surface UPDATE | Temporal fixture |
| R1-D09 | Daily rollover uses workspace timezone without deleting learning/saved history | Sleep/midnight test |
| R1-D10 | Summary/Why Now/risk and optional angle grounded in inspectable evidence | Real candidate review and validation tests |
| R1-D11 | Zero useful angles is valid; clearly labeled rumors can remain visible | No-angle and rumor fixtures |
| R1-D12 | Score index, missingness, confidence, formula and original snapshot retained | Scoring/config snapshot tests |
| R1-D13 | Compact dashboard/basic detail and source links match enabled R1 capabilities | UI review; no active research button |
| R1-D14 | Freshness/count defaults and overrides work without code edits | Settings flow test |
| R1-D15 | Structured skip/save/open/select/writing/publication events persist idempotently | Event replay and database checks |
| R1-D16 | Story without angle can link to published URL, preserving recommendation identity | Lineage integration test |
| R1-D17 | No unapproved cost or silent paid fallback; actual free capability documented | Provider capability test and budget tests |
| R1-D18 | No secrets/runtime data in Git or browser build | Ignore rules, sanitized logs, relevant screening |
| R1-D19 | Counts, times, stage/source/model errors and usage status inspectable | Run report |
| R1-D20 | Crash/restart/cancel/overlap behavior preserves committed work | Recovery tests |
| R1-D21 | Backup restores IDs, config and actions; device-loss limitation stated | Restored sample and integrity checks |
| R1-D22 | Unit/contract/integration/UI smoke and initial editorial fixtures pass | Relevant test report/CI |
| R1-D23 | Architecture/roadmap/decision/agent/handoff docs describe actual behavior | Repository document review |
| R1-D24 | Three real pilot sessions, at least one useful candidate, baseline/quality notes and limits recorded | Owner pilot report |

No aggregate pass compensates for failed evidence, cost or security criteria. Disabled optional features stay deferred. Fully automated research/performance are not required in R1, but lineage and manual article linking are.

## 7. Initial evaluation set

At minimum: exact duplicate, syndicated copy, same URL update, bilingual same event, same named person/different event, unknown publication time, rumor/single-source, no useful angle, saturated event with genuinely new angle, unsupported consequence, contradictory claims, quota/source failure and restart. Synthetic fixtures are clearly nonpublishable `.invalid` examples. Live editorial review separately checks relevance and whether support actually entails the claim.

Measure clustering false merges/splits, duplicated cards, unsupported angle rate and useful-candidate rate on reviewed samples. Avoid brittle tests that demand a specific model wording. Prompt/provider changes run the same fixtures; promising output still needs human review. Grow to the future 50–100 historical scenarios gradually rather than blocking first usage.

## 8. Observability and handoff

Each run records section, effective configuration, source results, raw/reused items, document/cluster revisions, analysis/cache hits, scored/unscored/displayed candidates, stage duration, external-call count, known/unknown usage, budget-stop and error codes. Logs cannot include tokens/cookies/private data by default. Logging is local and bounded; no paid monitoring requirement.

Each slice handoff states completed acceptance IDs, exact test commands/results, known limitations, migration/config changes, synchronization state and next authorized task. Follow existing mandatory handoff sections. Commit coherent changes on an isolated reviewable branch; do not begin the next slice just because an agent has time remaining.

## 9. First engineering task brief

**Task:** R1.0 baseline alignment only. Read the package and current repo, capture main commit, update local-first/manual-only documentation and configuration semantics, propose additive lineage/optional-angle contracts, implement migration and configuration tests. Preserve existing foundation behavior except documented supersessions. No real source calls, AI requests, cron, D1/Worker deployment or paid fallback. End with passing offline checks and a reviewable handoff identifying R1.1 prerequisites.
