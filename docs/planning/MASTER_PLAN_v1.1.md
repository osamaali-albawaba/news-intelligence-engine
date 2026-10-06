# News Intelligence Engine — Master Plan v1.1

**Full Product Architecture and Release Strategy**  
Version: 1.1 | Date: 2026-10-06 | Status: Proposed planning baseline for review  
Product owner: Osama Ali | Initial newsroom: Al Bawaba English

## 1. Document authority and evidence boundary

This package consolidates the complete conversation pasted into this chat, all 24 sections and tables of `News_Intelligence_Engine_Master_Plan_v1.0(1).docx`, and all 29 repository files at tree `99533963972c9e303a9c947ab77998a98b1b14d7`. Repository: https://github.com/osamaali-albawaba/news-intelligence-engine. Earlier discovery conversations that were not supplied are not claimed as reviewed.

Explicit user decisions take precedence over assistant proposals and older repository defaults. A user answer without its original question is not evidence of an additional decision: infrastructure answers 6, 10 and the empty 11 remain context-limited. Marfeel authorization is explicitly described in the supplied discovery summary; its account entitlement and credentials remain unverified. Product discovery question 5, concerning shared newsroom versus individual recommendations, was not answered directly; individual personalization was accepted separately and does not settle newsroom assignment behavior.

This is a planning deliverable. No repository write, provisioning, live collection, paid service activation or product implementation occurs through issuing it. Approval of a later baseline should record its exact version. R1 scope, cost permissions and implementation authorization must be explicit in the engineering handoff; old Phase 0-only instructions should be reconciled rather than silently ignored.

Use `REQUIREMENTS_TRACEABILITY.md` to preserve the original 85-item vision and additional handoff requirements. Use `PHASE_0_ALIGNMENT.md` for existing code decisions. Future tasks should cite the relevant requirement IDs and release acceptance criteria.

## 2. Product definition

The engine answers: **What should I write about now, what is the strongest defensible angle, and why is this opportunity worth my time?**

It turns fragmented Arabic and English reporting, permitted official material, and later social and newsroom-performance signals into ranked editorial opportunities. It groups reports about an event, separates new developments from repetition, identifies useful details or angles, and explains its recommendation through inspectable evidence.

For the first three months, the North Star is: **Find high-potential stories and defensible angles exceptionally well, as early as possible.** The product is judged on better and faster discovery. Research, SEO, performance and social intelligence earn their scope by helping that loop. Broad article generation, a general SEO suite and SaaS infrastructure do not belong in the initial pilot.

Initial user: Osama, an English Al Bawaba journalist/editor. Sections: News, Business, The Node. Discovery: Arabic and English. Output: English. The Node's exact editorial taxonomy is an open configuration decision; do not silently substitute a generic technology feed. Audience geography remains configurable; do not infer a permanent Middle East-only audience from the user's location.

The default result target is **up to ten useful opportunities per selected section**, never ten mandatory results. Fewer or zero results are valid. A story may be useful without a differentiated angle. An angle may be useful within a widely covered story. Therefore, the product ranks opportunities at two levels: a story-level candidate with an optional best angle, and an angle-level assessment when an angle exists. One event card avoids clutter; its detail view can preserve multiple angles.

## 3. Confirmed constraints

| Constraint | Required behavior |
| --- | --- |
| Existing subscriptions | ChatGPT and Gemini, described by the user as $20 each, already paid. They are not treated as API credits. |
| Incremental operating cost | Target $0/month. No automatic upgrade or paid fallback. |
| Exceptional spend | At most approximately $5–10/month, only after a concrete explicit approval. This is not an already authorized monthly allowance. |
| Infrastructure | User device directly; GitHub and suitable free sources/services. No slashTEC or company AWS resources. |
| Deployment | Local-first pilot; hosted execution is an optional future decision. |
| Availability | Best effort. Device sleep or downtime is acceptable; disclose stale results. |
| Speed | Progressive results; optimize cost before scan latency. Keep browser interactions responsive. |
| Data use | User accepts provider learning from data to avoid cost; apply source permissions and distinguish public news from private newsroom data. |
| Product control | AI recommends; journalist verifies and decides; human publishes. |
| Paid integrations | Disabled until approved; social access must not become a prerequisite for useful discovery. |
| Future direction | First organizational prospect: Al Bawaba; independent dashboard plus future CMS integration. |

Zero incremental service spend does not promise zero electricity, internet or hardware consumption. No additional hardware purchase is assumed. Browser responsiveness and scan duration are separate: slow discovery may be acceptable, a blocked interface is not.

## 4. Success and measurement

