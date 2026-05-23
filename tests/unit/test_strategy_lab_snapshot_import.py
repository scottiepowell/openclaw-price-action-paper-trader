from pathlib import Path

from price_action_paper_trader.adapters.strategy_lab_reader import (
    load_paper_readiness_matrix,
    load_paper_review_queue,
    load_paper_watch_journal,
    load_replay_evidence_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_DIR = ROOT / "data_refs" / "strategy_lab" / "snapshots" / "strategy_lab_snapshot_v1"


def test_strategy_lab_snapshot_directory_exists():
    assert SNAPSHOT_DIR.is_dir()
    assert (SNAPSHOT_DIR / "README.md").is_file()
    assert (SNAPSHOT_DIR / "MANIFEST.yaml").is_file()


def test_strategy_lab_reader_scaffold_returns_empty_placeholders():
    assert load_replay_evidence_matrix() == []
    assert load_paper_readiness_matrix() == []
    assert load_paper_review_queue() == []
    assert load_paper_watch_journal() == []
