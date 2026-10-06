-- v1.1 additive lineage. 0001 is unchanged and legacy rows remain intact.
-- Existing IDs are reused only in distinct version tables for initial backfill.
-- No exposure, source rights or full historical config is invented by migration.
BEGIN IMMEDIATE;
CREATE TABLE organizations (id TEXT PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE workspace_context (
 user_id TEXT PRIMARY KEY REFERENCES user_settings(user_id),
 organization_id TEXT NOT NULL REFERENCES organizations(id),
 timezone TEXT NOT NULL, active_day TEXT
);
CREATE TABLE config_snapshots (
 id TEXT PRIMARY KEY, config_hash TEXT NOT NULL UNIQUE, schema_version INTEGER NOT NULL,
 profile_id TEXT, effective_json TEXT NOT NULL CHECK(json_valid(effective_json)),
 reconstruction_complete INTEGER NOT NULL CHECK(reconstruction_complete IN (0,1)),
 parent_id TEXT REFERENCES config_snapshots(id), created_at TEXT NOT NULL
);
-- Legacy config is explicitly incomplete: version labels cannot reconstruct it.
INSERT INTO config_snapshots(id,config_hash,schema_version,effective_json,reconstruction_complete,created_at)
 SELECT 'legacy:'||id,'legacy:'||id,1,
 json_object('audience_version',audience_version,'prompt_version',prompt_version,'legacy_analysis_id',id),0,created_at
 FROM analyses;
CREATE TABLE source_versions (
 id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(id), version INTEGER NOT NULL,
 config_json TEXT NOT NULL CHECK(json_valid(config_json)), created_at TEXT,
 UNIQUE(source_id,version)
);
INSERT INTO source_versions(id,source_id,version,config_json)
 SELECT id,id,1,json_object('name',name,'adapter',adapter,'url',url,'category',category,'tier',tier,
 'publisher_group',publisher_group,'syndication_origin',syndication_origin,'enabled',enabled,
 'languages',json(languages_json),'regions',json(regions_json),'topics',json(topics_json),
 'permissions',json(permissions_json),'permission_status',permission_status,
 'poll_interval_minutes',poll_interval_minutes,'priority',priority) FROM sources;
CREATE TABLE acquisition_observations (
 id TEXT PRIMARY KEY, source_version_id TEXT NOT NULL REFERENCES source_versions(id),
 run_id TEXT NOT NULL REFERENCES collection_runs(id), observed_at TEXT NOT NULL,
 status TEXT NOT NULL CHECK(status IN ('success','revalidated','partial','failed')),
 error_code TEXT, details_json TEXT NOT NULL CHECK(json_valid(details_json))
);
CREATE TABLE document_versions (
 id TEXT PRIMARY KEY, document_id TEXT NOT NULL REFERENCES documents(id), version INTEGER NOT NULL,
 raw_item_id TEXT REFERENCES raw_items(id) ON DELETE SET NULL,
 headline TEXT NOT NULL, snippet TEXT, permitted_text TEXT, content_hash TEXT NOT NULL,
 language TEXT, access_status TEXT NOT NULL CHECK(access_status IN ('full_text','excerpt','snippet_only','unavailable')),
 published_at TEXT, fetched_at TEXT NOT NULL, updated_at TEXT, retention_until TEXT,
 UNIQUE(document_id,version), UNIQUE(document_id,content_hash)
);
INSERT INTO document_versions(id,document_id,version,raw_item_id,headline,snippet,permitted_text,content_hash,
 language,access_status,published_at,fetched_at,retention_until)
 SELECT id,id,1,raw_item_id,headline,snippet,permitted_text,content_hash,language,access_status,
 published_at,discovered_at,retention_until FROM documents;
ALTER TABLE evidence_passages ADD COLUMN document_version_id TEXT REFERENCES document_versions(id);
UPDATE evidence_passages SET document_version_id=document_id;
CREATE TABLE evidence_availability (
 passage_id TEXT NOT NULL REFERENCES evidence_passages(id), recorded_at TEXT NOT NULL,
 state TEXT NOT NULL CHECK(state IN ('available','expired','removed','source_unavailable')),
 reason TEXT NOT NULL, PRIMARY KEY(passage_id,recorded_at)
);
CREATE TABLE cluster_revisions (
 id TEXT PRIMARY KEY, cluster_id TEXT NOT NULL REFERENCES clusters(id), revision INTEGER NOT NULL,
 event_description TEXT NOT NULL, change_reason TEXT NOT NULL, created_at TEXT NOT NULL,
 UNIQUE(cluster_id,revision)
);
INSERT INTO cluster_revisions(id,cluster_id,revision,event_description,change_reason,created_at)
 SELECT id,id,1,event_description,'legacy baseline',last_seen_at FROM clusters;
CREATE TABLE cluster_revision_documents (
 revision_id TEXT NOT NULL REFERENCES cluster_revisions(id),
 document_version_id TEXT NOT NULL REFERENCES document_versions(id),
 PRIMARY KEY(revision_id,document_version_id)
);
INSERT INTO cluster_revision_documents SELECT cluster_id,document_id FROM cluster_documents;
ALTER TABLE analyses ADD COLUMN cluster_revision_id TEXT REFERENCES cluster_revisions(id);
ALTER TABLE analyses ADD COLUMN config_snapshot_id TEXT REFERENCES config_snapshots(id);
UPDATE analyses SET cluster_revision_id=cluster_id, config_snapshot_id='legacy:'||id;
CREATE TABLE scan_request_context (
 request_id TEXT PRIMARY KEY REFERENCES scan_requests(id), schema_version INTEGER NOT NULL,
 section TEXT NOT NULL CHECK(section IN ('news','business','the_node')),
 freshness_hours INTEGER NOT NULL CHECK(freshness_hours IN (24,48,72)),
 result_limit INTEGER NOT NULL CHECK(result_limit BETWEEN 1 AND 10),
 config_snapshot_id TEXT NOT NULL REFERENCES config_snapshots(id),
 payload_hash TEXT NOT NULL, scope_hash TEXT NOT NULL
);
-- Legacy requests lack section/effective config: no context is fabricated.
CREATE TABLE opportunity_scores (
 id TEXT PRIMARY KEY, subject_type TEXT NOT NULL CHECK(subject_type IN ('story','angle')),
 cluster_revision_id TEXT NOT NULL REFERENCES cluster_revisions(id),
 angle_id TEXT REFERENCES angles(id), config_snapshot_id TEXT NOT NULL REFERENCES config_snapshots(id),
 created_at TEXT NOT NULL, formula_version TEXT NOT NULL,
 weights_json TEXT NOT NULL CHECK(json_valid(weights_json)),
 overall_status TEXT NOT NULL CHECK(overall_status IN ('measured','estimated','not_measured')),
 overall_value REAL, overall_basis TEXT NOT NULL,
 confidence_status TEXT NOT NULL CHECK(confidence_status IN ('measured','estimated','not_measured')),
 confidence_value REAL,
 CHECK((subject_type='story' AND angle_id IS NULL) OR (subject_type='angle' AND angle_id IS NOT NULL)),
 CHECK((overall_status='not_measured' AND overall_value IS NULL) OR
       (overall_status IN ('measured','estimated') AND overall_value IS NOT NULL AND overall_value BETWEEN 0 AND 100)),
 CHECK((confidence_status='not_measured' AND confidence_value IS NULL) OR
       (confidence_status IN ('measured','estimated') AND confidence_value IS NOT NULL AND confidence_value BETWEEN 0 AND 100))
);
INSERT INTO opportunity_scores
 SELECT s.id,'angle',a.cluster_revision_id,s.angle_id,a.config_snapshot_id,s.created_at,s.weights_version,
 s.weights_json,s.overall_status,s.overall_value,s.overall_basis,'not_measured',NULL
 FROM score_snapshots s JOIN angles g ON g.id=s.angle_id JOIN analyses a ON a.id=g.analysis_id;
CREATE TABLE opportunity_score_components (
 score_id TEXT NOT NULL REFERENCES opportunity_scores(id), name TEXT NOT NULL,
 status TEXT NOT NULL CHECK(status IN ('measured','estimated','not_measured')),
 value REAL, basis TEXT NOT NULL CHECK(length(trim(basis))>0), observed_at TEXT,
 methodology TEXT, unit TEXT NOT NULL DEFAULT 'index_0_100', PRIMARY KEY(score_id,name),
 CHECK((status='not_measured' AND value IS NULL) OR
       (status IN ('measured','estimated') AND value IS NOT NULL AND value BETWEEN 0 AND 100))
);
INSERT INTO opportunity_score_components(score_id,name,status,value,basis)
 SELECT snapshot_id,name,status,value,basis FROM score_components;
CREATE TABLE recommendations (
 id TEXT PRIMARY KEY, cluster_revision_id TEXT NOT NULL REFERENCES cluster_revisions(id),
 angle_id TEXT REFERENCES angles(id), analysis_id TEXT REFERENCES analyses(id),
 score_id TEXT REFERENCES opportunity_scores(id), config_snapshot_id TEXT NOT NULL REFERENCES config_snapshots(id),
 section TEXT CHECK(section IN ('news','business','the_node')),
 summary TEXT NOT NULL, why_now TEXT,
 support_status TEXT NOT NULL CHECK(support_status IN ('supported','needs_review','unconfirmed','not_analyzed')),
 verification_label TEXT NOT NULL CHECK(verification_label IN ('VERIFIED','REPORTED','SINGLE SOURCE','UNVERIFIED','ORIGIN UNKNOWN')),
 risks_json TEXT NOT NULL DEFAULT '[]' CHECK(json_valid(risks_json)),
 created_at TEXT NOT NULL
);
-- Historical angle-associated actions gain an explicit legacy recommendation.
-- Unknown section, score-at-exposure and Why Now stay null, not reconstructed.
INSERT INTO recommendations(id,cluster_revision_id,angle_id,analysis_id,config_snapshot_id,summary,
 support_status,verification_label,created_at)
 SELECT g.id,a.cluster_revision_id,g.id,a.id,a.config_snapshot_id,a.summary,
 g.verification_status,'ORIGIN UNKNOWN',g.created_at FROM angles g JOIN analyses a ON a.id=g.analysis_id;
CREATE TABLE recommendation_support (
 recommendation_id TEXT NOT NULL REFERENCES recommendations(id),
 field TEXT NOT NULL CHECK(field IN ('summary','why_now','risk','angle_rationale')),
 passage_id TEXT NOT NULL REFERENCES evidence_passages(id),
 role TEXT NOT NULL CHECK(role IN ('supports','contradicts','context')),
 PRIMARY KEY(recommendation_id,field,passage_id,role)
);
CREATE TABLE recommendation_observations (
 recommendation_id TEXT NOT NULL REFERENCES recommendations(id),
 field TEXT NOT NULL CHECK(field IN ('summary','why_now','risk')),
 basis TEXT NOT NULL, observed_at TEXT NOT NULL,
 PRIMARY KEY(recommendation_id,field,basis)
);
CREATE TABLE impressions (
 id TEXT PRIMARY KEY, recommendation_id TEXT NOT NULL REFERENCES recommendations(id),
 user_id TEXT NOT NULL REFERENCES user_settings(user_id), session_id TEXT NOT NULL,
 active_day TEXT NOT NULL, displayed_at TEXT NOT NULL, rank INTEGER NOT NULL CHECK(rank>0),
 projection_json TEXT NOT NULL CHECK(json_valid(projection_json)), render_version TEXT NOT NULL,
 idempotency_key TEXT NOT NULL, UNIQUE(user_id,idempotency_key)
);
CREATE TABLE user_events (
 id TEXT PRIMARY KEY, user_id TEXT NOT NULL REFERENCES user_settings(user_id),
 recommendation_id TEXT NOT NULL REFERENCES recommendations(id),
 impression_id TEXT REFERENCES impressions(id), angle_id TEXT REFERENCES angles(id),
 score_id TEXT REFERENCES opportunity_scores(id),
 kind TEXT NOT NULL CHECK(kind IN ('good','bad','saved','rejected','written','opened','selected','writing','published','skipped','correction')),
 reason_code TEXT, reason_text TEXT, compensates_event_id TEXT REFERENCES user_events(id),
 idempotency_key TEXT NOT NULL, created_at TEXT NOT NULL, UNIQUE(user_id,idempotency_key)
);
INSERT INTO user_events(id,user_id,recommendation_id,angle_id,score_id,kind,reason_text,idempotency_key,created_at)
 SELECT id,user_id,angle_id,angle_id,score_snapshot_id,kind,reason,'legacy:'||id,created_at FROM feedback_events;
CREATE TABLE article_records (
 id TEXT PRIMARY KEY, canonical_url TEXT NOT NULL UNIQUE, published_at TEXT,
 recorded_at TEXT NOT NULL, user_id TEXT NOT NULL REFERENCES user_settings(user_id)
);
INSERT INTO article_records SELECT id,article_url,published_at,recorded_at,user_id FROM written_articles;
CREATE TABLE article_recommendations (
 article_id TEXT NOT NULL REFERENCES article_records(id),
 recommendation_id TEXT NOT NULL REFERENCES recommendations(id), angle_id TEXT REFERENCES angles(id),
 confirmed_by TEXT NOT NULL REFERENCES user_settings(user_id), linked_at TEXT NOT NULL,
 PRIMARY KEY(article_id,recommendation_id)
);
INSERT INTO article_recommendations SELECT id,angle_id,angle_id,user_id,recorded_at FROM written_articles;
CREATE INDEX recommendations_section_time ON recommendations(section,created_at);
CREATE INDEX events_recommendation ON user_events(recommendation_id,created_at);
CREATE INDEX revisions_document ON document_versions(document_id,version);
INSERT INTO schema_versions VALUES(2,strftime('%Y-%m-%dT%H:%M:%SZ','now'));
CREATE TRIGGER config_snapshots_no_update BEFORE UPDATE ON config_snapshots BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER config_snapshots_no_delete BEFORE DELETE ON config_snapshots BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER source_versions_no_update BEFORE UPDATE ON source_versions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER source_versions_no_delete BEFORE DELETE ON source_versions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER document_versions_no_update BEFORE UPDATE ON document_versions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER document_versions_no_delete BEFORE DELETE ON document_versions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER cluster_revisions_no_update BEFORE UPDATE ON cluster_revisions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER cluster_revisions_no_delete BEFORE DELETE ON cluster_revisions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER cluster_revision_documents_no_update BEFORE UPDATE ON cluster_revision_documents BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER cluster_revision_documents_no_delete BEFORE DELETE ON cluster_revision_documents BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER opportunity_scores_no_update BEFORE UPDATE ON opportunity_scores BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER opportunity_scores_no_delete BEFORE DELETE ON opportunity_scores BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER opportunity_score_components_no_update BEFORE UPDATE ON opportunity_score_components BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER opportunity_score_components_no_delete BEFORE DELETE ON opportunity_score_components BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER recommendations_no_update BEFORE UPDATE ON recommendations BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER recommendations_no_delete BEFORE DELETE ON recommendations BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER recommendation_support_no_update BEFORE UPDATE ON recommendation_support BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER recommendation_support_no_delete BEFORE DELETE ON recommendation_support BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER recommendation_observations_no_update BEFORE UPDATE ON recommendation_observations BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER recommendation_observations_no_delete BEFORE DELETE ON recommendation_observations BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER impressions_no_update BEFORE UPDATE ON impressions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER impressions_no_delete BEFORE DELETE ON impressions BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER user_events_no_update BEFORE UPDATE ON user_events BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER user_events_no_delete BEFORE DELETE ON user_events BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER article_recommendations_no_update BEFORE UPDATE ON article_recommendations BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER article_recommendations_no_delete BEFORE DELETE ON article_recommendations BEGIN SELECT RAISE(ABORT,'Immutable snapshot/event'); END;
CREATE TRIGGER analyses_no_update BEFORE UPDATE ON analyses BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER analyses_no_delete BEFORE DELETE ON analyses BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER evidence_passages_no_update BEFORE UPDATE ON evidence_passages BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER evidence_passages_no_delete BEFORE DELETE ON evidence_passages BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER statements_no_update BEFORE UPDATE ON statements BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER statements_no_delete BEFORE DELETE ON statements BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER statement_evidence_no_update BEFORE UPDATE ON statement_evidence BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER statement_evidence_no_delete BEFORE DELETE ON statement_evidence BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER angles_no_update BEFORE UPDATE ON angles BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER angles_no_delete BEFORE DELETE ON angles BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER angle_evidence_no_update BEFORE UPDATE ON angle_evidence BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER angle_evidence_no_delete BEFORE DELETE ON angle_evidence BEGIN SELECT RAISE(ABORT,'Immutable evidence/analysis'); END;
CREATE TRIGGER document_version_passage_match BEFORE INSERT ON evidence_passages
WHEN NEW.document_version_id IS NULL OR NOT EXISTS(
 SELECT 1 FROM document_versions WHERE id=NEW.document_version_id AND document_id=NEW.document_id)
BEGIN SELECT RAISE(ABORT,'Passage requires matching immutable document version'); END;
CREATE TRIGGER recommendation_lineage BEFORE INSERT ON recommendations
WHEN (NEW.analysis_id IS NOT NULL AND NOT EXISTS(
 SELECT 1 FROM analyses WHERE id=NEW.analysis_id AND cluster_revision_id=NEW.cluster_revision_id))
 OR (NEW.angle_id IS NOT NULL AND NOT EXISTS(
 SELECT 1 FROM angles g JOIN analyses a ON a.id=g.analysis_id
 WHERE g.id=NEW.angle_id AND a.cluster_revision_id=NEW.cluster_revision_id
 AND (NEW.analysis_id IS NULL OR g.analysis_id=NEW.analysis_id)))
 OR (NEW.score_id IS NOT NULL AND NOT EXISTS(
 SELECT 1 FROM opportunity_scores WHERE id=NEW.score_id AND cluster_revision_id=NEW.cluster_revision_id))
BEGIN SELECT RAISE(ABORT,'Recommendation lineage mismatch'); END;
CREATE TRIGGER event_lineage BEFORE INSERT ON user_events
WHEN (NEW.impression_id IS NOT NULL AND NOT EXISTS(
 SELECT 1 FROM impressions WHERE id=NEW.impression_id AND recommendation_id=NEW.recommendation_id AND user_id=NEW.user_id))
 OR (NEW.angle_id IS NOT NULL AND NOT EXISTS(
 SELECT 1 FROM recommendations WHERE id=NEW.recommendation_id AND angle_id=NEW.angle_id))
 OR (NEW.score_id IS NOT NULL AND NOT EXISTS(
 SELECT 1 FROM recommendations r JOIN opportunity_scores s ON s.cluster_revision_id=r.cluster_revision_id
 WHERE r.id=NEW.recommendation_id AND s.id=NEW.score_id))
BEGIN SELECT RAISE(ABORT,'Event lineage mismatch'); END;
COMMIT;
