# R1.1 readiness review

Reviewed 2026-10-06, from `feat/r1-0-foundation-alignment` at
`9371f7e946e6929820d0006d6e61269b6a9ac858`.
This is readiness documentation requested by the owner, not authorization to
implement R1.1. The approved v1.1 plans and R1.0 architecture remain the baseline.
No dependencies were installed, services started, source adapters enabled, runtime
database created or main branch merged during this review.

## Inspected environment: G01

These are facts about the Windows execution host accessible to this session.
This is not a Codex Cloud Linux environment. They do not establish the capabilities
of another laptop, nor confirm that this host is the intended pilot machine.
GitHub Actions uses a separate Ubuntu runner; a passing CI check does not demonstrate
that a double-click Windows launcher or browser UI works on the owner's computer.

| Area | Observed | Readiness / remaining work |
| --- | --- | --- |
| OS | Windows 11 Pro, 10.0.26200, 64-bit; PowerShell | Windows launcher is a viable first target; owner pilot-machine confirmation pending. |
| Memory / disk | 15.7 GiB RAM; C: 235.1 GiB free of 475.9 GiB | No hardware purchase indicated for the proposed API/SQLite/UI slice. No local-model capacity or measured runtime performance claim. |
| Python | 3.12.10; pip 25.0.1; standard venv available | Meets project Python floor. No project `.venv`; create one during authorized implementation. |
| Python executable | `C:/Users/MCC/AppData/Local/Programs/Python/Python312/python.exe` | Launcher should resolve its own project environment rather than depend on this user's absolute path. |
| SQLite / tests | SQLite 3.49.1; stdlib unittest available | Existing offline migrations/tests runnable; runtime worker not implemented. |
| Node / npm | Absent from PATH; existing portable Node 22.20.0 / npm 10.9.3 under `C:/Users/MCC/AppData/Local/Temp/nie-r1-tooling/node-v22.20.0-win-x64/` | Sufficient for current contract checks. Temporary location is not a durable launcher prerequisite. Use durable free tooling or a prebuilt UI before pilot reliance. No global install performed. |
| API dependencies | fastapi, uvicorn, httpx, feedparser not importable | FastAPI/Uvicorn remain candidates, not installed or locked. Select only needed free dependencies and lock them in implementation; do not install speculative packages now. |
| UI dependencies | Only TypeScript 5.9.3 locked; React/Vite absent | No dashboard implementation exists. Browser users should consume built assets; a Vite development server is not the eventual everyday launcher. |
| Timezone | `ZoneInfo('Asia/Amman')` raises ZoneInfoNotFoundError; tzdata absent | Add a locked timezone-data dependency or equivalent verified support during implementation; UTC storage is separate from workspace-day display. |
| Browser | Chrome and Edge executables present in standard Program Files locations | Availability verified; browser launch/loopback interaction not tested because no application exists. |
| Git | Installed; requested branch and its origin ref agree at starting SHA | Foundation clean at review start; preserve branch/history. |
| Runtime files | No launcher/API handlers/worker/UI or project `.venv` | Expected implementation work, not evidence of a broken existing application. No owner runtime DB supplied or searched for elsewhere. |

Startup constraints to prove in R1.1: bind only to loopback; validate local session
and Origin before mutations; one durable worker; safe startup/restart and occupied
port errors; launcher resolves project paths (including spaces), checks prerequisites,
opens a normal browser and exposes useful failure messages. A sleeping/offline device
will not collect news. Current 120-second budgets are proposals, not a measured SLA.
No ports, firewall rules, background startup tasks or power settings were changed.

## News first: G02 owner-review proposal

Status: proposed, awaiting owner review. Configuration remains `definition_status:
pending`; this document does not silently approve or hardcode section rules.
News is a good first section because it directly serves the breaking-news shift
workflow while Business and The Node still need separate scope definitions.

| Decision | Proposed rule |
| --- | --- |
| Include | Politics, elections, diplomacy, conflict/security, humanitarian crises, major disasters, and consequential public-interest health/climate developments. |
| Geography | Worldwide; select by the configurable audience profile, significance and freshness. No permanent Middle East or international-only restriction. |
| Event threshold | A concrete new event, decision, disclosure, material update or well-attributed lead; background alone is insufficient. Official announcements are attributed to their issuer, not independently established facts. |
| Exclude | Routine company earnings/markets/investment advice, consumer gadgets/product launches, celebrity/entertainment, routine sport, lifestyle, shopping and promotional material. Do not route exclusions into an unconfirmed The Node taxonomy. |
| Cross-section cases | Sanctions, a financial collapse affecting public services, a cyberattack on critical infrastructure or a major sports governance/security scandal can qualify through their public-interest event, not merely their commercial/technology/sport subject. |
| Rumors / opinion | A traceable attributed unverified lead can remain visible with SINGLE SOURCE/UNVERIFIED labels. No anonymous unsourced viral rumor acquisition. Opinion is context and labeled interpretation; it does not prove the event. |
| Freshness / count | Proposed default 24 hours, selectable 24/48/72; up to ten relevant results without padding. Unknown publication time remains unknown and cannot silently pass the freshness filter. |
| Languages / presentation | Arabic and English discovery, English interface/output. Keep original Arabic title/excerpt and language visible; English translation is a separate labeled derivative, not an assumed AI capability in R1.1. |

