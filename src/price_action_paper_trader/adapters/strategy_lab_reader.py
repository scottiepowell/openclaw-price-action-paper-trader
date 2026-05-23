"""Read-only Strategy Lab snapshot importer.

This module reads imported Strategy Lab artifacts from the local snapshot
boundary only. It does not write back to Strategy Lab and it does not include
broker, Alpaca, or execution logic.
"""

from __future__ import annotations

from csv import DictReader
from pathlib import Path
from typing import Any


SNAPSHOT_ROOT = Path(__file__).resolve().parents[3] / "data_refs" / "strategy_lab" / "snapshots" / "strategy_lab_snapshot_v1"


def _resolve_snapshot_root(snapshot_root: str | Path | None = None) -> Path:
    root = Path(snapshot_root) if snapshot_root is not None else SNAPSHOT_ROOT
    if not root.exists():
        raise FileNotFoundError(f"Strategy Lab snapshot root not found: {root}")
    return root


def _coerce_value(value: str) -> Any:
    text = value.strip()
    if text == "":
        return ""
    lower = text.lower()
    if lower == "true":
        return True
    if lower == "false":
        return False
    try:
        if "." in text:
            return float(text)
        return int(text)
    except ValueError:
        return text


def _load_csv(relative_path: str, snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    root = _resolve_snapshot_root(snapshot_root)
    csv_path = root / relative_path
    if not csv_path.is_file():
        raise FileNotFoundError(f"Strategy Lab snapshot file not found: {csv_path}")
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = DictReader(handle)
        return [
            {key: _coerce_value(value) if isinstance(value, str) else value for key, value in row.items()}
            for row in reader
        ]


def load_replay_evidence_matrix(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    return _load_csv("runs/replay/replay_evidence_matrix.csv", snapshot_root)


def load_paper_readiness_matrix(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    return _load_csv("runs/paper_readiness/paper_readiness_matrix.csv", snapshot_root)


def load_paper_review_queue(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    return _load_csv("runs/paper_review/paper_review_queue.csv", snapshot_root)


def load_paper_watch_journal(snapshot_root: str | Path | None = None) -> list[dict[str, Any]]:
    return _load_csv("runs/paper_journal/paper_watch_journal.csv", snapshot_root)
