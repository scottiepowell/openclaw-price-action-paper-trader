"""Risk gate placeholder."""

from price_action_paper_trader.domain.risk import RiskDecision


def phase0_risk_gate() -> RiskDecision:
    return RiskDecision(allowed=False, reason="Phase 0 blocks broker action")
