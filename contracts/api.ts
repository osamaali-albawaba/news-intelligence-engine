/** R1.0 v1.1 contracts only. Local API/worker/UI are not implemented. */
export type Section = 'news' | 'business' | 'the_node';
export type StatementKind = 'reported_fact' | 'attributed_claim' | 'editorial_interpretation' | 'possible_consequence';
export type Metric = (
  | { status: 'not_measured'; value: null; basis: string }
  | { status: 'measured' | 'estimated'; value: number; basis: string }
) & { observedAt?: string | null; methodology?: string; unit?: string };
export type ScanTrigger = 'manual' | 'scheduled'; // scheduled is disabled in pilot policy
export type ScanStatus = 'queued' | 'running' | 'completed' | 'partial' | 'failed' | 'cancelled';
export interface ScanRequest {
  schemaVersion: 2;
  idempotencyKey: string;
  section: Section;
  freshnessHours: 24 | 48 | 72;
  resultLimit: number; // validated integer 1-10; fewer/zero actual results valid
  profileId?: string;
}
export interface EffectiveSettings {
  configId: string;
  configHash: string;
  schemaVersion: number;
  effective: Record<string, unknown>;
}
export interface ScanResponse {
  schemaVersion: 2;
  requestId: string;
  jobId: string;
  status: ScanStatus;
  joinedExisting: boolean;
  scopeHash: string;
  effectiveSettings: EffectiveSettings;
  requestedAt: string;
  message: string;
}
export interface ScanProgress {
  jobId: string;
  status: ScanStatus;
  stage: string;
  sourcesAttempted: number;
  sourcesSucceeded: number;
  sourcesFailed: number;
  signalCount: number;
  clusterCount: number;
  opportunityCount: number;
  cacheHits: number;
  newModelCalls: number;
  lastCollectionAt: string | null;
  lastAnalysisAt: string | null;
  limitations: string[];
}
export interface Statement {
  text: string;
  kind: StatementKind;
  evidenceIds: string[];
  attribution: string | null;
}
export interface EvidenceReference {
  id: string;
  documentId: string;
  documentVersionId: string;
  sourceUrl: string;
  passage: string;
  locator: string;
  contentHash: string;
  language: string | null;
  availability: 'available' | 'expired' | 'removed' | 'source_unavailable';
}
export interface SupportedText {
  text: string;
  evidenceIds: string[];
  systemObservations: string[];
}
export interface Opportunity {
  schemaVersion: 2;
  recommendationId: string;
  clusterId: string;
  clusterRevisionId: string;
  analysisId: string | null;
  scoreSnapshotId: string | null;
  impressionId: string | null; // no invented exposure before render
  configId: string;
  section: Section;
  story: SupportedText;
  angleId: string | null;
  angle: string | null;
  whyNow: SupportedText;
  whyItCouldWork: SupportedText;
  alternativeAngles: string[];
  supportStatus: 'supported' | 'needs_review' | 'unconfirmed' | 'not_analyzed';
  verificationLabel: 'VERIFIED' | 'REPORTED' | 'SINGLE SOURCE' | 'UNVERIFIED' | 'ORIGIN UNKNOWN';
  state: 'NEW' | 'SEEN' | 'UPDATE' | 'NEW ANGLE';
  statements: Statement[];
  risks: Statement[];
  evidence: EvidenceReference[];
  metrics: Record<string, Metric>;
  opportunityScore: Metric;
  evidenceConfidence: Metric;
  coverageSample: {
    publisherCount: number; independentOriginCount: number; angleMatchCount: number | null;
    observedAt: string; windowStart: string; windowEnd: string;
    languages: Record<string, number>;
  } | null;
  publishedAt: string | null;
  discoveredAt: string;
  limitations: string[];
}
export type FeedbackKind = 'good' | 'bad' | 'saved' | 'rejected' | 'written' | 'opened' | 'selected' | 'writing' | 'published' | 'skipped' | 'correction';
export interface FeedbackRequest {
  schemaVersion: 2;
  idempotencyKey: string;
  recommendationId: string;
  impressionId: string | null;
  angleId: string | null;
  scoreSnapshotId: string | null;
  kind: FeedbackKind;
  reasonCode?: string;
  reason?: string;
  compensatesEventId?: string;
}
export interface ArticleLinkRequest {
  schemaVersion: 2;
  recommendationIds: string[];
  angleId: string | null;
  articleUrl: string; // validate HTTP(S); do not fetch automatically
  publishedAt: string | null;
}
