"""Domain model for paper-review candidates."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PaperCandidate:
    candidate_id: str
    replay_id: str
    symbol: str
    side: str
    setup_type: str
    readiness_status: str
    broker_action_allowed: bool = False
