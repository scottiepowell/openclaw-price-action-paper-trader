from dataclasses import FrozenInstanceError
from datetime import datetime, timedelta, timezone
import inspect

import pytest

from price_action_paper_trader.domain.approval import ApprovalArtifact
from price_action_paper_trader.cli import main as cli_main
from price_action_paper_trader.services.manual_approval_service import (
    APPROVAL_TEMPLATE_IDS,
    build_manual_approval_templates,
    generate_manual_approval_artifacts,
    validate_manual_approvals,
)
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.simulated_submission_service import (
    SIMULATED_REJECTED,
    SIMULATED_SUBMITTED,
    generate_simulated_submission_artifacts,
    submit_simulated_approved_order,
)


def _future_iso(hours: int = 24) -> str:
    return (datetime.now(timezone.utc) + timedelta(hours=hours)).isoformat()


def _sample_plan():
    plans = build_order_plans()
    return next(plan for plan in plans if plan.candidate_id == "PTC-004")


def _approved_template() -> ApprovalArtifact:
    plan = _sample_plan()
    return ApprovalArtifact(
        approval_id="APR-PTC-004",
        candidate_id=plan.candidate_id,
        order_plan_id="OP-PTC-004",
        symbol=plan.symbol,
        side=plan.side,
        approved_by="Scott",
        approved_at=datetime.now(timezone.utc).isoformat(),
        expires_at=_future_iso(12),
        approval_status="approved",
        approval_scope="simulated_only",
        broker_action_allowed=False,
        notes="manual approval for simulated execution",
    )


def test_manual_approval_templates_cover_all_phase_7_candidates():
    templates = build_manual_approval_templates()

    assert [template.approval_id for template in templates] == [f"APR-{candidate_id}" for candidate_id in APPROVAL_TEMPLATE_IDS]
    assert all(template.approval_status == "pending" for template in templates)
    assert all(template.approval_scope == "simulated_only" for template in templates)
    assert all(template.broker_action_allowed is False for template in templates)


def test_generate_manual_approval_artifacts_writes_queue(tmp_path):
    report = generate_manual_approval_artifacts(output_root=tmp_path)

    assert report["count"] == 11
    assert report["queue_markdown"].is_file()
    assert report["queue_csv"].is_file()
    assert report["readme"].is_file()
    assert len(report["template_documents"]) == 11
    assert all(path.is_file() for path in report["template_documents"])
    assert len(report["compatibility_documents"]) == 11
    assert all(path.is_file() for path in report["compatibility_documents"])
    assert (tmp_path / "PTC-004-approval.md").is_file()
    assert (tmp_path / "PTC-035-approval.md").is_file()


def test_validate_manual_approvals_is_clean():
    issues = validate_manual_approvals()

    assert issues == []


def test_simulated_submission_happy_path_and_fail_closed_cases():
    plan = _sample_plan()
    approval = _approved_template()

    submitted = submit_simulated_approved_order(plan, approval)
    rejected_expired = submit_simulated_approved_order(
        plan,
        ApprovalArtifact(**{**approval.__dict__, "expires_at": "2020-01-01T00:00:00+00:00"}),
    )
    rejected_pending = submit_simulated_approved_order(
        plan,
        ApprovalArtifact(**{**approval.__dict__, "approval_status": "pending"}),
    )
    rejected_mismatch = submit_simulated_approved_order(
        plan,
        ApprovalArtifact(**{**approval.__dict__, "order_plan_id": "OP-PTC-999"}),
    )

    assert submitted.submission_status == SIMULATED_SUBMITTED
    assert submitted.broker_action_allowed is False
    assert submitted.order_plan_id == "OP-PTC-004"
    assert rejected_expired.submission_status == SIMULATED_REJECTED
    assert "expired" in rejected_expired.notes
    assert rejected_pending.submission_status == SIMULATED_REJECTED
    assert "approved" in rejected_pending.notes
    assert rejected_mismatch.submission_status == SIMULATED_REJECTED
    assert "order plan mismatch" in rejected_mismatch.notes


def test_generate_simulated_submission_artifacts_writes_queue(tmp_path):
    plan = _sample_plan()
    approval = _approved_template()
    report = generate_simulated_submission_artifacts(plans=[plan], approvals=[approval], output_root=tmp_path)

    assert report["count"] == 1
    assert report["queue_markdown"].is_file()
    assert report["queue_csv"].is_file()


def test_phase_7_modules_have_no_network_or_alpaca_dependency():
    import price_action_paper_trader.services.manual_approval_service as manual_module
    import price_action_paper_trader.services.simulated_submission_service as submission_module

    manual_source = inspect.getsource(manual_module).lower()
    submission_source = inspect.getsource(submission_module).lower()

    for source in (manual_source, submission_source):
        assert "alpaca" not in source
        assert "requests" not in source
        assert "urllib" not in source
        assert "http.client" not in source


def test_approval_artifact_is_read_only():
    approval = _approved_template()

    with pytest.raises(FrozenInstanceError):
        approval.symbol = "TEST"  # type: ignore[misc]


def test_cli_validate_command_succeeds():
    assert cli_main(["approvals", "validate"]) == 0
