"""Offline execution journal and reconciliation reporting.

This layer is read/write only to local files. It never talks to a broker or
network service and keeps `broker_action_allowed` false everywhere.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable, Sequence

from price_action_paper_trader.adapters.simulated_broker import SIMULATED_REJECTED, SIMULATED_SUBMITTED
from price_action_paper_trader.adapters.strategy_lab_reader import load_paper_review_queue, load_paper_watch_journal
from price_action_paper_trader.domain.execution_journal import ExecutionJournalEntry, ExecutionReconciliationReport
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.domain.execution_record import ExecutionRecord
from price_action_paper_trader.services.order_plan_builder import build_order_plans


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "execution_journal"
READY_REVIEW_STATUS = "READY_FOR_PAPER_REVIEW"


def _safe_get(obj: Any, name: str, default: Any = "") -> Any:
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _candidate_map(snapshot_root: str | Path | None = None) -> dict[str, dict[str, Any]]:
    review_rows = load_paper_review_queue(snapshot_root)
    watch_rows = load_paper_watch_journal(snapshot_root)
    watch_by_candidate = {str(row.get("candidate_id") or ""): row for row in watch_rows}

    merged: dict[str, dict[str, Any]] = {}
    for row in review_rows:
        candidate_id = str(row.get("candidate_id") or "")
        merged[candidate_id] = {
            "candidate_id": candidate_id,
            "replay_id": str(row.get("replay_id") or ""),
            "setup_type": str(row.get("setup_type") or ""),
            "source_watch_journal_id": str(row.get("journal_id") or ""),
            "source_status": str(row.get("source_status") or ""),
            "paper_review_status": str(row.get("paper_review_status") or ""),
            "watch_status": str(row.get("watch_status") or ""),
        }
        watch_row = watch_by_candidate.get(candidate_id, {})
        merged[candidate_id].update(
            {
                "watch_source_journal_id": str(watch_row.get("journal_id") or merged[candidate_id]["source_watch_journal_id"]),
                "watch_status": str(watch_row.get("watch_status") or merged[candidate_id]["watch_status"]),
                "paper_review_status": str(watch_row.get("paper_review_status") or merged[candidate_id]["paper_review_status"]),
                "planned_entry_price": float(watch_row.get("planned_entry_price") or 0.0),
                "planned_target_price": float(watch_row.get("planned_target_price") or 0.0),
                "planned_invalidation_level": float(watch_row.get("planned_invalidation_level") or 0.0),
            }
        )
    return merged


def _plan_map(plans: Sequence[OrderPlan] | None = None, snapshot_root: str | Path | None = None) -> dict[str, OrderPlan]:
    if plans is None:
        plans = build_order_plans(snapshot_root)
    return {plan.candidate_id: plan for plan in plans}


def _record_key(record: Any) -> str:
    return str(_safe_get(record, "candidate_id", "")).strip()


def _execution_id(record: Any) -> str:
    return str(_safe_get(record, "simulated_order_id", _safe_get(record, "execution_id", ""))).strip()


def _malformed_reason(record: Any) -> str:
    candidate_id = _record_key(record)
    symbol = str(_safe_get(record, "symbol", "")).strip()
    side = str(_safe_get(record, "side", "")).strip()
    execution_id = _execution_id(record)
    if not candidate_id:
        return "missing candidate id"
    if not symbol:
        return "missing symbol"
    if not side:
        return "missing side"
    if not execution_id:
        return "missing execution id"
    fill_price = _safe_get(record, "fill_price", 0.0)
    try:
        if float(fill_price) < 0:
            return "negative fill price"
    except (TypeError, ValueError):
        return "invalid fill price"
    return ""


def _duplicate_reason(candidate_id: str, execution_id: str, seen_candidates: set[str], seen_executions: set[str]) -> str:
    if candidate_id in seen_candidates:
        return "duplicate candidate execution record"
    if execution_id in seen_executions:
        return "duplicate execution id"
    return ""


def _lineage_id(candidate_id: str, replay_id: str, execution_id: str, snapshot_source: str) -> str:
    seed = "|".join([candidate_id, replay_id, execution_id, snapshot_source])
    return f"EJ-{sha256(seed.encode('utf-8')).hexdigest()[:16].upper()}"


def build_execution_journal_entries(
    records: Sequence[Any],
    plans: Sequence[OrderPlan] | None = None,
    approved_candidate_ids: Iterable[str] | None = None,
    snapshot_root: str | Path | None = None,
) -> list[ExecutionJournalEntry]:
    plan_by_candidate = _plan_map(plans, snapshot_root)
    candidate_meta = _candidate_map(snapshot_root)
    approved = {candidate_id.strip() for candidate_id in (approved_candidate_ids or []) if candidate_id.strip()}

    entries: list[ExecutionJournalEntry] = []
    seen_candidates: set[str] = set()
    seen_executions: set[str] = set()

    for index, record in enumerate(records, start=1):
        candidate_id = _record_key(record)
        execution_id = _execution_id(record)
        malformed_reason = _malformed_reason(record)
        duplicate_reason = _duplicate_reason(candidate_id, execution_id, seen_candidates, seen_executions) if not malformed_reason else ""
        plan = plan_by_candidate.get(candidate_id)
        meta = candidate_meta.get(candidate_id, {})

        execution_status = str(_safe_get(record, "execution_status", "")).strip()
        fill_status = str(_safe_get(record, "fill_status", "")).strip()
        fill_price = float(_safe_get(record, "fill_price", 0.0) or 0.0)
        notes = str(_safe_get(record, "notes", "")).strip()
        snapshot_source = str(_safe_get(record, "snapshot_source", _safe_get(plan, "snapshot_source", "")) or "")
        plan_status = str(_safe_get(plan, "plan_status", ""))
        source_plan_snapshot_source = str(_safe_get(plan, "snapshot_source", snapshot_source) or snapshot_source)
        replay_id = str(meta.get("replay_id") or "")
        setup_type = str(meta.get("setup_type") or "")
        source_watch_journal_id = str(meta.get("watch_source_journal_id") or meta.get("source_watch_journal_id") or "")
        source_status = str(meta.get("source_status") or "")
        watch_status = str(meta.get("watch_status") or "")
        target_price = float(meta.get("planned_target_price") or _safe_get(plan, "target_price", 0.0) or 0.0)
        invalidation_level = float(meta.get("planned_invalidation_level") or _safe_get(plan, "invalidation_level", 0.0) or 0.0)
        manual_approval_granted = candidate_id in approved

        if malformed_reason:
            reconciliation_status = "MALFORMED"
        elif duplicate_reason:
            reconciliation_status = "DUPLICATE"
        elif execution_status in {SIMULATED_REJECTED, "REJECTED", "BLOCKED"}:
            reconciliation_status = "REJECTED"
        elif fill_status in {"FILLED", "PARTIALLY_FILLED"}:
            reconciliation_status = "CLOSED"
        elif manual_approval_granted:
            reconciliation_status = "OPEN"
        else:
            reconciliation_status = "PENDING_APPROVAL"

        if not replay_id and candidate_id in plan_by_candidate:
            replay_id = source_watch_journal_id.replace("PWJ", "HR") if source_watch_journal_id else ""

        lineage_id = _lineage_id(candidate_id, replay_id, execution_id, source_plan_snapshot_source)

        entry = ExecutionJournalEntry(
            journal_id=f"EJ-{index:03d}",
            candidate_id=candidate_id,
            replay_id=replay_id,
            symbol=str(_safe_get(record, "symbol", _safe_get(plan, "symbol", ""))).strip().upper(),
            side=str(_safe_get(record, "side", _safe_get(plan, "side", ""))).strip().lower(),
            setup_type=setup_type or str(_safe_get(plan, "classification", "")).strip(),
            source_watch_journal_id=source_watch_journal_id,
            source_plan_status=plan_status,
            source_plan_snapshot_source=source_plan_snapshot_source,
            execution_id=execution_id,
            execution_status=execution_status,
            manual_approval_required=True,
            manual_approval_granted=manual_approval_granted,
            broker_action_allowed=False,
            fill_status=fill_status,
            fill_price=fill_price,
            target_price=target_price,
            invalidation_level=invalidation_level,
            reconciliation_status=reconciliation_status,
            duplicate_of=duplicate_reason,
            malformed_reason=malformed_reason,
            notes=notes,
            created_at_utc=str(_safe_get(record, "submission_timestamp_utc", "")).strip(),
            snapshot_source=snapshot_source,
            lineage_id=lineage_id,
        )
        entries.append(entry)

        if candidate_id:
            seen_candidates.add(candidate_id)
        if execution_id:
            seen_executions.add(execution_id)

    return entries


def summarize_execution_journal(entries: Sequence[ExecutionJournalEntry]) -> ExecutionReconciliationReport:
    total_entries = len(entries)
    approved_entries = sum(1 for entry in entries if entry.manual_approval_granted)
    pending_approval_entries = sum(1 for entry in entries if entry.reconciliation_status == "PENDING_APPROVAL")
    open_entries = sum(1 for entry in entries if entry.reconciliation_status == "OPEN")
    closed_entries = sum(1 for entry in entries if entry.reconciliation_status == "CLOSED")
    rejected_entries = sum(1 for entry in entries if entry.reconciliation_status == "REJECTED")
    duplicate_entries = sum(1 for entry in entries if entry.reconciliation_status == "DUPLICATE")
    malformed_entries = sum(1 for entry in entries if entry.reconciliation_status == "MALFORMED")
    return ExecutionReconciliationReport(
        total_entries=total_entries,
        approved_entries=approved_entries,
        pending_approval_entries=pending_approval_entries,
        open_entries=open_entries,
        closed_entries=closed_entries,
        rejected_entries=rejected_entries,
        duplicate_entries=duplicate_entries,
        malformed_entries=malformed_entries,
        journal_entries=tuple(entries),
    )


def serialize_execution_journal_entry(entry: ExecutionJournalEntry) -> dict[str, Any]:
    data = asdict(entry)
    data["fill_price"] = f"{entry.fill_price:.2f}"
    data["target_price"] = f"{entry.target_price:.2f}"
    data["invalidation_level"] = f"{entry.invalidation_level:.2f}"
    data["manual_approval_required"] = str(entry.manual_approval_required).lower()
    data["manual_approval_granted"] = str(entry.manual_approval_granted).lower()
    data["broker_action_allowed"] = str(entry.broker_action_allowed).lower()
    return data


def _write_csv(entries: Sequence[ExecutionJournalEntry], output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "execution_journal.csv"
    fieldnames = list(serialize_execution_journal_entry(entries[0]).keys()) if entries else [
        "journal_id",
        "candidate_id",
        "replay_id",
        "symbol",
        "side",
        "setup_type",
        "source_watch_journal_id",
        "source_plan_status",
        "source_plan_snapshot_source",
        "execution_id",
        "execution_status",
        "manual_approval_required",
        "manual_approval_granted",
        "broker_action_allowed",
        "fill_status",
        "fill_price",
        "target_price",
        "invalidation_level",
        "reconciliation_status",
        "duplicate_of",
        "malformed_reason",
        "notes",
        "created_at_utc",
        "snapshot_source",
        "lineage_id",
        "offline_only_boundary",
        "simulated_only_boundary",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(serialize_execution_journal_entry(entry))
    return path


def _write_markdown(entries: Sequence[ExecutionJournalEntry], report: ExecutionReconciliationReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "execution_journal.md"
    lines = [
        "# Execution Journal",
        "",
        "Offline-only execution journal and reconciliation summary.",
        "",
        f"- Total entries: {report.total_entries}",
        f"- Approved entries: {report.approved_entries}",
        f"- Pending approval entries: {report.pending_approval_entries}",
        f"- Open entries: {report.open_entries}",
        f"- Closed entries: {report.closed_entries}",
        f"- Rejected entries: {report.rejected_entries}",
        f"- Duplicate entries: {report.duplicate_entries}",
        f"- Malformed entries: {report.malformed_entries}",
        "",
        "| journal_id | candidate_id | execution_id | status | approval | reconciliation | broker_action_allowed |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        lines.append(
            f"| {entry.journal_id} | {entry.candidate_id} | {entry.execution_id} | {entry.execution_status} | {str(entry.manual_approval_granted).lower()} | {entry.reconciliation_status} | {str(entry.broker_action_allowed).lower()} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_json(report: ExecutionReconciliationReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "execution_reconciliation_report.json"
    payload = {
        "total_entries": report.total_entries,
        "approved_entries": report.approved_entries,
        "pending_approval_entries": report.pending_approval_entries,
        "open_entries": report.open_entries,
        "closed_entries": report.closed_entries,
        "rejected_entries": report.rejected_entries,
        "duplicate_entries": report.duplicate_entries,
        "malformed_entries": report.malformed_entries,
        "broker_action_allowed": False,
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _write_audit_markdown(report: ExecutionReconciliationReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "execution_reconciliation_report.md"
    path.write_text(
        "\n".join(
            [
                "# Execution Reconciliation Report",
                "",
                "- Offline-only: true",
                "- Network access: prohibited",
                "- Alpaca access: prohibited",
                "- Broker action allowed: false",
                f"- Total entries: {report.total_entries}",
                f"- Approved entries: {report.approved_entries}",
                f"- Pending approval entries: {report.pending_approval_entries}",
                f"- Open entries: {report.open_entries}",
                f"- Closed entries: {report.closed_entries}",
                f"- Rejected entries: {report.rejected_entries}",
                f"- Duplicate entries: {report.duplicate_entries}",
                f"- Malformed entries: {report.malformed_entries}",
                "",
                "This artifact is a local audit summary only. It does not submit orders or call a broker.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def generate_execution_journal_artifacts(
    approved_candidate_ids: Iterable[str],
    snapshot_root: str | Path | None = None,
    output_root: str | Path | None = None,
    records: Sequence[Any] | None = None,
    plans: Sequence[OrderPlan] | None = None,
) -> dict[str, Any]:
    approved_candidate_ids = tuple(approved_candidate_ids)
    plans = list(plans or build_order_plans(snapshot_root))
    records = list(records or [])
    if not records:
        from price_action_paper_trader.adapters.simulated_broker import submit_simulated_orders

        records = submit_simulated_orders(plans)

    entries = build_execution_journal_entries(
        records=records,
        plans=plans,
        approved_candidate_ids=approved_candidate_ids,
        snapshot_root=snapshot_root,
    )
    report = summarize_execution_journal(entries)
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT

    csv_path = _write_csv(entries, output_root_path)
    md_path = _write_markdown(entries, report, output_root_path)
    json_path = _write_json(report, output_root_path)
    audit_md_path = _write_audit_markdown(report, output_root_path)

    return {
        "count": len(entries),
        "entries": entries,
        "report": report,
        "queue_csv": csv_path,
        "queue_markdown": md_path,
        "report_json": json_path,
        "report_markdown": audit_md_path,
    }
