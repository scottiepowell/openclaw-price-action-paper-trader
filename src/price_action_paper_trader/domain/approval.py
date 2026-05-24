"""Domain model for manual approval artifacts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ApprovalArtifact:
    approval_id: str
    candidate_id: str
    order_plan_id: str
    symbol: str
    side: str
    approved_by: str = ""
    approved_at: str = ""
    expires_at: str = ""
    approval_status: str = "pending"
    approval_scope: str = "simulated_only"
    broker_action_allowed: bool = False
    notes: str = ""
    offline_only_boundary: str = "offline-only"
    simulated_only_boundary: str = "simulated-only"
