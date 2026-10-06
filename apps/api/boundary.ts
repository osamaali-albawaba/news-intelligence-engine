import type { ArticleLinkRequest, FeedbackRequest, ScanProgress, ScanRequest, ScanResponse } from '../../contracts/api';

/** Specification only. R1.1 implements a Python loopback HTTP boundary. */
export interface EditorAPI {
  scanNow(request: ScanRequest): Promise<ScanResponse>;
  scanProgress(jobId: string): Promise<ScanProgress>;
  feedback(request: FeedbackRequest): Promise<{ eventId: string }>;
  linkArticle(request: ArticleLinkRequest): Promise<{ articleId: string }>;
}
