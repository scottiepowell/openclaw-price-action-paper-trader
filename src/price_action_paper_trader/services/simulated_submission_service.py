"""Simulated submission service for manually approved order plans.

This layer is offline-only and fails closed on every safety check.
"""

from __future__ import annotations

import csv
from dataclasses import asdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable, Sequence

from price_action_paper_trader.domain.approval import ApprovalArtifact
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.domain.risk import RiskDecision
from price_action_paper_trader.domain.simulated_submission import SimulatedSubmissionRecord
from price_action_paper_trader.services.manual_approval_service import (
    DEFAULT_OUTPUT_ROOT as APPROVAL_OUTPUT_ROOT,
    load_manual_approval_queue,
)
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.risk_gate import phase3_risk_gate


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "simulated_submissions"
SIMULATED_SUBMITTED = "SIMULATED_SUBMITTED"
SIMULATED_REJECTED = "SIMULATED_REJECTED"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def derive_order_plan_id(candidate_id: str) -> str:
    return f"OP-{candidate_id.strip().upper()}"


def _submission_seed(plan: OrderPlan, approval: ApprovalArtifact) -> str:
    return "|".join(
        [
            plan.candidate_id.strip().upper(),
            plan.symbol.strip().upper(),
            plan.side.strip().lower(),
            approval.approval_id.strip().upper(),
            approval.order_plan_id.strip().upper(),
            approval.approval_status.strip().lower(),
            approval.approval_scope.strip().lower(),
        ]
    )


def _submission_id(plan: OrderPlan, approval: ApprovalArtifact) -> str:
    digest = sha256(_submission_seed(plan, approval).encode("utf-8")).hexdigest()[:12].upper()
    return f"SS-{approval.approval_id.strip().upper()}-{digest}"


def _broker_order_id(plan: OrderPlan, approval: ApprovalArtifact) -> str:
    digest = sha256(("broker|" + _submission_seed(plan, approval)).encode("utf-8")).hexdigest()[:12].upper()
    return f"SIM-BROKER-{plan.candidate_id.strip().upper()}-{digest}"


def _parse_iso(value: str) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _approval_not_expired(approval: ApprovalArtifact, now_utc: datetime | None = None) -> bool:
    now_utc = now_utc or datetime.now(timezone.utc)
    expires_at = _parse_iso(approval.expires_at)
    if expires_at is None:
        return False
    return expires_at > now_utc


def _malformed_reason(plan: OrderPlan | None, approval: ApprovalArtifact | None) -> str:
    if plan is None:
        return "missing order plan"
    if approval is None:
        return "missing approval artifact"
    if not plan.candidate_id.strip():
        return "missing candidate id"
    if not plan.symbol.strip():
        return "missing symbol"
    if not plan.side.strip():
        return "missing side"
    if not approval.approval_id.strip():
        return "missing approval id"
    if not approval.candidate_id.strip():
        return "missing approval candidate id"
    if not approval.order_plan_id.strip():
        return "missing approval order plan id"
    return ""


def _build_record(
    plan: OrderPlan,
    approval: ApprovalArtifact,
    submission_status: str,
    risk_gate_status: str,
    risk_gate_reason: str,
    notes: str,
) -> SimulatedSubmissionRecord:
    return SimulatedSubmissionRecord(
        simulated_submission_id=_submission_id(plan, approval),
        approval_id=approval.approval_id.strip(),
        candidate_id=plan.candidate_id.strip().upper(),
        order_plan_id=derive_order_plan_id(plan.candidate_id),
        symbol=plan.symbol.strip().upper(),
        side=plan.side.strip().lower(),
        simulated_broker_order_id=_broker_order_id(plan, approval),
        submission_status=submission_status,
        submitted_at=_utc_now(),
        broker_action_allowed=False,
        notes=notes,
        approval_status=approval.approval_status,
        approval_scope=approval.approval_scope,
        risk_gate_status=risk_gate_status,
        risk_gate_reason=risk_gate_reason,
    )


