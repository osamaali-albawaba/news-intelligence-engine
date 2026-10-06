# Architecture Risk Review and Open Decisions

Version 1.1 | 2026-10-06

## A. Critical changes before coding resumes

| Risk | Concrete current evidence | Required response | Severity |
| --- | --- | --- | --- |
| Remote-first drift | ARCHITECTURE D1/Worker/Actions versus latest local-first decision | Align runtime/doc/config; hosted deployment optional | High |
| Latent scheduling | scheduled.enabled=true and validator requires both triggers | Disable automation and revise validator before live execution | High |
| Missing free AI capability | Protocol exists; no provider/key/entitlement verified | Test actual free-only project/model and quotas before R1.3 | Blocking for intelligence |
| Mandatory angle suppresses valid stories | SQL score/feedback/article require angle; scoring eligibility requires angle | Story recommendation identity and nullable angle | High |
| Rumors silently excluded | confidence minimum 70, supported-angle requirement | Separate visibility/verification; explicit rumor lead handling | High |
| Evidence versions lost | URL identity stores one content; membership references document | Immutable document versions and cluster revisions | High |
| Day-one measurement incomplete | feedback enum does not capture impressions/open/select | Recommendation and exposure IDs/events in R1 | High |
| Score reproducibility incomplete | mutable user prefs; version label without full effective settings | Immutable config/source/prompt snapshots and original rank | High |
| Scan intent missing | ScanRequest only retry key; global scope | section/window/count/settings and compatible join semantics | High |
| Misleading numeric score | provisional weights and no historical calibration | Relative experimental index; no probability/pageview claim | High |
| Research UI conflict | R1 card includes Deep Research, R1 non-scope excludes it | Show only enabled actions; R2 feature gate | Medium |
| Verification conflation | internal supported state differs from requested verification labels | Map documented evidence support and editorial verification separately | High |
| Retention versus history | immutable history needs permission-aware removal | Tombstones and explicit unavailable evidence status | High |
| SQL migrations break invariants | current tests use positional inserts and old enums | Migration fixtures, explicit-column test inserts, protected invariant tests | Medium |
| Expensive backend-first delay | earlier vertical slices postpone real UI | Minimal usable local scan screen in R1.1 | Medium |

## B. Risks during use

Weak source selection can make technically correct code editorially useless: review yield, language/section diversity, timeliness and independent origins. Evaluate clustering false merges before polished ranking. Do not confuse small monitored samples with global originality.

AI reasoning cannot discover current facts without an acquisition channel. Deep research must actually collect or accept permitted evidence and disclose its scope. Valid evidence IDs can still be semantically unrelated. Editorial review and fixtures test support, not just schema shape.

Missing search/social signals are unknown rather than low performance. A fixed base formula avoids incomparable dynamically renormalized scores. High apparent precision should not mask provisional inputs. Scoring can surface rumor leads without claiming they are verified.

Free APIs may change access/quota, and grounding/tools may have separate charges. Fail closed on paid/unknown modes. Do not interpret provider-used-for-training acceptance as a blanket permission to send confidential Marfeel data or source material lacking AI-transmission rights. Keep private performance local by default; review permissions before sending aggregates externally.

Learning has selection bias: the journalist chooses what is published; missing outcomes and unpublished recommendations do not equal zero views. Large events, distribution, timing and article age confound comparisons. R4 must retain unchanged baselines, chronology and sample/cohort limitations.

Local downtime is acceptable, data loss is not desirable. Daily rollover must survive sleep; backup must preserve IDs and demonstrate restore. A copy on the same disk does not solve device loss. Keep runtime artifacts and secrets out of Git even while repository is public.

## C. Open-decision register

