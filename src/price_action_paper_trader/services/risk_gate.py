"""Risk gate logic for offline paper plans."""

from __future__ import annotations

from datetime import datetime, timezone

from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.domain.risk import RiskDecision, RiskGateContext


READY_STATUS = "READY_FOR_PAPER_REVIEW"
PHASE3_RULE = "Phase 3"


def phase0_risk_gate() -> RiskDecision:
    return RiskDecision(allowed=False, reason="Phase 0 blocks broker action", rule="Phase 0")


def _parse_iso_utc(value: str) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _directional_prices_are_valid(plan: OrderPlan) -> bool:
    side = plan.side.lower()
    if side == "bullish":
        return plan.target_price > plan.entry_reference > 0 and plan.invalidation_level < plan.entry_reference
    if side == "bearish":
        return plan.target_price < plan.entry_reference and plan.invalidation_level > plan.entry_reference
    return False


def phase3_risk_gate(plan: OrderPlan, context: RiskGateContext | None = None) -> RiskDecision:
    context = context or RiskGateContext()
    candidate_id = plan.candidate_id.strip()
    symbol = plan.symbol.strip().upper()

    if not candidate_id:
        return RiskDecision(False, "missing candidate id", rule=PHASE3_RULE, symbol=symbol)

    if context.ready_candidate_ids and candidate_id not in context.ready_candidate_ids:
        return RiskDecision(False, "non-paper-review candidate blocked", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    if candidate_id in context.seen_candidate_ids:
        return RiskDecision(False, "duplicate candidate blocked", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    if plan.readiness_status and plan.readiness_status != READY_STATUS:
        return RiskDecision(False, "non-paper-review candidate blocked", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    if symbol not in context.supported_symbols:
        return RiskDecision(False, "unsupported symbol blocked", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    if plan.target_price <= 0 or plan.invalidation_level <= 0:
        return RiskDecision(False, "missing target or invalidation level", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    if not _directional_prices_are_valid(plan):
        return RiskDecision(False, "plan prices do not match trade direction", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    plan_created_at = _parse_iso_utc(plan.created_at_utc)
    if plan_created_at is None:
        return RiskDecision(False, "missing or invalid plan timestamp", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    age_hours = (context.now_utc - plan_created_at).total_seconds() / 3600
    if age_hours > context.max_plan_age_hours:
        return RiskDecision(False, "stale plan blocked", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)

    return RiskDecision(True, "plan passed Phase 3 risk gate", rule=PHASE3_RULE, candidate_id=candidate_id, symbol=symbol)