The success chain is interconnected: better/faster discovery → better selection → less research time and greater publishing capacity → stronger readership → better understanding of traffic sources → better future recommendations. No single outcome proves success and no traffic uplift is guaranteed.

Before evaluating the pilot, record baseline manual discovery sessions in comparable sections and shifts. The previous assistant mentioned roughly five stories per shift; this has not been independently confirmed by the user's answers and must not become a fixed acceptance target. Collect actual baseline output and research time instead.

| Measure | Definition | Interpretation |
| --- | --- | --- |
| Time to usable opportunity | Minutes from scan/start of comparable manual search to the first user-judged useful story | Compare section and shift context; report sample size. |
| Discovery lift | User says an accepted story would otherwise have been missed or found later | Useful qualitative evidence, not a proven counterfactual. |
| Exposure-to-open rate | Unique opened recommendation impressions / unique displayed recommendation impressions | Requires exposure logging; hidden results are not rejections. |
| Selection/adoption | Selections, research starts and published links per exposed recommendation | Keep each stage separate; avoid double-counting retries. |
| Publishing capacity | Articles per comparable shift plus quality/verification notes | Workload and editorial assignments are confounders. |
| Traffic outcomes | Native metric, observation window and article age retained | Users, pageviews and sessions cannot be interchanged. |
| Search outcomes | Search traffic separated where available | No invented search metric if connector lacks it. |
| Trust and quality | Unsupported claims, misleading angles, clustering errors, useful/weak angle judgments | A high traffic score cannot excuse weak evidence. |

Day-one event capture covers displayed → opened → selected/rejected/saved → writing/published where implemented. Research events start in R2. R1 records a manual published URL to preserve the linkage; automated performance ingestion remains R3. Do not build a writing editor merely to record writing status.

Numeric business-success thresholds remain owner-set after baseline collection. Operational DoD checks in the release plans are concrete; they are not claims of business validation. A small number of scans proves operability, not predictive accuracy.

## 5. Intelligence lifecycle and boundaries

DISCOVER → NORMALIZE → CLUSTER → UNDERSTAND → FIND ANGLES → SCORE → RECOMMEND → RESEARCH → HUMAN DECISION → MANUAL ARTICLE LINK → MEASURE → DIAGNOSE → LEARN.

The diagram of logical modules is not an execution order in which UI runs last. UI reads persisted incremental state throughout the scan. Performance and learning operate asynchronously after publication.

| Module | Owns | Does not own |
| --- | --- | --- |
| Source adapters | Permitted acquisition, provenance, source-specific parsing and failure details | Ranking or presentation |
| Scan orchestration | Budget, idempotency, stage state, bounded worker execution | Editorial judgment |
| Normalization | URL/timestamp/language normalization and document versions | Provider interpretation |
| Clustering | Event membership, entity aliases, revision tracking, merge/split audit | Final factual verification |
| Intelligence | Evidence-linked summaries, claims, candidate angles and limitations | Autonomous publication |
| Scoring | Versioned components, opportunity ordering and explanations | Fetching or inventing measurements |
| Research | Explicitly requested story/angle/question investigation | Automatic deep analysis of every candidate |
| Performance | Connector-specific ingestion and metric definitions | Rewriting original recommendations |
| Learning | Evaluation and proposed calibration | Unapproved active weight changes |
| Local API/UI | Validated requests, progress, navigation and user events | Duplicate scoring implementations |

These are code boundaries within a modular monolith, not ten services. Prefer a single Python application, one local SQLite database and one browser UI. No Redis, Kubernetes, vector database or distributed event bus is required for R1.

## 6. Proposed local architecture

Retain Python for the engine and TypeScript/React/Vite as the proposed browser stack. Use a small Python HTTP boundary alongside the engine rather than requiring a Cloudflare Worker. FastAPI is a reasonable candidate, with exact dependency versions selected and locked during implementation. The user does not need a framework decision now to review the product plan.

A local launcher starts the API and a single worker; a production UI build is served locally. Development may use Vite separately. Durable jobs live in SQLite; HTTP returns a job ID and never holds the browser request open for the full analysis. The worker writes checkpoints; polling reads persisted progress and opportunities. Database transactions remain short; network/model calls happen outside transactions.

Bind to loopback by default. Keep secrets on the server. Local origin checks and a local session token protect mutations. No OAuth or enterprise login is required for a loopback single-user pilot. LAN exposure and remotely hosted access are separate security decisions. The laptop must be awake and the application running for processing; no background uptime promise is made.