| ID | Decision | Needed by | Default/safe path | Evidence to close |
| --- | --- | --- | --- | --- |
| O01 | Actual OS, Python/Node, RAM/disk and launch workflow | R1.1 | Local lightweight pipeline, no GPU assumption | Device/runtime inspection |
| O02 | The Node editorial inclusion/exclusion rules | Three-section R1 exit | No assumed tech taxonomy | Owner definition/examples |
| O03 | Approved first sources and body/excerpt rights | R1.1 | Reviewed compact batch, others disabled | Source dossiers/sample acquisition |
| O04 | Free API/provider/model entitlement and quotas | R1.3 | Disabled until tested; no paid fallback | Actual project-level request and quota/billing check |
| O05 | Baseline workload and pilot success thresholds | R1 utility review | Record actual sessions; five stories/shift unconfirmed | Baseline notes/owner targets |
| O06 | Workspace reset timezone | R1.2 | Proposed Asia/Amman; UTC storage | Confirm chosen profile setting |
| O07 | Confidence rubric/index bands/initial weights | R1.3 | Small transparent provisional base formula | Fixture/editorial review, not guessed calibration |
| O08 | Source-aware retention and off-device backup destination | R1.5 | Retain only permitted evidence; local export | Rights/storage review and restore proof |
| O09 | Free targeted research/search access | R2 | Known permitted sources/manual evidence with limits | Capability test; no imaginary full-web search |
| O10 | Marfeel account capabilities, metric definitions, API/export | R3 | Authorized manual import if available | Sample query/export reconciliation |
| O11 | Adequate calibration cohorts and methodology | R4 | Descriptive results until supportable | Dataset manifest, coverage/holdout review |
| O12 | Shared versus personalized newsroom queues | R5 | No assumed assignment rules | Al Bawaba workflow discovery |
| O13 | Roles, CMS adapter, hosting/data ownership | R5 | Independent dashboard, manual publishing | Sponsor requirements and cost decision |
| O14 | White-label, pricing, individual plan and positioning | R5 business validation | Deferred; newsroom subscription hypothesis | Usage evidence, competitor/pricing research |
| O15 | Organization/private data transmission policy | Before private performance goes to AI | Local processing/aggregates, no automatic transmission | Organization authorization and provider terms |

No new batch of discovery questions is needed to write this plan. Open decisions are resolved at the relevant gate, not by inventing answers. O01–O04 are practical execution facts, not reasons to delay all planning.

## D. Decisions safe to defer

Specific cloud provider/database, distributed execution, OAuth/SSO, enterprise roles, final model-training approach, billing implementation, white-label, final pricing/name, international expansion and detailed R4/R5 task lists. Keep interfaces portable, avoid speculative implementations. Source/provider access cannot be deferred past the slices that use them.

## E. Readiness verdict

**READY WITH CHANGES** for R1.0 alignment and bounded source implementation once gates are met. **NOT READY** to claim operational free AI, completed R1 or a calibrated traffic predictor. The current foundation is testable but has no live collectors, model calls, scan endpoint or dashboard. The critical issues are manageable; they do not justify an 80-phase plan.

## F. Exact next action

After owner approval of the baseline, engineering starts the R1.0 task brief in R1_EXECUTION_PLAN. Preserve independent Git history and pass migration/config/contract checks. End with a handoff and the exact first-source prerequisite. This planning package does not itself modify main or provision services.

## G. External capability check

Official pages opened on 2026-10-06:

- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing — free API tier exists for selected models with limits; content-use policy differs by tier. This establishes a candidate path, not the user's account entitlement or sustained capacity.
- Gemini API billing: https://ai.google.dev/gemini-api/docs/billing — verify the actual project/tier before calls. Consumer subscription is not accepted here as proof of free API access.
- SQLite WAL: https://www.sqlite.org/wal.html — concurrent reads/writes can improve local UI behavior; there remains a single writer and same-host WAL constraints.
- SQLite backup: https://www.sqlite.org/backup.html — consistent snapshot backup is a supported design; arbitrary live-file copy is not the proposed method.

Provider model names, quota amounts and hosted free-tier prices are deliberately not frozen into the plan. Recheck official pages and the account before activation. No external market/competitor research was performed because the user deferred it.
