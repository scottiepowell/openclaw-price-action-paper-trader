"""Read-only market data domain models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MarketDataBar:
    symbol: str
    timeframe: str
    timestamp: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    source: str
    feed: str
    fetched_at: str
    data_delay_minutes: int
    is_delayed: bool


@dataclass(frozen=True)
class MarketDataSnapshot:
    snapshot_id: str
    symbols: tuple[str, ...]
    timeframes: tuple[str, ...]
    window_start: str
    window_end: str
    fetched_at: str
    source: str
    feed: str
    data_delay_minutes: int
    is_live_execution_allowed: bool = False
    broker_action_allowed: bool = False
    bars: tuple[MarketDataBar, ...] = field(default_factory=tuple)
    snapshot_status: str = "market_data_unavailable"
    notes: str = ""


@dataclass(frozen=True)
class MarketContextAssessment:
    assessment_id: str
    candidate_id: str
    order_plan_id: str
    symbol: str
    side: str
    snapshot_id: str
    latest_bar_timestamp: str
    latest_close: float
    data_freshness_status: str
    plan_context_status: str
    human_review_required: bool = True
    broker_action_allowed: bool = False
    notes: str = ""


@dataclass(frozen=True)
class MarketContextAssessmentReport:
    overall_status: str
    total_approvals: int
    total_compatibility_files: int
    total_simulated_submissions: int
    total_journal_records: int
    total_reconciliation_records: int
    total_complete_traces: int
    incomplete_traces: int
    unsafe_broker_flags: int
    unsafe_approval_scopes: int
    assessment_rows: tuple[MarketContextAssessment, ...] = field(default_factory=tuple)

