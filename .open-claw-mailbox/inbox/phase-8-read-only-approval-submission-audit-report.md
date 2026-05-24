# Phase 8 — Read-only Approval and Simulated Submission Audit Report

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Goal

Add a read-only audit/report layer that summarizes the Phase 7 manual approval and simulated submission artifacts without changing state.

This phase should make it easy to review:

- approval queue status
- compatibility approval files
- simulated submission queue status
- risk-gate relationship
- journal/reconciliation consistency where existing artifacts already support it
- safety boundary status

This is a reporting phase only.

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not make broker/network calls.
Do not use broker credentials.
Do not enable paper execution.
Do not submit simulated orders as part of report generation.
Do not mutate approval artifacts.
Do not mutate simulated submission artifacts.
Do not mutate execution journals.
Do not mutate reconciliation artifacts.
Do not set `broker_action_allowed` true.
Do not change strategy logic.

Everything must remain offline-only and simulated-only.

## Current known state

Phase 7 added:

- manual approval domain/service support
- simulated submission service support
- approval queue artifacts under `runs/approvals/`
- simulated submission queue artifacts under `runs/simulated_submissions/`
- CLI commands:
  - `approvals list`
  - `approvals validate`
  - `approvals submit-simulated`

Phase 7.1 added compatibility approval files at the original requested paths:

- `runs/approvals/PTC-004-approval.md`
- `runs/approvals/PTC-005-approval.md`
- `runs/approvals/PTC-009-approval.md`
- `runs/approvals/PTC-017-approval.md`
- `runs/approvals/PTC-019-approval.md`
- `runs/approvals/PTC-021-approval.md`
- `runs/approvals/PTC-022-approval.md`
- `runs/approvals/PTC-024-approval.md`
- `runs/approvals/PTC-032-approval.md`
- `runs/approvals/PTC-034-approval.md`
- `runs/approvals/PTC-035-approval.md`

Recent verified status:

- compatibility files added: 11
- `PYTHONPATH=src pytest -q` passed with 46 tests
- no broker/network/live execution path was added
- `broker_action_allowed` remains false everywhere

## New capability

Add a read-only audit report generator.

Suggested files:

- `src/price_action_paper_trader/services/approval_audit_report_service.py`
- `tests/unit/test_approval_audit_report_service.py`

If the existing CLI pattern supports it, add:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals audit-report
```

or another similarly safe read-only command consistent with the current CLI style.

## Report artifacts

Generate read-only reports at:

- `runs/reports/approval_audit_report.md`
- `runs/reports/approval_audit_report.csv`

If JSON is already used elsewhere in the project, optional:

- `runs/reports/approval_audit_report.json`

Do not generate files outside `runs/reports/` unless existing project conventions require it.

## Report content

The report should include:

### 1. Summary

- total approvals
- total compatibility approval files expected
- total compatibility approval files found
- total simulated submissions
- number of pending approvals
- number of approved approvals
- number of rejected approvals
- number of expired approvals
- number of consumed approvals
- number of approvals with `approval_scope != simulated_only`
- number of approvals with `broker_action_allowed != false`
- number of simulated submissions with `broker_action_allowed != false`
- overall audit status: `pass`, `warning`, or `fail`

### 2. Approval queue audit

For each approval:

- approval_id
- candidate_id
- order_plan_id
- symbol
- side
- approval_status
- approval_scope
- broker_action_allowed
- expires_at
- audit_status
- audit_notes

### 3. Compatibility file audit

For each expected compatibility file:

- expected path
- found: true/false
- candidate_id
- approval_id if readable
- approval_status if readable
- approval_scope if readable
- broker_action_allowed if readable
- audit_status
- audit_notes

### 4. Simulated submission audit

For each simulated submission if any exist:

- simulated_submission_id
- approval_id
- candidate_id
- order_plan_id
- symbol
- side
- simulated_broker_order_id
- submission_status
- submitted_at
- broker_action_allowed
- audit_status
- audit_notes

If no simulated submissions exist, the report should say this clearly and treat it as acceptable.

### 5. Safety boundary audit

Explicitly report:

- broker_action_allowed all false: yes/no
- approval_scope all simulated_only: yes/no
- broker/network execution path detected by this audit: no
- report generation mutated source artifacts: no

## Audit status rules

Use conservative status rules:

- `pass` if all required artifacts exist and all safety fields are safe
- `warning` if optional artifacts are missing or no simulated submissions exist
- `fail` if required compatibility files are missing, unsafe scopes appear, or `broker_action_allowed` is true anywhere

No report condition should enable execution.

## Tests

Add or strengthen tests that verify:

- the report service is read-only
- approval queue summary counts are correct
- missing compatibility file is reported as fail
- pending approvals are accepted as normal
- no simulated submissions is accepted as warning or informational, not a failure
- `approval_scope != simulated_only` causes fail
- `broker_action_allowed true` in approvals causes fail
- `broker_action_allowed true` in simulated submissions causes fail
- generated markdown and CSV reports include the required sections/columns
- CLI audit-report command, if added, exits successfully for the current safe artifact set

## Verification

Run:

```bash
PYTHONPATH=src pytest -q
```

Also run, if implemented:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals audit-report
```

Then show:

```bash
git status --short
git diff --stat
```

## Commit and push

If changes are needed and tests pass:

```bash
git add src tests runs .open-claw-mailbox/outbox
git commit -m "Add Phase 8 approval audit report"
git push origin main
```

If tests fail, stop and report the exact failure.
If unrelated files appear, stop and report them before committing.

## Outbox response

Write the response to:

```text
.open-claw-mailbox/outbox/phase-8-read-only-approval-submission-audit-report-response.md
```

Include:

- files added/changed
- report artifacts generated
- CLI command added or not added
- pytest result
- commit SHA if committed
- audit report overall status
- confirmation no broker/network/live execution path was added
- confirmation no source artifacts were mutated by report generation except report outputs
- confirmation `broker_action_allowed` remains false everywhere
