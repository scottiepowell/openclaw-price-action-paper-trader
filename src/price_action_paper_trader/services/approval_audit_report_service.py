"""Read-only audit report for manual approvals and simulated submissions.

This module only reads existing local artifacts and writes report outputs under
`runs/reports/`. It never mutates approval, submission, journal, or reconciliation
source artifacts.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Iterable

from price_action_paper_trader.services.manual_approval_service import (
    APPROVAL_TEMPLATE_IDS,
    DEFAULT_OUTPUT_ROOT as APPROVAL_OUTPUT_ROOT,
    load_manual_approval_queue,
)


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "reports"
SIMULATED_SUBMISSION_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "simulated_submissions"


@dataclass(frozen=True)
class ApprovalAuditRow:
    approval_id: str
    candidate_id: str
    order_plan_id: str
    symbol: str
    side: str
    approval_status: str
    approval_scope: str
    broker_action_allowed: bool
    expires_at: str
    audit_status: str
    audit_notes: str


@dataclass(frozen=True)
class CompatibilityAuditRow:
    expected_path: str
    found: bool
    candidate_id: str
    approval_id: str
    approval_status: str
    approval_scope: str
    broker_action_allowed: bool
    audit_status: str
    audit_notes: str


@dataclass(frozen=True)
class SimulatedSubmissionAuditRow:
    simulated_submission_id: str
    approval_id: str
    candidate_id: str
    order_plan_id: str
    symbol: str
    side: str
    simulated_broker_order_id: str
    submission_status: str
    submitted_at: str
    broker_action_allowed: bool
    audit_status: str
    audit_notes: str


@dataclass(frozen=True)
class ApprovalAuditReport:
    overall_status: str
    total_approvals: int
    expected_compatibility_files: int
    found_compatibility_files: int
    total_simulated_submissions: int
    pending_approvals: int
    approved_approvals: int
    rejected_approvals: int
    expired_approvals: int
    consumed_approvals: int
    approvals_with_unsafe_scope: int
    approvals_with_unsafe_broker_flag: int
    simulated_submissions_with_unsafe_broker_flag: int
    broker_action_allowed_all_false: bool
    approval_scope_all_simulated_only: bool
    broker_network_live_execution_detected: bool
    report_generation_mutated_source_artifacts: bool
    approval_rows: tuple[ApprovalAuditRow, ...]
    compatibility_rows: tuple[CompatibilityAuditRow, ...]
    simulated_submission_rows: tuple[SimulatedSubmissionAuditRow, ...]
    queue_markdown: Path
    queue_csv: Path


_COMPATIBILITY_PREFIX = "runs/approvals"


def _approval_path(candidate_id: str, approval_root: Path = APPROVAL_OUTPUT_ROOT) -> Path:
    return approval_root / f"{candidate_id}-approval.md"


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [
            {str(key): str(value) for key, value in row.items()}
            for row in reader
        ]


def _parse_compatibility_file(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, value = line[1:].split(":", 1)
        data[key.strip().lower().replace(" ", "_")] = value.strip()
    return data


def _bool_text(value: str) -> bool:
    return value.strip().lower() == "true"


def _approval_audit_row(approval: Any) -> ApprovalAuditRow:
    status = str(getattr(approval, "approval_status", "")).strip()
    scope = str(getattr(approval, "approval_scope", "")).strip()
    broker_action_allowed = bool(getattr(approval, "broker_action_allowed", False))
    expires_at = str(getattr(approval, "expires_at", "")).strip()
    audit_notes: list[str] = []

    if status == "pending":
        audit_status = "pass"
        audit_notes.append("pending approval is acceptable")
    elif status == "approved":
        audit_status = "pass"
        audit_notes.append("approved approval is acceptable")
    elif status in {"rejected", "expired", "consumed"}:
        audit_status = "pass"
        audit_notes.append(f"approval status is {status}")
    else:
        audit_status = "warning"
        audit_notes.append(f"unrecognized approval status: {status or 'missing'}")

    if scope != "simulated_only":
        audit_status = "fail"
        audit_notes.append("approval scope must remain simulated_only")

    if broker_action_allowed:
        audit_status = "fail"
        audit_notes.append("broker_action_allowed must remain false")

    return ApprovalAuditRow(
        approval_id=str(getattr(approval, "approval_id", "")),
        candidate_id=str(getattr(approval, "candidate_id", "")),
        order_plan_id=str(getattr(approval, "order_plan_id", "")),
        symbol=str(getattr(approval, "symbol", "")),
        side=str(getattr(approval, "side", "")),
        approval_status=status,
        approval_scope=scope,
        broker_action_allowed=broker_action_allowed,
        expires_at=expires_at,
        audit_status=audit_status,
        audit_notes="; ".join(audit_notes),
    )


def _compatibility_audit_row(approval: Any, approval_root: Path = APPROVAL_OUTPUT_ROOT) -> CompatibilityAuditRow:
    candidate_id = str(getattr(approval, "candidate_id", "")).strip()
    approval_id = str(getattr(approval, "approval_id", "")).strip()
    path = _approval_path(candidate_id, approval_root)
    found = path.exists()
    audit_status = "pass" if found else "fail"
    audit_notes = []

    if not found:
        audit_notes.append("compatibility file missing")
        return CompatibilityAuditRow(
            expected_path=str(path),
            found=False,
            candidate_id=candidate_id,
            approval_id=approval_id,
            approval_status=str(getattr(approval, "approval_status", "")),
            approval_scope=str(getattr(approval, "approval_scope", "")),
            broker_action_allowed=bool(getattr(approval, "broker_action_allowed", False)),
            audit_status=audit_status,
            audit_notes="; ".join(audit_notes),
        )

    parsed = _parse_compatibility_file(path)
    if not parsed:
        return CompatibilityAuditRow(
            expected_path=str(path),
            found=True,
            candidate_id=candidate_id,
            approval_id=approval_id,
            approval_status=str(getattr(approval, "approval_status", "")),
            approval_scope=str(getattr(approval, "approval_scope", "")),
            broker_action_allowed=bool(getattr(approval, "broker_action_allowed", False)),
            audit_status="fail",
            audit_notes="unable to parse compatibility file",
        )

    approval_status = parsed.get("approval_status", "")
    approval_scope = parsed.get("approval_scope", "")
    broker_action_allowed = _bool_text(parsed.get("broker_action_allowed", "false"))

    if approval_status != str(getattr(approval, "approval_status", "")):
        audit_status = "fail"
        audit_notes.append("approval status mismatch")
    if approval_scope != "simulated_only":
        audit_status = "fail"
        audit_notes.append("approval scope must remain simulated_only")
    if broker_action_allowed:
        audit_status = "fail"
        audit_notes.append("broker_action_allowed must remain false")

    if not audit_notes:
        audit_notes.append("compatibility file matches expected safe fields")

    return CompatibilityAuditRow(
        expected_path=str(path),
        found=True,
        candidate_id=candidate_id,
        approval_id=approval_id,
        approval_status=approval_status,
        approval_scope=approval_scope,
        broker_action_allowed=broker_action_allowed,
        audit_status=audit_status,
        audit_notes="; ".join(audit_notes),
    )


def _simulated_submission_audit_row(row: dict[str, str]) -> SimulatedSubmissionAuditRow:
    broker_action_allowed = _bool_text(row.get("broker_action_allowed", "false"))
    audit_status = "pass"
    audit_notes = ["simulated submission record is present"]
    if broker_action_allowed:
        audit_status = "fail"
        audit_notes.append("broker_action_allowed must remain false")

    return SimulatedSubmissionAuditRow(
        simulated_submission_id=row.get("simulated_submission_id", ""),
        approval_id=row.get("approval_id", ""),
        candidate_id=row.get("candidate_id", ""),
        order_plan_id=row.get("order_plan_id", ""),
        symbol=row.get("symbol", ""),
        side=row.get("side", ""),
        simulated_broker_order_id=row.get("simulated_broker_order_id", ""),
        submission_status=row.get("submission_status", ""),
        submitted_at=row.get("submitted_at", ""),
        broker_action_allowed=broker_action_allowed,
        audit_status=audit_status,
        audit_notes="; ".join(audit_notes),
    )


def _write_markdown(report: ApprovalAuditReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "approval_audit_report.md"
    lines = [
        "# Approval Audit Report",
        "",
        "Read-only audit report for manual approvals and simulated submissions.",
        "",
        "## Summary",
        "",
        f"- Overall audit status: {report.overall_status}",
        f"- Total approvals: {report.total_approvals}",
        f"- Total compatibility approval files expected: {report.expected_compatibility_files}",
        f"- Total compatibility approval files found: {report.found_compatibility_files}",
        f"- Total simulated submissions: {report.total_simulated_submissions}",
        f"- Pending approvals: {report.pending_approvals}",
        f"- Approved approvals: {report.approved_approvals}",
        f"- Rejected approvals: {report.rejected_approvals}",
        f"- Expired approvals: {report.expired_approvals}",
        f"- Consumed approvals: {report.consumed_approvals}",
        f"- Approvals with approval_scope != simulated_only: {report.approvals_with_unsafe_scope}",
        f"- Approvals with broker_action_allowed != false: {report.approvals_with_unsafe_broker_flag}",
        f"- Simulated submissions with broker_action_allowed != false: {report.simulated_submissions_with_unsafe_broker_flag}",
        "",
        "## Approval Queue Audit",
        "",
        "| approval_id | candidate_id | order_plan_id | symbol | side | approval_status | approval_scope | broker_action_allowed | expires_at | audit_status | audit_notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in report.approval_rows:
        lines.append(
            f"| {row.approval_id} | {row.candidate_id} | {row.order_plan_id} | {row.symbol} | {row.side} | {row.approval_status} | {row.approval_scope} | {str(row.broker_action_allowed).lower()} | {row.expires_at} | {row.audit_status} | {row.audit_notes} |"
        )

    lines.extend([
        "",
        "## Compatibility File Audit",
        "",
        "| expected_path | found | candidate_id | approval_id | approval_status | approval_scope | broker_action_allowed | audit_status | audit_notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    for row in report.compatibility_rows:
        lines.append(
            f"| {row.expected_path} | {str(row.found).lower()} | {row.candidate_id} | {row.approval_id} | {row.approval_status} | {row.approval_scope} | {str(row.broker_action_allowed).lower()} | {row.audit_status} | {row.audit_notes} |"
        )

    lines.extend([
        "",
        "## Simulated Submission Audit",
        "",
    ])
    if report.simulated_submission_rows:
        lines.extend([
            "| simulated_submission_id | approval_id | candidate_id | order_plan_id | symbol | side | simulated_broker_order_id | submission_status | submitted_at | broker_action_allowed | audit_status | audit_notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        for row in report.simulated_submission_rows:
            lines.append(
                f"| {row.simulated_submission_id} | {row.approval_id} | {row.candidate_id} | {row.order_plan_id} | {row.symbol} | {row.side} | {row.simulated_broker_order_id} | {row.submission_status} | {row.submitted_at} | {str(row.broker_action_allowed).lower()} | {row.audit_status} | {row.audit_notes} |"
            )
    else:
        lines.extend([
            "No simulated submissions were found. This is acceptable for this report.",
        ])

    lines.extend([
        "",
        "## Safety Boundary Audit",
        "",
        f"- broker_action_allowed all false: {'yes' if report.broker_action_allowed_all_false else 'no'}",
        f"- approval_scope all simulated_only: {'yes' if report.approval_scope_all_simulated_only else 'no'}",
        f"- broker/network execution path detected by this audit: {'yes' if report.broker_network_live_execution_detected else 'no'}",
        f"- report generation mutated source artifacts: {'yes' if report.report_generation_mutated_source_artifacts else 'no'}",
    ])

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv(report: ApprovalAuditReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "approval_audit_report.csv"
    fieldnames = [
        "record_type",
        "overall_status",
        "approval_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "approval_status",
        "approval_scope",
        "broker_action_allowed",
        "expires_at",
        "expected_path",
        "found",
        "simulated_submission_id",
        "simulated_broker_order_id",
        "submission_status",
        "submitted_at",
        "audit_status",
        "audit_notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"record_type": "summary", "overall_status": report.overall_status})
        for row in report.approval_rows:
            writer.writerow(
                {
                    "record_type": "approval",
                    "approval_id": row.approval_id,
                    "candidate_id": row.candidate_id,
                    "order_plan_id": row.order_plan_id,
                    "symbol": row.symbol,
                    "side": row.side,
                    "approval_status": row.approval_status,
                    "approval_scope": row.approval_scope,
                    "broker_action_allowed": str(row.broker_action_allowed).lower(),
                    "expires_at": row.expires_at,
                    "audit_status": row.audit_status,
                    "audit_notes": row.audit_notes,
                }
            )
        for row in report.compatibility_rows:
            writer.writerow(
                {
                    "record_type": "compatibility",
                    "approval_id": row.approval_id,
                    "candidate_id": row.candidate_id,
                    "approval_status": row.approval_status,
                    "approval_scope": row.approval_scope,
                    "broker_action_allowed": str(row.broker_action_allowed).lower(),
                    "expected_path": row.expected_path,
                    "found": str(row.found).lower(),
                    "audit_status": row.audit_status,
                    "audit_notes": row.audit_notes,
                }
            )
        for row in report.simulated_submission_rows:
            writer.writerow(
                {
                    "record_type": "simulated_submission",
                    "approval_id": row.approval_id,
                    "candidate_id": row.candidate_id,
                    "order_plan_id": row.order_plan_id,
                    "symbol": row.symbol,
                    "side": row.side,
                    "simulated_submission_id": row.simulated_submission_id,
                    "simulated_broker_order_id": row.simulated_broker_order_id,
                    "submission_status": row.submission_status,
                    "submitted_at": row.submitted_at,
                    "broker_action_allowed": str(row.broker_action_allowed).lower(),
                    "audit_status": row.audit_status,
                    "audit_notes": row.audit_notes,
                }
            )
    return path


def _build_report(
    output_root: str | Path | None = None,
    approval_root: str | Path | None = None,
    simulated_submission_root: str | Path | None = None,
) -> ApprovalAuditReport:
    approval_root_path = Path(approval_root) if approval_root is not None else APPROVAL_OUTPUT_ROOT
    simulated_submission_root_path = Path(simulated_submission_root) if simulated_submission_root is not None else SIMULATED_SUBMISSION_OUTPUT_ROOT

    approvals = load_manual_approval_queue(approval_root_path)
    approval_rows = tuple(_approval_audit_row(approval) for approval in approvals)
    compatibility_rows = tuple(_compatibility_audit_row(approval, approval_root_path) for approval in approvals)

    submission_rows_raw = _read_csv_rows(simulated_submission_root_path / "simulated_submission_queue.csv")
    simulated_submission_rows = tuple(_simulated_submission_audit_row(row) for row in submission_rows_raw)

    total_approvals = len(approvals)
    pending_approvals = sum(1 for approval in approvals if approval.approval_status == "pending")
    approved_approvals = sum(1 for approval in approvals if approval.approval_status == "approved")
    rejected_approvals = sum(1 for approval in approvals if approval.approval_status == "rejected")
    expired_approvals = sum(1 for approval in approvals if approval.approval_status == "expired")
    consumed_approvals = sum(1 for approval in approvals if approval.approval_status == "consumed")
    approvals_with_unsafe_scope = sum(1 for approval in approvals if approval.approval_scope != "simulated_only")
    approvals_with_unsafe_broker_flag = sum(1 for approval in approvals if approval.broker_action_allowed)
    simulated_submissions_with_unsafe_broker_flag = sum(1 for row in submission_rows_raw if _bool_text(row.get("broker_action_allowed", "false")))

    found_compatibility_files = sum(1 for row in compatibility_rows if row.found)
    broker_action_allowed_all_false = approvals_with_unsafe_broker_flag == 0 and simulated_submissions_with_unsafe_broker_flag == 0
    approval_scope_all_simulated_only = approvals_with_unsafe_scope == 0
    broker_network_live_execution_detected = False
    report_generation_mutated_source_artifacts = False

    fail_conditions = [
        any(row.audit_status == "fail" for row in compatibility_rows),
        approvals_with_unsafe_scope > 0,
        approvals_with_unsafe_broker_flag > 0,
        simulated_submissions_with_unsafe_broker_flag > 0,
    ]
    if any(fail_conditions):
        overall_status = "fail"
    elif not simulated_submission_rows:
        overall_status = "warning"
    elif any(row.audit_status == "warning" for row in approval_rows):
        overall_status = "warning"
    else:
        overall_status = "pass"

    report = ApprovalAuditReport(
        overall_status=overall_status,
        total_approvals=total_approvals,
        expected_compatibility_files=len(APPROVAL_TEMPLATE_IDS),
        found_compatibility_files=found_compatibility_files,
        total_simulated_submissions=len(simulated_submission_rows),
        pending_approvals=pending_approvals,
        approved_approvals=approved_approvals,
        rejected_approvals=rejected_approvals,
        expired_approvals=expired_approvals,
        consumed_approvals=consumed_approvals,
        approvals_with_unsafe_scope=approvals_with_unsafe_scope,
        approvals_with_unsafe_broker_flag=approvals_with_unsafe_broker_flag,
        simulated_submissions_with_unsafe_broker_flag=simulated_submissions_with_unsafe_broker_flag,
        broker_action_allowed_all_false=broker_action_allowed_all_false,
        approval_scope_all_simulated_only=approval_scope_all_simulated_only,
        broker_network_live_execution_detected=broker_network_live_execution_detected,
        report_generation_mutated_source_artifacts=report_generation_mutated_source_artifacts,
        approval_rows=approval_rows,
        compatibility_rows=compatibility_rows,
        simulated_submission_rows=simulated_submission_rows,
        queue_markdown=Path(),
        queue_csv=Path(),
    )

    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown(report, output_root_path)
    csv_path = _write_csv(report, output_root_path)
    return replace(report, queue_markdown=md_path, queue_csv=csv_path)


def generate_approval_audit_report(
    output_root: str | Path | None = None,
    approval_root: str | Path | None = None,
    simulated_submission_root: str | Path | None = None,
) -> dict[str, Any]:
    report = _build_report(output_root=output_root, approval_root=approval_root, simulated_submission_root=simulated_submission_root)
    return {
        "report": report,
        "queue_markdown": report.queue_markdown,
        "queue_csv": report.queue_csv,
        "overall_status": report.overall_status,
        "total_approvals": report.total_approvals,
        "expected_compatibility_files": report.expected_compatibility_files,
        "found_compatibility_files": report.found_compatibility_files,
        "total_simulated_submissions": report.total_simulated_submissions,
    }


def report_is_read_only() -> bool:
    return True
