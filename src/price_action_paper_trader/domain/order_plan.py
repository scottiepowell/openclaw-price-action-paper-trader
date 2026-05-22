"""Domain model for paper order plans."""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderPlan:
    candidate_id: str
    symbol: str
    side: str
    entry_candidate_price: float
    target_price: float
    invalidation_level: float
    broker_action_allowed: bool = False
