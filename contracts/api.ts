/** Phase 0 wire contracts. No HTTP handlers, collection, or dispatch implemented. */
export type StatementKind =
  | 'reported_fact' | 'attributed_claim'
  | 'editorial_interpretation' | 'possible_consequence';
export type Metric =
  | { status: 'not_measured'; value: null; basis: string }
  | { status: 'measured' | 'estimated'; value: number; basis: string };
export type ScanTrigger = 'scheduled' | 'manual';
export type ScanStatus = 'queued' | 'running' | 'completed' | 'partial' | 'failed' | 'cancelled';
export interface ScanRequest {
  /** Client retry identity; authenticated server sets trigger and user identity. */
  idempotencyKey: string;
}
export interface ScanResponse {
  jobId: string;
  status: ScanStatus;
  joinedExisting: boolean;
  requestedAt: string;
  /** Scheduling is best effort; never promise an instant result. */
  message: string;
}
export interface ScanProgress {
  jobId: string;
  status: ScanStatus;
  sourcesAttempted: number;
  sourcesSucceeded: number;
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
  sourceUrl: string;
  passage: string;
  locator: string;
  contentHash: string;
}
export interface Opportunity {
  id: string;
  clusterId: string;
  story: string;
  angle: string;
  whyItCouldWork: string;
  alternativeAngles: string[];
  verificationStatus: 'supported' | 'needs_review' | 'unconfirmed';
  statements: Statement[];
  evidence: EvidenceReference[];
  metrics: Record<string, Metric>;
  opportunityScore: Metric;
  coverageSample: { publisherCount: number; angleMatchCount: number; observedAt: string };
  limitations: string[];
}
export type FeedbackKind = 'good' | 'bad' | 'saved' | 'rejected' | 'written';
export interface FeedbackRequest {
  angleId: string;
  scoreSnapshotId: string | null;
  kind: FeedbackKind;
  articleUrl?: string;
  reason?: string;
}
