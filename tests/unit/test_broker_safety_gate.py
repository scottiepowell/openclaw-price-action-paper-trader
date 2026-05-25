from datetime import datetime, timezone

from price_action_paper_trader.domain.manual_approval import ManualApproval
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.services.broker_safety_gate import broker_safety_gate


SAFE_BROKER_CONFIG = {
    "broker": {
        "provider": "alpaca",
        "mode": "paper",
        "enabled": False,
        "allow_live_trading": False,
        "require_manual_approval": True,
        "submit_orders": False,
        "broker_action_allowed_default": False,
        "required_env_vars": [
            "ALPACA_PAPER_API_KEY",
            "ALPACA_PAPER_SECRET_KEY",
            "ALPACA_PAPER_BASE_URL",
        ],
        "manual_approval_present": True,
    }
}


def _plan() -> OrderPlan:
    return OrderPlan(
        candidate_id="PTC-004",
        symbol="NVDA",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=305.52,
        target_price=309.05,
        invalidation_level=298.46,
        risk_notes="manual approval test",
        readiness_status="READY_FOR_PAPER_REVIEW",
        plan_status="DRAFT",
        snapshot_source="data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1",
        broker_action_allowed=False,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
    )


def test_broker_safety_gate_blocks_missing_manual_approval():
    decision = broker_safety_gate(_plan(), config=SAFE_BROKER_CONFIG)

    assert decision.allowed is False
    assert decision.broker_action_allowed is False
    assert "manual approval" in decision.reason


def test_broker_safety_gate_blocks_non_paper_mode():
    bad_config = {"broker": {**SAFE_BROKER_CONFIG["broker"], "mode": "live"}}

    decision = broker_safety_gate(_plan(), config=bad_config, manual_approval=ManualApproval(candidate_id="PTC-004", approval_status="APPROVED", broker_action_allowed=True, approved_by="Scott", approval_timestamp_utc="2026-05-24T13:47:00+00:00", approval_scope="paper-only"))

    assert decision.allowed is False
    assert "non-paper" in decision.reason or "live" in decision.reason


def test_broker_safety_gate_blocks_risk_rejected_plan():
    approval = ManualApproval(
        candidate_id="PTC-004",
        approved_by="Scott",
        approval_timestamp_utc="2026-05-24T13:47:00+00:00",
        approval_scope="paper-only",
        approval_status="APPROVED",
        paper_only=True,
        broker_action_allowed=True,
    )
    blocked_plan = OrderPlan(
        **{**_plan().__dict__, "target_price": 0.0}
    )

    decision = broker_safety_gate(blocked_plan, config=SAFE_BROKER_CONFIG, manual_approval=approval)

    assert decision.allowed is False
    assert "risk" in decision.reason or "target" in decision.reason
