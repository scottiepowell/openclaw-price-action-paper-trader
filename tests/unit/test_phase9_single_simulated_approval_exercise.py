from pathlib import Path

from price_action_paper_trader.services.phase9_approval_exercise_service import (
    build_phase9_approved_exercise,
    generate_phase9_single_simulated_approval_exercise_artifacts,
)


def test_phase9_controlled_approved_exercise_is_simulated_only():
    approval = build_phase9_approved_exercise()

    assert approval.approval_id == "APR-PTC-004"
    assert approval.candidate_id == "PTC-004"
    assert approval.order_plan_id == "OP-PTC-004"
    assert approval.symbol == "NVDA"
    assert approval.side == "bullish"
    assert approval.approval_status == "approved"
    assert approval.approval_scope == "simulated_only"
    assert approval.broker_action_allowed is False


def test_phase9_single_simulated_approval_exercise_creates_one_submission_and_warning_report(tmp_path):
    approval_root = tmp_path / "approval_exercises" / "phase-9"
    submission_root = tmp_path / "simulated_submissions"
    report_root = tmp_path / "reports"

    result = generate_phase9_single_simulated_approval_exercise_artifacts(
        approval_output_root=approval_root,
        submission_output_root=submission_root,
        report_output_root=report_root,
    )

    exercise_markdown = result["exercise_markdown"]
    submission_report = result["submission_report"]
    audit_report = result["audit_report"]

    assert exercise_markdown.is_file()
    assert "approval_status: approved" in exercise_markdown.read_text(encoding="utf-8")
    assert "approval_scope: simulated_only" in exercise_markdown.read_text(encoding="utf-8")
    assert "broker_action_allowed: false" in exercise_markdown.read_text(encoding="utf-8")

    assert submission_report["count"] == 1
    assert submission_report["queue_markdown"].is_file()
    assert submission_report["queue_csv"].is_file()

    csv_text = submission_report["queue_csv"].read_text(encoding="utf-8")
    assert csv_text.count("SS-APR-PTC-004-") == 1
    assert "APR-PTC-004,PTC-004,OP-PTC-004,NVDA,bullish" in csv_text
    assert ",false," in csv_text

    report = audit_report["report"]
    assert audit_report["total_simulated_submissions"] == 1
    assert report.overall_status == "warning"
    assert report.pending_approvals > 0
    assert report.broker_action_allowed_all_false is True
    assert report.approval_scope_all_simulated_only is True
    assert report.broker_network_live_execution_detected is False
    assert report.report_generation_mutated_source_artifacts is False

    report_md = audit_report["queue_markdown"].read_text(encoding="utf-8")
    assert "Conservative warning reason: pending approvals remain in the queue" in report_md

