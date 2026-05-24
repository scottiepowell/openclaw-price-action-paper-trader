"""Domain model for manual paper-order approval."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ManualApproval:
    candidate_id: str
    approved_by: str = ""
    approval_timestamp_utc: str = ""
    approval_scope: str = ""
    approval_status: str = "NOT_APPROVED"
    paper_only: bool = True
    broker_action_allowed: bool = False
    notes: str = ""
