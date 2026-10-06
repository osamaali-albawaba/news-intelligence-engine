import type { FeedbackRequest, ScanProgress, ScanRequest, ScanResponse } from '../../contracts/api';

/** Specification only. Phase 5 implements authenticated endpoints. */
export interface EditorAPI {
  scanNow(request: ScanRequest): Promise<ScanResponse>;
  scanProgress(jobId: string): Promise<ScanProgress>;
  feedback(request: FeedbackRequest): Promise<{ eventId: string }>;
}
