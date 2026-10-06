# R1.0 Foundation Alignment checklist

Authority: owner approved planning v1.1; execution limited to R1.0. Archive and
hashes in baseline/manifest.json. Attachment text itself is unchanged; future
release instructions do not authorize their execution.

| R1.0 item | Disposition / evidence |
| --- | --- |
| Current main captured and archived | 0900eafefd8fa8829e45a64923755f48afd220e7, baseline ZIP + hash manifest |
| Nine planning files directly preserved | docs/planning, byte hashes checked offline |
| Existing docs file retained | docs/legacy/original-docs-file.txt, original bytes |
| Local-first boundaries | Root docs and decisions D015-D023; no runtime implemented |
| Manual-on/scheduled-off | config/scan.json and validator/guard tests |
| No disabled request dispatch | All capability flags false, fail-closed guard and spy test |
| Section/window/count/profile | Python intent + TS v2 request; 24/48/72, 1-10, scopes |
| Optional angle and rumor-label separation | TS card; story/angle score schema; zero-angle validation |
| Summary/Why Now support | Known evidence/system observations validation; semantic check deferred |
| Immutable evidence/config history | Migration 0002, populated fixture + on-disk reload |
| Recommendations/impressions/events/articles | Explicit lineage, optional angle, idempotent events, rank projection |
| Existing IDs and original migration | Populated v1 preservation test; 0001 unchanged |
| Snapshot reproducibility/cache | Effective JSON/hash plus extraction/translation/behavior; separate score cache |
| Null/missing metrics | Original protected tests plus new schema constraints |
| Old decisions preserved | D001-D014 retained, supersessions appended |
| No R1.1/activation | No API server/worker/UI, adapters/providers/cron/deployment added |

Related requirements: V17-V19, V24-V28, V35/V46/V53/V56/V60/V62/V71-V78/V85,
H02/H03/H06/H07/H08/H13 and R1.0 acceptance. R1-D01-D24 are release-wide criteria,
not all satisfied by this alignment. Live demonstrations and editorial utility
remain later gates. See HANDOFF for actual test/CI result, not just this checklist.

Migration rollback: untouched Git baseline plus portable archive. For an owner
runtime database, obtain a tested pre-migration backup first; no live database or
production migration was executed. Immutability is not permission to keep forbidden
text; later retention removal needs explicit tombstone/redaction design.
