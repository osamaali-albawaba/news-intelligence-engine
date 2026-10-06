# Architecture ? approved v1.1 / R1.0 foundation

## Authority and runtime boundaries

User-approved v1.1 planning lives in `docs/planning/`; original attachment bytes
are retained. This document describes R1.0 implementation, not a claim that R1
runtime features exist. The former remote-first design is archived at starting
main 0900eafefd8fa8829e45a64923755f48afd220e7 and superseded in DECISIONS.md.

Pilot target: modular Python monolith, small loopback HTTP boundary, one durable
local worker, local SQLite, and local browser UI. React/TypeScript/Vite remains
proposed. FastAPI is a candidate for R1.1, not an installed dependency or selected
locked runtime today. Bind to 127.0.0.1 and require local session/Origin validation
before mutations. No OAuth, company AWS, remote worker or cloud requirement.
The device must be awake for work; old cross-device/continuous uptime goals are
future capabilities. Storage/execution/auth boundaries remain replaceable.

GitHub holds code, approved plans, config templates and synthetic fixtures. It
never holds runtime newsroom data, credentials or performance exports. Current
visibility must be verified from the remote, not inferred from old handoffs.

## Implemented offline boundaries

| Module | R1.0 implementation |
| --- | --- |
| engine/config.py | Validate manual-on/scheduled-off, all capabilities disabled, sections and weights |
| engine/alignment.py | Immutable effective JSON capture, scan intent and compatible-scope hashes, fail-closed capability guard |
| engine/contracts.py | Adapter/provider protocols; four claim kinds; zero-or-more angles; summary/Why Now support |
| engine/cache.py | Analysis evidence/model/prompt/audience/extraction/translation/behavior key; separate score key |
| engine/storage.py | Offline ordered migrations; no runtime DB startup |
| migrations/0002_local_lineage.sql | Additive version/recommendation/impression/event/article lineage |
| contracts/api.ts | v2 wire declarations, optional angle and separate snapshot/impression/verification identities |
| scripts/check_foundation.py | All migrations, planning/archive integrity, handoff, source screening |

No HTTP handler, scan queue admission/execution, network acquisition, model call,
clustering, scoring computation, UI, retention worker or cloud setup is added.
Capability checks must precede future dispatch; changing a provider environment
variable cannot authorize a disabled capability. Offline tests prove guard refusal,
not functioning live integrations.

## Scan intent and future local execution

POST /api/scans contract carries schema version, retry key, section, freshness
24/48/72, integer result limit 1-10 and optional profile. Future boundary resolves
and persists full effective settings, user/org and settings defaults/overrides.
One-scan overrides never mutate saved defaults. Current capture contains audience,
source configuration, scoring, capability/budget and section settings.

Identical requester/key with identical normalized intent/config replays the prior
response; a different payload under the same key is a conflict. Compatible section,
window/count/profile/config scopes may join. Incompatible scopes queue behind one
worker; never silently join News and Business. Hash contracts are implemented;
transactional admission, conflict response and worker recovery belong to R1.1.
Legacy global-scope jobs remain legacy data, not eligible for blind joining.

Future worker: short SQLite transactions, durable lease/ownership token, bounded
network work outside locks, checkpoints, cancellation and restart recovery. API
returns request/job IDs immediately and UI polls committed progress. No scheduler
or GitHub dispatch rescues jobs in the local pilot. No total scan-latency SLA.
Manual intent can be configured while execution is still disabled in R1.0.

## Evidence, versioning and optional angles

Preserve reported fact, attributed claim, editorial interpretation and possible
consequence. Summary/Why Now need known supporting passages or explicitly labeled
system observations for Why Now. Risk statements use the same typed support.
Reference validation establishes provenance only; semantic entailment, documented
verification and actual acquisition rights remain R1.3 work and human review.

Angle count may be zero. Story-level score/recommendation/action/article linkage
must work without an angle. Rumor leads may be visible with UNVERIFIED or SINGLE
SOURCE labels; confidence does not grant factual truth. User labels VERIFIED,
REPORTED, SINGLE SOURCE, UNVERIFIED, ORIGIN UNKNOWN are separate from machine support
states supported/needs_review/unconfirmed/not_analyzed. No automated publish-ready
state or minimum confidence threshold suppresses all investigative leads.

Canonical URL identifies a document. Immutable document versions preserve exact
allowed text; cluster revisions freeze membership version IDs. Evidence passage
version links are backfilled additively. Source versions preserve available
acquisition config. Category/tier do not imply reliability, permission or independent
origin. en/ar discovery and English output are profile settings, not implemented
translation/clustering. The Node definitions remain unconfirmed.

## Migration and lineage

0001 is untouched. 0002 retains legacy tables/IDs and backfills version records,
legacy recommendations, event and article edges. Old angle-only scores remain
readable; new opportunity_scores can target a story revision or angle. Do not
write new product behavior into old angle-required tables. Unknown historical
source acquisition version, full effective settings, section, score-at-exposure
and impression history are not invented. Config reconstructions explicitly carry
reconstruction_complete=0. Legacy recommendation support status is retained, but
verification is ORIGIN UNKNOWN rather than a fabricated verification decision.

New complete config snapshots include JSON and hash, not only a version label.
Recommendations retain analysis/config/score references. Impressions preserve
actual rank, day/session, display projection and retry identity. User events are
append-only/idempotent and permit compensating corrections. Manual article URLs
can link multiple recommendations, with optional angle and unknown publication
stamp. No content is automatically fetched from a recorded article URL.

Immutable snapshots are SQL-protected from casual update/delete. Future rights-
required removal must explicitly handle source-aware tombstones and permitted
redaction while retaining legal provenance; these triggers must not be used to
justify keeping forbidden text. No retention/deletion implementation exists here.
Evidence_availability records state without replacing original claims. Local
recovery/consistent backup/restore comes in R1.5, with an owner-controlled off-device
destination required before relying on data against device loss.

Tests apply schema from empty and from populated v1; verify preserved IDs, story-only
feedback/article links, repeat migration, null constraints and immutable reload.
Only synthetic temporary databases are migrated. Actual runtime data elsewhere is
unknown; do not apply 0002 to an owner database without backup/restore review.

## Scoring and cache

Metrics retain measured/estimated/not_measured, nulls, basis and observation/
methodology/unit metadata. Performance values remain native units in future R3,
not 0-100. Optional social/search have no active weight. The provisional fixed R1
base uses audience relevance, freshness, newsworthiness and curiosity. It is a
configuration proposal, not calculated ranking or calibration. A missing required
weighted input withholds score, with no per-card renormalization. Confidence is
shown separately. Coverage/novelty refer to monitored samples only.

Analysis key includes evidence, provider/model, prompt/schema, audience and
extraction/translation/behavior versions. Score key uses analysis/subject and
scoring formula/config. Weight-only changes do not force a new identical AI call.
Historical scores and display projections never get overwritten by re-scoring.

## Deferred and prerequisites

R1.1: local environment/launcher decision, first confirmed section, reviewed
permitted source dossier. R1.3: actual free-only provider project/model entitlement,
quota/data-policy/cost test. R1.5: editorial baseline, permission-aware retention
and demonstrated off-device backup/restore. R2 research, R3 Marfeel/performance,
R4 evaluated owner-approved learning, R5 SaaS/CMS/automation are deferred.
No paid service is enabled by planning approval. Subscription access is not API
entitlement. No source/AI call, schedule or infrastructure was activated in R1.0.
