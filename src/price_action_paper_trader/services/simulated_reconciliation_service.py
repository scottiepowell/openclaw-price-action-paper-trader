"""Offline-only reconciliation for simulated execution journal artifacts."""

from __future__ import annotations

import csv
from dataclasses import asdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any

from price_action_paper_trader.domain.simulated_journal import (
    SimulatedExecutionJournalRecord,
    SimulatedReconciliationRecord,
    SimulatedReconciliationReport,
)
from price_action_paper_trader.services.simulated_execution_journal_service import (
    DEFAULT_OUTPUT_ROOT as DEFAULT_JOURNAL_OUTPUT_ROOT,
    DEFAULT_SUBMISSION_ROOT,
    read_simulated_submission_rows,
)


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "reconciliation"
RECONCILED_SIMULATED_ONLY = "RECONCILED_SIMULATED_ONLY"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _bool_text(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


def _read_journal_rows(journal_root: str | Path | None = None) -> list[dict[str, str]]:
    root = Path(journal_root) if journal_root is not None else DEFAULT_JOURNAL_OUTPUT_ROOT
    path = root / "simulated_execution_journal.csv"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [{str(key): str(value) for key, value in row.items()} for row in reader]


def _journal_record_from_row(row: dict[str, str]) -> SimulatedExecutionJournalRecord:
    return SimulatedExecutionJournalRecord(
        journal_record_id=row.get("journal_record_id", "").strip(),
        simulated_submission_id=row.get("simulated_submission_id", "").strip(),
        approval_id=row.get("approval_id", "").strip(),
        candidate_id=row.get("candidate_id", "").strip(),
        order_plan_id=row.get("order_plan_id", "").strip(),
        symbol=row.get("symbol", "").strip(),
        side=row.get("side", "").strip(),
        simulated_broker_order_id=row.get("simulated_broker_order_id", "").strip(),
        execution_status=row.get("execution_status", "").strip(),
        journaled_at=row.get("journaled_at", "").strip(),
        broker_action_allowed=_bool_text(row.get("broker_action_allowed", "false")),
        notes=row.get("notes", "").strip(),
        submission_status=row.get("submission_status", "").strip(),
    )


def _reconciliation_id(submission_id: str, journal_id: str, status: str) -> str:
    seed = "|".join([submission_id, journal_id, status])
    digest = sha256(seed.encode("utf-8")).hexdigest()[:12].upper()
    prefix = submission_id or journal_id or "RECON"
    return f"RC-{prefix}-{digest}"


def build_simulated_reconciliation_records(
    submission_rows: list[dict[str, str]],
    journal_rows: list[dict[str, str]],
) -> tuple[list[SimulatedReconciliationRecord], SimulatedReconciliationReport]:
    submission_by_id = {row.get("simulated_submission_id", "").strip(): row for row in submission_rows if row.get("simulated_submission_id", "").strip()}
    journal_by_id = {row.get("simulated_submission_id", "").strip(): row for row in journal_rows if row.get("simulated_submission_id", "").strip()}
    all_ids = sorted(set(submission_by_id) | set(journal_by_id))

    records: list[SimulatedReconciliationRecord] = []
    missing_submission_records = 0
    missing_journal_records = 0
    mismatched_records = 0
    unsafe_broker_flags = 0

    for simulated_submission_id in all_ids:
        submission = submission_by_id.get(simulated_submission_id)
        journal = journal_by_id.get(simulated_submission_id)
        status = RECONCILED_SIMULATED_ONLY
        notes: list[str] = ["offline simulation only; reconciliation completed"]

        if submission is None:
            status = "MISSING_SUBMISSION_RECORD"
            missing_submission_records += 1
            notes = ["missing submission record"]
        elif journal is None:
            status = "MISSING_JOURNAL_RECORD"
            missing_journal_records += 1
            notes = ["missing journal record"]
        else:
            fields_to_compare = (
                "approval_id",
                "candidate_id",
                "order_plan_id",
                "symbol",
                "side",
                "simulated_broker_order_id",
                "submission_status",
            )
            mismatched_fields = [field for field in fields_to_compare if str(submission.get(field, "")).strip() != str(journal.get(field, "")).strip()]
            if _bool_text(submission.get("broker_action_allowed", "false")) or _bool_text(journal.get("broker_action_allowed", "false")):
                status = "UNSAFE_BROKER_FLAG"
                unsafe_broker_flags += 1
                notes = ["broker_action_allowed must remain false"]
            elif mismatched_fields:
                status = "ID_MISMATCH"
                mismatched_records += 1
                notes = ["mismatched fields: " + ", ".join(mismatched_fields)]

        record = SimulatedReconciliationRecord(
            reconciliation_id=_reconciliation_id(
                simulated_submission_id,
                str((journal or {}).get("journal_record_id", "")).strip(),
                status,
            ),
            simulated_submission_id=simulated_submission_id,
            journal_record_id=str((journal or {}).get("journal_record_id", "")).strip(),
            candidate_id=str((submission or journal or {}).get("candidate_id", "")).strip(),
            order_plan_id=str((submission or journal or {}).get("order_plan_id", "")).strip(),
            symbol=str((submission or journal or {}).get("symbol", "")).strip(),
            side=str((submission or journal or {}).get("side", "")).strip(),
            simulated_broker_order_id=str((submission or journal or {}).get("simulated_broker_order_id", "")).strip(),
            submission_status=str((submission or {}).get("submission_status", "")).strip(),
            execution_status=str((journal or {}).get("execution_status", "")).strip(),
            reconciliation_status=status,
            reconciled_at=_utc_now(),
            broker_action_allowed=False,
            notes="; ".join(notes),
        )
        records.append(record)

    broker_action_allowed_all_false = all(not _bool_text(row.get("broker_action_allowed", "false")) for row in submission_rows) and all(
        not _bool_text(row.get("broker_action_allowed", "false")) for row in journal_rows
    )
    overall_status = "pass"
    if missing_submission_records or missing_journal_records or mismatched_records or unsafe_broker_flags or not records:
        overall_status = "fail"

    report = SimulatedReconciliationReport(
        overall_status=overall_status,
        total_submission_records=len(submission_rows),
        total_journal_records=len(journal_rows),
        total_reconciliation_records=len(records),
        broker_action_allowed_all_false=broker_action_allowed_all_false,
        missing_submission_records=missing_submission_records,
        missing_journal_records=missing_journal_records,
        mismatched_records=mismatched_records,
        unsafe_broker_flags=unsafe_broker_flags,
        reconciliation_records=tuple(records),
    )
    return records, report


def _serialize_record(record: SimulatedReconciliationRecord) -> dict[str, Any]:
    data = asdict(record)
    data["broker_action_allowed"] = str(record.broker_action_allowed).lower()
    return data


def _write_markdown(report: SimulatedReconciliationReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_reconciliation_report.md"
    lines = [
        "# Simulated Reconciliation Report",
        "",
        "Offline-only reconciliation report for simulated execution journal artifacts.",
        "",
        f"- Overall status: {report.overall_status}",
        f"- Total submission records: {report.total_submission_records}",
        f"- Total journal records: {report.total_journal_records}",
        f"- Total reconciliation records: {report.total_reconciliation_records}",
        f"- broker_action_allowed all false: {'yes' if report.broker_action_allowed_all_false else 'no'}",
        f"- Missing submission records: {report.missing_submission_records}",
        f"- Missing journal records: {report.missing_journal_records}",
        f"- Mismatched records: {report.mismatched_records}",
        f"- Unsafe broker flags: {report.unsafe_broker_flags}",
        "",
        "| reconciliation_id | simulated_submission_id | journal_record_id | candidate_id | order_plan_id | symbol | side | simulated_broker_order_id | submission_status | execution_status | reconciliation_status | reconciled_at | broker_action_allowed | notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in report.reconciliation_records:
        lines.append(
            f"| {record.reconciliation_id} | {record.simulated_submission_id} | {record.journal_record_id} | {record.candidate_id} | {record.order_plan_id} | {record.symbol} | {record.side} | {record.simulated_broker_order_id} | {record.submission_status} | {record.execution_status} | {record.reconciliation_status} | {record.reconciled_at} | {str(record.broker_action_allowed).lower()} | {record.notes} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv(report: SimulatedReconciliationReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_reconciliation_report.csv"
    fieldnames = [
        "reconciliation_id",
        "simulated_submission_id",
        "journal_record_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "simulated_broker_order_id",
        "submission_status",
        "execution_status",
        "reconciliation_status",
        "reconciled_at",
        "broker_action_allowed",
        "notes",
        "offline_only_boundary",
        "simulated_only_boundary",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in report.reconciliation_records:
            writer.writerow(_serialize_record(record))
    return path


def generate_simulated_reconciliation_artifacts(
    submission_root: str | Path | None = None,
    journal_root: str | Path | None = None,
    output_root: str | Path | None = None,
) -> dict[str, Any]:
    submission_rows = read_simulated_submission_rows(submission_root if submission_root is not None else DEFAULT_SUBMISSION_ROOT)
    journal_rows = _read_journal_rows(journal_root)
    records, report = build_simulated_reconciliation_records(submission_rows, journal_rows)
    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown(report, output_root_path)
    csv_path = _write_csv(report, output_root_path)
    return {
        "count": len(records),
        "records": records,
        "report": report,
        "queue_markdown": md_path,
        "queue_csv": csv_path,
    }

