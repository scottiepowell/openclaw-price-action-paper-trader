# Phase 10 — Simulated Submission Journal and Reconciliation Drill

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Goal

Extend the Phase 9 simulated-only exercise into the existing execution journal and reconciliation layer, without adding any broker execution.

This phase should prove the offline lifecycle:

```text
controlled approved artifact
→ simulated submission record
→ simulated execution/journal record
→ reconciliation report
→ audit report update
```

This is still simulated-only and offline-only.

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not make broker/network calls.
Do not use broker credentials.
Do not enable paper execution.
Do not submit real or Alpaca paper orders.
Do not set `broker_action_allowed` true.
Do not change strategy logic.
Do not convert this into an autonomous execution loop.

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

Phase 7.1 added:

- compatibility approval files for all 11 PTC candidates

Phase 8 added:

- `approvals audit-report`
- `runs/reports/approval_audit_report.md`
- `runs/reports/approval_audit_report.csv`

Phase 9 added:

- one controlled approved exercise artifact for `APR-PTC-004`
- one simulated submission for `PTC-004 / OP-PTC-004 / NVDA / bullish`
- updated simulated submission queue
- updated approval audit report

Recent verified state:

- simulated submissions count: 1
- audit status: `warning` because pending approvals remain in the queue
- `PYTHONPATH=src pytest -q` passed with 54 tests
- no broker/network/live execution path was added
- no broker credentials were used
- `broker_action_allowed` remains false everywhere

## Exercise candidate

Use the existing Phase 9 simulated submission only:

```text
APR-PTC-004 / PTC-004 / OP-PTC-004 / NVDA / bullish
```

Do not create additional simulated submissions unless needed for tests in temporary test directories.

## New capability

Add a controlled offline service or command that can take the existing simulated submission record and create a corresponding simulated journal/reconciliation artifact.

Suggested files, depending on current project structure:

- `src/price_action_paper_trader/services/simulated_execution_journal_service.py`
- `src/price_action_paper_trader/services/simulated_reconciliation_service.py`
- `tests/unit/test_simulated_execution_journal_reconciliation.py`

If the project already has execution journal or reconciliation service files, prefer extending them minimally rather than creating duplicates.

## Journal artifact requirements

Create or update simulated-only journal artifacts under an appropriate existing path. Prefer existing project conventions if present. If no convention exists, use:

- `runs/execution_journal/simulated_execution_journal.md`
- `runs/execution_journal/simulated_execution_journal.csv`

A simulated journal record should include:

- `journal_record_id`
- `simulated_submission_id`
- `approval_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `simulated_broker_order_id`
- `execution_status`
- `journaled_at`
- `broker_action_allowed: false`
- `notes`

Use conservative status language such as:

```text
SIMULATED_JOURNALED
```

Do not claim a real fill or broker order.

## Reconciliation artifact requirements

Create or update simulated-only reconciliation artifacts under an appropriate existing path. Prefer existing project conventions if present. If no convention exists, use:

- `runs/reconciliation/simulated_reconciliation_report.md`
- `runs/reconciliation/simulated_reconciliation_report.csv`

A reconciliation record should include:

- `reconciliation_id`
- `simulated_submission_id`
- `journal_record_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `submission_status`
- `execution_status`
- `reconciliation_status`
- `reconciled_at`
- `broker_action_allowed: false`
- `notes`

Use conservative status language such as:

```text
RECONCILED_SIMULATED_ONLY
```

The reconciliation should check that:

- simulated submission exists
- journal record exists
- IDs match between submission and journal
- `broker_action_allowed` is false in all records
- no broker/network/live execution path is used

## CLI

If consistent with the existing CLI style, add a safe command such as:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals reconcile-simulated
```

or a better command name if the current CLI structure suggests one.

The command must be read/write only to local `runs/` artifacts and must not contact a broker.

## Audit report update

If reasonable, update the Phase 8 audit report or add a separate reconciliation audit report so it can summarize:

- total simulated submissions
- total simulated journal records
- total simulated reconciliation records
- mismatched submission/journal IDs
- unsafe broker flags
- reconciliation status

Do not make audit report generation mutate source artifacts except report outputs.

## Tests

Add or strengthen tests verifying:

- one simulated submission can produce one simulated journal record
- one simulated journal record can produce one reconciliation record
- mismatched IDs fail reconciliation
- missing journal record fails reconciliation
- missing submission record fails reconciliation
- `broker_action_allowed true` fails reconciliation
- no broker/network adapter is invoked
- generated markdown and CSV artifacts contain required fields
- CLI command, if added, succeeds for the current safe simulated artifact set

## Verification

Run:

```bash
PYTHONPATH=src pytest -q
```

If CLI command is added, also run it once and show output:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals reconcile-simulated
```

Then show:

```bash
git status --short
git diff --stat
```

## Commit and push

Before committing, ensure Python cache files are not tracked:

```bash
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
```

If changes are made and tests pass:

```bash
git add src tests runs .open-claw-mailbox/outbox .gitignore
git commit -m "Add Phase 10 simulated journal reconciliation drill"
git push origin main
```

If tests fail, stop and report the exact failure.
If unrelated files appear, stop and report them before committing.

## Outbox response

Write the response to:

```text
.open-claw-mailbox/outbox/phase-10-simulated-submission-journal-reconciliation-drill-response.md
```

Include:

- files added/changed
- whether the Phase 9 simulated submission was journaled
- simulated journal record count
- simulated reconciliation record count
- reconciliation status
- audit/report status if updated
- pytest result
- CLI command result if added
- commit SHA if committed
- confirmation no broker/network/live execution path was added
- confirmation no broker credentials were used
- confirmation `broker_action_allowed` remains false everywhere
