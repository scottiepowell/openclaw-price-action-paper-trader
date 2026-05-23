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
    assert (SNAPSHOT_DIR / "runs" / "replay" / "replay_evidence_matrix.csv").is_file()
    assert (SNAPSHOT_DIR / "runs" / "paper_readiness" / "paper_readiness_matrix.csv").is_file()
    assert (SNAPSHOT_DIR / "runs" / "paper_review" / "paper_review_queue.csv").is_file()
    assert (SNAPSHOT_DIR / "runs" / "paper_journal" / "paper_watch_journal.csv").is_file()


def test_strategy_lab_reader_loads_imported_snapshot_artifacts():
    replay = load_replay_evidence_matrix()
    readiness = load_paper_readiness_matrix()
    review_queue = load_paper_review_queue()
    journal = load_paper_watch_journal()

    assert len(replay) == 35
    assert len(readiness) == 35
    assert len(review_queue) == 11
    assert len(journal) == 11

    ready_candidates = {row["candidate_id"] for row in readiness if row["readiness_status"] == "READY_FOR_PAPER_REVIEW"}
    assert ready_candidates == {"PTC-004", "PTC-005", "PTC-009", "PTC-017", "PTC-019", "PTC-021", "PTC-022", "PTC-024", "PTC-032", "PTC-034", "PTC-035"}

    blocked_033 = next(row for row in readiness if row["candidate_id"] == "PTC-033")
    assert blocked_033["readiness_status"] == "BLOCKED_BY_TARGET_NOT_HIT"
    assert blocked_033["broker_action_allowed"] is False
    assert "PTC-033" not in {row["candidate_id"] for row in review_queue}

    assert all(row["real_market_evidence"] is True for row in replay)
    assert all(row["broker_action_allowed"] is False for row in readiness)
    assert all(row["broker_action_allowed"] is False for row in review_queue)
    assert all(row["broker_action_allowed"] is False for row in journal)
