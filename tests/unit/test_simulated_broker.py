from dataclasses import FrozenInstanceError
import inspect

import pytest

from price_action_paper_trader.adapters.simulated_broker import (
    SIMULATED_REJECTED,
    SIMULATED_SUBMITTED,
    generate_simulated_execution_artifacts,
    submit_simulated_order,
)
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.services.order_plan_builder import build_order_plans


def _sample_plan() -> OrderPlan:
    return OrderPlan(
        candidate_id="PTC-004",
        symbol="NVDA",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=305.52,
        target_price=309.05,
        invalidation_level=298.46,
        risk_notes="offline simulation only",
        readiness_status="READY_FOR_PAPER_REVIEW",
        plan_status="DRAFT",
        snapshot_source="data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1",
        broker_action_allowed=False,
        created_at_utc="2026-05-24T09:44:00+00:00",
    )


def test_only_approved_plans_submit_successfully():
    plans = build_order_plans()
    records = [submit_simulated_order(plan) for plan in plans]

    assert len(records) == 11
    assert all(record.execution_status == SIMULATED_SUBMITTED for record in records)
    assert all(record.broker_action_allowed is False for record in records)
    assert all(record.risk_gate_status == "PASSED" for record in records)


def test_blocked_and_malformed_plans_reject():
    blocked_plan = OrderPlan(**{**_sample_plan().__dict__, "readiness_status": "BLOCKED_BY_TARGET_NOT_HIT"})
    malformed_plan = OrderPlan(
        candidate_id="",
        symbol="NVDA",
        side="bullish",
        classification="confirmed_breakout",
        entry_reference=305.52,
        target_price=309.05,
        invalidation_level=298.46,
        risk_notes="malformed",
        readiness_status="READY_FOR_PAPER_REVIEW",
        plan_status="DRAFT",
        snapshot_source="data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1",
        broker_action_allowed=False,
        created_at_utc="2026-05-24T09:44:00+00:00",
    )

    blocked_record = submit_simulated_order(blocked_plan)
    malformed_record = submit_simulated_order(malformed_plan)

    assert blocked_record.execution_status == SIMULATED_REJECTED
    assert "risk gate" in blocked_record.notes
    assert malformed_record.execution_status == SIMULATED_REJECTED
    assert "missing candidate id" in malformed_record.notes


def test_deterministic_simulated_order_ids():
    plan = _sample_plan()

    first = submit_simulated_order(plan)
    second = submit_simulated_order(plan)

    assert first.simulated_order_id == second.simulated_order_id
    assert first.submission_timestamp_utc == second.submission_timestamp_utc


def test_generate_simulated_execution_artifacts_writes_queue(tmp_path):
    report = generate_simulated_execution_artifacts(output_root=tmp_path)

    assert report["count"] == 11
    assert report["queue_markdown"].is_file()
    assert report["queue_csv"].is_file()
    assert len(report["record_documents"]) == 11
    assert all(path.is_file() for path in report["record_documents"])


def test_simulated_broker_has_no_network_or_alpaca_dependency():
    import price_action_paper_trader.adapters.simulated_broker as module

    source = inspect.getsource(module).lower()
    assert "alpaca" not in source
    assert "requests" not in source
    assert "http.client" not in source
    assert "urllib" not in source


def test_execution_record_is_read_only():
    record = submit_simulated_order(_sample_plan())

    with pytest.raises(FrozenInstanceError):
        record.symbol = "TEST"  # type: ignore[misc]
