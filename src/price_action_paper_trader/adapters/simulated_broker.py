"""Offline-only simulated broker adapter.

This module never talks to a real broker and never opens a network connection.
"""

from __future__ import annotations

import csv
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any

from price_action_paper_trader.domain.execution_record import ExecutionRecord
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.risk_gate import phase3_risk_gate


SIMULATED_SUBMITTED = "SIMULATED_SUBMITTED"
SIMULATED_REJECTED = "SIMULATED_REJECTED"
DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "simulated_execution"
_TIMESTAMP_ANCHOR = datetime(2026, 5, 24, tzinfo=timezone.utc)


def _order_seed(plan: OrderPlan) -> str:
    if not isinstance(plan, OrderPlan):
        return "malformed-plan"
    return "|".join(
        [
            plan.candidate_id.strip(),
            plan.symbol.strip().upper(),
            plan.side.strip().lower(),
            plan.classification.strip(),
            f"{plan.entry_reference:.4f}",
            f"{plan.target_price:.4f}",
            f"{plan.invalidation_level:.4f}",
            plan.readiness_status.strip(),
            plan.snapshot_source.strip(),
        ]
    )


def _fake_order_id(plan: OrderPlan) -> str:
    if not isinstance(plan, OrderPlan):
        digest = sha256(b"malformed-plan").hexdigest()[:12].upper()
        return f"SIM-MALFORMED-{digest}"
    digest = sha256(_order_seed(plan).encode("utf-8")).hexdigest()[:12].upper()
    return f"SIM-{plan.candidate_id.strip()}-{digest}"


def _submission_timestamp(plan: OrderPlan) -> str:
    if not isinstance(plan, OrderPlan):
        return _TIMESTAMP_ANCHOR.isoformat()
    digest = int(sha256(_order_seed(plan).encode("utf-8")).hexdigest()[:8], 16)
    return (_TIMESTAMP_ANCHOR + timedelta(seconds=digest % 86400)).isoformat()


def _malformed_reason(plan: OrderPlan) -> str:
    if not isinstance(plan, OrderPlan):
        return "malformed plan object"
    if not plan.candidate_id.strip():
        return "missing candidate id"
    if not plan.symbol.strip():
        return "missing symbol"
    if not plan.side.strip():
        return "missing side"
    if plan.entry_reference < 0 or plan.target_price <= 0 or plan.invalidation_level <= 0:
        return "missing or invalid price levels"
    if plan.created_at_utc and not _is_iso_timestamp(plan.created_at_utc):
        return "invalid submission timestamp"
    return ""


def _is_iso_timestamp(value: str) -> bool:
    try:
        datetime.fromisoformat(value)
    except ValueError:
        return False
    return True


def _safe_plan_fields(plan: OrderPlan) -> tuple[str, str, str, str]:
    if not isinstance(plan, OrderPlan):
        return "", "", "", ""
    return (
        plan.candidate_id.strip(),
        plan.symbol.strip().upper(),
        plan.side.strip().lower(),
        plan.snapshot_source,
    )


def _build_record(
    plan: OrderPlan,
    execution_status: str,
    risk_gate_status: str,
    risk_gate_reason: str,
    notes: str,
) -> ExecutionRecord:
    candidate_id, symbol, side, snapshot_source = _safe_plan_fields(plan)
    return ExecutionRecord(
        candidate_id=candidate_id,
        symbol=symbol,
        side=side,
        simulated_order_id=_fake_order_id(plan),
        execution_status=execution_status,
        submission_timestamp_utc=_submission_timestamp(plan),
        fill_status="NOT_FILLED",
        fill_price=0.0,
        notes=notes,
        broker_action_allowed=False,
        risk_gate_status=risk_gate_status,
        risk_gate_reason=risk_gate_reason,
        snapshot_source=snapshot_source,
    )


def submit_simulated_order(plan: OrderPlan) -> ExecutionRecord:
    malformed_reason = _malformed_reason(plan)
    if malformed_reason:
        return _build_record(
            plan,
            SIMULATED_REJECTED,
            "MALFORMED",
            malformed_reason,
            f"offline simulation only; rejected: {malformed_reason}",
        )

    decision = phase3_risk_gate(plan)
    if not decision.allowed:
        return _build_record(
            plan,
            SIMULATED_REJECTED,
            "BLOCKED",
            decision.reason,
            f"offline simulation only; rejected by risk gate: {decision.reason}",
        )

    return _build_record(
        plan,
        SIMULATED_SUBMITTED,
        "PASSED",
        decision.reason,
        "offline simulation only; submitted without fills",
    )


