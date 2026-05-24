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
from price_action_paper_trader.services.order_plan_builder import build_order_plans
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

    submit_parser = approvals_subparsers.add_parser(
        "submit-simulated",
        help="submit one simulated-only approval",
    )
    submit_parser.add_argument("--approval-id", required=True)

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
