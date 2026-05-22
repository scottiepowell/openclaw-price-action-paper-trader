"""Journal domain objects."""

from dataclasses import dataclass


@dataclass(frozen=True)
class JournalEntry:
    journal_id: str
    candidate_id: str
    status: str = "pending"
    broker_action_allowed: bool = False
