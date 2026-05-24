from dataclasses import FrozenInstanceError
from pathlib import Path
import inspect

import pytest

from price_action_paper_trader.adapters.strategy_lab_reader import load_paper_readiness_matrix
from price_action_paper_trader.services.order_plan_builder import (
    build_order_plans,
    generate_order_plan_artifacts,
)


ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_DIR = ROOT / "data_refs" / "strategy_lab" / "snapshots" / "strategy_lab_snapshot_v1"


def test_only_ready_candidates_generate_plans():
    plans = build_order_plans()
    ready_ids = {
        row["candidate_id"]
        for row in load_paper_readiness_matrix()
        if row["readiness_status"] == "READY_FOR_PAPER_REVIEW"
    }

    assert {plan.candidate_id for plan in plans} == ready_ids
    assert len(plans) == 11


def test_blocked_candidates_do_not_generate_plans():
    plans = build_order_plans()
    blocked_ids = {
        row["candidate_id"]
        for row in load_paper_readiness_matrix()
        if row["readiness_status"] != "READY_FOR_PAPER_REVIEW"
    }

    assert blocked_ids.isdisjoint({plan.candidate_id for plan in plans})
    assert "PTC-033" in blocked_ids


def test_generated_plans_are_read_only_and_disabled():
    plans = build_order_plans()
    assert all(plan.broker_action_allowed is False for plan in plans)
    assert all(plan.plan_status == "DRAFT" for plan in plans)

    with pytest.raises(FrozenInstanceError):
        plans[0].symbol = "TEST"  # type: ignore[misc]


def test_generate_order_plan_artifacts_writes_queue(tmp_path):
    report = generate_order_plan_artifacts(output_root=tmp_path)

    assert report["count"] == 11
    assert report["queue_markdown"].is_file()
    assert report["queue_csv"].is_file()
    assert len(report["plan_documents"]) == 11
    assert all(path.is_file() for path in report["plan_documents"])


def test_order_plan_builder_has_no_alpaca_dependency():
    import price_action_paper_trader.services.order_plan_builder as module

    source = inspect.getsource(module).lower()
    assert "alpaca_paper_broker" not in source
    assert "alpaca" not in source

