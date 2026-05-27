"""Minimal CLI with safe manual-approval commands."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json

from price_action_paper_trader.services.manual_approval_service import (
    build_manual_approval_templates,
    find_manual_approval,
    generate_manual_approval_artifacts,
    load_manual_approval_queue,
    validate_manual_approvals,
)
from price_action_paper_trader.services.approval_audit_report_service import generate_approval_audit_report
from price_action_paper_trader.services.market_context_assessment_service import generate_market_context_assessment_report
from price_action_paper_trader.services.market_data_snapshot_service import generate_market_data_snapshot_artifacts, generate_unavailable_snapshot_artifacts
from price_action_paper_trader.services.order_plan_builder import build_order_plans
from price_action_paper_trader.services.simulated_execution_journal_service import generate_simulated_execution_journal_artifacts
from price_action_paper_trader.services.simulated_reconciliation_service import generate_simulated_reconciliation_artifacts
from price_action_paper_trader.services.simulated_submission_service import (
    SIMULATED_SUBMITTED,
    generate_simulated_submission_artifacts,
    submit_simulated_approved_order,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="price_action_paper_trader")
    subparsers = parser.add_subparsers(dest="command")

    approvals_parser = subparsers.add_parser("approvals", help="manual approval commands")
    approvals_subparsers = approvals_parser.add_subparsers(dest="approvals_command")

    approvals_subparsers.add_parser("list", help="list manual approval templates")
    approvals_subparsers.add_parser("validate", help="validate manual approval templates")
    approvals_subparsers.add_parser("audit-report", help="generate read-only approval audit report")
    approvals_subparsers.add_parser("reconcile-simulated", help="generate simulated journal and reconciliation reports")

    submit_parser = approvals_subparsers.add_parser(
        "submit-simulated",
        help="submit one simulated-only approval",
    )
    submit_parser.add_argument("--approval-id", required=True)

    market_data_parser = subparsers.add_parser("market-data", help="read-only market data commands")
    market_data_subparsers = market_data_parser.add_subparsers(dest="market_data_command")

    snapshot_parser = market_data_subparsers.add_parser("snapshot", help="generate a delayed market-data snapshot")
    snapshot_parser.add_argument("--symbols", default="", help="comma-separated symbols; defaults to current order-plan symbols")
    snapshot_parser.add_argument("--timeframes", default="5Min", help="comma-separated timeframes")
    snapshot_parser.add_argument("--delay-minutes", type=int, default=15)
    snapshot_parser.add_argument("--provider", choices=["fake", "unavailable"], default="fake")

    assess_parser = market_data_subparsers.add_parser("assess-context", help="generate a market context assessment report")
    assess_parser.add_argument("--snapshot-root", default=None)
    assess_parser.add_argument("--output-root", default=None)

    return parser


def _approval_payloads() -> list[dict[str, str]]:
    approvals = load_manual_approval_queue()
    if not approvals:
        approvals = build_manual_approval_templates()
    return [
        {
            "approval_id": approval.approval_id,
            "candidate_id": approval.candidate_id,
            "order_plan_id": approval.order_plan_id,
            "symbol": approval.symbol,
            "side": approval.side,
            "approval_status": approval.approval_status,
            "approval_scope": approval.approval_scope,
            "broker_action_allowed": str(approval.broker_action_allowed).lower(),
        }
        for approval in approvals
    ]


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command != "approvals":
        if args.command != "market-data":
            parser.print_help()
            return 0

        if args.market_data_command == "snapshot":
            symbols = [part.strip() for part in args.symbols.split(",") if part.strip()]
            if not symbols:
                symbols = [plan.symbol for plan in build_order_plans()]
            timeframes = [part.strip() for part in args.timeframes.split(",") if part.strip()]
            if args.provider == "unavailable":
                report = generate_unavailable_snapshot_artifacts(
                    symbols=symbols,
                    timeframes=timeframes,
                    delay_minutes=args.delay_minutes,
                )
            else:
                report = generate_market_data_snapshot_artifacts(
                    symbols=symbols,
                    timeframes=timeframes,
                    delay_minutes=args.delay_minutes,
                )
            print(
                json.dumps(
                    {
                        "status": report["provider_status"],
                        "count": report["count"],
                        "snapshot_id": report["snapshot"].snapshot_id,
                        "snapshot_markdown": str(report["queue_markdown"]),
                        "snapshot_csv": str(report["queue_csv"]),
                    },
                    indent=2,
                )
            )
            return 0

        if args.market_data_command == "assess-context":
            report = generate_market_context_assessment_report(
                snapshot_root=args.snapshot_root,
                output_root=args.output_root,
            )
            print(
                json.dumps(
                    {
                        "status": report["report"].overall_status,
                        "total_complete_traces": report["report"].total_complete_traces,
                        "incomplete_traces": report["report"].incomplete_traces,
                        "assessment_markdown": str(report["queue_markdown"]),
                        "assessment_csv": str(report["queue_csv"]),
                    },
                    indent=2,
                )
            )
            return 0

        parser.print_help()
        return 0

    if args.approvals_command == "list":
        report = generate_manual_approval_artifacts()
        print(json.dumps({"count": report["count"], "approvals": _approval_payloads()}, indent=2))
        return 0

    if args.approvals_command == "validate":
        approvals = load_manual_approval_queue()
        issues = validate_manual_approvals(approvals)
        if issues:
            for issue in issues:
                print(issue)
            return 1
        print(json.dumps({"status": "ok", "count": len(approvals)}))
        return 0

    if args.approvals_command == "audit-report":
        report = generate_approval_audit_report()
        print(
            json.dumps(
                {
                    "status": report["overall_status"],
                    "total_approvals": report["total_approvals"],
                    "expected_compatibility_files": report["expected_compatibility_files"],
                    "found_compatibility_files": report["found_compatibility_files"],
                    "total_simulated_submissions": report["total_simulated_submissions"],
                    "queue_markdown": str(report["queue_markdown"]),
                    "queue_csv": str(report["queue_csv"]),
                },
                indent=2,
            )
        )
        return 0

    if args.approvals_command == "reconcile-simulated":
        journal_report = generate_simulated_execution_journal_artifacts()
        reconciliation_report = generate_simulated_reconciliation_artifacts()
        payload = {
            "status": reconciliation_report["report"].overall_status,
            "journal_status": journal_report["report"].overall_status,
            "journal_count": journal_report["count"],
            "reconciliation_count": reconciliation_report["count"],
            "journal_markdown": str(journal_report["queue_markdown"]),
            "journal_csv": str(journal_report["queue_csv"]),
            "reconciliation_markdown": str(reconciliation_report["queue_markdown"]),
            "reconciliation_csv": str(reconciliation_report["queue_csv"]),
            "missing_submission_records": reconciliation_report["report"].missing_submission_records,
            "missing_journal_records": reconciliation_report["report"].missing_journal_records,
            "mismatched_records": reconciliation_report["report"].mismatched_records,
        }
        print(json.dumps(payload, indent=2))
        return 0 if reconciliation_report["report"].overall_status == "pass" else 1

    if args.approvals_command == "submit-simulated":
        approvals = load_manual_approval_queue()
        approval = find_manual_approval(args.approval_id, approvals)
        if approval is None:
            print(f"approval not found: {args.approval_id}")
            return 1

        if approval.approval_status.strip().lower() != "approved":
            print("submission blocked: approval status must be approved")
            return 1

        plans = build_order_plans()
        plan_by_candidate = {plan.candidate_id.strip().upper(): plan for plan in plans}
        plan = plan_by_candidate.get(approval.candidate_id.strip().upper())
        if plan is None:
            print(f"submission blocked: missing plan for {approval.candidate_id}")
            return 1

        record = submit_simulated_approved_order(plan, approval)
        if record.submission_status != SIMULATED_SUBMITTED:
            print(record.notes)
            return 1

        generate_simulated_submission_artifacts(plans=plans, approvals=approvals)
        print(json.dumps(asdict(record), indent=2))
        return 0

    approvals_parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