Use SQLite on a local disk. WAL is optional for overlapping reads/writes, not mandatory; it retains a single-writer constraint. Use an online backup mechanism or a clean closed-database backup, not arbitrary copying of a live main database file. Official design references: https://www.sqlite.org/wal.html and https://www.sqlite.org/backup.html. A tested restore is required before relying on the pilot's accumulated learning data.

GitHub stores source, configuration templates, approved documentation and synthetic fixtures. It is not the runtime database or a location for private newsroom metrics. Runtime database, exports and backups are ignored by Git. A local archive protects against software mistakes but does not protect against loss of the only device; an owner-controlled off-device backup destination is an open zero-cost decision.

Future migration should reuse adapters, intelligence and domain contracts. Storage, job execution and auth are replaceable boundaries. This reduces rework; it does not claim a multi-tenant cloud migration will require no engineering.

## 7. Source and discovery strategy

R1 uses permitted RSS/news/official sources in both languages. Source usefulness is a product concern: regional and small publications may have details absent from large outlets. Categories, editorial tiers, publisher ownership, confidence, originality and angle usefulness are independent fields.

A source dossier records stable source ID, sections, language, category, tier, access method, sample content availability, publisher group, known syndication origin, restrictions, retention permission, AI-transmission permission, reliability, freshness, costs and last review. There is no approved live source list in the repository: its example uses `.invalid` and is disabled. A model-generated list must not be treated as reviewed access.

Select a compact first batch capable of exercising Arabic/English reporting, primary material and independent news reports for the first section. Expand based on useful opportunities, not raw item volume. Ten, twenty or a hundred configured sources are not schema caps; per-run budgets bound work. Source priority plus aging prevents small sources from being permanently excluded.

Cheap steps run first: freshness and section filtering, canonical URL/content dedupe, permitted snippets, lightweight entities, basic clustering and preselection. Supporting bodies are fetched only when permitted and useful. Expensive analysis applies to the shortlist. Repeated evidence reuses cache; new source text or behavior settings invalidate the relevant stage only.

Social platforms X, Instagram, Reddit and YouTube are separate optional adapters. A social source can show an excerpt, account, time, available engagement observations and original link. Missing engagement is `not_measured`; unavailable posts are not invented. Free API access, search, quotas and permission are verified per platform before activation. R1 is not blocked by social completeness.

## 8. Temporal and cross-language intelligence

Store original publication time, publication timezone when available, first discovery time, fetch time and detected update time separately. Unknown publication time remains unknown and must not produce a misleading '12 min old' label.

Canonical URLs identify an article, not an immutable version. A changed body at the same URL creates a document revision. Cluster revisions preserve the exact member document versions used by an analysis. Minor formatting changes and another syndicated copy do not automatically count as a new development.

Entities retain surface forms, normalized aliases, type, language, resolution provenance and ambiguity. Arabic and English aliases can resolve to one entity. Shared names alone do not establish event identity: actor, action, location, event time and context matter. Uncertain matches stay separate or receive a review flag. R1 supports tested basic cross-language grouping; advanced gaps, semantic contradictions and rich timelines mature in R2.

Within the day, cards retain NEW/SEEN/UPDATE/NEW ANGLE. Repeated scans refresh the existing card without presenting it as a fresh opportunity. SEEN cards do not disappear automatically. UPDATE requires substantive new evidence; NEW ANGLE requires a materially distinct supported angle. A first exposure by this user differs from first discovery by the engine.

At midnight in the workspace timezone (initial proposal: Asia/Amman), create a new daily view. Storage timestamps remain UTC. Apply the reset lazily on next request/startup if the device was asleep. Saved items remain retrievable. Old clusters can be shown within the configured 24/48/72-hour window with accurate historical state; reset never erases provenance or makes an old story factually new.

## 9. Evidence, rumor and angle behavior

Preserve four statement kinds: reported fact, attributed claim, editorial interpretation and possible consequence. Each important summary claim, Why Now explanation, risk statement and angle rationale must map to relevant evidence or be explicitly identified as a system observation, such as missing coverage data. Merely validating a passage ID does not establish semantic support.

Verification labels available to users: VERIFIED, REPORTED, SINGLE SOURCE, UNVERIFIED, ORIGIN UNKNOWN. Keep this separate from machine support status (`supported`, `needs_review`, `unconfirmed`). VERIFIED means a documented verification basis, not 'AI said so' or 'many outlets copied it'. Count independent origins as well as publisher URLs.

Rumors can appear as leads with explicit labels and lower evidence confidence. They cannot be promoted to verified reporting because of views or engagement. A numeric confidence cutoff must not silently exclude all rumor leads. Maintain visibility status and verification requirements independently of traffic priority; the human decides whether to investigate.

