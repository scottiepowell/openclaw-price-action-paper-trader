"""Domain models for execution journals and reconciliation reports."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ExecutionJournalEntry:
    journal_id: str
    candidate_id: str
    replay_id: str
    symbol: str
    side: str
    setup_type: str
    source_watch_journal_id: str
    source_plan_status: str
    source_plan_snapshot_source: str
    execution_id: str
    execution_status: str
    manual_approval_required: bool = True
    manual_approval_granted: bool = False
    broker_action_allowed: bool = False
    fill_status: str = ""
    fill_price: float = 0.0
    target_price: float = 0.0
    invalidation_level: float = 0.0
    reconciliation_status: str = ""
    duplicate_of: str = ""
    malformed_reason: str = ""
    notes: str = ""
    created_at_utc: str = ""
    snapshot_source: str = ""
    lineage_id: str = ""
    offline_only_boundary: str = "offline-only"
    simulated_only_boundary: str = "simulated-only"


@dataclass(frozen=True)
class ExecutionReconciliationReport:
    total_entries: int
    approved_entries: int
    pending_approval_entries: int
    open_entries: int
    closed_entries: int
    rejected_entries: int
    duplicate_entries: int
    malformed_entries: int
    journal_entries: tuple[ExecutionJournalEntry, ...] = field(default_factory=tuple)
