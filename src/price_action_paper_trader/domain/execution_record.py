"""Domain model for simulated execution records."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionRecord:
    candidate_id: str
    symbol: str
    side: str
    simulated_order_id: str
    execution_status: str
    submission_timestamp_utc: str
    fill_status: str
    fill_price: float
    notes: str
    broker_action_allowed: bool = False
    risk_gate_status: str = ""
    risk_gate_reason: str = ""
    snapshot_source: str = ""
    offline_only_boundary: str = "offline-only"
    simulated_only_boundary: str = "simulated-only"
