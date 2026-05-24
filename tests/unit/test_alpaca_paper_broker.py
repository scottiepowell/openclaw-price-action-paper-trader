from dataclasses import FrozenInstanceError
import inspect

import pytest

from price_action_paper_trader.adapters.alpaca_paper_broker import AlpacaPaperBroker
from price_action_paper_trader.domain.manual_approval import ManualApproval
from price_action_paper_trader.services.broker_safety_gate import validate_broker_config


DEFAULT_CONFIG = {
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
    }
}


def _plan():
    return {
        "candidate_id": "PTC-004",
        "symbol": "NVDA",
        "side": "bullish",
        "classification": "confirmed_breakout",
        "entry_reference": 305.52,
        "target_price": 309.05,
        "invalidation_level": 298.46,
        "risk_notes": "manual approval test",
        "readiness_status": "READY_FOR_PAPER_REVIEW",
        "plan_status": "DRAFT",
        "snapshot_source": "data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1",
        "broker_action_allowed": False,
        "created_at_utc": "2026-05-24T09:44:00+00:00",
    }


def test_manual_approval_defaults_are_safe():
    approval = ManualApproval(candidate_id="PTC-004")

    assert approval.approval_status == "NOT_APPROVED"
    assert approval.paper_only is True
    assert approval.broker_action_allowed is False


def test_broker_validation_blocks_disabled_default_config():
    decision = validate_broker_config(DEFAULT_CONFIG)

    assert decision.allowed is False
    assert decision.broker_action_allowed is False
    assert "disabled" in decision.reason or "manual approval" in decision.reason


def test_alpaca_paper_broker_cannot_submit_by_default():
    broker = AlpacaPaperBroker(DEFAULT_CONFIG)
    approval = ManualApproval(candidate_id="PTC-004")

    config_decision = broker.validate_config()
    assert config_decision.allowed is False

    with pytest.raises(PermissionError):
        broker.submit_order(type("Plan", (), _plan())(), manual_approval=approval)

    with pytest.raises(RuntimeError):
        broker.get_order_status("SIM-123")


def test_alpaca_paper_broker_has_no_network_dependency():
    import price_action_paper_trader.adapters.alpaca_paper_broker as module

    source = inspect.getsource(module).lower()
    assert "alpaca_trade_api" not in source
    assert "alpaca-py" not in source
    assert "requests" not in source
    assert "http.client" not in source
    assert "urllib" not in source


def test_manual_approval_is_read_only():
    approval = ManualApproval(candidate_id="PTC-004")

    with pytest.raises(FrozenInstanceError):
        approval.approved_by = "test"  # type: ignore[misc]
