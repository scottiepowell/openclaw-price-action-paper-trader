"""Manual approval artifacts for simulated-only execution.

This layer stays offline, never touches broker APIs, and keeps
`broker_action_allowed` false for every generated artifact.
"""

from __future__ import annotations

import csv
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable, Sequence

from price_action_paper_trader.domain.approval import ApprovalArtifact
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.services.order_plan_builder import build_order_plans


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "approvals"
APPROVAL_TEMPLATE_IDS = (
    "PTC-004",
    "PTC-005",
    "PTC-009",
    "PTC-017",
    "PTC-019",
    "PTC-021",
    "PTC-022",
    "PTC-024",
    "PTC-032",
    "PTC-034",
    "PTC-035",
)
def _derive_order_plan_id(candidate_id: str) -> str:
    candidate_id = candidate_id.strip().upper()
    return f"OP-{candidate_id}"


def _approval_id(candidate_id: str) -> str:
    candidate_id = candidate_id.strip().upper()
    return f"APR-{candidate_id}"
def _format_template_notes(plan: OrderPlan) -> str:
    return f"manual approval required for simulated-only execution; follow phase 7 boundaries for {plan.candidate_id}"


def build_manual_approval_template(plan: OrderPlan) -> ApprovalArtifact:
    candidate_id = plan.candidate_id.strip().upper()
    return ApprovalArtifact(
        approval_id=_approval_id(candidate_id),
        candidate_id=candidate_id,
        order_plan_id=_derive_order_plan_id(candidate_id),
        symbol=plan.symbol.strip().upper(),
        side=plan.side.strip().lower(),
        approved_by="",
        approved_at="",
        expires_at="",
        approval_status="pending",
        approval_scope="simulated_only",
        broker_action_allowed=False,
        notes=_format_template_notes(plan),
    )


def build_manual_approval_templates(plans: Sequence[OrderPlan] | None = None) -> list[ApprovalArtifact]:
    plans = list(plans) if plans is not None else build_order_plans()
    plan_by_candidate = {plan.candidate_id.strip().upper(): plan for plan in plans}

    templates: list[ApprovalArtifact] = []
    for candidate_id in APPROVAL_TEMPLATE_IDS:
        plan = plan_by_candidate.get(candidate_id)
        if plan is None:
            raise ValueError(f"missing order plan for approval template {candidate_id}")
        templates.append(build_manual_approval_template(plan))
    return templates


def serialize_manual_approval(approval: ApprovalArtifact) -> dict[str, Any]:
    data = asdict(approval)
    data["broker_action_allowed"] = str(approval.broker_action_allowed).lower()
    return data


