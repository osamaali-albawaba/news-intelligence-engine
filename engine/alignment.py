"""R1.0 offline intent/config contracts. No API, worker, network or dispatch."""
from dataclasses import dataclass
import hashlib
import json
from typing import Mapping


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


@dataclass(frozen=True)
class ConfigSnapshot:
    config_hash: str
    effective_json: str
    schema_version: int = 2

    @classmethod
    def capture(cls, effective: Mapping[str, object]) -> "ConfigSnapshot":
        serialized = canonical_json(effective)
        return cls(hashlib.sha256(serialized.encode()).hexdigest(), serialized)


@dataclass(frozen=True)
class ScanIntent:
    idempotency_key: str
    section: str
    freshness_hours: int
    result_limit: int
    profile_id: str | None = None
    schema_version: int = 2

    def __post_init__(self) -> None:
        if not self.idempotency_key.strip() or self.schema_version != 2:
            raise ValueError("Invalid request identity/schema")
        if self.section not in {"news", "business", "the_node"}:
            raise ValueError("Unknown section")
        if type(self.freshness_hours) is not int or self.freshness_hours not in (24, 48, 72):
            raise ValueError("Freshness must be 24, 48 or 72 hours")
        if type(self.result_limit) is not int or not 1 <= self.result_limit <= 10:
            raise ValueError("Result limit must be 1-10; no padding")

    def payload_hash(self, snapshot: ConfigSnapshot) -> str:
        payload = {"schema": self.schema_version, "section": self.section,
                   "freshness_hours": self.freshness_hours, "result_limit": self.result_limit,
                   "profile_id": json.loads(snapshot.effective_json).get("intent", {}).get("profile_id", self.profile_id),
                   "config_hash": snapshot.config_hash}
        return hashlib.sha256(canonical_json(payload).encode()).hexdigest()

    def scope_hash(self, snapshot: ConfigSnapshot) -> str:
        return self.payload_hash(snapshot)  # retry identity does not determine compatibility


def effective_snapshot(configs: Mapping[str, object], intent: ScanIntent) -> ConfigSnapshot:
    # Overrides apply to one captured scan only; never mutate saved defaults.
    effective = json.loads(canonical_json(configs))
    profile_id = configs["audience"]["profile_id"]
    if intent.profile_id is not None and intent.profile_id != profile_id:
        raise ValueError("Unknown audience profile")
    effective["sections"]["freshness_hours"] = intent.freshness_hours
    effective["sections"]["result_limit"] = intent.result_limit
    effective["sections"]["selected_section"] = intent.section
    effective["intent"] = {"section": intent.section, "freshness_hours": intent.freshness_hours,
                           "result_limit": intent.result_limit, "profile_id": profile_id}
    return ConfigSnapshot.capture(effective)


def require_capability(configs: Mapping[str, object], capability: str) -> None:
    """Future dispatch boundaries must call this BEFORE accepting external work.

    It produces no jobs or external requests. R1.0 policy fails closed even if
    a caller passes a changed environment/provider name.
    """
    policy = configs["scan"]
    if not policy["execution_enabled"] or policy["capabilities"].get(capability) is not True:
        raise PermissionError(f"Capability disabled: {capability}")
