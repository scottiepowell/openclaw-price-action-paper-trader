# Phase 7 — Manual Approval Command Layer

## Goal

Add a manual approval command layer that allows one risk-approved order plan to be explicitly approved for **simulated execution only**.

This phase must not submit real Alpaca paper orders.

## Working directory

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

## Repository

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Hard safety boundaries

- Do not add Alpaca order submission.
- Do not add live trading.
- Do not add autonomous execution.
- Do not add background workers.
- Do not add schedulers.
- Do not make network calls.
- Do not use real broker credentials.
- Do not enable real paper execution.
- Do not set `broker_action_allowed` true.
- This phase is simulated-only.

## Current pipeline

```text
Strategy Lab snapshot
→ read-only loader
→ offline order plans
→ risk gate
→ simulated broker adapter
→ execution journal
→ reconciliation
→ Alpaca paper adapter scaffold / broker interface / safety gate
```

## New capability

Add a manual approval layer:

```text
risk-approved order plan
→ approval artifact
→ simulated submission
→ execution journal
→ reconciliation
```

## Requirements

Create domain/service support for manual approvals.

Suggested files:

- `src/price_action_paper_trader/domain/approval.py`
- `src/price_action_paper_trader/services/manual_approval_service.py`
- `src/price_action_paper_trader/services/simulated_submission_service.py`

Approval records should include:

- `approval_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `approved_by`
- `approved_at`
- `expires_at`
- `approval_status`:
  - `pending`
  - `approved`
  - `expired`
  - `rejected`
  - `consumed`
- `approval_scope`:
  - `simulated_only`
- `broker_action_allowed: false`
- `notes`

## Approval artifacts

Create:

- `runs/approvals/approval_queue.md`
- `runs/approvals/approval_queue.csv`
- `runs/approvals/README.md`

Create individual approval templates for current risk-approved plans:

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

All approval templates should default to:

```yaml
approval_status: pending
approval_scope: simulated_only
broker_action_allowed: false
```

## Simulated submission

Add a function/service that can take:

- one risk-approved order plan
- one matching approval artifact

and produce a simulated submission result only if:

- `approval_status` is `approved`
- `approval_scope` is `simulated_only`
- approval is not expired
- `candidate_id` matches
- `order_plan_id` matches
- risk gate passed
- `broker_action_allowed` remains `false`

The result should go to:

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

## CLI

If the repo already has a CLI pattern, add safe commands such as:

```bash
python -m price_action_paper_trader.cli approvals list
python -m price_action_paper_trader.cli approvals validate
```

A simulated-only command may be added if consistent with the existing CLI pattern:

```bash
python -m price_action_paper_trader.cli approvals submit-simulated --approval-id <id>
```

The simulated submit command must fail closed if any required safety field is missing, mismatched, expired, or unsafe.

## Acceptance criteria

- Approval domain model exists and uses explicit status/scope fields.
- `broker_action_allowed` is always `false` for approvals and simulated submissions.
- Approval templates exist for all listed PTC candidates and default to pending/simulated-only/no broker action.
- Approval queue markdown and CSV artifacts are generated.
- Simulated submission queue markdown and CSV artifacts are generated.
- Simulated submission service refuses to run unless approval and order plan match.
- Simulated submission service refuses expired, rejected, pending, consumed, wrong-scope, mismatched, or unsafe approvals.
- Risk gate passed status is required before simulated submission.
- No Alpaca order submission is added.
- No network calls are added.
- No credentials are introduced.
- No background workers or schedulers are added.
- CLI list/validate commands are present if the repo CLI pattern supports them.
- Tests or validation checks cover happy path and fail-closed safety cases.

## Suggested test cases

- approved + simulated_only + not expired + matching IDs + risk passed + broker_action_allowed false → simulated submission created
- pending approval → rejected
- expired approval → rejected
- rejected approval → rejected
- consumed approval → rejected
- wrong `candidate_id` → rejected
- wrong `order_plan_id` → rejected
- approval_scope not `simulated_only` → rejected
- broker_action_allowed true anywhere → rejected
- risk gate not passed → rejected

## Phase boundary note

This phase only creates a manual approval artifact and simulated submission layer. It must not make the existing Alpaca scaffold capable of placing paper orders.
