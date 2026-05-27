"""Offline-only simulated execution journal generation.

This service reads the existing simulated submission queue and converts it into
an execution journal artifact without touching any broker or network path.
"""

from __future__ import annotations

import csv
from dataclasses import asdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any

from price_action_paper_trader.domain.simulated_journal import (
    SimulatedExecutionJournalRecord,
    SimulatedExecutionJournalReport,
)


DEFAULT_SUBMISSION_ROOT = Path(__file__).resolve().parents[3] / "runs" / "simulated_submissions"
DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "execution_journal"
SIMULATED_JOURNALED = "SIMULATED_JOURNALED"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _bool_text(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


def _read_submission_rows(submission_root: str | Path | None = None) -> list[dict[str, str]]:
    root = Path(submission_root) if submission_root is not None else DEFAULT_SUBMISSION_ROOT
    path = root / "simulated_submission_queue.csv"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [{str(key): str(value) for key, value in row.items()} for row in reader]


def _journal_record_id(row: dict[str, str]) -> str:
    seed = "|".join(
        [
            row.get("simulated_submission_id", "").strip().upper(),
            row.get("approval_id", "").strip().upper(),
            row.get("candidate_id", "").strip().upper(),
            row.get("simulated_broker_order_id", "").strip().upper(),
        ]
    )
    digest = sha256(seed.encode("utf-8")).hexdigest()[:12].upper()
    return f"SJ-{row.get('approval_id', '').strip().upper()}-{digest}"


def _malformed_reason(row: dict[str, str]) -> str:
    required_fields = (
        "simulated_submission_id",
        "approval_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "simulated_broker_order_id",
        "submission_status",
        "submitted_at",
    )
    for field in required_fields:
        if not row.get(field, "").strip():
            return f"missing {field}"
    if row.get("submission_status", "").strip() != "SIMULATED_SUBMITTED":
        return "submission status must be SIMULATED_SUBMITTED"
    if _bool_text(row.get("broker_action_allowed", "false")):
        return "broker_action_allowed must remain false"
    return ""


def build_simulated_execution_journal_records(
    submission_rows: list[dict[str, str]],
) -> tuple[list[SimulatedExecutionJournalRecord], SimulatedExecutionJournalReport]:
    records: list[SimulatedExecutionJournalRecord] = []
    unsafe_broker_flags = 0
    malformed_submission_records = 0
    missing_submission_records = 0

    if not submission_rows:
        report = SimulatedExecutionJournalReport(
            overall_status="fail",
            total_submission_records=0,
            total_journal_records=0,
            broker_action_allowed_all_false=True,
            unsafe_broker_flags=0,
            missing_submission_records=1,
            malformed_submission_records=0,
            journaled_records=tuple(),
        )
        return records, report

    for row in submission_rows:
        malformed_reason = _malformed_reason(row)
        if malformed_reason:
            malformed_submission_records += 1
            if "broker_action_allowed" in malformed_reason:
                unsafe_broker_flags += 1
            continue

        journal_record = SimulatedExecutionJournalRecord(
            journal_record_id=_journal_record_id(row),
            simulated_submission_id=row["simulated_submission_id"].strip(),
            approval_id=row["approval_id"].strip(),
            candidate_id=row["candidate_id"].strip(),
            order_plan_id=row["order_plan_id"].strip(),
            symbol=row["symbol"].strip().upper(),
            side=row["side"].strip().lower(),
            simulated_broker_order_id=row["simulated_broker_order_id"].strip(),
            execution_status=SIMULATED_JOURNALED,
            journaled_at=_utc_now(),
            broker_action_allowed=False,
            notes="offline simulation only; journaled from simulated submission record",
            submission_status=row["submission_status"].strip(),
        )
        records.append(journal_record)

    total_submission_records = len(submission_rows)
    total_journal_records = len(records)
    broker_action_allowed_all_false = unsafe_broker_flags == 0
    overall_status = "pass"
    if missing_submission_records or malformed_submission_records or unsafe_broker_flags:
        overall_status = "fail"

    report = SimulatedExecutionJournalReport(
        overall_status=overall_status,
        total_submission_records=total_submission_records,
        total_journal_records=total_journal_records,
        broker_action_allowed_all_false=broker_action_allowed_all_false,
        unsafe_broker_flags=unsafe_broker_flags,
        missing_submission_records=missing_submission_records,
        malformed_submission_records=malformed_submission_records,
        journaled_records=tuple(records),
    )
    if total_journal_records != total_submission_records:
        report = SimulatedExecutionJournalReport(
            overall_status="fail" if overall_status == "pass" else overall_status,
            total_submission_records=total_submission_records,
            total_journal_records=total_journal_records,
            broker_action_allowed_all_false=broker_action_allowed_all_false,
            unsafe_broker_flags=unsafe_broker_flags,
            missing_submission_records=missing_submission_records or (total_submission_records - total_journal_records),
            malformed_submission_records=malformed_submission_records,
            journaled_records=tuple(records),
        )
    return records, report


def _serialize_record(record: SimulatedExecutionJournalRecord) -> dict[str, Any]:
    data = asdict(record)
    data["broker_action_allowed"] = str(record.broker_action_allowed).lower()
    return data


def _write_markdown(report: SimulatedExecutionJournalReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_execution_journal.md"
    lines = [
        "# Simulated Execution Journal",
        "",
        "Offline-only journal built from the simulated submission queue.",
        "",
        f"- Overall status: {report.overall_status}",
        f"- Total submission records: {report.total_submission_records}",
        f"- Total journal records: {report.total_journal_records}",
        f"- broker_action_allowed all false: {'yes' if report.broker_action_allowed_all_false else 'no'}",
        f"- Unsafe broker flags: {report.unsafe_broker_flags}",
        f"- Missing submission records: {report.missing_submission_records}",
        f"- Malformed submission records: {report.malformed_submission_records}",
        "",
        "| journal_record_id | simulated_submission_id | approval_id | candidate_id | order_plan_id | symbol | side | simulated_broker_order_id | execution_status | journaled_at | broker_action_allowed | notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in report.journaled_records:
        lines.append(
            f"| {record.journal_record_id} | {record.simulated_submission_id} | {record.approval_id} | {record.candidate_id} | {record.order_plan_id} | {record.symbol} | {record.side} | {record.simulated_broker_order_id} | {record.execution_status} | {record.journaled_at} | {str(record.broker_action_allowed).lower()} | {record.notes} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv(report: SimulatedExecutionJournalReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "simulated_execution_journal.csv"
    fieldnames = [
        "journal_record_id",
        "simulated_submission_id",
        "approval_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "simulated_broker_order_id",
        "execution_status",
        "journaled_at",
        "broker_action_allowed",
        "notes",
        "submission_status",
        "offline_only_boundary",
        "simulated_only_boundary",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in report.journaled_records:
            writer.writerow(_serialize_record(record))
    return path


def generate_simulated_execution_journal_artifacts(
    submission_root: str | Path | None = None,
    output_root: str | Path | None = None,
) -> dict[str, Any]:
    submission_rows = _read_submission_rows(submission_root)
    records, report = build_simulated_execution_journal_records(submission_rows)
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


def read_simulated_submission_rows(submission_root: str | Path | None = None) -> list[dict[str, str]]:
    return _read_submission_rows(submission_root)

