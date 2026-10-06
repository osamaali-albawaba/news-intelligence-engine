-- Synthetic populated v1 database for migration; no current news or credentials.
INSERT INTO sources(id,name,adapter,url,category,tier,enabled,publisher_group,poll_interval_minutes,permission_status,permissions_json)
VALUES('source','Synthetic source','fixture','https://source.example.invalid','official','primary',0,'fixture',60,'pending','{}');
INSERT INTO jobs(id,kind,scope,status,requested_at) VALUES('job','scan','legacy-global','completed','2026-01-01T00:00:00Z');
INSERT INTO scan_requests(id,job_id,trigger,requester,idempotency_key,requested_at) VALUES('request','job','manual','editor','legacy-key','2026-01-01T00:00:00Z');
INSERT INTO collection_runs(id,job_id,started_at) VALUES('run','job','2026-01-01T00:00:00Z');
INSERT INTO raw_items(id,source_id,run_id,discovered_at,payload_json,payload_hash) VALUES('raw','source','run','2026-01-01T00:00:00Z','{"synthetic":true}','raw-hash');
INSERT INTO documents(id,source_id,raw_item_id,canonical_url,headline,discovered_at,permitted_text,content_hash,access_status,publisher_group)
VALUES('document','source','raw','https://source.example.invalid/article','Synthetic report','2026-01-01T00:00:00Z','Original synthetic content','original-hash','full_text','fixture');
INSERT INTO evidence_passages(id,document_id,source_url,text,locator,content_hash,created_at)
VALUES('passage','document','https://source.example.invalid/article','Original synthetic content','paragraph 1','original-hash','2026-01-01T00:00:00Z');
INSERT INTO clusters(id,event_description,first_seen_at,last_seen_at,status) VALUES('cluster','Synthetic event','2026-01-01T00:00:00Z','2026-01-01T00:00:00Z','active');
INSERT INTO cluster_documents(cluster_id,document_id,similarity,membership_reason) VALUES('cluster','document',1,'Synthetic membership');
INSERT INTO analyses(id,cluster_id,snapshot_hash,cache_key,provider,model,prompt_version,audience_version,schema_version,created_at,summary)
VALUES('analysis','cluster','snapshot','legacy-cache','fixture','fixture-v1','prompt-v1','audience-v1','1','2026-01-01T00:00:00Z','Synthetic summary');
INSERT INTO statements(id,analysis_id,text,kind) VALUES('statement','analysis','Synthetic fact','reported_fact');
INSERT INTO statement_evidence(statement_id,passage_id,role) VALUES('statement','passage','supports');
INSERT INTO angles(id,analysis_id,title,category,why_it_could_work,verification_status,created_at)
VALUES('angle','analysis','Synthetic angle','explainer','Synthetic reason','needs_review','2026-01-01T00:00:00Z');
INSERT INTO angle_evidence(angle_id,passage_id,role) VALUES('angle','passage','supports');
INSERT INTO score_snapshots(id,angle_id,created_at,weights_version,weights_json,overall_status,overall_value,overall_basis,eligible)
VALUES('score','angle','2026-01-01T00:00:00Z','v1','{}','not_measured',NULL,'No measurement',0);
INSERT INTO score_components(snapshot_id,name,status,value,basis) VALUES('score','social_momentum','not_measured',NULL,'No connector');
INSERT INTO user_settings(user_id,audience_json,audience_version,updated_at) VALUES('editor','{}',1,'2026-01-01T00:00:00Z');
INSERT INTO feedback_events(id,user_id,angle_id,score_snapshot_id,kind,reason,created_at)
VALUES('feedback','editor','angle','score','good','Legacy reason','2026-01-01T00:00:00Z');
INSERT INTO written_articles(id,angle_id,user_id,article_url,recorded_at)
VALUES('article','angle','editor','https://publisher.example.invalid/written','2026-01-01T00:00:00Z');
