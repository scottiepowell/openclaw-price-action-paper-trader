from pathlib import Path

from price_action_paper_trader.config import broker_action_allowed, load_yaml_config
from price_action_paper_trader.services.paper_execution_service import broker_action_allowed as service_broker_action_allowed
from price_action_paper_trader.services.risk_gate import phase0_risk_gate


ROOT = Path(__file__).resolve().parents[2]


def test_default_config_blocks_broker_action():
    config = load_yaml_config(ROOT / "configs" / "default.yaml")
    assert broker_action_allowed(config) is False


def test_paper_config_keeps_order_submission_disabled():
    config = load_yaml_config(ROOT / "configs" / "paper.yaml")
    assert config["paper_account"]["enabled"] is False
    assert config["paper_account"]["order_submission_allowed"] is False
    assert config["paper_account"]["live_trading_allowed"] is False


def test_phase0_execution_service_blocks_broker_action():
    assert service_broker_action_allowed() is False


def test_phase0_risk_gate_blocks_action():
    decision = phase0_risk_gate()
    assert decision.allowed is False
    assert "Phase 0" in decision.reason
