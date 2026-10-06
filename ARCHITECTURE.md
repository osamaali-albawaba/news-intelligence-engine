# Architecture

## Product invariant

Rank supported **angles within event clusters**, not importance or headline
popularity alone. Preserve a small set of strong recommendations over a padded
list. A saturated event can contain a valuable, under-covered angle.

## Components and runtime

| Component | Target implementation | Phase 0 artifact |
| --- | --- | --- |
| Browser dashboard | React, TypeScript, Vite; static assets on Cloudflare | `apps/dashboard/README.md` |
| Private API | Small TypeScript Worker | `apps/api/boundary.ts`, `contracts/api.ts` |
| Persistence | Cloudflare D1; SQLite-compatible migrations | `migrations/0001_foundation.sql` |
| Collection/analysis | Python 3.12+ on GitHub Actions | `engine/contracts.py` |
| AI | Configurable provider; Gemini first, replaceable | `AIProvider` protocol; no real provider |
| Authentication | GitHub OAuth, allowlisted numeric user ID | Environment placeholders and API security contract |
| Performance | Optional independent connector; Marfeel later | `PerformanceConnector` protocol |

GitHub is the source of truth for code and configuration. D1 is the runtime
store for items, jobs, recommendations, feedback and performance. Data never
depends on a continuously running laptop. Python runner credentials stay in
GitHub Secrets; API credentials stay in Worker secrets, never browser assets.

## Funnel

1. Collect broadly from reviewed, permitted source adapters. Save allowed raw data.
2. Normalize canonical URLs, deduplicate exact content, preserve syndication origin.
3. Cluster event reports by content, entities, location and time.
4. Cheap shortlist before AI. Fetch permitted supporting bodies for candidates.
5. Analyze selected clusters with evidence passage IDs; validate structured output.
6. Assess each angle against observed coverage, then score eligible angles.
7. Show cached recommendations, explanations, alternatives and source support.
8. Persist editorial feedback and article URLs. Performance connectors come later.

Clustering, extraction, ranking and live pipeline implementations are outside
Phase 0. The SQL model establishes their storage boundaries without running them.

## Scheduled collection and SCAN NOW

Proposed endpoints in later phases:

- `POST /api/scans`: authenticated SCAN NOW request with idempotency key.
- `GET /api/scans/{id}`: progress, queue status, limitations, failure information.
- `GET /api/opportunities`: cached results and collection/analysis timestamps.
- `POST /api/feedback`: append an editorial decision, optionally record article URL.

Manual and scheduled triggers share the same pipeline and global scan scope.
Inside a database transaction, replay an existing requester/idempotency-key
request or join an active scan; otherwise create a queued job and its request.
The database partial unique index prevents overlapping queued/running scans.
Joining is visible: SCAN NOW may join an already running scan rather than start
another. Each request retains its trigger and requester for audit.

After committing the job, the server dispatches a future GitHub Actions workflow
using a least-privilege server-side credential. Return HTTP 202 with job ID, not
an instantaneous analysis promise. Dispatch failures leave recoverable queued
work; a later schedule discovers it. UI polls progress and retains old results.

The future runner atomically claims a lease, heartbeats, records partial source
success, and releases/completes work. Reclaim expired leases with bounded retries
and an ownership token so stale runners cannot overwrite a newer owner's results.
Use a shared Actions concurrency group as an additional guard, not the only lock.
Do not cancel an active scan when a new manual request arrives.

Apply server-side authentication, CSRF/Origin protection, daily manual limits,
cooldowns, item/time/token budgets and sanitized errors to both trigger paths.
Validate written URLs and redirects; allow only public HTTP(S) addresses, block
private/reserved networks and re-check every redirect before future content fetches.
No user-supplied URL is fetched in Phase 0.

Hourly scheduling at minute 17 is the initial proposal. A private GitHub Free
account includes 2,000 runner minutes/month, shared with other workflows. At
720 scans/month and two minutes each, collection uses about 1,440 minutes before
manual scans and CI. Measure actual runtime before promising this cadence.
Schedules can be delayed or dropped. Manual dispatch can also queue. This is
best-effort freshness, not a breaking-news SLA.

