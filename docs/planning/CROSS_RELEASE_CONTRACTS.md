# Cross-Release Contracts

Version 1.1 | Proposed design | 2026-10-06

## 1. Stability policy

Stable semantics matter more than freezing every field. Add compatible optional fields; version breaking contracts and migrate consumers. UUIDs identify domain records; configured source IDs may be stable human-readable keys. Store UTC ISO timestamps and original timezone metadata where relevant. All payloads carry schema version. Data from sources and models is untrusted input.

Logical lineage:

Source version → raw signal → document version → cluster revision → analysis run → optional angle → score snapshot → recommendation → impression → user event → article link → performance observation → calibration proposal.

Do not store this chain only as mutable JSON on a card. Explicit foreign keys and immutable snapshots make it auditable. One source report may support several statements; one article may derive from several recommendations; a score may exist for a story without an angle.

## 2. R1 entities and minimum retained fields

| Entity | Minimum fields | Identity and history rule |
| --- | --- | --- |
| Workspace context | organization_id, user_id, timezone, active_day | Seed one organization/user; no tenant-management UI. |
| Source configuration version | source_id, version, access method, sections/languages, publisher group, trust/permissions, cost profile, enabled, review time | Keep version used for acquisition; disabling a source preserves prior provenance. |
| Scan request | request_id, user_id, section, freshness, result_limit, settings_snapshot_id, idempotency_key, requested_at | Retry same key returns same operation; changed payload under same key returns conflict. |
| Scan job/run | job_id, run_id, scope_hash, request links, status, attempt, stage, counts, heartbeat, cancellation, errors, timestamps | Shared worker lease; requester and worker attempt are distinct. |
| Raw signal | signal_id, source/version, run_id, external ID/URL, payload/hash, discovered_at, source timestamps, permitted retention | Duplicate observations can reuse content while retaining acquisition occurrences. |
| Document | document_id, canonical_url, aliases, source and publisher provenance | URL is document identity; redirect aliases do not overwrite immutable revisions. |
| Document version | document_version_id, document_id, payload reference, headline, allowed content/snippet, hash, language, access status, published/fetched/updated time, retention | Never overwrite the text used by a prior analysis. |
| Evidence passage | passage_id, document_version_id, original text, locator, content hash, language, permitted storage/transmission, availability | Exact source passage; translation is a separate derived artifact. |
| Entity/alias | entity_id, type, surface alias, language, source provenance, resolution method/confidence | MBS/name aliases do not automatically merge ambiguous people. |
| Cluster/revision | cluster_id, revision_id, event description, actor/action/location/time, member version IDs, change reason, timestamps | Revision membership immutable; merge/split maps preserve old lineage. |
| Analysis run | analysis_id, cluster_revision_id, request/snapshot hash, provider/model, prompt/schema/config IDs, created_at, validation, limitations, usage | Append runs; cached reuse links to original run, not a fabricated new AI execution. |
| Statement/support | statement_id, analysis_id, text, kind, attribution, support/contradiction/context passage IDs | At least one relevant support is application-validated; contradiction alone is not support. |
| Angle | angle_id, analysis_id, text/category, rationale, evidence links, support status | Optional, not mandatory for a story. Revised angle creates a new version/ID link. |
| Score snapshot | score_id, subject_type, subject_id, formula/config ID, components/status/basis, overall/index, confidence, coverage basis | Subject may be story revision or angle; never rewrite score presented earlier. |
| Recommendation | recommendation_id, cluster_revision_id, optional angle_id, analysis_id, score_id, section, config IDs, created_at, Why Now, risk/status, evidence references | A displayed editorial proposal, distinct from cluster and angle. |
| Impression | impression_id, recommendation_id, user_id, session/day, displayed_at, rank, sort/filter, render/status version | Persist actual exposure; do not log every poll as a new unique exposure. |
| User event | event_id, user/org, recommendation_id, impression_id, optional angle/score, type/reason, created_at, request key | Append-only, idempotent; later corrections use a compensating event. |
| Article/link | article_id, canonical URL, publication/record time, author/section where known, link edges to recommendations/angles, confirmed by | Manual link in R1; many-to-many, no automated authorship inference. |
| Configuration snapshot | config_id/hash, schema, profile/version, effective settings, weights, prompts, source-set ID, created_at/parent | Full effective settings preserved; a version label alone is insufficient. |
| Usage ledger | call_id, job/analysis, provider/project/model, requested/actual tokens if known, quota reservation, cost status/basis, time | Unknown usage/cost is null; cost guard checks occur before external calls. |

