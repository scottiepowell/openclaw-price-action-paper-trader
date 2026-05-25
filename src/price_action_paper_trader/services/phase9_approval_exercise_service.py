"""Controlled Phase 9 approval exercise helpers.

This module creates one approved simulated-only approval artifact for
PTC-004 and drives the offline simulated submission/report flow without
touching any broker or network path.
"""

from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

from price_action_paper_trader.domain.approval import ApprovalArtifact
from price_action_paper_trader.services.approval_audit_report_service import generate_approval_audit_report
from price_action_paper_trader.services.manual_approval_service import serialize_manual_approval
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.simulated_submission_service import generate_simulated_submission_artifacts


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "approval_exercises" / "phase-9"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_phase9_approved_exercise() -> ApprovalArtifact:
    plan = next(plan for plan in build_order_plans() if plan.candidate_id == "PTC-004")
    return ApprovalArtifact(
        approval_id="APR-PTC-004",
        candidate_id=plan.candidate_id,
        order_plan_id="OP-PTC-004",
        symbol=plan.symbol,
        side=plan.side,
        approved_by="phase-9-controlled-exercise",
        approved_at=_utc_now(),
        expires_at=(datetime.now(timezone.utc) + timedelta(hours=12)).isoformat(),
        approval_status="approved",
        approval_scope="simulated_only",
        broker_action_allowed=False,
        notes="controlled phase 9 simulated-only approval exercise for PTC-004",
    )


def _write_phase9_exercise_markdown(approval: ApprovalArtifact, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "APR-PTC-004-approved-exercise.md"
    payload = serialize_manual_approval(approval)
    lines = [
        "# Phase 9 Controlled Approved Exercise",
        "",
        "This artifact is offline-only and simulated-only.",
        "",
        "```yaml",
    ]
    for key in (
        "approval_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "approval_status",
        "approval_scope",
        "broker_action_allowed",
    ):
        lines.append(f"{key}: {payload[key]}")
    lines.extend([
        "```",
        "",
        f"- Approved by: {approval.approved_by}",
        f"- Approved at: {approval.approved_at}",
        f"- Expires at: {approval.expires_at}",
        f"- Notes: {approval.notes}",
        "",
        "This controlled approval must never enable real broker action.",
    ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def generate_phase9_single_simulated_approval_exercise_artifacts(
    approval_output_root: str | Path | None = None,
    submission_output_root: str | Path | None = None,
    report_output_root: str | Path | None = None,
) -> dict[str, Any]:
    approval = build_phase9_approved_exercise()
    approval_root_path = Path(approval_output_root) if approval_output_root is not None else DEFAULT_OUTPUT_ROOT
    submission_root_path = Path(submission_output_root) if submission_output_root is not None else None
    report_root_path = Path(report_output_root) if report_output_root is not None else None

    exercise_markdown = _write_phase9_exercise_markdown(approval, approval_root_path)

    plan = next(plan for plan in build_order_plans() if plan.candidate_id == approval.candidate_id)
    submission_report = generate_simulated_submission_artifacts(
        plans=[plan],
        approvals=[approval],
        output_root=submission_root_path,
    )

    audit_report = generate_approval_audit_report(
        output_root=report_root_path,
    )

    return {
        "approval": approval,
        "exercise_markdown": exercise_markdown,
        "submission_report": submission_report,
        "audit_report": audit_report,
    }
