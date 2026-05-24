"""Disabled Alpaca paper broker scaffold.

This is a paper-only, config-gated placeholder. It does not submit orders in
this phase and does not require the Alpaca SDK.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from price_action_paper_trader.domain.manual_approval import ManualApproval
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.services.broker_safety_gate import (
    BrokerSafetyDecision,
    broker_safety_gate,
    validate_broker_config,
)


@dataclass(frozen=True)
class BlockedBrokerResult:
    reason: str
    broker_action_allowed: bool = False
    order_id: str = ""
    order_status: str = "BLOCKED"


class AlpacaPaperBroker:
    def __init__(self, config: dict[str, Any] | None = None):
        self.config = dict(config or {})

    def validate_config(self) -> BrokerSafetyDecision:
        return validate_broker_config(self.config)

    def submit_order(
        self,
        approved_order: OrderPlan,
        manual_approval: ManualApproval | None = None,
    ) -> BlockedBrokerResult:
        decision = broker_safety_gate(approved_order, config=self.config, manual_approval=manual_approval)
        if decision.allowed:
            return BlockedBrokerResult(reason="broker submission disabled in this phase")
        raise PermissionError(decision.reason)

    def get_order_status(self, order_id: str) -> BlockedBrokerResult:
        raise RuntimeError(f"order status unavailable in disabled scaffold: {order_id}")
