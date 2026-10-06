"""Validate Phase 0 JSON configuration without external dependencies."""
import json
from pathlib import Path

COMPONENTS = (
    "newsworthiness", "freshness", "breaking_potential", "curiosity",
    "controversy", "emotional_intensity", "recognizable_entities",
    "social_momentum", "search_interest", "visual_potential", "angle_novelty",
    "coverage_saturation", "source_confidence", "audience_relevance",
    "expected_short_term_traffic", "expected_long_tail_potential",
)
CATEGORIES = {"wire", "major_international", "regional", "official",
              "entertainment", "specialist", "social_trend", "other"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_config(config_dir: Path) -> dict:
    configs = {name: json.loads((config_dir / filename).read_text(encoding="utf-8"))
               for name, filename in {
                   "sources": "sources.example.json", "audience": "audience.json",
                   "scoring": "scoring.json", "scan": "scan.json",
               }.items()}
    for name, value in configs.items():
        require(value.get("schema_version") == 1, f"{name}: unsupported schema version")
    sources = configs["sources"]
    require(isinstance(sources["sources"], list), "sources must be a list")
    seen = set()
    for source in sources["sources"]:
        require(source["id"] not in seen, "Duplicate source ID")
        seen.add(source["id"])
        require(source["category"] in CATEGORIES, "Unknown source category")
        require(source["tier"] in sources["tiers"], "Unknown source tier")
        require(source["poll_interval_minutes"] > 0, "Invalid polling interval")
        require(source["permissions"]["review_status"] in {"pending", "approved", "denied"},
                "Unknown permission review status")
        require(not source["enabled"] or source["permissions"]["review_status"] == "approved",
                "Enabled source needs approved permission review")
    audience = configs["audience"]
    require(bool(audience["output_language"]), "Audience requires output language")
    for field in ("regions", "languages", "topics", "excluded_topics", "recognizable_entities"):
        require(isinstance(audience[field], list), f"Audience {field} must be a list")
    scoring = configs["scoring"]
    require(set(scoring["components"]) == set(COMPONENTS), "Scoring components incomplete")
    require(all(isinstance(v, (float, int)) and not isinstance(v, bool) and 0 <= v <= 1
                for v in scoring["weights"].values()), "Invalid weights")
    require(set(scoring["weights"]) <= set(COMPONENTS), "Unknown weighted component")
    require(abs(sum(scoring["weights"].values()) - 1) < 1e-9, "Weights must sum to one")
    require(scoring["missing_policy"] == "withhold_score", "Missing metrics may not become zero")
    scan = configs["scan"]
    require(scan["manual"]["enabled"] and scan["scheduled"]["enabled"],
            "Both trigger modes must be configured")
    require(scan["execution_enabled"] is False, "Phase 0 must not enable live execution")
    require(scan["manual"]["cooldown_seconds"] > 0, "Manual cooldown must be positive")
    for field in ("max_sources_per_run", "max_items_per_source", "max_ai_calls_per_day",
                  "max_ai_input_tokens_per_day", "max_ai_output_tokens_per_day"):
        require(scan["limits"][field] > 0, f"Invalid limit {field}")
    return configs
