"""Read-only Strategy Lab snapshot importer scaffold.

This module is intentionally non-executing.
It exists so future phases can read imported Strategy Lab snapshots without
adding broker, Alpaca, or live-execution logic here.
"""

from pathlib import Path
from typing import Any


SNAPSHOT_ROOT = Path(__file__).resolve().parents[3] / "data_refs" / "strategy_lab" / "snapshots" / "strategy_lab_snapshot_v1"


def load_replay_evidence_matrix(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    """Placeholder loader for replay evidence matrix snapshots."""

    return []


def load_paper_readiness_matrix(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    """Placeholder loader for paper readiness matrix snapshots."""

    return []


def load_paper_review_queue(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    """Placeholder loader for paper review queue snapshots."""

    return []


def load_paper_watch_journal(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    """Placeholder loader for paper watch journal snapshots."""

    return []
