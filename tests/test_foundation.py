import copy
import hashlib
import json
import math
from pathlib import Path
import sqlite3
import tempfile
import unittest
from uuid import UUID

from engine.cache import analysis_cache_key
from engine.config import validate_config
from engine.contracts import (AnalysisRequest, AnalysisResult, AngleDraft, EvidencePassage,
                              AIProvider, CollectionRequest, CollectionResult, DiscoveryItem,
                              MeasurementStatus, Metric, SourceAdapter, SourceFailure,
                              Statement, StatementKind, validate_analysis)
from scripts.check_foundation import HANDOFF_SECTIONS, validate_handoff

ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads((ROOT / 'tests/fixtures/synthetic_cluster.json').read_text())
        documents = {d['id']: d for d in self.fixture['documents']}
        passages = tuple(EvidencePassage(
            UUID(p['id']), UUID(p['document_id']), documents[p['document_id']]['url'],
            p['text'], p['locator'], hashlib.sha256(p['text'].encode()).hexdigest()
        ) for p in self.fixture['passages'])
        self.request = AnalysisRequest(UUID(self.fixture['cluster_id']), 'synthetic-hash',
                                       'fixture-v1', {'regions': []}, passages, 1000)
        statements = tuple(Statement(s['text'], StatementKind(s['kind']),
                                    tuple(UUID(i) for i in s['evidence_ids']), s['attribution'])
                           for s in self.fixture['statements'])
        angles = tuple(AngleDraft(a['title'], a['category'], a['why_it_could_work'],
                                 tuple(UUID(i) for i in a['evidence_ids']), a['verification_status'])
                       for a in self.fixture['angles'])
        self.result = AnalysisResult('Synthetic schedule change', statements, angles,
                                     ('Synthetic fixture only',), 'fixture', 'fixture-v1', None, None,
                                     summary_evidence_ids=(passages[0].id,),
                                     why_now='A newly announced synthetic change',
                                     why_now_evidence_ids=(passages[0].id,))

    def test_fixture_preserves_four_statement_kinds_and_valid_support(self):
        self.assertEqual({s.kind for s in self.result.statements}, set(StatementKind))
        validate_analysis(self.result, self.request)

    def test_dangling_evidence_rejected(self):
        from dataclasses import replace
        wrong = replace(self.result.angles[0], evidence_ids=(UUID(int=42),))
        with self.assertRaisesRegex(ValueError, 'unknown evidence'):
            validate_analysis(replace(self.result, angles=(wrong,)), self.request)

    def test_attributed_claim_requires_speaker(self):
        with self.assertRaises(ValueError):
            Statement('Claim', StatementKind.ATTRIBUTED_CLAIM, (UUID(int=1),))

    def test_missing_metrics_remain_null(self):
        for name, item in self.fixture['metrics'].items():
            metric = Metric(MeasurementStatus(item['status']), item['value'], item['basis'])
            if name in {'social_momentum', 'search_interest'}:
                self.assertIsNone(metric.value)
        with self.assertRaises(ValueError):
            Metric(MeasurementStatus.NOT_MEASURED, 0, 'Unavailable')

    def test_invalid_measured_values_rejected(self):
        for value in (None, -1, 101, math.nan, math.inf, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Metric(MeasurementStatus.MEASURED, value, 'Observed')

    def test_cache_tracks_model_prompt_evidence_and_audience(self):
        args = dict(snapshot_hash='a', provider='fixture', model='v1', prompt_version='v1',
                    audience={'regions': [], 'topics': ['business']})
        original = analysis_cache_key(**args)
        self.assertEqual(original, analysis_cache_key(**args))
        for field, value in [('snapshot_hash', 'b'), ('provider', 'other'), ('model', 'v2'),
                             ('prompt_version', 'v2'), ('audience', {'regions': ['Europe']})]:
            changed = dict(args, **{field: value})
            self.assertNotEqual(original, analysis_cache_key(**changed))

    def test_provider_can_be_substituted_without_changing_request(self):
        from dataclasses import replace
        original = self.result

        class SyntheticProvider:
            def __init__(self, name):
                self.provider_name = name
                self.model = 'synthetic'

            def analyze(self, request: AnalysisRequest) -> AnalysisResult:
                return replace(original, provider=self.provider_name, model=self.model)

        for name in ('synthetic-a', 'synthetic-b'):
            provider: AIProvider = SyntheticProvider(name)
            result = provider.analyze(self.request)
            validate_analysis(result, self.request)
            self.assertEqual(result.provider, name)

    def test_source_contract_allows_partial_results_and_isolated_failure(self):
        class SyntheticSource:
            adapter_name = 'synthetic_fixture'

            def collect(self, request: CollectionRequest) -> CollectionResult:
                item = DiscoveryItem(UUID(int=2), request.source_id, 'Synthetic headline',
                                     'https://source.example.invalid/item', '2026-01-01T00:00:00Z',
                                     None, None, 'Synthetic snippet', None, 'snippet_only', 'en')
                return CollectionResult((item,), None, SourceFailure('timeout', 'Synthetic timeout', True))

        adapter: SourceAdapter = SyntheticSource()
        result = adapter.collect(CollectionRequest('synthetic', None, 1, UUID(int=1)))
        self.assertEqual(len(result.items), 1)
        self.assertTrue(result.failure.retryable)


class HandoffTests(unittest.TestCase):
    def test_required_sections_present(self):
        validate_handoff((ROOT / 'HANDOFF.md').read_text(encoding='utf-8'))

    def test_missing_or_empty_section_rejected(self):
        text = '\n'.join(f'## {section}\nCompleted\n' for section in HANDOFF_SECTIONS)
        for section in HANDOFF_SECTIONS:
            with self.subTest(section=section), self.assertRaises(ValueError):
                validate_handoff(text.replace(f'## {section}\nCompleted\n', f'## {section}\n'))


class ConfigTests(unittest.TestCase):
    def test_defaults_are_offline_and_audience_is_unrestricted(self):
        configs = validate_config(ROOT / 'config')
        self.assertFalse(configs['scan']['execution_enabled'])
        self.assertFalse(any(s['enabled'] for s in configs['sources']['sources']))
        self.assertEqual(configs['audience']['regions'], [])

    def test_many_sources_without_fixed_twenty_source_cap(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for path in (ROOT / 'config').glob('*.json'):
                (target / path.name).write_text(path.read_text(), encoding='utf-8')
            sources = json.loads((target / 'sources.example.json').read_text())
            template = sources['sources'][0]
            sources['sources'] = [dict(copy.deepcopy(template), id=f'source-{i}') for i in range(500)]
            (target / 'sources.example.json').write_text(json.dumps(sources))
            self.assertEqual(len(validate_config(target)['sources']['sources']), 500)

    def test_unreviewed_source_cannot_be_enabled(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for path in (ROOT / 'config').glob('*.json'):
                (target / path.name).write_text(path.read_text(), encoding='utf-8')
            sources = json.loads((target / 'sources.example.json').read_text())
            sources['sources'][0]['enabled'] = True
            (target / 'sources.example.json').write_text(json.dumps(sources))
            with self.assertRaisesRegex(ValueError, 'approved permission'):
                validate_config(target)


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.executescript((ROOT / 'migrations/0001_foundation.sql').read_text())
        self.db.execute("INSERT INTO clusters VALUES ('cluster','Synthetic','2026-01-01T00:00:00Z','2026-01-01T00:00:00Z','active')")
        self.db.execute("INSERT INTO analyses VALUES ('analysis','cluster','hash','cache','fixture','v1','v1','1','1','2026-01-01T00:00:00Z','Synthetic','[]',NULL,NULL)")
        self.db.execute("INSERT INTO angles VALUES ('angle','analysis','Synthetic angle','explainer','Synthetic reason','needs_review','2026-01-01T00:00:00Z')")
        self.db.execute("INSERT INTO score_snapshots VALUES ('score','angle','2026-01-01T00:00:00Z','v1','{}','not_measured',NULL,'Missing input',0)")

    def tearDown(self):
        self.db.close()

    def test_migration_integrity(self):
        self.assertEqual(self.db.execute('PRAGMA integrity_check').fetchone()[0], 'ok')
        self.assertEqual(self.db.execute('PRAGMA foreign_key_check').fetchall(), [])

    def test_metric_null_constraints(self):
        self.db.execute("INSERT INTO score_components VALUES ('score','social_momentum','not_measured',NULL,'No connector')")
        for status, value in [('not_measured', 0), ('measured', None), ('estimated', 101)]:
            with self.subTest(status=status, value=value), self.assertRaises(sqlite3.IntegrityError):
                self.db.execute('INSERT INTO score_components VALUES (?,?,?,?,?)',
                                ('score', 'search_interest', status, value, 'Test'))

    def test_scan_triggers_share_active_job_and_retry_identity(self):
        self.db.execute("INSERT INTO jobs(id,kind,scope,requested_at) VALUES ('job','scan','global','2026-01-01T00:00:00Z')")
        for trigger in ('manual', 'scheduled'):
            self.db.execute('INSERT INTO scan_requests VALUES (?,?,?,?,?,?)',
                            (trigger, 'job', trigger, 'editor' if trigger == 'manual' else 'scheduler',
                             trigger + '-key', '2026-01-01T00:00:00Z'))
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO jobs(id,kind,scope,requested_at) VALUES ('duplicate','scan','global','2026-01-01T00:00:00Z')")
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO scan_requests VALUES ('retry','job','manual','editor','manual-key','2026-01-01T00:00:00Z')")
        self.db.execute("UPDATE jobs SET status='completed' WHERE id='job'")
        self.db.execute("INSERT INTO jobs(id,kind,scope,requested_at) VALUES ('next','scan','global','2026-01-01T01:00:00Z')")

    def test_attributed_claim_constraint(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO statements VALUES ('s','analysis','Test','attributed_claim',NULL)")

    def test_feedback_is_append_only(self):
        self.db.execute("INSERT INTO user_settings VALUES ('editor','{}',1,'{}','2026-01-01T00:00:00Z')")
        self.db.execute("INSERT INTO feedback_events VALUES ('feedback','editor','angle','score','good',NULL,'2026-01-01T00:00:00Z')")
        for sql in ("UPDATE feedback_events SET kind='bad' WHERE id='feedback'",
                    "DELETE FROM feedback_events WHERE id='feedback'"):
            with self.assertRaises(sqlite3.IntegrityError):
                self.db.execute(sql)


if __name__ == '__main__':
    unittest.main()