def submit_simulated_orders(plans: list[OrderPlan]) -> list[ExecutionRecord]:
    seen: set[str] = set()
    records: list[ExecutionRecord] = []
    for plan in plans:
        record = submit_simulated_order(plan)
        if record.candidate_id in seen and record.execution_status == SIMULATED_SUBMITTED:
            record = ExecutionRecord(
                **{**asdict(record), "execution_status": SIMULATED_REJECTED, "risk_gate_status": "BLOCKED", "risk_gate_reason": "duplicate candidate blocked", "notes": "offline simulation only; rejected by duplicate guard"}
            )
        seen.add(record.candidate_id)
        records.append(record)
    return records


def serialize_execution_record(record: ExecutionRecord) -> dict[str, Any]:
    data = asdict(record)
    data["fill_price"] = f"{record.fill_price:.2f}"
    data["broker_action_allowed"] = str(record.broker_action_allowed).lower()
    return data


def _write_markdown_queue(records: list[ExecutionRecord], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_execution_queue.md"
    lines = [
        "# Simulated Execution Queue",
        "",
        "This queue is offline-only, simulated-only, and keeps `broker_action_allowed: false` for every record.",
        "",
        f"Generated records: {len(records)}",
        "",
        "| candidate_id | symbol | side | simulated_order_id | execution_status | risk_gate_status | broker_action_allowed |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            f"| {record.candidate_id} | {record.symbol} | {record.side} | {record.simulated_order_id} | {record.execution_status} | {record.risk_gate_status} | {str(record.broker_action_allowed).lower()} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv_queue(records: list[ExecutionRecord], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_execution_queue.csv"
    fieldnames = list(serialize_execution_record(records[0]).keys()) if records else [
        "candidate_id",
        "symbol",
        "side",
        "simulated_order_id",
        "execution_status",
        "submission_timestamp_utc",
        "fill_status",
        "fill_price",
        "notes",
        "broker_action_allowed",
        "risk_gate_status",
        "risk_gate_reason",
        "snapshot_source",
        "offline_only_boundary",
        "simulated_only_boundary",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(serialize_execution_record(record))
    return path


def _write_record_documents(records: list[ExecutionRecord], output_root: Path) -> list[Path]:
    record_dir = output_root / "records"
    record_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for record in records:
        path = record_dir / f"{record.candidate_id}-simulated-execution.md"
        path.write_text(
            "\n".join(
                [
                    f"# {record.candidate_id} Simulated Execution",
                    "",
                    f"- Candidate ID: {record.candidate_id}",
                    f"- Symbol: {record.symbol}",
                    f"- Side: {record.side}",
                    f"- Simulated order ID: {record.simulated_order_id}",
                    f"- Execution status: {record.execution_status}",
                    f"- Submission timestamp UTC: {record.submission_timestamp_utc}",
                    f"- Fill status: {record.fill_status}",
                    f"- Fill price: {record.fill_price:.2f}",
                    f"- Notes: {record.notes}",
                    f"- Snapshot source: {record.snapshot_source}",
                    f"- Risk gate status: {record.risk_gate_status}",
                    f"- Risk gate reason: {record.risk_gate_reason}",
                    f"- Broker action allowed: {str(record.broker_action_allowed).lower()}",
                    f"- Offline-only boundary: {record.offline_only_boundary}",
                    f"- Simulated-only boundary: {record.simulated_only_boundary}",
                    "",
                    "This is an offline-only simulated execution artifact. No broker submission, no network calls, and no live execution are allowed.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        paths.append(path)
    return paths


def generate_simulated_execution_artifacts(snapshot_root: str | Path | None = None, output_root: str | Path | None = None) -> dict[str, Any]:
    plans = build_order_plans(snapshot_root)
    records = submit_simulated_orders(plans)
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown_queue(records, output_root_path)
    csv_path = _write_csv_queue(records, output_root_path)
    record_paths = _write_record_documents(records, output_root_path)
    return {
        "count": len(records),
        "plans": plans,
        "records": records,
        "queue_markdown": md_path,
        "queue_csv": csv_path,
        "record_documents": record_paths,
    }
