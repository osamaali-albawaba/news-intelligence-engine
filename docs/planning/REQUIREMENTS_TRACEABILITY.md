# Requirements Traceability and Decision Provenance

Version 1.1 | 2026-10-06

## Coverage standard

Each of the original 85 numbered vision items is retained below with a planning destination and scope state. This is a coverage register, not a claim that every assistant-generated feature was explicitly approved by the user. Inherited design intent is preserved unless a conflict is explained in the alignment/risk documents. Future capabilities remain future even when present in the data contracts.

References: Master = MASTER_PLAN_v1.1.md; Contracts = CROSS_RELEASE_CONTRACTS.md; Release Map = RELEASE_MAP.md; Alignment = PHASE_0_ALIGNMENT.md; Risks = ARCHITECTURE_RISK_REVIEW.md; Backlog = PRODUCT_BACKLOG.md. R1-D identifiers are in R1_EXECUTION_PLAN.md.

## Original 85-item vision mapping

| ID | Original topic | Destination | Treatment |
| --- | --- | --- | --- |
| V01 | Product Vision | Master 2 | Core |
| V02 | North Star | Master 2,13 | Core first 3 months |
| V03 | Initial User | Master 2 | R1 |
| V04 | Product Success Model | Master 4 | R1 measurement; outcomes R3 |
| V05 | Core Product Loop | Master 5 | R1–R4 |
| V06 | Fundamental Product Principle | Master 3,9 | All releases |
| V07 | Discovery Strategy | Master 7 | R1 |
| V08 | Source Architecture | Master 5,7; Contracts 4 | R1 extension boundary |
| V09 | Source Configuration | Contracts 2,4 | R1 |
| V10 | Trust versus Usefulness | Master 7,9,10 | R1 |
| V11 | Rumors | Master 9; R1-D11 | R1 visible and labeled |
| V12 | Cross-Language Intelligence | Master 8; R1-D06 | Basic R1; advanced R2 |
| V13 | Story Clustering | Master 8; Contracts 2,3 | R1 |
| V14 | Duplicate Intelligence | Master 8; R1-D07,D08 | R1; NEW ANGLE when supported |
| V15 | Freshness 24/48/72h | Master 8,11 | R1 |
| V16 | Story Memory and Daily Reset | Master 8; Contracts 11 | R1 |
| V17 | Manual First / Auto Scan Disabled | Master 3,6; Alignment | R1; automation R5 |
| V18 | Section-Based Scan | Master 2,11; Contracts 5 | R1 |
| V19 | Initial Result Target | Master 2,11 | Up to ten; no padding |
| V20 | Progressive Discovery | Master 6,11; R1-D04 | R1 |
| V21 | Opportunity Intelligence / Cheap Funnel | Master 7; R1.3 | R1 |
| V22 | Opportunity Score and Components | Master 10 | R1 provisional; calibration R4 |
| V23 | Primary Ranking Objective | Master 2,10 | Traffic opportunity, not abstract importance |
| V24 | Scoring Integrity / Missing Data | Master 10; Contracts 8 | R1 |
| V25 | Angle Intelligence / No Quota | Master 9; R1-D11 | R1 optional angle |
| V26 | Angle Diversity and Categories | Master 9 | R1 basic; R2 rich |
| V27 | Evidence-First Angles / Claim Types | Master 9; Contracts 7 | R1 |
| V28 | Why Now | Master 9,11; Contracts 7 | R1 evidence-backed |
| V29 | Risk Labels | Master 9,11 | R1 |
| V30 | SKIP Recommendation | Master 9 | R1 advice, not deletion |
| V31 | Dashboard UX | Master 11; R1.4 | R1; research action deferred |
| V32 | Sorting | Master 11 | R1 when supported by data |
| V33 | Scan UX and Settings | Master 11 | R1 |
| V34 | Result State NEW/SEEN/UPDATE/NEW ANGLE | Master 8 | R1 first three; latter when supported |
| V35 | Structured Feedback | Master 4,11; Contracts 5 | R1 |
| V36 | Research Room | Master 11; Release Map R2 | R2 |
| V37 | Source Navigation and Social Evidence | Master 7,11 | News R1; social R2 optional |
| V38 | Deep Research Two Levels | Release Map R2; Contracts 9 | R2 on-demand |
| V39 | Unanswered Questions / Find Answer | Release Map R2 | R2 |
| V40 | Al Bawaba Coverage Intelligence | Master 9; Release Map R2 | R2 |
| V41 | Selected Angle / Headlines / Writing / Published URL | Master 11; Contracts 2,5,9 | Manual tracking R1; research/headlines R2 |
| V42 | Writing Assistant | Backlog B21 | Deferred beyond first 3 months |
| V43 | SEO | Backlog B02 | On-demand extension; not broad R1 suite |
| V44 | Performance Model Decomposition | Master 12; Release Map R3 | R3 supported metrics only |
| V45 | Marfeel | Master 12; Risks O10 | R3 actual capability verification |
| V46 | Recommendation to Performance Link | Contracts 2,10; Release Map R3 | IDs/events/manual URL R1; ingestion R3 |
| V47 | Performance Diagnosis | Master 12; Release Map R4 | R4 hypotheses, not causality |
| V48 | Learning / Accept or Reject Weights | Master 12; Contracts 10 | R4 controlled |
| V49 | Historical Performance Research | Master 12; Release Map R3 | R3 before final calibrated scoring |
| V50 | Control Layer | Master 11; Contracts 5 | R1 basics; R2 mature |
| V51 | Natural-Language Behavior Control | Master 11; Contracts 9 | R2 constrained preview |
| V52 | Profiles and Modes | Master 11; Backlog B23 | My Default R1; further modes R2 |
| V53 | Configuration Versioning | Contracts 2,5,7 | R1 snapshots; R2 controls |
| V54 | Cost Constraint and Subscription Separation | Master 3; R1 G04 | All releases |
| V55 | Hard Cost Guardrail | Master 3; R1 5 | No paid activation without approval |
| V56 | Local-First | Master 6; Alignment | R1 pilot default |
| V57 | Availability | Master 3,6 | Best effort |
| V58 | Cost Before Speed | Master 3,11 | Progressive results; responsive UI |
| V59 | Data Retention | Contracts 11; Risks O08 | Daily view is not deletion |
| V60 | Security | Master 6; R1-D18 | All releases |
| V61 | Architecture Modules | Master 5 | Modular monolith |
| V62 | AI Provider Independence | Contracts 7 | R1 boundary and validated provider |
| V63 | Capability versus Enabled Feature | Master 13; Backlog | Extension points, no premature features |
| V64 | Release 1 Make It Useful | R1 Execution Plan | Detailed slices and DoD |
| V65 | Release 2 Make It Smart | Release Map R2 | Architectural depth |
| V66 | Release 3 Make It Learn | Release Map R3 | Architectural data/connector depth |
| V67 | Release 4 Make It Better | Release Map R4 | Evaluated approved calibration |
| V68 | Release 5 Make It a Product | Release Map R5 | High level, adoption-gated |
| V69 | Three-Month Focus | Master 13 | Directional goals, no invented fixed deadline |
| V70 | Change Control | Master 15; Backlog change rule | All releases |
| V71 | Agent Rules | Master 15; R1 task brief | Approved scope only |
| V72 | Git Workflow | Master 15; Alignment | Reviewable coherent changes and handoff |
| V73 | One-Agent Ownership | Master 15 | No concurrent same-feature edits |
| V74 | Testing Pyramid | Master 15; R1 7 | Relevant unit/contract/integration/UI |
| V75 | Synthetic Fixtures | R1 7; Alignment | Clearly nonpublishable cases |
| V76 | Regression Protection / 50–100 Scenarios | Master 15; R1 7 | Grow evaluation set progressively |
| V77 | Observability | R1 8; Contracts 2 | R1 local logs, usage and lineage |
| V78 | Decision Log | Master 15; Alignment decision updates | Preserve superseded decisions |
| V79 | Business Development Path | Master 14 | Personal evidence to Al Bawaba adoption |
| V80 | Initial Commercial Direction | Master 14; Backlog B18,B20 | Newsroom hypothesis; optional individual |
| V81 | Organization-Specific Intelligence | Master 12; Contracts 10 | R4 design/R5 isolation |
| V82 | Deferred Business Questions | Master 14; Risks D | No premature pricing/white-label decisions |
| V83 | Major Risks | Architecture Risk Review | Explicit evidence and mitigation |
| V84 | Most Important Rule | Master 2,15 | Better stories/angles faster |
| V85 | Immediate Execution Path / Alignment | Alignment; R1.0 | KEEP/CHANGE/ADD/DEFER before coding |