Do not implement R2–R5 tables merely to fill the diagram. R1 must implement the minimal rows it actually produces and keep extension-compatible identifiers. Single-organization defaults prepare lineage; they are not proof of tenant isolation.

## 3. R1 schema adaptation

The existing migration already includes sources, jobs, raw items, documents, clusters, analyses, passages, statements, angles, score snapshots, feedback, written articles and performance observations. Its strongest invariants should remain. Required design changes:

1. Add immutable document versions. Existing `documents.content_hash` and `permitted_text` represent one mutable article record; existing passage links cannot alone preserve all updates.
2. Add cluster revisions and membership versions. Current `cluster_documents` points to document identity only.
3. Add recommendation and impression identity. Current API Opportunity ID has no corresponding recommendations table.
4. Make story-level score/recommendation possible. `score_snapshots.angle_id`, feedback and written article links currently require an angle; a null angle must be a valid story workflow.
5. Add structured events and article linkage. Existing feedback enum is only good/bad/saved/rejected/written and cannot represent exposure, opening, selections or detailed skip reasons reliably.
6. Preserve full configuration/source-set snapshots. `audience_version` is not enough to reproduce full behavior; user settings currently overwrite preferences.
7. Add section-aware scope and temporal states. Current scan request contains only an idempotency key, and global job scope cannot blindly join News and Business scans.
8. Add metric-definition/window provenance before R3. Existing performance rows lack explicit unit, attribution source and import dedupe key.

If migration 0001 has been applied anywhere, append reviewed migrations rather than editing it. Even if only synthetic databases exist, prefer additive changes to preserve test coverage and migration history. Tests must create databases from zero and migrate a populated v1 fixture. Future incompatible redesign is allowed only with explicit exported baseline and import/rollback verification.

## 4. SourceAdapter and acquisition contract

Input: source configuration version, cursor, section/freshness intent, maximum items, run identity and permitted access policy. Output: typed signals, next cursor, source observations and sanitized errors. Items and a partial error can coexist. Commit cursor only after item persistence. Conditional fetch metadata and rate limits are source-specific. A 304 response records successful revalidation, not new content.

Canonicalization strips only known tracking parameters; it must not remove IDs or language variants that change content. Preserve raw URL and redirect chain. Exact hashes suppress duplicate storage; syndication provenance prevents ten copies from being treated as ten independent corroborations. Same URL with changed text creates a new revision, not a new unrelated article.

## 5. Scan/API contract

### POST /api/scans

Request: `schema_version`, `idempotency_key`, `section`, `freshness_hours`, `result_limit`, optional `profile_id`, validated one-scan overrides. Server sets user/org, resolves defaults and records effective config. Response: job/request IDs, status, joined_existing, effective settings, requested time, human-readable message. Acceptance is asynchronous; no promise of instantaneous AI output.

Same requester/key and same payload replay the first response. Same key with different payload is a conflict. Identical active scope may join. A different section/config does not silently join an incompatible job; queue behind the single worker or return a visible queued state. A future Scan All uses child section scopes, not three copies of an unbounded scan.

### GET /api/scans/{id}

Return queued/running/completed/partial/failed/cancelled, current stage, attempted/successful/failed sources, signal/cluster/opportunity counts, created/updated results, collection and analysis timestamps, limitations and sanitized failures. Counts distinguish reused cached analyses from new model calls. Do not expose credentials or raw provider error bodies.

### GET /api/opportunities

Filter by section/day, sort and result state; paginate. Return snapshot-consistent card projections with optional angle, nullable score, score status, evidence confidence, verification label, Why Now, risks, source/origin counts, publication/discovery times and analysis completeness. Stable ordering uses score then freshness then stable ID. Unscored candidates use an explicitly separate provisional ordering.

### GET /api/opportunities/{id}

Return the recommendation snapshot, exact supporting evidence, source-specific details, available angles and limitations. A newer analysis is discoverable without replacing the earlier snapshot invisibly.

### POST /api/events and POST /api/articles

Events use client-generated retry keys and validated enums. Article creation validates HTTP(S) URL without automatically fetching arbitrary user URLs. Duplicate URL creates a link to the existing article rather than duplicate performance identity. Manual publication time can be unknown. A user can link a story without choosing an angle.

### Configuration operations

GET current profile; POST preview/save new version; POST restore as new active version. A one-scan override must never overwrite the default. No configuration endpoint can activate a paid provider or weaken non-negotiable evidence rules without a separately approved capability change.

## 6. Job and restart semantics

A single local worker claims durable queued jobs in a transaction and obtains an ownership token. Network/AI work runs outside database locks. Save bounded stage checkpoints and source outcomes. On restart, mark stale running attempts interrupted and safely resume/retry according to stage semantics. Unknown model-call completion must not be retried repeatedly without consuming the bounded call budget. Persist call intent before dispatch and reconcile when possible.

