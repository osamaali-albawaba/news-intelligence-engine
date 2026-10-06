-- SQLite-compatible D1 foundation. IDs are application-generated UUIDs.
-- All times use UTC ISO-8601 strings. No secrets or live-source data here.
PRAGMA foreign_keys = ON;

CREATE TABLE schema_versions (
    version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL
);
INSERT INTO schema_versions VALUES (1, strftime('%Y-%m-%dT%H:%M:%SZ', 'now'));

CREATE TABLE sources (
    id TEXT PRIMARY KEY, name TEXT NOT NULL, adapter TEXT NOT NULL,
    url TEXT NOT NULL, category TEXT NOT NULL, tier TEXT NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 0 CHECK (enabled IN (0,1)),
    publisher_group TEXT NOT NULL, syndication_origin TEXT,
    poll_interval_minutes INTEGER NOT NULL CHECK (poll_interval_minutes > 0),
    priority INTEGER NOT NULL DEFAULT 50,
    languages_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(languages_json)),
    regions_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(regions_json)),
    topics_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(topics_json)),
    permission_status TEXT NOT NULL CHECK (permission_status IN ('pending','approved','denied')),
    permissions_json TEXT NOT NULL CHECK (json_valid(permissions_json)),
    cursor TEXT, last_success_at TEXT,
    CHECK (enabled = 0 OR permission_status = 'approved')
);
CREATE INDEX sources_classification ON sources(category, tier, enabled);
CREATE INDEX sources_due ON sources(enabled, last_success_at, priority);

CREATE TABLE user_settings (
    user_id TEXT PRIMARY KEY, audience_json TEXT NOT NULL CHECK (json_valid(audience_json)),
    audience_version INTEGER NOT NULL, preferences_json TEXT NOT NULL DEFAULT '{}' CHECK (json_valid(preferences_json)),
    updated_at TEXT NOT NULL
);

CREATE TABLE jobs (
    id TEXT PRIMARY KEY, kind TEXT NOT NULL CHECK (kind IN ('scan','deep_analysis')),
    scope TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'queued'
      CHECK (status IN ('queued','running','completed','partial','failed','cancelled')),
    requested_at TEXT NOT NULL, started_at TEXT, finished_at TEXT,
    lease_owner TEXT, lease_expires_at TEXT, heartbeat_at TEXT,
    attempt INTEGER NOT NULL DEFAULT 0 CHECK (attempt >= 0),
    payload_json TEXT NOT NULL DEFAULT '{}' CHECK (json_valid(payload_json)),
    progress_json TEXT NOT NULL DEFAULT '{}' CHECK (json_valid(progress_json)),
    error_code TEXT
);
-- Manual and scheduled scans share one active job per scope.
CREATE UNIQUE INDEX one_active_job_per_scope ON jobs(kind, scope)
    WHERE status IN ('queued','running');
CREATE INDEX jobs_pending ON jobs(status, requested_at);

CREATE TABLE scan_requests (
    id TEXT PRIMARY KEY, job_id TEXT NOT NULL REFERENCES jobs(id),
    trigger TEXT NOT NULL CHECK (trigger IN ('scheduled','manual')),
    requester TEXT NOT NULL, idempotency_key TEXT NOT NULL,
    requested_at TEXT NOT NULL,
    UNIQUE(requester, idempotency_key)
);

CREATE TABLE collection_runs (
    id TEXT PRIMARY KEY, job_id TEXT NOT NULL REFERENCES jobs(id),
    started_at TEXT NOT NULL, finished_at TEXT,
    source_results_json TEXT NOT NULL DEFAULT '{}' CHECK (json_valid(source_results_json)),
    item_count INTEGER NOT NULL DEFAULT 0 CHECK (item_count >= 0)
);

CREATE TABLE raw_items (
    id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(id),
    run_id TEXT NOT NULL REFERENCES collection_runs(id),
    discovered_at TEXT NOT NULL, payload_json TEXT NOT NULL CHECK (json_valid(payload_json)),
    payload_hash TEXT NOT NULL, retention_until TEXT,
    UNIQUE(source_id, payload_hash)
);
CREATE INDEX raw_items_retention ON raw_items(retention_until);

