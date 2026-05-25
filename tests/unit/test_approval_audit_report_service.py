from __future__ import annotations

import csv
from pathlib import Path

from price_action_paper_trader.cli import main as cli_main
from price_action_paper_trader.services.approval_audit_report_service import (
    generate_approval_audit_report,
    report_is_read_only,
)
from price_action_paper_trader.services.manual_approval_service import generate_manual_approval_artifacts


def _safe_roots(tmp_path: Path) -> tuple[Path, Path, Path]:
    approval_root = tmp_path / "approvals"
    submission_root = tmp_path / "simulated_submissions"
    report_root = tmp_path / "reports"
    generate_manual_approval_artifacts(output_root=approval_root)
    submission_root.mkdir(parents=True, exist_ok=True)
    (submission_root / "simulated_submission_queue.csv").write_text(
        "simulated_submission_id,approval_id,candidate_id,order_plan_id,symbol,side,simulated_broker_order_id,submission_status,submitted_at,broker_action_allowed,notes,approval_status,approval_scope,risk_gate_status,risk_gate_reason,offline_only_boundary,simulated_only_boundary\n",
        encoding="utf-8",
    )
    return approval_root, submission_root, report_root


def test_report_service_is_read_only():
    assert report_is_read_only() is True


def test_generate_report_writes_markdown_and_csv(tmp_path):
    approval_root, submission_root, report_root = _safe_roots(tmp_path)
    report = generate_approval_audit_report(
        output_root=report_root,
        approval_root=approval_root,
        simulated_submission_root=submission_root,
    )

    md_path = report["queue_markdown"]
    csv_path = report["queue_csv"]
    md_text = md_path.read_text(encoding="utf-8")
    csv_text = csv_path.read_text(encoding="utf-8")

    assert report["overall_status"] == "warning"
    assert md_path.is_file()
    assert csv_path.is_file()
    assert "# Approval Audit Report" in md_text
    assert "## Summary" in md_text
    assert "## Approval Queue Audit" in md_text
    assert "## Compatibility File Audit" in md_text
    assert "## Simulated Submission Audit" in md_text
    assert "## Safety Boundary Audit" in md_text
    assert "Conservative warning reason: pending approvals remain in the queue" in md_text
    assert "record_type,overall_status,approval_id,candidate_id,order_plan_id,symbol,side,approval_status,approval_scope,broker_action_allowed,expires_at,expected_path,found,simulated_submission_id,simulated_broker_order_id,submission_status,submitted_at,audit_status,audit_notes" in csv_text


def test_missing_compatibility_file_reports_fail(tmp_path):
    approval_root, submission_root, report_root = _safe_roots(tmp_path)
    (approval_root / "PTC-004-approval.md").unlink()

    report = generate_approval_audit_report(
        output_root=report_root,
        approval_root=approval_root,
        simulated_submission_root=submission_root,
    )["report"]

    assert report.overall_status == "fail"
    assert any(row.candidate_id == "PTC-004" and row.audit_status == "fail" for row in report.compatibility_rows)


def test_unsafe_approval_scope_and_broker_flag_fail_closed(tmp_path):
    approval_root, submission_root, report_root = _safe_roots(tmp_path)
    csv_path = approval_root / "approval_queue.csv"
    rows = []
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    rows[0]["approval_scope"] = "other_scope"
    rows[0]["broker_action_allowed"] = "true"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    report = generate_approval_audit_report(
        output_root=report_root,
        approval_root=approval_root,
        simulated_submission_root=submission_root,
    )["report"]

    assert report.overall_status == "fail"
    assert report.approvals_with_unsafe_scope == 1
    assert report.approvals_with_unsafe_broker_flag == 1
    assert report.broker_action_allowed_all_false is False
    assert report.approval_scope_all_simulated_only is False


def test_unsafe_simulated_submission_broker_flag_fail_closed(tmp_path):
    approval_root, submission_root, report_root = _safe_roots(tmp_path)
    csv_path = submission_root / "simulated_submission_queue.csv"
    csv_path.write_text(
        "simulated_submission_id,approval_id,candidate_id,order_plan_id,symbol,side,simulated_broker_order_id,submission_status,submitted_at,broker_action_allowed,notes,approval_status,approval_scope,risk_gate_status,risk_gate_reason,offline_only_boundary,simulated_only_boundary\n"
        "SS-APR-PTC-004-FAKE,APR-PTC-004,PTC-004,OP-PTC-004,NVDA,bullish,SIM-BROKER-PTC-004-FAKE,SIMULATED_SUBMITTED,2026-05-24T00:00:00+00:00,true,offline simulation only,approved,simulated_only,PASSED,ok,offline-only,simulated-only\n",
        encoding="utf-8",
    )

    report = generate_approval_audit_report(
        output_root=report_root,
        approval_root=approval_root,
        simulated_submission_root=submission_root,
    )["report"]

    assert report.overall_status == "fail"
    assert report.simulated_submissions_with_unsafe_broker_flag == 1
    assert any(row.broker_action_allowed is True and row.audit_status == "fail" for row in report.simulated_submission_rows)


def test_cli_audit_report_command_succeeds():
    assert cli_main(["approvals", "audit-report"]) == 0