Angles are optional and variable in number. Search for hidden details, contradictions, consequences, curiosity, controversy, personalities, quotes, numbers, unanswered questions, unexpected connections, next developments, cross-language gaps and social reactions only when supported. Do not force one of every category. Distinct wording is not angle diversity. 'No strong angle found' is acceptable and does not automatically suppress a useful developing story.

SKIP is an editorial recommendation with an explanation; it does not delete a story or force the user's decision. Saturation is a monitored-source observation, not proof that every publication has covered the angle. Al Bawaba coverage must distinguish the event, the selected angle and a genuinely new update.

## 10. Scoring design

The headline objective is traffic opportunity, including useful angles, rather than political importance or source prestige alone. The 0–100 number is an experimental relative opportunity index; it is not a probability of success or predicted pageviews. Numeric labels such as HIGH are versioned configurable bands; exact cutoffs are a provisional tuning decision.

Avoid circular scoring: 'traffic potential' is the aggregate objective, not another independent weighted copy of the same aggregate. Confidence remains visibly separate from opportunity value. Freshness, novelty, audience relevance, curiosity, breaking potential, controversy, observed coverage and measured social/search signals may inform the model. Initial feature definitions and rubrics must state basis and direction; high saturation reduces the coverage-opportunity component, it does not accidentally add positive weight.

Use a deliberately small R1 base formula whose required components can actually be assessed. Preserve the repository's missing-input policy: if a required weighted component is absent, withhold the aggregate. Do not silently treat absence as zero or dynamically renormalize every card over a different set of components. Optional social/SEO components have zero active weight until a reviewed formula version supports them. Display 'Not scored — missing evidence' with a separate provisional ordering; do not pretend its rank is comparable to a fully scored card.

Each recommendation freezes its analysis, component values/status/basis, weights, formula, settings, evidence snapshot and display rank. A later re-score creates another snapshot. Reordering does not rewrite what the journalist originally saw. Research may improve the score using newly acquired evidence, retaining the earlier score.

## 11. UX and control layer

Desktop-first dashboard, no thumbnails. Tabs: News, Business, The Node. Primary action: SCAN NOW for selected section. Settings remain adjacent rather than interrupting every scan. Defaults: 24-hour freshness and up to ten results, both configurable; 48/72-hour presets remain available. Optional Scan All is later within R1 only if the single-section flow is stable and the same budget guard applies.

Compact card: score and band, headline, available trend/freshness/source count, Why Now, optional best angle, useful tags, risk, Open and structured feedback. Never show fake trend badges or unsupported sorting. Alternatives include newest, trending, most novel, breaking and social only when the required data exists. Preliminary analysis is visibly different from completed scoring. Old valid results remain visible during a scan and failure.

R1 Open leads to basic story/evidence detail. Deep Research appears only when R2 is enabled; omit a dead actionable button in R1. Feedback reasons: Not Interested, Already Covered, Weak Angle, Save for Later. Save is a positive workflow state, not a negative training label. Mark as Writing, select an available angle and manually record an article URL without building article composition.

R2 Research Room includes summary, Why This Could Get Views, timeline, available angles, hidden details, unanswered questions, contradictions, news sources, social posts, Al Bawaba coverage and verification risks. 'Research Story', 'Research This Angle' and 'Find Answer' create separate bounded user-intent jobs. Selected angle detail includes evidence, key facts, angle score and suggested headlines, each grounded in the chosen angle; these headlines do not constitute a writing assistant.

Controls are versioned data: freshness, count, rumor visibility/tolerance, source emphasis, angle behavior, social, novelty, breaking and future SEO emphasis. My Default is the initial profile; Breaking/Social/SEO/Hidden Angles presets follow validated capability. One-scan overrides do not alter defaults. Natural-language behavior control in R2 translates instructions into a previewable constrained configuration/prompt change. It cannot create credentials, enable paid features, override evidence rules or execute arbitrary code. Restore creates a new active version pointing to prior values; it does not erase history.

## 12. Performance and learning architecture

R3 links recommendation exposure → selected story/angle → writing/published URL → connector observations. Publication may combine recommendations or substantially change the angle; use explicit many-to-many links and user confirmation rather than guessing from title similarity. Keep articles not originating in this engine available for historical comparison with origin marked.

Marfeel is an independent connector. Discovery summary reports Explore/Get JSON API and fields dates, filters, groupBy, metrics, order, granularity, URL/title/topicCategory/uniqueUsers. These are reported observations, not a tested connector specification. Verify the user's actual account, pagination, sampling, timezones, metric units, attribution and API entitlement before implementation. A permitted manual export/import route is an R3 fallback, not fabricated connector success.