def _write_markdown_queue(approvals: Sequence[ApprovalArtifact], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "approval_queue.md"
    lines = [
        "# Manual Approval Queue",
        "",
        "This queue is offline-only and keeps `broker_action_allowed: false` for every approval.",
        "",
        f"Generated approvals: {len(approvals)}",
        "",
        "| approval_id | candidate_id | order_plan_id | symbol | side | approval_status | approval_scope | broker_action_allowed |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for approval in approvals:
        lines.append(
            f"| {approval.approval_id} | {approval.candidate_id} | {approval.order_plan_id} | {approval.symbol} | {approval.side} | {approval.approval_status} | {approval.approval_scope} | {str(approval.broker_action_allowed).lower()} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv_queue(approvals: Sequence[ApprovalArtifact], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "approval_queue.csv"
    fieldnames = list(serialize_manual_approval(approvals[0]).keys()) if approvals else [
        "approval_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "approved_by",
        "approved_at",
        "expires_at",
        "approval_status",
        "approval_scope",
        "broker_action_allowed",
        "notes",
        "offline_only_boundary",
        "simulated_only_boundary",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for approval in approvals:
            writer.writerow(serialize_manual_approval(approval))
    return path


def _write_template_documents(approvals: Sequence[ApprovalArtifact], output_root: Path) -> list[Path]:
    template_dir = output_root / "templates"
    template_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for approval in approvals:
        path = template_dir / f"{approval.approval_id}-approval-template.md"
        path.write_text(
            "\n".join(
                [
                    f"# {approval.approval_id} Approval Template",
                    "",
                    f"- Approval ID: {approval.approval_id}",
                    f"- Candidate ID: {approval.candidate_id}",
                    f"- Order plan ID: {approval.order_plan_id}",
                    f"- Symbol: {approval.symbol}",
                    f"- Side: {approval.side}",
                    f"- Approved by: {approval.approved_by}",
                    f"- Approved at: {approval.approved_at}",
                    f"- Expires at: {approval.expires_at}",
                    f"- Approval status: {approval.approval_status}",
                    f"- Approval scope: {approval.approval_scope}",
                    f"- Broker action allowed: {str(approval.broker_action_allowed).lower()}",
                    f"- Notes: {approval.notes}",
                    "",
                    "This template is simulated-only. It must never be used to enable real broker action.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        paths.append(path)
    return paths


def _write_readme(output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "README.md"
    path.write_text(
        "\n".join(
            [
                "# Manual Approvals",
                "",
                "Offline-only approval artifacts for simulated execution.",
                "",
                "- `approval_queue.md` / `approval_queue.csv` list the manual approval templates.",
                "- `templates/` holds one markdown template per approved candidate.",
                "- `broker_action_allowed` must remain false everywhere.",
                "- `approval_scope` must remain `simulated_only`.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def generate_manual_approval_artifacts(
    plans: Sequence[OrderPlan] | None = None,
    output_root: str | Path | None = None,
) -> dict[str, Any]:
    approvals = build_manual_approval_templates(plans)
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown_queue(approvals, output_root_path)
    csv_path = _write_csv_queue(approvals, output_root_path)
    template_paths = _write_template_documents(approvals, output_root_path)
    readme_path = _write_readme(output_root_path)
    return {
        "count": len(approvals),
        "approvals": approvals,
        "queue_markdown": md_path,
        "queue_csv": csv_path,
        "template_documents": template_paths,
        "readme": readme_path,
    }


def load_manual_approval_queue(output_root: str | Path | None = None) -> list[ApprovalArtifact]:
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    queue_path = output_root_path / "approval_queue.csv"
    if not queue_path.exists():
        return build_manual_approval_templates()

    approvals: list[ApprovalArtifact] = []
    with queue_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            approvals.append(
                ApprovalArtifact(
                    approval_id=str(row.get("approval_id") or ""),
                    candidate_id=str(row.get("candidate_id") or ""),
                    order_plan_id=str(row.get("order_plan_id") or ""),
                    symbol=str(row.get("symbol") or "").upper(),
                    side=str(row.get("side") or "").lower(),
                    approved_by=str(row.get("approved_by") or ""),
                    approved_at=str(row.get("approved_at") or ""),
                    expires_at=str(row.get("expires_at") or ""),
                    approval_status=str(row.get("approval_status") or "pending"),
                    approval_scope=str(row.get("approval_scope") or "simulated_only"),
                    broker_action_allowed=str(row.get("broker_action_allowed") or "false").strip().lower() == "true",
                    notes=str(row.get("notes") or ""),
                )
            )
    return approvals


def find_manual_approval(approval_id: str, approvals: Iterable[ApprovalArtifact] | None = None) -> ApprovalArtifact | None:
    approvals = list(approvals) if approvals is not None else load_manual_approval_queue()
    needle = approval_id.strip()
    for approval in approvals:
        if approval.approval_id == needle:
            return approval
    return None


def validate_manual_approvals(approvals: Sequence[ApprovalArtifact] | None = None) -> list[str]:
    approvals = list(approvals) if approvals is not None else build_manual_approval_templates()
    issues: list[str] = []
    approvals_by_id = {approval.approval_id: approval for approval in approvals}

    for candidate_id in APPROVAL_TEMPLATE_IDS:
        approval_id = _approval_id(candidate_id)
        approval = approvals_by_id.get(approval_id)
        if approval is None:
            issues.append(f"missing approval template for {candidate_id}")
            continue
        if approval.candidate_id != candidate_id:
            issues.append(f"candidate mismatch for {approval_id}")
        if approval.order_plan_id != _derive_order_plan_id(candidate_id):
            issues.append(f"order plan mismatch for {approval_id}")
        if approval.approval_status != "pending":
            issues.append(f"approval status must default to pending for {approval_id}")
        if approval.approval_scope != "simulated_only":
            issues.append(f"approval scope must default to simulated_only for {approval_id}")
        if approval.broker_action_allowed:
            issues.append(f"broker action must remain false for {approval_id}")
        if not approval.symbol or not approval.side:
            issues.append(f"missing symbol or side for {approval_id}")
    return issues
