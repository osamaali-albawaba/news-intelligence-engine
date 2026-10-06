# Release Map and Gates

Version 1.1 | Proposed baseline | 2026-10-06

## 1. Release policy

The five releases express user outcomes, not isolated technical layers. R1 is implementation-level; R2/R3 are architectural; R4 describes evaluated calibration; R5 is deliberately high level. Dates are learning targets. Release completion is recorded with evidence, limitations and the tested version.

| Release | Value | Principal dependency | Enables |
| --- | --- | --- | --- |
| R1 — Make It Useful | A usable real-shift discovery workflow | Permitted sources; local runtime; verified free AI path for intelligence | R2 research and day-one event history |
| R2 — Make It Smart | Faster defensible differentiation and verification | Stable evidence/recommendations; bounded research acquisition | Rich angle selection and publication lineage |
| R3 — Make It Learn | Know what was recommended, selected, published and observed | Manual article links; compatible authorized performance access | Evaluated outcomes for calibration |
| R4 — Make It Better | Improve recommendations with evidence and owner control | Usable cohorts and frozen prediction history | Organization-specific improvement process |
| R5 — Make It a Product | Adopted newsroom product | Demonstrated personal value and organizational commitment | Broader newsroom/commercial validation |

## 2. R1 — Make It Useful

### Entry

Approved v1.1 planning baseline or explicitly selected R1 subset; Phase 0 alignment documented; known device/runtime facts; first-section definition; proposed source dossiers. Live AI entitlement can remain pending during ingestion slices, but must be validated before R1 intelligence is accepted.

### Features and non-scope

Manual section scan, permitted Arabic/English signals, normalized document versions, exact dedupe and basic event clustering, progressive local dashboard, optional supported angle, score/rationale/risk, source detail, structured feedback, selected/writing state and manual published URL, daily view reset, crash recovery, budgets and baseline event logging.

No deep research, broad social dependence, SEO engine, article writing, automated scheduling, performance connector, SaaS tenancy or CMS write. Basic cross-language clustering is R1; sophisticated language-gap intelligence is R2.

### Required data

R1 entities in CROSS_RELEASE_CONTRACTS, including recommendation/impression IDs and effective configuration snapshots. Do not postpone exposure history until R3.

### Acceptance, DoD and exit

Every mandatory criterion R1-D01–R1-D24 in R1_EXECUTION_PLAN passes. A user can complete the workflow without developer tools. At least three real sessions exercise reuse/error handling and yield at least one useful investigation candidate. Owner records qualitative utility; no fabricated traffic proof. All relevant automated checks pass, restore works, no unapproved cost is required, and limitations are explicit. Exit report records tested commit, sources/provider/config versions, example lineage and unresolved dependencies.

## 3. R2 — Make It Smart

### Objective and scope

Turn a promising recommendation into an evidence-backed, differentiated angle faster than the manual process. Research Room: story research, selected-angle research, question-specific Find Answer, timeline, hidden details, contradictions, unanswered questions, news/social evidence, bilingual coverage gaps and Al Bawaba event/angle coverage. Mature controls, presets, versioned natural-language behavior preview, selected-angle facts/headlines and writing/published workflow refinements.

### Entry and dependencies

R1 usable; immutable evidence and cluster revisions; source access for targeted research; validated provider budget; agreed definition of a useful angle. Research must have an acquisition path, not merely rephrase the existing summary. If web search/grounding is not available free, use permitted known-source collection/manual added evidence and disclose scope. Provider reasoning cannot substitute for source retrieval.

### Data and architecture

Research jobs/artifacts, target questions and answers, timeline events, contradiction links, entity/alias refinements, monitored coverage samples, Al Bawaba matches and config history. Keep research requests separate from scans. Story/angle/question job scope keys prevent duplicate spend. Evidence injection is permitted content, not an arbitrary unrestricted scraper. Translation retains original text and identifiers; research results reference new and reused evidence distinctly.

### Non-scope