## Additional handoff requirements

| ID | Requirement | Destination |
| --- | --- | --- |
| H01 | Full R1–R5 objectives/user value/scope/non-scope/data/dependencies/acceptance/DoD/entry/exit | Release Map and R1 Execution Plan |
| H02 | Raw signal through learning lineage | Contracts 1–3,9–10 |
| H03 | Evidence support for every important generated conclusion | Master 9; Contracts 7 |
| H04 | Old story/repetition/development/new angle/long timeline distinction | Master 8; Contracts 2,9 |
| H05 | Arabic/English entity resolution | Master 8; Contracts 2,9 |
| H06 | Original prediction preserved after scoring changes | Contracts 2,8,10 |
| H07 | Exact effective configuration reproducibility | Contracts 2,7 |
| H08 | Provider/model/prompt/schema identification | Contracts 7 |
| H09 | Source replacement without changing scoring | Master 5,7; Contracts 4 |
| H10 | Cheap processing before costly intelligence | Master 7; R1.3 |
| H11 | Failure isolation | R1 failure matrix |
| H12 | Classified backlog including all named future ideas | Backlog B01–B35 |
| H13 | Separate architecture preparation from feature implementation | Master 13; Contracts 2 |
| H14 | No coding, five-release structure, no fake distant task detail | Master 1; Release Map |
| H15 | Critical changes/deferred decisions/readiness/exact next action | Risks A,D,E,F |
| H16 | Rebuild permitted, full supplied information retained | Alignment reuse/rebuild; this register |
| H17 | All output in English | Entire package |

