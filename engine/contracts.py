"""Dependency-free contracts shared by future adapters and pipeline stages."""
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Mapping, Protocol, Sequence
from uuid import UUID


class StatementKind(StrEnum):
    REPORTED_FACT = "reported_fact"
    ATTRIBUTED_CLAIM = "attributed_claim"
    EDITORIAL_INTERPRETATION = "editorial_interpretation"
    POSSIBLE_CONSEQUENCE = "possible_consequence"


class MeasurementStatus(StrEnum):
    MEASURED = "measured"
    ESTIMATED = "estimated"
    NOT_MEASURED = "not_measured"


@dataclass(frozen=True)
class Metric:
    status: MeasurementStatus
    value: float | None
    basis: str
    observed_at: str | None = None
    methodology: str | None = None
    unit: str = "index_0_100"

    def __post_init__(self) -> None:
        if not isinstance(self.status, MeasurementStatus):
            raise ValueError("Metric status must be a MeasurementStatus")
        if not self.basis.strip():
            raise ValueError("Metric requires a basis or reason for missing data")
        if self.status == MeasurementStatus.NOT_MEASURED:
            if self.value is not None:
                raise ValueError("Not measured metrics must have a null value")
        elif self.value is None or isinstance(self.value, bool) or not 0 <= self.value <= 100:
            raise ValueError("Measured/estimated metrics require a finite value from 0 to 100")


@dataclass(frozen=True)
class DiscoveryItem:
    id: UUID
    source_id: str
    headline: str
    url: str
    discovered_at: str
    published_at: str | None
    author: str | None
    snippet: str | None
    permitted_text: str | None
    content_access: str
    language: str | None
    entities: tuple[str, ...] = ()
    countries: tuple[str, ...] = ()
    people: tuple[str, ...] = ()
    organizations: tuple[str, ...] = ()
    topics: tuple[str, ...] = ()


@dataclass(frozen=True)
class CollectionRequest:
    source_id: str
    cursor: str | None
    max_items: int
    run_id: UUID
    source_config_version: str = "legacy"
    section: str = "news"
    freshness_hours: int = 24
    permissions: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class SourceFailure:
    code: str
    message: str  # sanitized; never credentials, cookies, or raw auth responses
    retryable: bool


@dataclass(frozen=True)
class CollectionResult:
    items: tuple[DiscoveryItem, ...]
    next_cursor: str | None
    failure: SourceFailure | None = None
    observations: tuple[Mapping[str, object], ...] = ()


class SourceAdapter(Protocol):
    """Fetch only permitted content; respect robots, terms, auth, and bounds.

    Partial results may coexist with a failure. Cursor is persisted only after
    item storage succeeds. One source failure must not abort other adapters.
    """

    adapter_name: str

    def collect(self, request: CollectionRequest) -> CollectionResult: ...


@dataclass(frozen=True)
class EvidencePassage:
    id: UUID
    document_id: UUID
    source_url: str
    text: str
    locator: str
    content_hash: str
    document_version_id: UUID | None = None
    language: str | None = None
    availability: str = "available"


@dataclass(frozen=True)
class Statement:
    text: str
    kind: StatementKind
    evidence_ids: tuple[UUID, ...]
    attribution: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.kind, StatementKind):
            raise ValueError("Unknown statement kind")
        if not self.text.strip() or not self.evidence_ids:
            raise ValueError("Statements require text and evidence references")
        if self.kind == StatementKind.ATTRIBUTED_CLAIM and (not self.attribution or not self.attribution.strip()):
            raise ValueError("Attributed claims require attribution")


@dataclass(frozen=True)
class AngleDraft:
    title: str
    category: str
    why_it_could_work: str
    evidence_ids: tuple[UUID, ...]
    verification_status: str  # supported / needs_review / unconfirmed


@dataclass(frozen=True)
class AnalysisRequest:
    cluster_id: UUID
    snapshot_hash: str
    prompt_version: str
    audience_profile: Mapping[str, object]
    passages: tuple[EvidencePassage, ...]
    max_output_tokens: int
    cluster_revision_id: UUID | None = None
    effective_config_hash: str | None = None
    extraction_version: str = "legacy"
    translation_version: str = "none"
    behavior_version: str = "1"
    output_schema_version: str = "2"
    system_observations: tuple[str, ...] = ()


@dataclass(frozen=True)
class AnalysisResult:
    summary: str
    statements: tuple[Statement, ...]
    angles: tuple[AngleDraft, ...]
    limitations: tuple[str, ...]
    provider: str
    model: str
    input_tokens: int | None
    output_tokens: int | None
    summary_evidence_ids: tuple[UUID, ...] = ()
    why_now: str = ""
    why_now_evidence_ids: tuple[UUID, ...] = ()
    why_now_observations: tuple[str, ...] = ()
    risks: tuple[Statement, ...] = ()


class AIProvider(Protocol):
    """Provider-independent structured output; no model name in pipeline logic.

    Raise ProviderError on quota, timeout, malformed output, or unavailable
    service. Validate output and evidence references before persistence.
    """

    provider_name: str
    model: str

    def analyze(self, request: AnalysisRequest) -> AnalysisResult: ...


class ProviderError(Exception):
    def __init__(self, code: str, retryable: bool = False) -> None:
        super().__init__(code)
        self.code = code
        self.retryable = retryable


class PerformanceConnector(Protocol):
    """Future independent interface. No Marfeel implementation in the MVP."""

    def observations(self, article_url: str) -> Sequence[Mapping[str, object]]: ...


def validate_analysis(result: AnalysisResult, request: AnalysisRequest) -> None:
    """Reject dangling references and factual-looking unsupported output."""
    known = {passage.id for passage in request.passages}
    if not result.summary.strip() or not result.provider or not result.model:
        raise ValueError("Analysis requires summary and provider provenance")
    if not result.summary_evidence_ids or not set(result.summary_evidence_ids) <= known:
        raise ValueError("Summary requires known evidence support")
    if not result.why_now.strip() or not (result.why_now_evidence_ids or result.why_now_observations):
        raise ValueError("Why Now requires evidence or explicit system observations")
    if not set(result.why_now_evidence_ids) <= known:
        raise ValueError("Why Now contains unknown evidence")
    if not set(result.why_now_observations) <= set(request.system_observations):
        raise ValueError("Why Now contains unknown system observations")
    if any(not observation.strip() for observation in result.why_now_observations):
        raise ValueError("Empty system observation")
    for entry in (*result.statements, *result.angles, *result.risks):
        if not entry.evidence_ids or not set(entry.evidence_ids) <= known:
            raise ValueError("Analysis contains missing or unknown evidence references")
    for angle in result.angles:
        if angle.verification_status not in {"supported", "needs_review", "unconfirmed"}:
            raise ValueError("Invalid angle verification status")
        if not angle.title.strip() or not angle.why_it_could_work.strip():
            raise ValueError("Angles require a title and rationale")