CREATE TABLE documents (
    id TEXT PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(id),
    raw_item_id TEXT REFERENCES raw_items(id) ON DELETE SET NULL,
    canonical_url TEXT NOT NULL UNIQUE, headline TEXT NOT NULL,
    author TEXT, published_at TEXT, discovered_at TEXT NOT NULL,
    snippet TEXT, permitted_text TEXT, language TEXT,
    content_hash TEXT NOT NULL,
    access_status TEXT NOT NULL CHECK (access_status IN ('full_text','excerpt','snippet_only','unavailable')),
    publisher_group TEXT NOT NULL, syndication_origin TEXT, retention_until TEXT
);
CREATE INDEX documents_content_hash ON documents(content_hash);
CREATE INDEX documents_published ON documents(published_at);

CREATE TABLE document_entities (
    document_id TEXT NOT NULL REFERENCES documents(id),
    kind TEXT NOT NULL CHECK (kind IN ('person','organization','country','topic','other')),
    value TEXT NOT NULL, provenance TEXT NOT NULL,
    PRIMARY KEY(document_id, kind, value)
);
CREATE INDEX entities_lookup ON document_entities(kind, value);

CREATE TABLE clusters (
    id TEXT PRIMARY KEY, event_description TEXT NOT NULL,
    first_seen_at TEXT NOT NULL, last_seen_at TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('active','archived'))
);
CREATE INDEX clusters_recent ON clusters(last_seen_at);
CREATE TABLE cluster_documents (
    cluster_id TEXT NOT NULL REFERENCES clusters(id),
    document_id TEXT NOT NULL REFERENCES documents(id),
    similarity REAL CHECK (similarity >= 0 AND similarity <= 1),
    membership_reason TEXT NOT NULL, PRIMARY KEY(cluster_id, document_id)
);

CREATE TABLE analyses (
    id TEXT PRIMARY KEY, cluster_id TEXT NOT NULL REFERENCES clusters(id),
    snapshot_hash TEXT NOT NULL, cache_key TEXT NOT NULL UNIQUE,
    provider TEXT NOT NULL, model TEXT NOT NULL, prompt_version TEXT NOT NULL,
    audience_version TEXT NOT NULL, schema_version TEXT NOT NULL,
    created_at TEXT NOT NULL, summary TEXT NOT NULL,
    limitations_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(limitations_json)),
    input_tokens INTEGER CHECK (input_tokens >= 0), output_tokens INTEGER CHECK (output_tokens >= 0)
);

CREATE TABLE evidence_passages (
    id TEXT PRIMARY KEY, document_id TEXT NOT NULL REFERENCES documents(id),
    source_url TEXT NOT NULL, text TEXT NOT NULL, locator TEXT NOT NULL,
    content_hash TEXT NOT NULL, created_at TEXT NOT NULL
);

CREATE TABLE statements (
    id TEXT PRIMARY KEY, analysis_id TEXT NOT NULL REFERENCES analyses(id),
    text TEXT NOT NULL,
    kind TEXT NOT NULL CHECK (kind IN ('reported_fact','attributed_claim','editorial_interpretation','possible_consequence')),
    attribution TEXT,
    CHECK (kind != 'attributed_claim' OR (attribution IS NOT NULL AND length(trim(attribution)) > 0))
);
CREATE TABLE statement_evidence (
    statement_id TEXT NOT NULL REFERENCES statements(id),
    passage_id TEXT NOT NULL REFERENCES evidence_passages(id),
    role TEXT NOT NULL CHECK (role IN ('supports','contradicts','context')),
    PRIMARY KEY(statement_id, passage_id, role)
);

CREATE TABLE angles (
    id TEXT PRIMARY KEY, analysis_id TEXT NOT NULL REFERENCES analyses(id),
    title TEXT NOT NULL, category TEXT NOT NULL,
    why_it_could_work TEXT NOT NULL,
    verification_status TEXT NOT NULL CHECK (verification_status IN ('supported','needs_review','unconfirmed')),
    created_at TEXT NOT NULL
);
CREATE TABLE angle_evidence (
    angle_id TEXT NOT NULL REFERENCES angles(id),
    passage_id TEXT NOT NULL REFERENCES evidence_passages(id),
    role TEXT NOT NULL CHECK (role IN ('supports','contradicts','context')),
    PRIMARY KEY(angle_id, passage_id, role)
);

