"""Read-only market context assessment over market-data snapshots."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import Any, Sequence

from price_action_paper_trader.domain.market_data import MarketContextAssessment, MarketContextAssessmentReport, MarketDataSnapshot
from price_action_paper_trader.domain.order_plan import OrderPlan
from price_action_paper_trader.services.market_data_snapshot_service import DEFAULT_OUTPUT_ROOT as MARKET_DATA_OUTPUT_ROOT, generate_market_data_snapshot_artifacts
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.approval_audit_report_service import generate_approval_audit_report


DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "reports"
DEFAULT_SNAPSHOT_ROOT = Path(__file__).resolve().parents[3] / "runs" / "market_data"


def _read_snapshot(snapshot_root: str | Path | None = None) -> MarketDataSnapshot | None:
    root = Path(snapshot_root) if snapshot_root is not None else DEFAULT_SNAPSHOT_ROOT
    csv_path = root / "latest_market_snapshot.csv"
    if not csv_path.exists():
        return None
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return None
    first = rows[0]
    bars = []
    for row in rows:
        if not str(row.get("symbol", "")).strip():
            continue
        bars.append(
            {
                "symbol": row.get("symbol", ""),
                "timeframe": row.get("timeframe", ""),
                "timestamp": row.get("timestamp", ""),
                "open": float(row.get("open", 0.0) or 0.0),
                "high": float(row.get("high", 0.0) or 0.0),
                "low": float(row.get("low", 0.0) or 0.0),
                "close": float(row.get("close", 0.0) or 0.0),
                "volume": int(float(row.get("volume", 0) or 0)),
                "source": row.get("source", ""),
                "feed": row.get("feed", ""),
                "fetched_at": row.get("fetched_at", ""),
                "data_delay_minutes": int(float(row.get("data_delay_minutes", 0) or 0)),
                "is_delayed": str(row.get("is_delayed", "false")).strip().lower() == "true",
            }
        )
    from price_action_paper_trader.domain.market_data import MarketDataBar

    return MarketDataSnapshot(
        snapshot_id=str(first.get("snapshot_id", "")),
        symbols=tuple(dict.fromkeys(str(row.get("symbol", "")).strip().upper() for row in rows if str(row.get("symbol", "")).strip())),
        timeframes=tuple(dict.fromkeys(str(row.get("timeframe", "")).strip() for row in rows if str(row.get("timeframe", "")).strip())),
        window_start=str(first.get("window_start", "")),
        window_end=str(first.get("window_end", "")),
        fetched_at=str(first.get("fetched_at", "")),
        source=str(first.get("source", "")),
        feed=str(first.get("feed", "")),
        data_delay_minutes=int(float(first.get("data_delay_minutes", 0) or 0)),
        is_live_execution_allowed=str(first.get("is_live_execution_allowed", "false")).strip().lower() == "true",
        broker_action_allowed=str(first.get("broker_action_allowed", "false")).strip().lower() == "true",
        bars=tuple(MarketDataBar(**bar) for bar in bars),
        snapshot_status=str(first.get("snapshot_status", "market_data_unavailable")),
        notes=str(first.get("notes", "")),
    )


def _serialize_assessment(row: MarketContextAssessment) -> dict[str, Any]:
    data = asdict(row)
    data["human_review_required"] = str(row.human_review_required).lower()
    data["broker_action_allowed"] = str(row.broker_action_allowed).lower()
    data["latest_close"] = f"{row.latest_close:.2f}"
    return data


def _latest_bar_for_symbol(snapshot: MarketDataSnapshot, symbol: str) -> tuple[Any, ...]:
    bars = [bar for bar in snapshot.bars if bar.symbol.upper() == symbol.upper()]
    if not bars:
        return tuple()
    bars.sort(key=lambda bar: bar.timestamp)
    return tuple(bars)


def _assess_plan(plan: OrderPlan, snapshot: MarketDataSnapshot) -> MarketContextAssessment:
    bars = _latest_bar_for_symbol(snapshot, plan.symbol)
    if not bars:
        return MarketContextAssessment(
            assessment_id=_assessment_id(plan, snapshot.snapshot_id, "insufficient_data"),
            candidate_id=plan.candidate_id,
            order_plan_id=f"OP-{plan.candidate_id}",
            symbol=plan.symbol,
            side=plan.side,
            snapshot_id=snapshot.snapshot_id,
            latest_bar_timestamp="",
            latest_close=0.0,
            data_freshness_status="unavailable",
            plan_context_status="insufficient_data",
            human_review_required=True,
            broker_action_allowed=False,
            notes="no bars available for symbol",
        )

    latest_bar = bars[-1]
    latest_close = float(latest_bar.close)
    first_close = float(bars[0].close)
    trend_up = latest_close > first_close
    trend_down = latest_close < first_close
    freshness_status = "fresh" if snapshot.data_delay_minutes <= 15 else "stale"

    if freshness_status == "stale":
        plan_status = "stale"
        notes = "snapshot delay exceeds safe threshold"
    elif plan.side.lower() == "bullish" and latest_close <= plan.invalidation_level:
        plan_status = "invalidated"
        notes = "latest close is at or below invalidation level for bullish plan"
    elif plan.side.lower() == "bearish" and latest_close >= plan.invalidation_level:
        plan_status = "invalidated"
        notes = "latest close is at or above invalidation level for bearish plan"
    elif plan.side.lower() == "bullish" and trend_up and latest_close >= plan.entry_reference:
        plan_status = "aligned"
        notes = "bullish trend and price above entry reference"
    elif plan.side.lower() == "bearish" and trend_down and latest_close <= plan.entry_reference:
        plan_status = "aligned"
        notes = "bearish trend and price below entry reference"
    else:
        plan_status = "mixed"
        notes = "symbol matches, but price action is mixed against the plan"

    return MarketContextAssessment(
        assessment_id=_assessment_id(plan, snapshot.snapshot_id, plan_status),
        candidate_id=plan.candidate_id,
        order_plan_id=f"OP-{plan.candidate_id}",
        symbol=plan.symbol,
        side=plan.side,
        snapshot_id=snapshot.snapshot_id,
        latest_bar_timestamp=latest_bar.timestamp,
        latest_close=latest_close,
        data_freshness_status=freshness_status,
        plan_context_status=plan_status,
        human_review_required=True,
        broker_action_allowed=False,
        notes=notes,
    )


def _assessment_id(plan: OrderPlan, snapshot_id: str, status: str) -> str:
    seed = "|".join([plan.candidate_id.strip().upper(), plan.symbol.strip().upper(), snapshot_id, status])
    return f"MCA-{sha256(seed.encode('utf-8')).hexdigest()[:16].upper()}"


def _write_markdown(report: MarketContextAssessmentReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "market_context_assessment_report.md"
    lines = [
        "# Market Context Assessment Report",
        "",
        f"- Overall manifest status: {report.overall_status}",
        f"- Total approvals: {report.total_approvals}",
        f"- Total compatibility approval files: {report.total_compatibility_files}",
        f"- Total simulated submissions: {report.total_simulated_submissions}",
        f"- Total journal records: {report.total_journal_records}",
        f"- Total reconciliation records: {report.total_reconciliation_records}",
        f"- Total complete traces: {report.total_complete_traces}",
        f"- Incomplete traces: {report.incomplete_traces}",
        f"- Unsafe broker flags: {report.unsafe_broker_flags}",
        f"- Unsafe approval scopes: {report.unsafe_approval_scopes}",
        "",
        "| assessment_id | candidate_id | order_plan_id | symbol | side | snapshot_id | latest_bar_timestamp | latest_close | data_freshness_status | plan_context_status | human_review_required | broker_action_allowed | notes |",
        "| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in report.assessment_rows:
        lines.append(
            f"| {row.assessment_id} | {row.candidate_id} | {row.order_plan_id} | {row.symbol} | {row.side} | {row.snapshot_id} | {row.latest_bar_timestamp} | {row.latest_close:.2f} | {row.data_freshness_status} | {row.plan_context_status} | {str(row.human_review_required).lower()} | {str(row.broker_action_allowed).lower()} | {row.notes} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_csv(report: MarketContextAssessmentReport, output_root: Path) -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    path = output_root / "market_context_assessment_report.csv"
    fieldnames = [
        "assessment_id",
        "candidate_id",
        "order_plan_id",
        "symbol",
        "side",
        "snapshot_id",
        "latest_bar_timestamp",
        "latest_close",
        "data_freshness_status",
        "plan_context_status",
        "human_review_required",
        "broker_action_allowed",
        "notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in report.assessment_rows:
            writer.writerow(_serialize_assessment(row))
    return path


def build_market_context_assessments(snapshot: MarketDataSnapshot, plans: Sequence[OrderPlan] | None = None) -> list[MarketContextAssessment]:
    plans = list(plans) if plans is not None else build_order_plans()
    return [_assess_plan(plan, snapshot) for plan in plans]


def generate_market_context_assessment_report(
    snapshot_root: str | Path | None = None,
    output_root: str | Path | None = None,
    plans: Sequence[OrderPlan] | None = None,
) -> dict[str, Any]:
    snapshot = _read_snapshot(snapshot_root)
    if snapshot is None:
        symbols = [plan.symbol for plan in (plans or build_order_plans())]
        snapshot_result = generate_market_data_snapshot_artifacts(symbols=symbols, timeframes=("5Min",), delay_minutes=15, output_root=MARKET_DATA_OUTPUT_ROOT)
        snapshot = snapshot_result["snapshot"]

    plans = list(plans) if plans is not None else build_order_plans()
    assessment_rows = build_market_context_assessments(snapshot, plans)

    approval_audit = generate_approval_audit_report()
    simulated_submission_rows = list(_read_csv_rows(Path(__file__).resolve().parents[3] / "runs" / "simulated_submissions" / "simulated_submission_queue.csv"))
    journal_rows = list(_read_csv_rows(Path(__file__).resolve().parents[3] / "runs" / "execution_journal" / "simulated_execution_journal.csv"))
    reconciliation_rows = list(_read_csv_rows(Path(__file__).resolve().parents[3] / "runs" / "reconciliation" / "simulated_reconciliation_report.csv"))

    complete_traces = 0
    incomplete_traces = 0
    for row in assessment_rows:
        submission = next((item for item in simulated_submission_rows if item.get("candidate_id") == row.candidate_id), None)
        journal = next((item for item in journal_rows if item.get("candidate_id") == row.candidate_id), None)
        reconciliation = next((item for item in reconciliation_rows if item.get("candidate_id") == row.candidate_id), None)
        if submission and journal and reconciliation and submission.get("simulated_submission_id") and journal.get("journal_record_id") and reconciliation.get("reconciliation_id"):
            complete_traces += 1
        else:
            incomplete_traces += 1

    unsafe_broker_flags = 0
    unsafe_approval_scopes = approval_audit["report"].approvals_with_unsafe_scope
    overall_status = "warning" if incomplete_traces else "pass"
    if any(row.plan_context_status in {"invalidated", "stale"} for row in assessment_rows):
        overall_status = "warning"

    report = MarketContextAssessmentReport(
        overall_status=overall_status,
        total_approvals=approval_audit["report"].total_approvals,
        total_compatibility_files=approval_audit["report"].found_compatibility_files,
        total_simulated_submissions=len(simulated_submission_rows),
        total_journal_records=len(journal_rows),
        total_reconciliation_records=len(reconciliation_rows),
        total_complete_traces=complete_traces,
        incomplete_traces=incomplete_traces,
        unsafe_broker_flags=unsafe_broker_flags,
        unsafe_approval_scopes=unsafe_approval_scopes,
        assessment_rows=tuple(assessment_rows),
    )

    output_root_path = Path(output_root) if output_root is not None else DEFAULT_OUTPUT_ROOT
    md_path = _write_markdown(report, output_root_path)
    csv_path = _write_csv(report, output_root_path)
    return {
        "report": report,
        "queue_markdown": md_path,
        "queue_csv": csv_path,
        "snapshot": snapshot,
    }


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return [{str(key): str(value) for key, value in row.items()} for row in csv.DictReader(handle)]
