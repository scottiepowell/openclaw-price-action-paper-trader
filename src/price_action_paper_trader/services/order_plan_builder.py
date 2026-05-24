"""Build offline paper order plans from imported Strategy Lab snapshots."""

from __future__ import annotations

import csv
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from price_action_paper_trader.adapters.strategy_lab_reader import (
    load_paper_readiness_matrix,
    load_paper_review_queue,
)
from price_action_paper_trader.domain.order_plan import OrderPlan


READY_STATUS = "READY_FOR_PAPER_REVIEW"
PLAN_STATUS = "DRAFT"
DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "order_plans"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _normalize_row(row: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in row.items() if value is not None}


def _snapshot_source(snapshot_root: str | Path | None) -> str:
    if snapshot_root is None:
        return "data_refs/strategy_lab/snapshots/strategy_lab_snapshot_v1"
    return str(Path(snapshot_root))


def build_order_plan(candidate_row: dict[str, Any], readiness_row: dict[str, Any] | None = None, snapshot_root: str | Path | None = None) -> OrderPlan:
    readiness_row = readiness_row or {}
    classification = str(candidate_row.get("replay_classification") or readiness_row.get("classification") or "")
    entry_reference = float(candidate_row.get("entry_candidate_price") or 0.0)
    target_price = float(candidate_row.get("target_price") or 0.0)
    invalidation_level = float(candidate_row.get("invalidation_level") or 0.0)
    risk_notes = str(candidate_row.get("next_action") or readiness_row.get("blocking_reason") or "offline planning only")

    return OrderPlan(
        candidate_id=str(candidate_row.get("candidate_id") or readiness_row.get("candidate_id") or ""),
        symbol=str(candidate_row.get("symbol") or readiness_row.get("symbol") or ""),
        side=str(candidate_row.get("side") or readiness_row.get("side") or ""),
        classification=classification,
        entry_reference=entry_reference,
        target_price=target_price,
        invalidation_level=invalidation_level,
        risk_notes=risk_notes,
        readiness_status=str(readiness_row.get("readiness_status") or ""),
        plan_status=PLAN_STATUS,
        snapshot_source=_snapshot_source(snapshot_root),
        broker_action_allowed=False,
        created_at_utc=_utc_now(),
    )


def build_order_plans(snapshot_root: str | Path | None = None) -> list[OrderPlan]:
    review_queue = load_paper_review_queue(snapshot_root)
    readiness_matrix = load_paper_readiness_matrix(snapshot_root)
    readiness_by_candidate = {str(row["candidate_id"]): row for row in readiness_matrix}

    plans: list[OrderPlan] = []
    for candidate_row in review_queue:
        candidate_id = str(candidate_row.get("candidate_id") or "")
        readiness_row = readiness_by_candidate.get(candidate_id, {})
        if str(readiness_row.get("readiness_status") or "") != READY_STATUS:
            continue
        plans.append(build_order_plan(candidate_row, readiness_row, snapshot_root))
    return plans


def serialize_order_plan(plan: OrderPlan) -> dict[str, Any]:
    data = asdict(plan)
    data["entry_reference"] = f"{plan.entry_reference:.2f}"
    data["target_price"] = f"{plan.target_price:.2f}"
    data["invalidation_level"] = f"{plan.invalidation_level:.2f}"
    data["broker_action_allowed"] = str(plan.broker_action_allowed).lower()
    return data


def _write_markdown_queue(plans: list[OrderPlan], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    queue_path = output_root / "order_plan_queue.md"
    lines = [
        "# Offline Order Plan Queue",
        "",
        "This queue is read-only and keeps `broker_action_allowed: false` for every plan.",
        "",
        f"Generated plans: {len(plans)}",
        "",
        "| candidate_id | symbol | side | classification | entry_reference | target_price | invalidation_level | plan_status | broker_action_allowed |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for plan in plans:
        lines.append(
            f"| {plan.candidate_id} | {plan.symbol} | {plan.side} | {plan.classification} | {plan.entry_reference:.2f} | {plan.target_price:.2f} | {plan.invalidation_level:.2f} | {plan.plan_status} | {str(plan.broker_action_allowed).lower()} |"
        )
    queue_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return queue_path


def _write_csv_queue(plans: list[OrderPlan], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    queue_path = output_root / "order_plan_queue.csv"
    fieldnames = list(serialize_order_plan(plans[0]).keys()) if plans else [
        "candidate_id",
        "symbol",
        "side",
        "classification",
        "entry_reference",
        "target_price",
        "invalidation_level",
        "risk_notes",
        "readiness_status",
        "plan_status",
        "snapshot_source",
        "broker_action_allowed",
        "created_at_utc",
    ]
    with queue_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for plan in plans:
            writer.writerow(serialize_order_plan(plan))
    return queue_path


def _write_plan_documents(plans: list[OrderPlan], output_root: Path) -> list[Path]:
    plan_dir = output_root / "plans"
    plan_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for plan in plans:
        path = plan_dir / f"{plan.candidate_id}-order-plan.md"
        path.write_text(
            "\n".join(
                [
                    f"# {plan.candidate_id} Order Plan",
                    "",
                    f"- Candidate ID: {plan.candidate_id}",
                    f"- Symbol: {plan.symbol}",
                    f"- Side: {plan.side}",
                    f"- Replay classification: {plan.classification}",
                    f"- Entry reference: {plan.entry_reference:.2f}",
                    f"- Target price: {plan.target_price:.2f}",
                    f"- Invalidation level: {plan.invalidation_level:.2f}",
                    f"- Read-only risk notes: {plan.risk_notes}",
                    f"- Readiness status: {plan.readiness_status}",
                    f"- Plan status: {plan.plan_status}",
                    f"- Snapshot source: {plan.snapshot_source}",
                    f"- Broker action allowed: {str(plan.broker_action_allowed).lower()}",
                    "",
                    "This is an offline planning artifact only. No broker submission or live execution is allowed.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        paths.append(path)
    return paths


def generate_order_plan_artifacts(snapshot_root: str | Path | None = None, output_root: str | Path | None = None) -> dict[str, Any]:
    plans = build_order_plans(snapshot_root)
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown_queue(plans, output_root_path)
    csv_path = _write_csv_queue(plans, output_root_path)
    plan_paths = _write_plan_documents(plans, output_root_path)
    return {
        "count": len(plans),
        "plans": plans,
        "queue_markdown": md_path,
        "queue_csv": csv_path,
        "plan_documents": plan_paths,
    }