CREATE TABLE coverage_observations (
    id TEXT PRIMARY KEY, angle_id TEXT NOT NULL REFERENCES angles(id),
    observed_at TEXT NOT NULL, window_start TEXT NOT NULL, window_end TEXT NOT NULL,
    publisher_count INTEGER NOT NULL CHECK (publisher_count >= 0),
    angle_match_count INTEGER NOT NULL CHECK (angle_match_count >= 0 AND angle_match_count <= publisher_count),
    sample_json TEXT NOT NULL CHECK (json_valid(sample_json)),
    methodology_version TEXT NOT NULL, limitations TEXT NOT NULL
);

CREATE TABLE score_snapshots (
    id TEXT PRIMARY KEY, angle_id TEXT NOT NULL REFERENCES angles(id),
    created_at TEXT NOT NULL, weights_version TEXT NOT NULL,
    weights_json TEXT NOT NULL CHECK (json_valid(weights_json)),
    overall_status TEXT NOT NULL CHECK (overall_status IN ('measured','estimated','not_measured')),
    overall_value REAL, overall_basis TEXT NOT NULL,
    eligible INTEGER NOT NULL CHECK (eligible IN (0,1)),
    CHECK ((overall_status = 'not_measured' AND overall_value IS NULL) OR
      (overall_status IN ('measured','estimated') AND overall_value IS NOT NULL AND overall_value BETWEEN 0 AND 100))
);
CREATE TABLE score_components (
    snapshot_id TEXT NOT NULL REFERENCES score_snapshots(id),
    name TEXT NOT NULL, status TEXT NOT NULL CHECK (status IN ('measured','estimated','not_measured')),
    value REAL, basis TEXT NOT NULL CHECK (length(trim(basis)) > 0),
    PRIMARY KEY(snapshot_id, name),
    CHECK ((status = 'not_measured' AND value IS NULL) OR
      (status IN ('measured','estimated') AND value IS NOT NULL AND value BETWEEN 0 AND 100))
);

CREATE TABLE feedback_events (
    id TEXT PRIMARY KEY, user_id TEXT NOT NULL REFERENCES user_settings(user_id),
    angle_id TEXT NOT NULL REFERENCES angles(id),
    score_snapshot_id TEXT REFERENCES score_snapshots(id),
    kind TEXT NOT NULL CHECK (kind IN ('good','bad','saved','rejected','written')),
    reason TEXT, created_at TEXT NOT NULL
);
CREATE TRIGGER feedback_no_update BEFORE UPDATE ON feedback_events
BEGIN SELECT RAISE(ABORT, 'Feedback is append-only'); END;
CREATE TRIGGER feedback_no_delete BEFORE DELETE ON feedback_events
BEGIN SELECT RAISE(ABORT, 'Feedback is append-only'); END;

CREATE TABLE written_articles (
    id TEXT PRIMARY KEY, angle_id TEXT NOT NULL REFERENCES angles(id),
    user_id TEXT NOT NULL REFERENCES user_settings(user_id),
    article_url TEXT NOT NULL UNIQUE, published_at TEXT, recorded_at TEXT NOT NULL
);
CREATE TABLE performance_observations (
    id TEXT PRIMARY KEY, article_id TEXT NOT NULL REFERENCES written_articles(id),
    connector TEXT NOT NULL, observed_at TEXT NOT NULL,
    window_start TEXT NOT NULL, window_end TEXT NOT NULL,
    metric TEXT NOT NULL, value REAL CHECK (value >= 0),
    status TEXT NOT NULL CHECK (status IN ('measured','not_measured')),
    provenance TEXT NOT NULL,
    CHECK ((status = 'not_measured' AND value IS NULL) OR
      (status = 'measured' AND value IS NOT NULL))
);