Track total traffic, search/Google, Flipboard, social, referral, velocity and longevity only where definitions and data permit. Compare article-age-aligned windows and compatible metrics. Retain raw observations and reproducible derived values, with missingness, late arrival and correction history. Zero is valid only when the source explicitly reports measured zero.

Historical analysis includes top/low performers, source-specific winners, spikes/long-tail stories, sections and publication timing. This informs a candidate scoring version, not retroactive proof that the original score was right.

R4 compares frozen predictions with outcomes, reports hypotheses rather than unsupported causality, and suggests weight changes with data size, uncertainty, affected cohorts and evaluation. Human approval is mandatory. Use chronological evaluation, an unchanged baseline and section-aware cohorts. Displayed-but-not-selected, unpublished and missing-metric cases cannot be treated as failed articles. Prefer fewer features and simpler models when data is sparse. Organization-specific learning is prepared in R4 and isolated operationally in R5.

## 13. Releases and three-month focus

R1 Make It Useful; R2 Make It Smart; R3 Make It Learn; R4 Make It Better; R5 Make It a Product. Full entry/exit gates are in `RELEASE_MAP.md`; R1's vertical slices are in `R1_EXECUTION_PLAN.md`. Do not rename these five releases into dozens of phases.

Month 1 aims for usable discovery and real feedback. Month 2 aims for stronger evidence-backed research and angles. Month 3 aims to begin outcome linkage and evaluate discovery improvement. These are directional milestones, not a promise that R1–R4 will all finish in 90 days. R3 performance work may start later if source/API access or user capacity is insufficient. R4 learning is gated by data quality and evaluable observations, not calendar pressure.

Prepare stable lineage now; implement future features when their release begins. Organization IDs and immutable snapshots are inexpensive preparation. Billing screens, tenant provisioning, distributed schedulers and speculative model training are premature implementation.

## 14. Commercial path

Personal pilot → internal measured evidence → Al Bawaba pilot proposal → newsroom/CMS integration → external validation. Primary commercial hypothesis: newsroom subscription. Individual subscriptions remain possible. Value proposition, competitor research and final pricing are deliberately deferred to business validation; no market uniqueness claim is made.

Future journalists may have different editorial profiles while sharing organization-specific performance intelligence. Whether the newsroom shares one queue, personal queues or assignment controls is TBD on R5 entry. Writer analytics are not architecturally prohibited, as the user explicitly requested, but are deferred and require contextual metric definitions rather than a simplistic writer score. White-label remains possible, not promised.

## 15. Change control and engineering practice

New ideas enter backlog, not the current task automatically. A scope change records requirement ID, release value, dependencies, cost and acceptance impact. The product owner decides scope; coding agents implement it. A contract adjustment is not permission to invent adjacent product features.

Use one active feature owner. Pull safely; work on a coherent branch; test; commit; synchronize; update handoff. No simultaneous edits of the same feature by Codex and Antigravity. Prefer reviewable branches over routine direct-main changes. Do not force push or discard another agent's work. Keep the project separate from any parent AWS evidence repository.

HANDOFF retains CURRENT STATUS, LAST COMPLETED TASK, FILES CHANGED, WHAT WORKS, KNOWN ISSUES, NEXT TASK and TEST INSTRUCTIONS. Include tested commit, actual test output, unavailable checks and owner. Documentation-only updates must not automatically trigger live runtime provisioning.

Testing combines adapters/normalization/contracts, bilingual clustering fixtures, null semantics, scoring behavior, evidence validation, restart/idempotency, user flows and editorial usefulness review. Maintain synthetic examples and later 50–100 curated historical scenarios as capacity permits. Evaluation set size is an evolving asset, not an initial gate that delays the first useful pilot.

## 16. Readiness and exact next action

**Verdict: READY WITH CHANGES for foundation alignment and a first real-source slice; NOT READY for unrestricted live AI operation or a claimed complete R1.** Source access, API/free-tier entitlement, hardware and section taxonomy still need practical verification.

Next engineering action after baseline approval: capture current main commit and local runtime facts, produce/confirm the Phase 0 KEEP/CHANGE/ADD/DEFER checklist, then implement R1.0's contract/configuration alignment and SQLite migration tests. No paid service, scheduler, cloud deployment or live model fallback is enabled. The first user-facing milestone remains: choose News → SCAN NOW → inspect real grouped signals; then add validated opportunity intelligence.

Do not restart the repository merely because rewriting was permitted. Preserve working evidence contracts and 18 passing offline tests unless a concrete incompatibility justifies replacement. A clean replacement is acceptable with an archived baseline, a documented mapping and no silent loss of history.