## Explicit user decisions and ambiguities

| ID | Supplied answer/decision | Meaning preserved |
| --- | --- | --- |
| U01 | $20 ChatGPT and $20 Gemini already paid; no more spend except possible $5–10 | Incremental $0 target; exception needs actual approval; subscriptions not API credits |
| U02 | No slashTEC resources; rely on device/GitHub/free sources | Local-first, company resources prohibited |
| U03 | No current cloud budget; future option uncertain | No mandatory hosted runtime |
| U04 | Downtime is not catastrophic | Best-effort local availability |
| U05 | Accept data used for training, avoid cost and slow site | Free-data-use acceptance plus source/privacy constraints; responsive UI separate from scan speed |
| U06 | All success outcomes interconnected; measurement accepted | Multi-metric chain, event capture from first usage |
| U07 | First organization Al Bawaba | Personal validation then Al Bawaba adoption evidence |
| U08 | Independent dashboard and integrated CMS | Dashboard now; CMS future architecture |
| U09 | Personalization yes | R5 journalist profiles, not early multi-user build |
| U10 | Value proposition and competitors later | Business validation deferred; no uniqueness claims |
| U11 | Newsroom subscription; perhaps individuals | Commercial hypotheses, no settled price |
| U12 | Human control yes, sources yes | Human verification/decision/publication; inspectable claims |
| U13 | Do not prohibit writer analytics | Preserve option; outside first-three-month scope |
| U14 | Organization-specific performance model yes | Scoped learning, not universal traffic rules |
| U15 | White-label maybe/uncertain | Optional R5 decision |
| U16 | Exceptional discovery for first three months | Product North Star preserved |
| U17 | Rebuild allowed | Reuse is a reasoned recommendation, not a user restriction |
| U18 | English deliverables | All documents/labels in English |
| U19 | Infrastructure numbered yes answers without original questions; blank 11 | No additional permissions or technical facts invented |
| U20 | Shared newsroom versus individual queue not directly answered | Open R5 workflow decision |

The transcript's 'GitHub private repo' is inherited intent; user temporarily changed visibility to public for access. The package records actual public status without assuming a permanent change in runtime privacy. The earlier 'five stories/shift' baseline is assistant-supplied and remains unconfirmed. Marfeel capability fields are reported prior discovery, not newly tested entitlement.

## v1.0 attachment coverage

All sections 1–24 were read. Sections 1–5 map to Master 1–5; 6–8 to Master 7–10 and Contracts; 9–10 to Master 11; 11 to Master 12/Release Map R3–R4; 12–14 to Master 3,5–6; 15 to Release Map; 16–19 to R1 Execution Plan; 20 to Master 15; 21 to Risks; 22 to Master 14; 23–24 to Alignment/R1.0 and readiness verdict. Its complete table content is preserved by meaning, with conflicts explicitly resolved rather than copied blindly.

## Contradiction resolutions

Local-first supersedes remote-first default. Manual-only supersedes enabled scheduling. Up to ten supersedes 10–20 proposal. Optional angle supersedes angle-required storage. Visible labeled rumor leads supersede rigid confidence suppression. SEEN persistence means no new card, not disappearance. Deep Research is R2 rather than a dead R1 action. Numeric score is experimental; nullable scoring remains supported. Manual URL/events start R1, automated metrics R3. UI begins in the first usable slice. Date targets do not force learning before enough data exists.

## Review boundary

Coverage is checked against supplied text/document/repository only. Unprovided earlier conversations, actual local databases, the user's device, account-specific APIs and current news-source permissions remain outside the verified evidence boundary. They are open gates, not guessed facts.
