from datetime import datetime, timezone

from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.domain.risk import RiskGateContext
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.risk_gate import phase3_risk_gate


def test_phase3_risk_gate_allows_current_order_plans():
    plans = build_order_plans()
    ready_ids = {plan.candidate_id for plan in plans}
    context = RiskGateContext(ready_candidate_ids=frozenset(ready_ids))

    decisions = [phase3_risk_gate(plan, context) for plan in plans]

    assert all(decision.allowed for decision in decisions)
    assert {decision.candidate_id for decision in decisions} == ready_ids


def test_phase3_risk_gate_blocks_duplicate_candidates():
    plan = OrderPlan(
        candidate_id="PTC-004",
        symbol="NVDA",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=305.52,
        target_price=309.05,
        invalidation_level=298.46,
        risk_notes="duplicate test",
        created_at_utc="2026-05-24T00:00:00+00:00",
    )
    context = RiskGateContext(seen_candidate_ids=frozenset({"PTC-004"}), now_utc=datetime(2026, 5, 24, tzinfo=timezone.utc))

    decision = phase3_risk_gate(plan, context)

    assert decision.allowed is False
    assert "duplicate" in decision.reason


def test_phase3_risk_gate_blocks_missing_target_and_invalidation():
    plan = OrderPlan(
        candidate_id="PTC-900",
        symbol="NVDA",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=305.52,
        target_price=0.0,
        invalidation_level=0.0,
        risk_notes="missing levels",
        created_at_utc="2026-05-24T00:00:00+00:00",
    )
    context = RiskGateContext(ready_candidate_ids=frozenset({"PTC-900"}), now_utc=datetime(2026, 5, 24, tzinfo=timezone.utc))

    decision = phase3_risk_gate(plan, context)

    assert decision.allowed is False
    assert "missing target or invalidation" in decision.reason


def test_phase3_risk_gate_blocks_non_paper_review_candidates():
    plan = OrderPlan(
        candidate_id="PTC-903",
        symbol="NVDA",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=305.52,
        target_price=309.05,
        invalidation_level=298.46,
        risk_notes="blocked",
        readiness_status="BLOCKED_BY_TARGET_NOT_HIT",
        created_at_utc="2026-05-24T00:00:00+00:00",
    )

    decision = phase3_risk_gate(plan, RiskGateContext(now_utc=datetime(2026, 5, 24, tzinfo=timezone.utc)))

    assert decision.allowed is False
    assert "non-paper-review" in decision.reason


def test_phase3_risk_gate_blocks_unsupported_symbols_and_stale_plans():
    unsupported_plan = OrderPlan(
        candidate_id="PTC-901",
        symbol="XYZ",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=1.0,
        target_price=2.0,
        invalidation_level=0.5,
        risk_notes="unsupported symbol",
        created_at_utc="2026-05-24T00:00:00+00:00",
    )
    stale_plan = OrderPlan(
        candidate_id="PTC-902",
        symbol="NVDA",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=305.52,
        target_price=309.05,
        invalidation_level=298.46,
        risk_notes="stale",
        created_at_utc="2026-05-20T00:00:00+00:00",
    )
    now = datetime(2026, 5, 24, tzinfo=timezone.utc)

    unsupported_decision = phase3_risk_gate(unsupported_plan, RiskGateContext(ready_candidate_ids=frozenset({"PTC-901"}), now_utc=now))
    stale_decision = phase3_risk_gate(stale_plan, RiskGateContext(ready_candidate_ids=frozenset({"PTC-902"}), now_utc=now, max_plan_age_hours=24.0))

    assert unsupported_decision.allowed is False
    assert "unsupported" in unsupported_decision.reason
    assert stale_decision.allowed is False
    assert "stale" in stale_decision.reason