Writing editor, broad SEO suite, automatic changes to published content, automated weight learning, paid social dependence or mandatory full-web coverage. Research Topic is an optional R2 candidate after core research works; see backlog.

### Acceptance and DoD

| ID | Criterion |
| --- | --- |
| R2-D01 | Story research adds inspectable material or reports no new useful evidence; does not fabricate completeness. |
| R2-D02 | Angle research is tied to the selected angle and keeps original score/analysis history. |
| R2-D03 | Find Answer returns supported answer, partial evidence or unanswered state with limitations. |
| R2-D04 | Contradictory claims remain visible; inference is not presented as reported fact. |
| R2-D05 | At least one bilingual fixture demonstrates a sampled language gap and ambiguous aliases avoid false merging. |
| R2-D06 | Al Bawaba coverage distinguishes event coverage from angle coverage and meaningful update. |
| R2-D07 | Social evidence fields remain null when unavailable; adapters can fail without breaking research. |
| R2-D08 | Config changes preview, save, one-scan override and restore work; paid capabilities cannot be enabled by natural-language instruction. |
| R2-D09 | Research jobs survive interruption, preserve lineage and enforce per-request/daily budget. |
| R2-D10 | User compares representative real research sessions with the manual workflow and records utility/time and weak-angle cases. |

Exit requires passing applicable criteria with disabled optional adapters listed honestly. Free targeted-research access is a real gate for that feature; a disabled Research button is not a completed research capability. R2 enables explicit selected-angle lineage and fuller event logs for R3.

## 4. R3 — Make It Learn

### Objective and scope

Connect recommendation decisions to observed article outcomes. Discover Marfeel capabilities, implement connector or authorized manual import, ingest historical articles, separate traffic-source metrics, normalize compatible comparisons and produce descriptive reports.

### Entry and dependencies

R1/R2 IDs and event history available; published URLs recorded; authorized sample/export or tested connector access. Full R2 completion is not a hard dependency for importing article metrics: R3 can link story-only R1 recommendations. Do not force research completion before legitimate outcome tracking.

### Capability discovery artifact

Record credentials mechanism without exposing secrets, account entitlement, metric definitions, dimensions, sample query, pagination, time zone, granularity, article matching, attribution, sampling, freshness, corrections, rate limits and failure behavior. The supplied Marfeel field list is a starting hypothesis. Validate native results against a permitted UI/export sample before making comparisons.

### Data and architecture

Connector capabilities; raw import batches; normalized observations; article aliases and link confidence; metric definitions; age-aligned derived aggregates; historical cohorts. Unmatched imported articles remain unmatched instead of attaching to a similar recommendation. Existing URLs and author identities are not inferred to be universal across organizations.

### Non-scope

Autonomous weight adjustment, causal postmortems, generic employee ranking, billing or other-organization ingestion. Search Console/other connectors are optional additions after Marfeel semantics work.

### Acceptance and DoD

| ID | Criterion |
| --- | --- |
| R3-D01 | A real published article is linked back to its original recommendation/score, including story-only cases. |
| R3-D02 | Import/connector replay does not duplicate observations; corrections retain provenance. |
| R3-D03 | Metric values reconcile to an authorized sample using the same metric/window/timezone. |
| R3-D04 | Missing, measured zero and late/unavailable observations are visibly distinct. |
| R3-D05 | Search/Flipboard/social/referral comparisons appear only for supported attribution dimensions. |
| R3-D06 | Historical articles outside the engine retain external origin and cannot fabricate recommendation history. |
| R3-D07 | Comparisons align article age and metric units, exposing section/sample-size limitations. |
| R3-D08 | Failures/backoff/cursors and incremental sync are tested; no credential is committed. |
| R3-D09 | Descriptive reports cover available top/low performers, spikes/long-tail, sections and timing without causal claims. |

Exit: a traceable real recommendation-to-outcome example plus reproducible import/reconciliation evidence. If only manual import is operational, label the release 'outcome tracking via manual import'; do not claim the API connector is complete. Sparse performance data does not imply R4 calibration readiness.

