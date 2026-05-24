# Phase 7.1 — Manual Approval Layer Audit and Contract Hardening

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Goal

Audit the Phase 7 manual approval + simulated submission implementation against the original mailbox contract, then make only minimal corrections needed to preserve safety, artifact compatibility, and CLI reliability.

This is a hardening/audit phase, not a feature expansion phase.

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not make network calls.
Do not use broker credentials.
Do not enable paper execution.
Do not set `broker_action_allowed` true.
Do not redesign the strategy pipeline.
Do not add new trading logic.

Everything must remain simulated-only and offline-only.

## Context

Phase 7 was pushed in commit:

```text
74c9b9863b0228d39dec69f856b6687b864d1dcc
```

OpenClaw reported:

- manual approval and simulated submission domain models added
- offline-only approval artifact generation added
- validation and simulated submission services added
- CLI commands added:
  - `approvals list`
  - `approvals validate`
  - `approvals submit-simulated`
- generated approval and simulated submission artifacts under `runs/`
- `PYTHONPATH=src pytest -q` passed with 46 tests
- `broker_action_allowed` remained false everywhere
- no live broker/network path was added

## Audit requirements

### 1. Domain model safety

Confirm approval records include:

- `approval_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `approved_by`
- `approved_at`
- `expires_at`
- `approval_status`
- `approval_scope`
- `broker_action_allowed`
- `notes`

Confirm simulated submission records include:

- `simulated_submission_id`
- `approval_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `simulated_broker_order_id`
- `submission_status`
- `submitted_at`
- `broker_action_allowed`

### 2. Approval statuses

Confirm supported approval statuses are:

- `pending`
- `approved`
- `expired`
- `rejected`
- `consumed`

### 3. Approval scope

Confirm the only allowed scope is:

- `simulated_only`

### 4. Broker safety

Confirm `broker_action_allowed` is always false.

Add or strengthen tests if needed so any true value fails validation or simulated submission.

### 5. Artifact path contract

The original Phase 7 request asked for these individual approval templates:

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

If the implementation currently generates only files under `runs/approvals/templates/`, preserve that layout if useful, but also add compatibility copies or generated aliases at the exact original paths listed above.

Do not remove existing generated templates unless tests and docs are updated safely.

### 6. Queue artifacts

Confirm these exist and are generated correctly:

- `runs/approvals/approval_queue.md`
- `runs/approvals/approval_queue.csv`
- `runs/approvals/README.md`
- `runs/simulated_submissions/simulated_submission_queue.md`
- `runs/simulated_submissions/simulated_submission_queue.csv`

### 7. CLI smoke checks

Run or add tests for:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals list
PYTHONPATH=src python -m price_action_paper_trader.cli approvals validate
```

For `submit-simulated`, verify it fails closed by default because templates are pending:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli approvals submit-simulated --approval-id APR-PTC-004
```

Expected behavior:

- pending approval blocks submission
- no broker/network action happens
- exit code is non-zero or clearly blocked
- output explains that approval status must be approved

### 8. Fail-closed tests

Ensure tests cover:

- pending approval rejected
- expired approval rejected
- rejected approval rejected
- consumed approval rejected
- wrong candidate_id rejected
- wrong order_plan_id rejected
- wrong approval_scope rejected
- broker_action_allowed true rejected
- risk gate not passed rejected
- approved + simulated_only + not expired + matching IDs + risk passed + broker_action_allowed false succeeds as simulated-only

### 9. Documentation

Update README or generated artifact notes only as needed to clarify:

- this is offline-only
- this is simulated-only
- generated approvals are not broker permissions
- `broker_action_allowed` must remain false
- `submit-simulated` does not submit to Alpaca

## Verification

Run:

```bash
PYTHONPATH=src pytest -q
```

Also show:

```bash
git status --short
git diff --stat
```

## Commit and push

If changes are needed and tests pass:

```bash
git add src tests runs .open-claw-mailbox/outbox
git commit -m "Harden Phase 7 manual approval artifact contract"
git push origin main
```

If no changes are needed, do not create an empty commit.

## Outbox response

Write the response to:

```text
.open-claw-mailbox/outbox/phase-7-1-manual-approval-audit-response.md
```

Include:

- whether any path/filename drift was found
- whether compatibility approval files were added
- pytest result
- commit SHA if a commit was created
- confirmation that no broker/network/live execution path was added
- confirmation that `broker_action_allowed` remains false everywhere