**Phase 0 installs CI only. No cron or collection workflow is active.**

## Scalable source registry

The registry accepts arbitrary source count; 12–20 is an initial operating choice,
not a schema limit. Use stable source IDs, indexed categories and per-source due
times. Registry size and per-run batch budget are independent. Later collectors
must choose due sources fairly, with priority plus aging to prevent starvation.
Use bounded concurrency, per-host rate limits, conditional requests and backoff.

Category describes content type: wire, major international, regional, official,
entertainment, specialist, social/trend, other. Tier describes editorial handling:
primary, established, discovery. Neither guarantees factual accuracy. Track common
publisher ownership and syndicated origin to avoid false corroboration.
Permission records explicitly govern retention and AI transmission. Robots
compliance is necessary where applicable but does not establish licensing rights.

## Evidence and AI boundaries

Every statement retains one of four kinds:

- `reported_fact`: supported report of what happened.
- `attributed_claim`: what an identified source says; not automatically fact.
- `editorial_interpretation`: an explicitly labeled editorial inference.
- `possible_consequence`: a contingent outcome, not an established development.

Statements and angles reference persisted source passages and immutable content
hashes. Contradictions are retained. Provider results must not introduce unknown
evidence references. Referential checks alone do not establish truth: later
semantic validation and human editorial review remain necessary.

`AIProvider` returns provider-independent structured results. Provider/model are
configured through environment variables and a future explicit registry. Unknown
providers fail clearly; never silently invoke a paid fallback. Quota, timeouts and
malformed outputs are typed failures. External content is untrusted prompt data.

Cache keys include content snapshot, provider, model, prompt version, output-schema
version and the audience profile. Reanalyze changed evidence or configuration, not
identical content. Provider usage may itself be unknown; store null, not zero.

## Missing metrics, coverage and scoring

Each metric stores status, nullable value, and basis. `not_measured` requires null;
measured/estimated values are bounded 0–100. Social and search absence remains
visible. Coverage scores describe a timestamped monitored-source sample, not the
entire web. Novelty compares claims/consequences, not cosmetic title differences.

The proposed score weights are versioned configuration, not permanent constants.
No scoring implementation exists yet. A missing required weighted component
withholds the overall score instead of converting it to zero. Metrics that have
no weight can remain missing without blocking other valid estimates. Source
confidence is an eligibility gate, not merely a compensable score component.
Unconfirmed/needs-review angles cannot become publish-ready due to high traffic
potential. Expected traffic is an experimental relative estimate, not pageviews.

## Storage and retention

Migration includes sources, raw items, documents/entities, clusters/membership,
analyses, passages, typed statements, angles/support, coverage samples, scores,
jobs/requests/runs, user profiles, append-only feedback, written articles and
future performance observations. Foreign keys and checks protect null semantics,
attribution, score bounds, retry identity and concurrent active-job uniqueness.

The application supplies UUIDs and UTC ISO-8601 timestamps. SQL accepts text IDs
for portability; application boundaries validate UUIDs and timestamp formats.
Migration is locally verified with SQLite. Actual D1 deployment remains untested.
Production writes must atomically persist statements/angles with evidence links;
foreign keys cannot enforce the existence of at least one supporting passage.

Proposed transient retention is 30 days, constrained by each source's permissions.
Deletion jobs must respect saved evidence references; do not delete a referenced
passage while silently retaining its unsupported recommendation. No retention
job or backup/export process runs in Phase 0. Add operational backup/restore checks
before production.

## Cost and access references

Planning references checked 2026-10-06; recheck before deployment:

- [Workers limits](https://developers.cloudflare.com/workers/platform/limits/): free CPU allowance makes heavy processing unsuitable for the API Worker.
- [D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/): bounded storage and daily row quotas.
- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions): account-wide private runner allowance.
- [GitHub schedules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows): best-effort scheduling.
- [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing) and [limits](https://ai.google.dev/gemini-api/docs/rate-limits): model/account-dependent access and data-use terms.
- [Marfeel Reporting API](https://www.marfeel.com/docs/analytics/api-docs/marfeel-reporting-api-developer-guide): official connector possible subject to account entitlement.

No paid service or unauthorized source access is enabled by this foundation.