R1.1 raw rows must say 'not yet analyzed'. They must not imply verified claims,
AI summaries, angles or scores. Preserve reported fact, attributed claim,
editorial interpretation and possible consequence. Social/search/performance remain
not_measured with null values. A source link and attribution are always inspectable.

## Source readiness: G03

The [initial source dossier](sources/INITIAL_NEWS_SOURCE_REVIEW.md) records a small
five-feed research shortlist: GOV.UK English, UN News Arabic/English, and QNA
General Arabic/English. It also records BBC and Al Jazeera deferrals. These are
candidates, not an enabled source registry. Language editions of one publisher
are one origin; official sources cannot substitute for independent reporting.

GOV.UK provides the strongest documented no-cost reuse basis for a first English
adapter, limited to qualifying licensed text with attribution and exclusions.
Its officially linked Atom URL was verified from the catalogue; no feed items
were collected or stored. Representative permitted content and response behavior
still need an authorized bounded demonstration before G03 is fully accepted.
UN and QNA remain conditional/blocked for this application's storage/use scope.
No current permission-cleared Arabic batch or independent newsroom batch has been
established. A free feed URL is not evidence of free professional reuse rights.

## READY / BLOCKED prerequisites

| Prerequisite | Status | Exact next evidence |
| --- | --- | --- |
| R1.0 baseline / history / contracts | READY | Prior local and branch CI checks passed; approved planning bytes preserved. |
| G01 inspected Windows host | READY for development preparation; pilot target unresolved | Owner confirms same machine or another target. Durable Node location, project environment/dependency locks, timezone data and launcher/browser smoke proof belong to implementation. |
| G02 first section | BLOCKED pending owner review | Confirm News inclusion/exclusion above or identify changes; Business/The Node do not block a confirmed News-only slice. |
| G03 first adapter | CONDITIONAL | GOV.UK licensed-field review and bounded permitted sample/HTTP behavior after implementation authorization. No source enabled now. |
| G03 bilingual / independent-origin batch | BLOCKED | Clarify UN notification and internal storage scope or existing no-cost rights; QNA no-cost permission; verify exact current endpoints/robots/retention. Add a permission-cleared independent newsroom origin before declaring the batch representative. |
| R1.1 implementation authorization | BLOCKED by current scope | Owner explicitly authorizes implementation after reviewing this report. Readiness work alone does not open this gate. |
| Free-only operating boundary | READY | No paid dependencies/services, AI entitlement or cloud account needed for the raw local slice. All live capability flags remain false. |
| G04 AI entitlement | DEFERRED to R1.3 | Do not request keys, enable billing or test an AI API for R1.1 readiness. |
| G05 editorial baseline / G06 off-device recovery | DEFERRED to later pilot gates | Existing plan applies; neither is silently accepted or a reason to repeat the plan now. |

Only owner-specific unknowns were asked: News rules, intended pilot computer and
whether an existing no-cost publisher agreement covers the internal tool. Replies
not yet received are recorded as unresolved, never inferred from elapsed time.

## Exact first implementation task, after authorization

Implement the **Windows local News scan vertical slice** from this branch: one
double-click launcher serving built browser assets and a loopback Python API,
SQLite-backed durable single-worker scan admission/progress, and a News screen
with SCAN NOW, progress, raw 'not yet analyzed' rows and original source links.
Use only the first permission-cleared GOV.UK Atom adapter initially; confirm its
permitted sample and content fields before dispatch. Persist effective News intent,
normalized URLs/timestamps/language and allowed signal/document versions before
advancing the source cursor. Make requests idempotent, enforce budgets/timeouts/
conditional requests/backoff, and isolate source errors. Lock only the free runtime
and UI dependencies actually used. Do not activate other sections, AI, scheduling,
paid services or deployment. Grow the bilingual/independent batch only as rights
and endpoints pass G03; a one-source English demonstration is not complete R1.1.

First acceptance demonstration: launch without developer tools, press SCAN NOW,
observe committed progress and raw permitted rows, open their sources, reload and
see persisted state. Verify replay does not unnecessarily recollect and a simulated
second-source timeout preserves results. No artificial score or angle is produced.
No implementation or live integration acceptance is claimed by this review.
