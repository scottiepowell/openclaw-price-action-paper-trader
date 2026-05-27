import csv
import inspect
from pathlib import Path

import pytest

from price_action_paper_trader.cli import main as cli_main
from price_action_paper_trader.services.phase9_approval_exercise_service import build_phase9_approved_exercise
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.simulated_execution_journal_service import (
    SIMULATED_JOURNALED,
    build_simulated_execution_journal_records,
    generate_simulated_execution_journal_artifacts,
    read_simulated_submission_rows,
)
from price_action_paper_trader.services.simulated_reconciliation_service import (
    RECONCILED_SIMULATED_ONLY,
    build_simulated_reconciliation_records,
    generate_simulated_reconciliation_artifacts,
)
from price_action_paper_trader.services.simulated_submission_service import generate_simulated_submission_artifacts


def _phase9_submission_root(tmp_path: Path) -> tuple[Path, Path]:
    submission_root = tmp_path / "simulated_submissions"
    approval = build_phase9_approved_exercise()
    plan = next(plan for plan in build_order_plans() if plan.candidate_id == approval.candidate_id)
    generate_simulated_submission_artifacts(plans=[plan], approvals=[approval], output_root=submission_root)
    return submission_root, submission_root / "simulated_submission_queue.csv"


def test_phase9_submission_can_be_journaled_and_reconciled(tmp_path):
    submission_root, submission_csv = _phase9_submission_root(tmp_path)
    journal_root = tmp_path / "execution_journal"
    reconciliation_root = tmp_path / "reconciliation"

    journal_report = generate_simulated_execution_journal_artifacts(submission_root=submission_root, output_root=journal_root)
    reconciliation_report = generate_simulated_reconciliation_artifacts(
        submission_root=submission_root,
        journal_root=journal_root,
        output_root=reconciliation_root,
    )

    assert journal_report["count"] == 1
    assert journal_report["report"].overall_status == "pass"
    assert journal_report["report"].journaled_records[0].execution_status == SIMULATED_JOURNALED
    assert journal_report["report"].journaled_records[0].broker_action_allowed is False
    assert journal_report["queue_markdown"].is_file()
    assert journal_report["queue_csv"].is_file()

    journal_md = journal_report["queue_markdown"].read_text(encoding="utf-8")
    journal_csv = journal_report["queue_csv"].read_text(encoding="utf-8")
    assert "journal_record_id" in journal_md
    assert "simulated_submission_id" in journal_md
    assert "broker_action_allowed" in journal_md
    assert "journal_record_id" in journal_csv
    assert "SIMULATED_JOURNALED" in journal_csv

    assert reconciliation_report["count"] == 1
    assert reconciliation_report["report"].overall_status == "pass"
    assert reconciliation_report["report"].reconciliation_records[0].reconciliation_status == RECONCILED_SIMULATED_ONLY
    assert reconciliation_report["report"].reconciliation_records[0].broker_action_allowed is False
    assert reconciliation_report["queue_markdown"].is_file()
    assert reconciliation_report["queue_csv"].is_file()

    reconciliation_md = reconciliation_report["queue_markdown"].read_text(encoding="utf-8")
    reconciliation_csv = reconciliation_report["queue_csv"].read_text(encoding="utf-8")
    assert "reconciliation_id" in reconciliation_md
    assert "reconciliation_status" in reconciliation_md
    assert "RECONCILED_SIMULATED_ONLY" in reconciliation_csv
    assert "broker_action_allowed" in reconciliation_csv


def test_journal_service_fail_closed_on_unsafe_submission(tmp_path):
    submission_root, submission_csv = _phase9_submission_root(tmp_path)
    payload = submission_csv.read_text(encoding="utf-8")
    payload = payload.replace(",false,offline simulation only; submitted without fills,approved,simulated_only,PASSED,plan passed Phase 3 risk gate,", ",true,offline simulation only; submitted without fills,approved,simulated_only,PASSED,plan passed Phase 3 risk gate,")
    submission_csv.write_text(payload, encoding="utf-8")

    journal_report = generate_simulated_execution_journal_artifacts(submission_root=submission_root, output_root=tmp_path / "execution_journal")
    assert journal_report["count"] == 0
    assert journal_report["report"].overall_status == "fail"
    assert journal_report["report"].broker_action_allowed_all_false is False
    assert journal_report["report"].unsafe_broker_flags == 1


@pytest.mark.parametrize(
    ("mutator", "expected_status", "expected_missing_submission", "expected_missing_journal", "expected_mismatch"),
    [
        (None, "pass", 0, 0, 0),
        ("missing_journal", "fail", 0, 1, 0),
        ("missing_submission", "fail", 1, 0, 0),
        ("mismatch", "fail", 0, 0, 1),
        ("unsafe_flag", "fail", 0, 0, 0),
    ],
)
def test_reconciliation_fail_closed_cases(tmp_path, mutator, expected_status, expected_missing_submission, expected_missing_journal, expected_mismatch):
    submission_root, submission_csv = _phase9_submission_root(tmp_path)
    journal_root = tmp_path / "execution_journal"
    generate_simulated_execution_journal_artifacts(submission_root=submission_root, output_root=journal_root)

    if mutator == "missing_journal":
        journal_root = tmp_path / "missing_journal"
    elif mutator == "missing_submission":
        submission_root = tmp_path / "missing_submission"
    elif mutator == "mismatch":
        journal_csv = journal_root / "simulated_execution_journal.csv"
        text = journal_csv.read_text(encoding="utf-8").replace(",PTC-004,", ",PTC-999,", 1)
        journal_csv.write_text(text, encoding="utf-8")
    elif mutator == "unsafe_flag":
        journal_csv = journal_root / "simulated_execution_journal.csv"
        text = journal_csv.read_text(encoding="utf-8").replace(",false,offline simulation only; journaled from simulated submission record,", ",true,offline simulation only; journaled from simulated submission record,", 1)
        journal_csv.write_text(text, encoding="utf-8")

    reconciliation_report = generate_simulated_reconciliation_artifacts(
        submission_root=submission_root,
        journal_root=journal_root,
        output_root=tmp_path / "reconciliation",
    )

    assert reconciliation_report["report"].overall_status == expected_status
    assert reconciliation_report["report"].missing_submission_records == expected_missing_submission
    assert reconciliation_report["report"].missing_journal_records == expected_missing_journal
    assert reconciliation_report["report"].mismatched_records == expected_mismatch


def test_simulated_journal_and_reconciliation_have_no_network_or_broker_dependency():
    import price_action_paper_trader.services.simulated_execution_journal_service as journal_module
    import price_action_paper_trader.services.simulated_reconciliation_service as reconciliation_module

    journal_source = inspect.getsource(journal_module).lower()
    reconciliation_source = inspect.getsource(reconciliation_module).lower()

    for source in (journal_source, reconciliation_source):
        assert "alpaca" not in source
        assert "requests" not in source
        assert "urllib" not in source
        assert "http.client" not in source
        assert "submit_simulated_orders" not in source


def test_cli_reconcile_simulated_command_succeeds():
    assert cli_main(["approvals", "reconcile-simulated"]) == 0