Cancellation is cooperative: stop dispatching new work; retain already committed results. Cancellation does not imply that an external provider call was never charged. Device sleep/offline states produce clear paused/stale indicators. No scheduler is required to rescue queued jobs; local startup/worker handles recovery. Future scheduled triggers use the same domain jobs with automation disabled during pilot.

## 7. AIProvider contract and reproducibility

Input: permitted evidence passages with IDs, cluster revision, audience/behavior snapshot, prompt template/hash/version, output schema, budget. Output: summary with claim support, Why Now support/system-observation basis, typed statements, zero-or-more angles, risks, limitations and provider/model metadata. Record token/usage data when available. No prompt instruction asks the model to invent sources or prove global novelty.

Validate parse/schema, references, attribution, allowed states, and semantic relevance before trusted display. An unknown reference is rejected; retry at most once under reserved budget for a recoverable formatting failure. Repeated malformed output is a visible failure, not an unvalidated JSON display. Source pages cannot override system instructions or invoke tools.

Cache analysis on evidence snapshot, extraction/translation versions, provider/model, prompt/schema and effective audience/angle behavior. Cache scoring separately on analysis and scoring/config versions. Changing weights should not require an identical evidence analysis call. New evidence or a substantive cluster revision invalidates relevant analysis. Preserve exact historical analysis even if later cache entries supersede it.

## 8. Measurement and scoring semantics

Metrics carry `status`, nullable `value`, `basis`, `observed_at` and methodology/units. UI score components may use 0–100; performance observations retain native nonnegative units and do not use the score bounds. Distinguish measured, estimated and not_measured. Unknown cost can use an explicit unknown status outside metric schemas.

Required missing weighted components withhold aggregate. Optional unavailable components remain null and unweighted. Confidence does not compensate for novelty and traffic does not establish credibility. Do not label a rumor 'publish-ready'; the product has no automated editorial approval state.

Coverage samples identify monitored sources, window, independent origins, observed language counts, angle matches and acquisition limitations. An Arabic/English gap is relative to that sample, not the entire news web. Angle eligibility for investigation differs from verified reporting eligibility.

## 9. R2 extension contracts

ResearchJob: ID, request type (story/angle/question), recommendation/cluster/angle/question target, budget/config, status/checkpoints and outcome. ResearchArtifact: summary/answer/timeline/contradictions and evidence snapshots; analysis provider metadata. A question can be unanswered; absence of an answer is not a model error.

TimelineEvent links multiple source claims and conflicting times. Contradiction links explicit statement IDs and evidence with unresolved/resolved state; never manufacture a resolution. CoverageMatch links an Al Bawaba document/version to event and angle with method, confidence and review status. External-link disappearance updates availability, preserving permitted original provenance.

BehaviorInstruction stores original text, parsed bounded change, preview, user acceptance, active config ID and restore parent. Research cannot silently mutate the original recommendation or active default profile.

## 10. R3–R5 extension contracts

Performance observation: article ID, connector/account, native metric definition/version, traffic attribution, window/timezone, value/status/unit, source record/import key, ingestion time, sampling/revision flags and provenance. Connector capabilities explicitly enumerate supported dimensions, granularity and limitations. Identical import replay is idempotent; corrected data creates a revision.

CalibrationProposal: ID, organization, data snapshot/cohort, baseline/candidate config, methodology/evaluation versions, holdout results, uncertainty, explanation, approval state/actor/time, activation and rollback links. Candidate does not become active on creation.

R5 organization/user/membership/role dimensions enforce isolation at query, cache, jobs, files and connectors, not only in URLs. Article history and model versions remain scoped. CMSAdapter supports approved read context and user-confirmed links initially; publishing remains a human CMS operation. Automated scanning adds trigger policies and per-org budgets without a second intelligence pipeline. Billing/white-label implementation stays TBD.

## 11. Retention, deletion and export

Daily workspace rollover is only a view operation. Cache/discovery retention is source-aware and configurable; the old 30-day proposal is not a blanket final policy. Long-lived feedback and published/performance history are learning assets. Referenced evidence is retained only when permitted; where expiry mandates removal, record a tombstone and visibly mark the analysis no longer fully inspectable. Do not keep forbidden full text because a foreign key references it.

Export portable database/content manifests with schema/config/prompt versions, source restrictions and hashes. Restore preserves IDs, lineage and pending-job safety. Git backups must not carry credentials or real newsroom data. Append-only workflow history means corrections are events; it does not prevent an eventual authorized organization deletion policy in R5.
