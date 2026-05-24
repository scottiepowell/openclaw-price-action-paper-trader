"""Domain model for simulated submissions approved by hand."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SimulatedSubmissionRecord:
    simulated_submission_id: str
    approval_id: str
    candidate_id: str
    order_plan_id: str
    symbol: str
    side: str
    simulated_broker_order_id: str
    submission_status: str
    submitted_at: str
    broker_action_allowed: bool = False
    notes: str = ""
    approval_status: str = ""
    approval_scope: str = ""
    risk_gate_status: str = ""
    risk_gate_reason: str = ""
    offline_only_boundary: str = "offline-only"
    simulated_only_boundary: str = "simulated-only"
