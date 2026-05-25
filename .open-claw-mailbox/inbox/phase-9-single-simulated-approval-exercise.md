# Phase 9 — Single Simulated Approval Exercise

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Goal

Run one controlled simulated-only approval exercise to prove the Phase 7 manual approval path works end-to-end:

```text
approved manual approval artifact
→ simulated-only submission service
→ simulated submission queue artifacts
→ read-only audit report update
```

This phase must remain offline-only and simulated-only.

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not make broker/network calls.
Do not use broker credentials.
Do not enable paper execution.
Do not set `broker_action_allowed` true.
Do not change strategy logic.
Do not submit real or Alpaca paper orders.

Everything must remain simulated-only and offline-only.

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

Phase 7.1 added compatibility approval files for all 11 PTC candidates.

Phase 8 added:

- `approvals audit-report`
- `runs/reports/approval_audit_report.md`
- `runs/reports/approval_audit_report.csv`

Recent verified state:

- `PYTHONPATH=src pytest -q` passed with 52 tests
- report status was `warning` because there were zero simulated submissions
- approvals were pending
- compatibility files found: 11 of 11
- no broker/network/live execution path was added
- `broker_action_allowed` remains false everywhere

## Exercise candidate

Use one candidate only:

```text
PTC-004 / APR-PTC-004 / OP-PTC-004 / NVDA / bullish
```

## Required behavior

Create a controlled approved artifact or controlled test fixture for `APR-PTC-004` that allows simulated submission only.

The approved artifact must have:

```yaml
approval_id: APR-PTC-004
candidate_id: PTC-004
order_plan_id: OP-PTC-004
symbol: NVDA
side: bullish
approval_status: approved
approval_scope: simulated_only
broker_action_allowed: false
```

Do not turn broker action on.

Do not mutate the baseline pending compatibility files unless the implementation already uses the queue as the mutable approval source and tests document that behavior.

Prefer a controlled generated exercise artifact if the existing design supports it, such as:

```text
runs/approval_exercises/phase-9/APR-PTC-004-approved-exercise.md
```

or a clearly documented test fixture/service path.

## Simulated submission output

After running the simulated-only approval path, produce/update:

- `runs/simulated_submissions/simulated_submission_queue.md`
- `runs/simulated_submissions/simulated_submission_queue.csv`

The simulated submission record should include:

- `simulated_submission_id`
- `approval_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `simulated_broker_order_id`
- `submission_status`
- `submitted_at`
- `broker_action_allowed: false`

## Audit report update

Regenerate:

- `runs/reports/approval_audit_report.md`
- `runs/reports/approval_audit_report.csv`

The audit should show:

- total simulated submissions: 1
- no unsafe approval scopes
- no unsafe broker flags
- no broker/network/live execution path
- `broker_action_allowed` false for the simulated submission

If the audit status remains `warning`, explain why. A warning is acceptable if it is due to pending approvals or another conservative informational rule.

## CLI checks

Run:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals list
PYTHONPATH=src python -m price_action_paper_trader.cli approvals validate
PYTHONPATH=src python -m price_action_paper_trader.cli approvals audit-report
```

If using the CLI to submit the simulated approval, ensure it remains simulated-only and uses the controlled approved artifact safely.

Do not use CLI behavior that would require broker credentials or network access.

## Tests

Add or strengthen tests verifying:

- a single approved `APR-PTC-004` simulated-only artifact creates exactly one simulated submission
- `broker_action_allowed` remains false in approval and submission records
- the audit report sees one simulated submission
- pending baseline approvals remain safe
- unsafe `broker_action_allowed true` still fails
- unsafe `approval_scope` still fails
- mismatched candidate/order IDs still fail
- no broker/network adapter is invoked

## Verification

Run:

```bash
PYTHONPATH=src pytest -q
```

Then show:

```bash
git status --short
git diff --stat
```

## Commit and push

If changes are made and tests pass:

```bash
git add src tests runs .open-claw-mailbox/outbox
 git commit -m "Add Phase 9 single simulated approval exercise"
git push origin main
```

If tests fail, stop and report the exact failure.
If unrelated files appear, stop and report them before committing.

## Outbox response

Write the response to:

```text
.open-claw-mailbox/outbox/phase-9-single-simulated-approval-exercise-response.md
```

Include:

- files added/changed
- whether `APR-PTC-004` was exercised
- simulated submission count after the exercise
- audit report overall status after the exercise
- pytest result
- commit SHA if committed
- confirmation no broker/network/live execution path was added
- confirmation no broker credentials were used
- confirmation `broker_action_allowed` remains false everywhere
