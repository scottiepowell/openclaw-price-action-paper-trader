"""Risk gate domain objects."""

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class RiskDecision:
    allowed: bool
    reason: str
    rule: str = ""
    candidate_id: str = ""
    symbol: str = ""


@dataclass(frozen=True)
class RiskGateContext:
    ready_candidate_ids: frozenset[str] = frozenset()
    supported_symbols: frozenset[str] = frozenset(
        {
            "AMZN",
            "AVGO",
            "GOOGL",
            "IWM",
            "META",
            "MSFT",
            "NVDA",
            "QQQ",
            "SPY",
            "TSLA",
        }
    )
    max_plan_age_hours: float = 24.0
    seen_candidate_ids: frozenset[str] = frozenset()
    now_utc: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
