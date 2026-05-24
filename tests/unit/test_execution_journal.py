from dataclasses import FrozenInstanceError
import inspect

import pytest

from price_action_paper_trader.adapters.simulated_broker import submit_simulated_orders
from price_action_paper_trader.domain.execution_record import ExecutionRecord
from price_action_paper_trader.services.execution_journal import (
    build_execution_journal_entries,
    generate_execution_journal_artifacts,
    summarize_execution_journal,
)
from price_action_paper_trader.services.order_plan_builder import build_order_plans


def test_execution_journal_preserves_lineage_and_offline_boundary():
    plans = build_order_plans()
    records = submit_simulated_orders(plans)
    approved_ids = {plan.candidate_id for plan in plans}

    entries = build_execution_journal_entries(records=records, plans=plans, approved_candidate_ids=approved_ids)
    report = summarize_execution_journal(entries)

    assert report.total_entries == 11
    assert report.approved_entries == 11
    assert report.pending_approval_entries == 0
    assert report.open_entries == 11
    assert report.closed_entries == 0
    assert report.duplicate_entries == 0
    assert report.malformed_entries == 0
    assert all(entry.broker_action_allowed is False for entry in entries)
    assert all(entry.manual_approval_granted is True for entry in entries)
    assert all(entry.lineage_id.startswith("EJ-") for entry in entries)
    assert {entry.replay_id for entry in entries} == {"HR-004", "HR-005", "HR-009", "HR-017", "HR-019", "HR-021", "HR-022", "HR-024", "HR-032", "HR-034", "HR-035"}


def test_execution_journal_detects_duplicates_and_malformed_records():
    plans = build_order_plans()
    records = submit_simulated_orders(plans)
    duplicate_records = list(records) + [records[0]]
    malformed = ExecutionRecord(
        candidate_id="",
        symbol="NVDA",
        side="bullish",
        simulated_order_id="SIM-MALFORMED",
        execution_status="SIMULATED_REJECTED",
        submission_timestamp_utc="2026-05-24T00:00:00+00:00",
        fill_status="NOT_FILLED",
        fill_price=0.0,
        notes="missing candidate",
        broker_action_allowed=False,
        risk_gate_status="MALFORMED",
        risk_gate_reason="missing candidate id",
        snapshot_source="data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1",
    )
    duplicate_records.append(malformed)

    entries = build_execution_journal_entries(
        records=duplicate_records,
        plans=plans,
        approved_candidate_ids={plan.candidate_id for plan in plans},
    )
    report = summarize_execution_journal(entries)

    assert report.total_entries == 13
    assert report.duplicate_entries == 1
    assert report.malformed_entries == 1
    assert entries[-2].reconciliation_status == "DUPLICATE"
    assert entries[-1].reconciliation_status == "MALFORMED"
    assert "duplicate" in entries[-2].duplicate_of
    assert "missing candidate" in entries[-1].malformed_reason


def test_generate_execution_journal_artifacts_writes_reports(tmp_path):
    plans = build_order_plans()
    report = generate_execution_journal_artifacts(
        approved_candidate_ids={plan.candidate_id for plan in plans},
        output_root=tmp_path,
    )

    assert report["count"] == 11
    assert report["queue_csv"].is_file()
    assert report["queue_markdown"].is_file()
    assert report["report_json"].is_file()
    assert report["report_markdown"].is_file()


def test_execution_journal_has_no_network_or_alpaca_dependency():
    import price_action_paper_trader.services.execution_journal as module

    source = inspect.getsource(module).lower()
    assert "import alpaca" not in source
    assert "from alpaca" not in source
    assert "requests" not in source
    assert "http.client" not in source
    assert "urllib" not in source


def test_execution_journal_entries_are_read_only():
    plans = build_order_plans()
    records = submit_simulated_orders(plans)
    entry = build_execution_journal_entries(records=records, plans=plans, approved_candidate_ids={plan.candidate_id for plan in plans})[0]

    with pytest.raises(FrozenInstanceError):
        entry.symbol = "TEST"  # type: ignore[misc]
