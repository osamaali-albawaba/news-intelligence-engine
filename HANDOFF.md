# Handoff

## CURRENT STATUS

Approved baseline: planning v1.1. R1.0 implementation remains complete; the latest
owner request authorized R1.1 readiness only, not implementation. Owner: Codex;
no concurrent feature owner. Branch: feat/r1-0-foundation-alignment.
Checkout: C:/Projects/news-intelligence-engine, separate from AWS evidence repo.
Readiness starting commit: 9371f7e946e6929820d0006d6e61269b6a9ac858; clean and
matching origin branch at inspection. Main remains 0900eafefd8fa8829e45a64923755f48afd220e7.
Origin: https://github.com/osamaali-albawaba/news-intelligence-engine.git.
Prior latest branch CI succeeded:
https://github.com/osamaali-albawaba/news-intelligence-engine/actions/runs/37499213225
Repository visibility is owner-controlled public; no visibility change requested.
Current readiness documentation commit/push/CI verification pending at this writing.
No R1.1 code, real collector, API service, AI, schedule, deployment or paid service enabled.

## LAST COMPLETED TASK

Prepared R1.1 readiness facts from the requested R1.0 branch. Inspected Windows
host tooling/capacity, distinguished it from another owner laptop and Ubuntu CI,
proposed News boundaries for owner review, and researched a small bilingual
source shortlist using official catalogues and access/licence documents.
Recorded permission/retention/AI unknowns separately from public access. No
publisher notification/contact or news sample/corpus acquisition occurred.

## FILES CHANGED

HANDOFF.md; docs/R1_1_READINESS.md; docs/sources/INITIAL_NEWS_SOURCE_REVIEW.md.
Documentation only. Approved nine planning files, baseline archive, code, config,
capability flags, migrations and dependency locks remain unchanged.

## WHAT WORKS

Existing R1.0 offline contracts/configuration/migration and synthetic checks.
Windows 11 host: Python 3.12.10, SQLite 3.49.1, Git, browsers, 15.7 GiB RAM,
235.1 GiB C: free. Portable Node 22.20.0/npm 10.9.3 supports contract checks;
not a durable installation. GOV.UK official Atom link and qualifying OGL reuse
basis verified. QNA bilingual and UN Arabic feed links verified from official
catalogues; this does not clear application storage/AI rights.

## KNOWN ISSUES

No launcher/API/worker/browser UI implemented. API/UI dependencies and `.venv`
absent; Node/npm not on PATH; Asia/Amman zoneinfo data unavailable. Browser
executables present, application smoke test unavailable. Intended pilot computer
and proposed News rules await owner response. Source rights, permitted sample,
retention and technical response checks incomplete; no cleared Arabic or independent
newsroom batch. UN English catalogue robots-denied and candidate feed URL not
primary-verified. UN notification/internal-tool scope unresolved; QNA reuse rights
unresolved; BBC/Al Jazeera deferred. Existing owner agreements unknown. No AI API
entitlement requested/tested; G04 belongs to R1.3. Actual owner runtime DB elsewhere
unknown. Current docs-only check/sync status recorded below after execution.

## NEXT TASK

Finish readiness documentation checks, commit/push this dedicated branch and verify
remote SHA/CI; then stop. Do not merge main or implement R1.1 automatically.
Owner reviews G01 pilot machine and G02 News rules; G03 licensed sample/first-source
scope plus bilingual/independent batch remain conditional or blocked as recorded.
After explicit implementation authorization: local Windows launcher + loopback API
+ durable single worker + minimal News SCAN NOW/progress/raw-list screen, initially
only permission-cleared GOV.UK Atom fields. Full first task and acceptance are in
docs/R1_1_READINESS.md. One English institutional source is not complete R1.1.
Keep AI/scheduling/cloud/paid services disabled; no model account/key needed now.

## TEST INSTRUCTIONS

python scripts/check_foundation.py --handoff-base 9371f7e946e6929820d0006d6e61269b6a9ac858
python -m unittest discover -s tests -v
npm run typecheck (prepend the existing portable Node folder to this shell's PATH)
git diff --check -- . ':!docs/planning'
No new implementation/tests or dependency installation required for this docs-only
task. Run existing offline regression checks and integrity/handoff guard; confirm
only the three intended Markdown paths differ from the starting commit.
Current task checks passed: foundation/baseline hash/handoff guard, all 27 Python
tests, TypeScript typecheck and tracked-file whitespace check. New Markdown
whitespace and staged scope will be checked before commit. Push/new CI: pending.
No live launcher/source/UI integration acceptance claimed.
