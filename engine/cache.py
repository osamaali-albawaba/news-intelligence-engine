"""Canonical cache identity; changed audience or evidence invalidates results."""
import hashlib
import json
from typing import Mapping


def analysis_cache_key(*, snapshot_hash: str, provider: str, model: str,
                       prompt_version: str, audience: Mapping[str, object],
                       schema_version: str = "2", extraction_version: str = "legacy",
                       translation_version: str = "none", behavior_version: str = "1") -> str:
    value = {
        "snapshot_hash": snapshot_hash, "provider": provider, "model": model,
        "prompt_version": prompt_version, "audience": audience,
        "schema_version": schema_version, "extraction_version": extraction_version,
        "translation_version": translation_version, "behavior_version": behavior_version,
    }
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def score_cache_key(*, analysis_id: str, subject_id: str, formula_version: str,
                    scoring_config: Mapping[str, object]) -> str:
    value = {"analysis_id": analysis_id, "subject_id": subject_id,
             "formula_version": formula_version, "scoring_config": scoring_config}
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()
