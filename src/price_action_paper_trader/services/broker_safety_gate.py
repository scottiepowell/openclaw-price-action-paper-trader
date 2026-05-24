"""Safety gate for future paper-broker integration.

This module intentionally blocks all real submission attempts in the current
phase. It validates that future broker code remains paper-only, manual-only,
and disabled-by-default.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from price_action_paper_trader.domain.manual_approval import ManualApproval
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.domain.risk import RiskDecision
from price_action_paper_trader.services.risk_gate import phase3_risk_gate


@dataclass(frozen=True)
class BrokerSafetyDecision:
    allowed: bool
    reason: str
    broker_action_allowed: bool = False
    manual_approval_required: bool = True
    paper_only: bool = True
    checks: tuple[str, ...] = ()


def _broker_config(config: dict[str, Any] | None) -> dict[str, Any]:
    return dict((config or {}).get("broker", {}) or {})


def validate_broker_config(config: dict[str, Any] | None = None) -> BrokerSafetyDecision:
    broker = _broker_config(config)
    checks: list[str] = []

    provider = str(broker.get("provider", "alpaca")).strip().lower()
    mode = str(broker.get("mode", "paper")).strip().lower()
    enabled = bool(broker.get("enabled", False))
    live_trading_allowed = bool(broker.get("allow_live_trading", False))
    require_manual_approval = bool(broker.get("require_manual_approval", True))
    submit_orders = bool(broker.get("submit_orders", False))
    broker_action_allowed_default = bool(broker.get("broker_action_allowed_default", False))
    api_base_url = str(broker.get("base_url", "")).strip()
    manual_approval_present = bool(broker.get("manual_approval_present", False))
    env_keys = tuple(
        str(item).strip() for item in broker.get("required_env_vars", ()) if str(item).strip()
    )

    if provider != "alpaca":
        return BrokerSafetyDecision(False, "unsupported broker provider", checks=("provider",))
    checks.append("provider")

    if mode != "paper":
        return BrokerSafetyDecision(False, "non-paper broker mode blocked", checks=tuple(checks + ["mode"]))
    checks.append("mode")

    if enabled:
        return BrokerSafetyDecision(False, "broker must remain disabled by default", checks=tuple(checks + ["enabled"]))
    checks.append("enabled")

    if live_trading_allowed:
        return BrokerSafetyDecision(False, "live trading is prohibited", checks=tuple(checks + ["live_trading"]))
    checks.append("live_trading")

    if submit_orders:
        return BrokerSafetyDecision(False, "submit_orders must stay false in this phase", checks=tuple(checks + ["submit_orders"]))
    checks.append("submit_orders")

    if broker_action_allowed_default:
        return BrokerSafetyDecision(False, "broker_action_allowed_default must remain false", checks=tuple(checks + ["broker_action_allowed_default"]))
    checks.append("broker_action_allowed_default")

    if not require_manual_approval:
        return BrokerSafetyDecision(False, "manual approval is required", checks=tuple(checks + ["manual_approval"]))
    checks.append("manual_approval")

    if api_base_url:
        lowered = api_base_url.lower()
        if "alpaca.markets" in lowered or "paper" in lowered or "live" in lowered:
            return BrokerSafetyDecision(False, "live endpoint configuration is blocked", checks=tuple(checks + ["base_url"]))
    checks.append("base_url")

    if env_keys:
        checks.append("required_env_vars")

    if not manual_approval_present:
        return BrokerSafetyDecision(False, "manual approval missing", checks=tuple(checks))

    return BrokerSafetyDecision(True, "broker configuration passed safety validation", broker_action_allowed=True, checks=tuple(checks))


def broker_safety_gate(
    order_plan: OrderPlan,
    config: dict[str, Any] | None = None,
    manual_approval: ManualApproval | None = None,
    risk_decision: RiskDecision | None = None,
) -> BrokerSafetyDecision:
    risk_decision = risk_decision or phase3_risk_gate(order_plan)
    config_decision = validate_broker_config(config)

    if not config_decision.allowed:
        return BrokerSafetyDecision(
            False,
            config_decision.reason,
            broker_action_allowed=False,
            manual_approval_required=True,
            paper_only=True,
            checks=config_decision.checks,
        )

    if risk_decision is None or not risk_decision.allowed:
        return BrokerSafetyDecision(False, "blocked by risk gate", broker_action_allowed=False, checks=("risk_gate",))

    if manual_approval is None:
        return BrokerSafetyDecision(False, "manual approval required", broker_action_allowed=False, checks=("manual_approval",))

    if not manual_approval.paper_only:
        return BrokerSafetyDecision(False, "manual approval must be paper-only", broker_action_allowed=False, checks=("manual_approval.paper_only",))

    if not manual_approval.broker_action_allowed:
        return BrokerSafetyDecision(False, "manual approval does not allow broker action", broker_action_allowed=False, checks=("manual_approval.broker_action_allowed",))

    if manual_approval.approval_status != "APPROVED":
        return BrokerSafetyDecision(False, "manual approval not approved", broker_action_allowed=False, checks=("manual_approval.approval_status",))

    return BrokerSafetyDecision(True, "broker safety gate passed", broker_action_allowed=True, checks=("broker", "risk_gate", "manual_approval"))
