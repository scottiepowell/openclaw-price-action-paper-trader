"""Domain models for simulated execution journaling and reconciliation."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SimulatedExecutionJournalRecord:
    journal_record_id: str
    simulated_submission_id: str
    approval_id: str
    candidate_id: str
    order_plan_id: str
    symbol: str
    side: str
    simulated_broker_order_id: str
    execution_status: str
    journaled_at: str
    broker_action_allowed: bool = False
    notes: str = ""
    submission_status: str = ""
    offline_only_boundary: str = "offline-only"
    simulated_only_boundary: str = "simulated-only"


@dataclass(frozen=True)
class SimulatedExecutionJournalReport:
    overall_status: str
    total_submission_records: int
    total_journal_records: int
    broker_action_allowed_all_false: bool
    unsafe_broker_flags: int
    missing_submission_records: int
    malformed_submission_records: int
    journaled_records: tuple[SimulatedExecutionJournalRecord, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class SimulatedReconciliationRecord:
    reconciliation_id: str
    simulated_submission_id: str
    journal_record_id: str
    candidate_id: str
    order_plan_id: str
    symbol: str
    side: str
    simulated_broker_order_id: str
    submission_status: str
    execution_status: str
    reconciliation_status: str
    reconciled_at: str
    broker_action_allowed: bool = False
    notes: str = ""
    offline_only_boundary: str = "offline-only"
    simulated_only_boundary: str = "simulated-only"


@dataclass(frozen=True)
class SimulatedReconciliationReport:
    overall_status: str
    total_submission_records: int
    total_journal_records: int
    total_reconciliation_records: int
    broker_action_allowed_all_false: bool
    missing_submission_records: int
    missing_journal_records: int
    mismatched_records: int
    unsafe_broker_flags: int
    reconciliation_records: tuple[SimulatedReconciliationRecord, ...] = field(default_factory=tuple)