## 5. R4 — Make It Better

### Objective and scope

Use historical evidence to propose and evaluate improvements, not uncontrolled self-learning. Compare frozen rankings with outcomes, diagnose underperformance through hypotheses, propose weight changes and timing/search insights, support accept/reject/activate/rollback.

### Entry and dependencies

Compatible performance cohorts, known selection/exposure history, article-age windows, reliable score/config versions and an editorial evaluation set. No universal minimum article count is invented. On entry, document whether each proposed analysis has adequate cohort size and coverage; suppress unsupported calibration when it does not.

### Architecture

A dataset builder freezes eligible observations and exclusions. A diagnostic process distinguishes known observations from hypotheses. A calibration process proposes bounded alternatives to the baseline. Offline evaluation uses chronological holdout and avoids future-data leakage. A reviewer sees cohort/sample/uncertainty and utility regressions. Accepted proposals create a new active config version. Rejected proposals remain in history. One-step rollback restores earlier effective values with a new activation record.

Use within-section/source-window comparisons first; exploratory correlations do not prove that changing headlines or publication time caused uplift. Writer/assignment effects, distribution and major events may confound results. Long-tail performance must not be judged from a one-hour window. An organization model is not a universal journalism model.

### Acceptance and DoD

| ID | Criterion |
| --- | --- |
| R4-D01 | Original prediction is reconstructed from recommendation-time snapshots, never from a later re-score. |
| R4-D02 | Dataset eligibility/exclusions and measured windows reproduce from a frozen manifest. |
| R4-D03 | Diagnosis labels hypotheses and confidence; incomplete performance causes inconclusive output. |
| R4-D04 | Candidate is compared to unchanged baseline on held-out data and editorial fixtures. |
| R4-D05 | No active config changes without recorded owner approval; rejection is preserved. |
| R4-D06 | Rollback recreates previous effective behavior and does not erase historical recommendations. |
| R4-D07 | Analysis reports selection bias, sparse cohorts and overfitting risks; unpublished items are not zero-traffic failures. |
| R4-D08 | Pilot observation of accepted changes is separated from offline evaluation and includes regressions. |

Exit: demonstrate a real evaluated candidate and approval/rollback path. If evidence is insufficient, report 'calibration deferred' rather than declaring validated improvement. R5 can proceed on personal value without forcing statistically credible automated calibration.

## 6. R5 — Make It a Product

### Objective and scope

After adoption interest, support newsroom organizations, users/roles, journalist profiles, organization-specific intelligence, an independent dashboard and CMS integration. Arabic output, automation, collaboration, possible individual plans, white-labeling and commercial controls are candidates, not a requirement to build every business feature at once.

### Entry

Personal value evidence, Al Bawaba sponsor/permission, operational/data ownership agreement and a hosting/cost decision. The pilot's $0 constraint stays in force until explicitly changed; 'R5' does not authorize spending.

### Architectural preparation

Tenant boundaries in database/cache/files/jobs/connectors; role-controlled access; organization configs; shared versus personal queue decision; CMS-specific adapter; user-controlled publishing; versioned localization; scheduling policy and caps; data export and tenant deletion; evaluated per-organization model activation. Free local pilot infrastructure is not promised sufficient for a commercial service.

### High-level acceptance/DoD

Demonstrate independent organization isolation, profile-specific recommendations, role checks, approved CMS flow and human publication control, operational onboarding/support/export, cost ownership and measurable pilot outcomes. Each enabled optional capability has its own acceptance evidence. Pricing, billing provider, detailed auth/hosting and white-label behavior are TBD on entry, after organizational needs are known. Newsroom subscription is the primary hypothesis; individual subscription remains optional.

## 7. Safe parallel preparation

Historical source/metric discovery may occur read-only while R1/R2 progress. R3 import is separable from rich research, and R5 business validation is separable from R4 calibration. Keep the release sequence as a product map rather than pretending every later release is blocked by every earlier feature. Only implement the currently authorized scope; all cross-release preparatory work must be named explicitly in the handoff.
