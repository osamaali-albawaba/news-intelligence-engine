import copy
from contextlib import closing
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import Mock, patch

from engine.alignment import ConfigSnapshot, ScanIntent, effective_snapshot, require_capability
from engine.cache import analysis_cache_key, score_cache_key
from engine.config import validate_config
from engine.contracts import validate_analysis
from engine.storage import migrate
import test_foundation

ROOT = Path(__file__).resolve().parents[1]


class AlignmentConfigTests(unittest.TestCase):
    def test_manual_on_scheduled_off_and_no_dispatch(self):
        configs = validate_config(ROOT / 'config')
        self.assertTrue(configs['scan']['manual']['enabled'])
        self.assertFalse(configs['scan']['scheduled']['enabled'])
        external_request = Mock()
        for capability in configs['scan']['capabilities']:
            with self.subTest(capability=capability), self.assertRaises(PermissionError):
                require_capability(configs, capability)
                external_request()
        external_request.assert_not_called()

    def test_effective_config_is_frozen_and_scope_is_compatible_only(self):
        configs = validate_config(ROOT / 'config')
        original = copy.deepcopy(configs)
        intent = ScanIntent('retry-key','news',48,5)
        snap = effective_snapshot(configs,intent)
        self.assertEqual(configs,original)
        self.assertEqual(json.loads(snap.effective_json)['intent']['freshness_hours'],48)
        self.assertEqual(json.loads(snap.effective_json)['sections']['freshness_hours'],48)
        with self.assertRaises(ValueError):
            effective_snapshot(configs,replace(intent,profile_id='unknown'))
        self.assertEqual(intent.scope_hash(snap), replace(intent,idempotency_key='other').scope_hash(snap))
        for change in ({'section':'business'},{'freshness_hours':72},{'result_limit':6}):
            other=replace(intent,**change)
            self.assertNotEqual(intent.scope_hash(snap),other.scope_hash(snap))
        other_snap=ConfigSnapshot.capture({'audience':{'regions':['different']}})
        self.assertNotEqual(intent.scope_hash(snap),intent.scope_hash(other_snap))
        configs['audience']['topics'].append('Changed after capture')
        self.assertNotIn('Changed after capture',snap.effective_json)

    def test_invalid_intent_rejected(self):
        for changes in ({'section':'technology'},{'freshness_hours':12},{'freshness_hours':True},{'result_limit':0},{'result_limit':11},{'result_limit':True}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                values = dict(idempotency_key='key',section='news',freshness_hours=24,result_limit=10)
                values.update(changes)
                ScanIntent(**values)

    def test_cache_versions_and_separate_scoring(self):
        args=dict(snapshot_hash='hash',provider='fixture',model='v1',prompt_version='v1',audience={})
        base=analysis_cache_key(**args)
        for field in ('extraction_version','translation_version','behavior_version'):
            self.assertNotEqual(base,analysis_cache_key(**args,**{field:'changed'}))
        a=score_cache_key(analysis_id='a',subject_id='story',formula_version='1',scoring_config={'freshness':1})
        b=score_cache_key(analysis_id='a',subject_id='story',formula_version='2',scoring_config={'freshness':1})
        self.assertNotEqual(a,b)
        self.assertEqual(base,analysis_cache_key(**args))

    def test_zero_angles_valid_and_summary_why_now_require_support(self):
        fixture=test_foundation.ContractTests();fixture.setUp()
        valid=replace(fixture.result,angles=())
        validate_analysis(valid,fixture.request)
        for change in ({'summary_evidence_ids':()},{'why_now':''},{'why_now_evidence_ids':(), 'why_now_observations':()}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_analysis(replace(valid,**change),fixture.request)
        with self.assertRaises(ValueError):
            validate_analysis(replace(valid,why_now_evidence_ids=(),why_now_observations=('Invented observation',)),fixture.request)
        validate_analysis(replace(valid,why_now_evidence_ids=(),why_now_observations=('Synthetic source acquisition time',)),replace(fixture.request,system_observations=('Synthetic source acquisition time',)))


class MigrationTests(unittest.TestCase):
    def populated(self,db):
        db.executescript((ROOT/'migrations/0001_foundation.sql').read_text())
        db.executescript((ROOT/'tests/fixtures/legacy_v1.sql').read_text())
        db.commit()

    def test_empty_database_and_repeat_migration(self):
        with sqlite3.connect(':memory:') as db:
            migrate(db,ROOT/'migrations');migrate(db,ROOT/'migrations')
            self.assertEqual(db.execute('SELECT version FROM schema_versions ORDER BY version').fetchall(),[(1,),(2,)])
            self.assertEqual(db.execute('PRAGMA integrity_check').fetchone()[0],'ok')

    def test_populated_v1_ids_and_history_preserved(self):
        with sqlite3.connect(':memory:') as db:
            self.populated(db)
            tables=('sources','jobs','scan_requests','raw_items','documents','evidence_passages','clusters','analyses','statements','angles','score_snapshots','feedback_events','written_articles')
            originals={t:db.execute('SELECT id FROM '+t).fetchall() for t in tables}
            migrate(db,ROOT/'migrations')
            for t in tables:
                self.assertEqual(originals[t],db.execute('SELECT id FROM '+t).fetchall())
            self.assertEqual(db.execute("SELECT text,document_version_id FROM evidence_passages WHERE id='passage'").fetchone(),('Original synthetic content','document'))
            self.assertEqual(db.execute("SELECT id,kind,reason_text FROM user_events").fetchone(),('feedback','good','Legacy reason'))
            self.assertEqual(db.execute('SELECT count(*) FROM impressions').fetchone()[0],0)
            self.assertEqual(db.execute('SELECT reconstruction_complete FROM config_snapshots').fetchone()[0],0)
            self.assertEqual(db.execute('PRAGMA foreign_key_check').fetchall(),[])

    def test_legacy_evidence_immutable_and_cross_cluster_lineage_rejected(self):
        with sqlite3.connect(':memory:') as db:
            self.populated(db);migrate(db,ROOT/'migrations')
            for sql in ("UPDATE evidence_passages SET text='Changed' WHERE id='passage'",
                        "UPDATE analyses SET summary='Changed' WHERE id='analysis'",
                        "UPDATE statements SET text='Changed' WHERE id='statement'"):
                with self.assertRaises(sqlite3.IntegrityError): db.execute(sql)
            db.execute("INSERT INTO clusters(id,event_description,first_seen_at,last_seen_at,status) VALUES('other','Other event','2026-01-01T00:00:00Z','2026-01-01T00:00:00Z','active')")
            db.execute("INSERT INTO cluster_revisions VALUES('other-rev','other',1,'Other event','Synthetic','2026-01-01T00:00:00Z')")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO recommendations(id,cluster_revision_id,angle_id,analysis_id,config_snapshot_id,summary,support_status,verification_label,created_at) VALUES('bad-rec','other-rev','angle','analysis','legacy:analysis','Mismatch','needs_review','ORIGIN UNKNOWN','2026-01-01T00:00:00Z')")

    def test_story_only_workflow_and_snapshots_survive_reload(self):
        with tempfile.TemporaryDirectory() as directory:
            file=Path(directory)/'synthetic.sqlite3'
            snap=effective_snapshot(validate_config(ROOT/'config'),ScanIntent('key','news',24,10))
            with closing(sqlite3.connect(file)) as db, db:
                self.populated(db);migrate(db,ROOT/'migrations')
                db.execute('INSERT INTO config_snapshots(id,config_hash,schema_version,effective_json,reconstruction_complete,created_at) VALUES(?,?,?,?,?,?)',('effective',snap.config_hash,2,snap.effective_json,1,'2026-01-01T01:00:00Z'))
                db.execute("INSERT INTO document_versions(id,document_id,version,headline,permitted_text,content_hash,access_status,fetched_at) VALUES('doc-v2','document',2,'Updated synthetic report','Updated content','new-hash','full_text','2026-01-01T01:00:00Z')")
                db.execute("INSERT INTO cluster_revisions VALUES('revision2','cluster',2,'Updated synthetic event','New report','2026-01-01T01:00:00Z')")
                db.execute("INSERT INTO cluster_revision_documents VALUES('revision2','doc-v2')")
                db.execute("INSERT INTO opportunity_scores(id,subject_type,cluster_revision_id,config_snapshot_id,created_at,formula_version,weights_json,overall_status,overall_basis,confidence_status) VALUES('story-score','story','revision2','effective','2026-01-01T01:00:00Z','base','{}','not_measured','Not scored','not_measured')")
                db.execute("INSERT INTO recommendations(id,cluster_revision_id,score_id,config_snapshot_id,section,summary,why_now,support_status,verification_label,created_at) VALUES('story-rec','revision2','story-score','effective','news','Synthetic story','Synthetic update','not_analyzed','UNVERIFIED','2026-01-01T01:00:00Z')")
                db.execute("INSERT INTO impressions VALUES(?,?,?,?,?,?,?,?,?,?)", ("impression","story-rec","editor","session","2026-01-01","2026-01-01T01:00:00Z",1,'{"score":null}',"2","exposure-key"))
                db.execute("INSERT INTO user_events(id,user_id,recommendation_id,impression_id,kind,reason_code,idempotency_key,created_at) VALUES('opened','editor','story-rec','impression','opened','inspect_story','event-key','2026-01-01T01:00:00Z')")
                db.execute("INSERT INTO article_records VALUES('story-article','https://publisher.example.invalid/story',NULL,'2026-01-01T01:00:00Z','editor')")
                db.execute("INSERT INTO article_recommendations VALUES('story-article','story-rec',NULL,'editor','2026-01-01T01:00:00Z')")
                for sql in ("UPDATE document_versions SET permitted_text='Overwrite' WHERE id='document'", "UPDATE config_snapshots SET effective_json='{}' WHERE id='effective'", "DELETE FROM user_events WHERE id='opened'", "UPDATE opportunity_scores SET overall_value=0 WHERE id='story-score'"):
                    with self.assertRaises(sqlite3.IntegrityError): db.execute(sql)
                with self.assertRaises(sqlite3.IntegrityError):
                    db.execute("INSERT INTO user_events(id,user_id,recommendation_id,kind,idempotency_key,created_at) VALUES('duplicate','editor','story-rec','opened','event-key','2026-01-01T01:00:00Z')")
                with self.assertRaises(sqlite3.IntegrityError):
                    db.execute("INSERT INTO opportunity_score_components(score_id,name,status,value,basis) VALUES('story-score','social_momentum','not_measured',0,'No connector')")
            with closing(sqlite3.connect(file)) as db, db:
                self.assertEqual(db.execute("SELECT angle_id FROM recommendations WHERE id='story-rec'").fetchone(),(None,))
                self.assertEqual(db.execute("SELECT effective_json FROM config_snapshots WHERE id='effective'").fetchone()[0],snap.effective_json)
                self.assertEqual(db.execute("SELECT permitted_text FROM document_versions WHERE id='document'").fetchone()[0],'Original synthetic content')
                self.assertEqual(db.execute('SELECT count(*) FROM article_recommendations WHERE angle_id IS NULL').fetchone()[0],1)
                self.assertEqual(db.execute('PRAGMA foreign_key_check').fetchall(),[])


if __name__=='__main__': unittest.main()