def submit_simulated_approved_order(
    plan: OrderPlan | None,
    approval: ApprovalArtifact | None,
    risk_decision: RiskDecision | None = None,
) -> SimulatedSubmissionRecord:
    malformed_reason = _malformed_reason(plan, approval)
    if malformed_reason:
        safe_plan = plan or OrderPlan(
            candidate_id="",
            symbol="",
            side="",
            classification="",
            entry_reference=0.0,
            target_price=0.0,
            invalidation_level=0.0,
            risk_notes="",
        )
        safe_approval = approval or ApprovalArtifact(
            approval_id="",
            candidate_id="",
            order_plan_id="",
            symbol="",
            side="",
        )
        return _build_record(
            safe_plan,
            safe_approval,
            SIMULATED_REJECTED,
            "MALFORMED",
            malformed_reason,
            f"offline simulation only; rejected: {malformed_reason}",
        )

    assert plan is not None
    assert approval is not None
    risk_decision = risk_decision or phase3_risk_gate(plan)
    if not risk_decision.allowed:
        return _build_record(
            plan,
            approval,
            SIMULATED_REJECTED,
            "BLOCKED",
            risk_decision.reason,
            f"offline simulation only; rejected by risk gate: {risk_decision.reason}",
        )

    if approval.approval_status.strip().lower() != "approved":
        return _build_record(
            plan,
            approval,
            SIMULATED_REJECTED,
            "BLOCKED",
            "approval status must be approved",
            "offline simulation only; rejected: approval status must be approved",
        )

    if approval.approval_scope.strip().lower() != "simulated_only":
        return _build_record(
            plan,
            approval,
            SIMULATED_REJECTED,
            "BLOCKED",
            "approval scope must be simulated_only",
            "offline simulation only; rejected: approval scope must be simulated_only",
        )

    if approval.broker_action_allowed:
        return _build_record(
            plan,
            approval,
            SIMULATED_REJECTED,
            "BLOCKED",
            "broker action must remain false",
            "offline simulation only; rejected: broker action must remain false",
        )

    if approval.candidate_id.strip().upper() != plan.candidate_id.strip().upper():
        return _build_record(
            plan,
            approval,
            SIMULATED_REJECTED,
            "BLOCKED",
            "candidate mismatch",
            "offline simulation only; rejected: candidate mismatch",
        )

    if approval.order_plan_id.strip().upper() != derive_order_plan_id(plan.candidate_id):
        return _build_record(
            plan,
            approval,
            SIMULATED_REJECTED,
            "BLOCKED",
            "order plan mismatch",
            "offline simulation only; rejected: order plan mismatch",
        )

    if not _approval_not_expired(approval):
        return _build_record(
            plan,
            approval,
            SIMULATED_REJECTED,
            "BLOCKED",
            "approval expired or missing expiry",
            "offline simulation only; rejected: approval expired or missing expiry",
        )

    return _build_record(
        plan,
        approval,
        SIMULATED_SUBMITTED,
        "PASSED",
        risk_decision.reason,
        "offline simulation only; submitted without fills",
    )


def submit_simulated_approved_orders(
    plans: Sequence[OrderPlan],
    approvals: Sequence[ApprovalArtifact],
) -> list[SimulatedSubmissionRecord]:
    approval_by_candidate = {approval.candidate_id.strip().upper(): approval for approval in approvals}
    records: list[SimulatedSubmissionRecord] = []
    for plan in plans:
        approval = approval_by_candidate.get(plan.candidate_id.strip().upper())
        records.append(submit_simulated_approved_order(plan, approval))
    return records


def serialize_simulated_submission(record: SimulatedSubmissionRecord) -> dict[str, Any]:
    data = asdict(record)
    data["broker_action_allowed"] = str(record.broker_action_allowed).lower()
    return data


def _write_markdown_queue(records: Sequence[SimulatedSubmissionRecord], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_submission_queue.md"
    lines = [
        "# Simulated Submission Queue",
        "",
        "This queue is offline-only and keeps `broker_action_allowed: false` for every submission.",
        "",
        f"Generated submissions: {len(records)}",
        "",
        "| simulated_submission_id | approval_id | candidate_id | order_plan_id | symbol | side | submission_status | broker_action_allowed |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            f"| {record.simulated_submission_id} | {record.approval_id} | {record.candidate_id} | {record.order_plan_id} | {record.symbol} | {record.side} | {record.submission_status} | {str(record.broker_action_allowed).lower()} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv_queue(records: Sequence[SimulatedSubmissionRecord], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_submission_queue.csv"
    fieldnames = list(serialize_simulated_submission(records[0]).keys()) if records else [
        "simulated_submission_id",
        "approval_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "simulated_broker_order_id",
        "submission_status",
        "submitted_at",
        "broker_action_allowed",
        "notes",
        "approval_status",
        "approval_scope",
        "risk_gate_status",
        "risk_gate_reason",
        "offline_only_boundary",
        "simulated_only_boundary",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(serialize_simulated_submission(record))
    return path


def generate_simulated_submission_artifacts(
    plans: Sequence[OrderPlan] | None = None,
    approvals: Sequence[ApprovalArtifact] | None = None,
    output_root: str | Path | None = None,
) -> dict[str, Any]:
    plans = list(plans) if plans is not None else build_order_plans()
    if approvals is None:
        approvals = load_manual_approval_queue(APPROVAL_OUTPUT_ROOT)
    approvals = [approval for approval in approvals if approval.approval_status.strip().lower() == "approved"]
    plan_by_candidate = {plan.candidate_id.strip().upper(): plan for plan in plans}

    records: list[SimulatedSubmissionRecord] = []
    for approval in approvals:
        plan = plan_by_candidate.get(approval.candidate_id.strip().upper())
        if plan is None:
            continue
        record = submit_simulated_approved_order(plan, approval)
        if record.submission_status == SIMULATED_SUBMITTED:
            records.append(record)
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown_queue(records, output_root_path)
    csv_path = _write_csv_queue(records, output_root_path)
    return {
        "count": len(records),
        "records": records,
        "queue_markdown": md_path,
        "queue_csv": csv_path,
    }


def find_simulated_submission_record(
    approval_id: str,
    records: Iterable[SimulatedSubmissionRecord] | None = None,
) -> SimulatedSubmissionRecord | None:
    records = list(records) if records is not None else []
    needle = approval_id.strip()
    for record in records:
        if record.approval_id == needle:
            return record
    return None
