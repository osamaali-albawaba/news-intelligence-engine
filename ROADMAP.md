# Roadmap

## Phase 0 — foundation

Deliver documentation, configurable audience/source/scanning/scoring structures,
SQL schema, provider/adapter contracts, synthetic fixtures, offline tests, CI,
Git isolation and agent handoff validation. No cloud provisioning or live calls.
Approval gate: stop after checks, handoff, commit and authorized primary push.

## Phase 1 — collection (requires user approval)

Review several sources individually for access, retention and AI-transmission
permissions. Implement RSS and official-source adapters, bounded extraction,
normalized storage, conditional fetches and per-source failure isolation. Add
scheduled and manual job execution on the same pipeline; test permissions,
idempotency, lease recovery and source fairness. Initially expose manual runs
through `workflow_dispatch`; browser SCAN NOW arrives with the private dashboard.
Configure D1 and runner access only when needed. No AI analysis yet.

## Phase 2 — clustering

Exact duplicate suppression plus reviewed event grouping. Include difficult
same-entity/different-event and syndicated-report tests. Preserve provenance.

## Phase 3 — evidence-linked AI angles

Implement provider registry and first authorized provider, structured validation,
cost funnel, quotas, cache, contradiction handling and semantic support review.
No unsupported claim becomes established fact. Analyze accessible bodies.

## Phase 4 — opportunity scoring

Implement versioned weights, missing-metric withholding, eligibility gates,
timestamped coverage samples and relative traffic estimates. Evaluate against
editorial usefulness, not only score stability.

## Phase 5 — browser MVP

Private GitHub login; 10–20 opportunities when sufficiently supported. Show story,
angle, rationale, alternatives, score, freshness, coverage, confidence and sources.
Include filters, progress-aware SCAN NOW, saved/rejected/good/bad/written feedback,
and article URL recording. Verify cross-device persistence and stale-data states.

## Later phases

6. Authorized social/trend adapters. Missing metrics remain not measured.
7. Article-performance linkage and permitted manual imports.
8. Independent Marfeel connector if account entitlement permits it.
9. Personalized learning with evaluated predictions, outcomes, selection bias,
   and editorial safeguards. Never treat missing performance as zero traffic.

MVP acceptance: reduces story-discovery effort; supported angles have inspectable
evidence; failures and limited coverage are visible; feedback survives devices;
processing runs remotely; costs are capped. No automated publishing.
