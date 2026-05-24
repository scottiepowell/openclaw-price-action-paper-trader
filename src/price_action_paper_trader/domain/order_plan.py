"""Domain model for offline paper order plans."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderPlan:
    candidate_id: str
    symbol: str
    side: str
    classification: str
    entry_reference: float
    target_price: float
    invalidation_level: float
    risk_notes: str
    readiness_status: str = ""
    plan_status: str = "DRAFT"
    snapshot_source: str = ""
    broker_action_allowed: bool = False
    created_at_utc: str = ""
