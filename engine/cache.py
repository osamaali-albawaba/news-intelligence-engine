"""Canonical cache identity; changed audience or evidence invalidates results."""
import hashlib
import json
from typing import Mapping


def analysis_cache_key(*, snapshot_hash: str, provider: str, model: str,
                       prompt_version: str, audience: Mapping[str, object],
                       schema_version: str = "1") -> str:
    value = {
        "snapshot_hash": snapshot_hash, "provider": provider, "model": model,
        "prompt_version": prompt_version, "audience": audience,
        "schema_version": schema_version,
    }
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()
