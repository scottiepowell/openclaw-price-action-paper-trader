# Phase 7 — Manual Approval Command Layer

Add a manual approval command layer for one risk-approved order plan to be explicitly approved for **simulated execution only**.

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

Strategy Lab snapshot → read-only loader → offline order plans → risk gate → simulated broker adapter → execution journal → reconciliation → Alpaca paper adapter scaffold / broker interface / safety gate

## New capability

risk-approved order plan → approval artifact → simulated submission → execution journal → reconciliation

## Suggested files

- `src/price_action_paper_trader/domain/approval.py`
- `src/price_action_paper_trader/services/manual_approval_service.py`
- `src/price_action_paper_trader/services/simulated_submission_service.py`

## Approval fields

- `approval_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `approved_by`
- `approved_at`
- `expires_at`
- `approval_status`: `pending`, `approved`, `expired`, `rejected`, `consumed`
- `approval_scope`: `simulated_only`
- `broker_action_allowed: false`
- `notes`

## Approval artifacts

Create:

- `runs/approvals/approval_queue.md`
- `runs/approvals/approval_queue.csv`
- `runs/approvals/README.md`

Create approval templates for:

- `PTC-004`
- `PTC-005`
- `PTC-009`
- `PTC-017`
- `PTC-019`
- `PTC-021`
- `PTC-022`
- `PTC-024`
- `PTC-032`
- `PTC-034`
- `PTC-035`

Each template must default to:

```yaml
approval_status: pending
approval_scope: simulated_only
broker_action_allowed: false
```

## Simulated submission requirements

Add a service/function that takes one risk-approved order plan and one matching approval artifact, then produces a simulated submission result only if:

- approval status is `approved`
- approval scope is `simulated_only`
- approval is not expired
- `candidate_id` matches
- `order_plan_id` matches
- risk gate passed
- `broker_action_allowed` remains `false`

Write results to:

- `runs/simulated_submissions/simulated_submission_queue.md`
- `runs/simulated_submissions/simulated_submission_queue.csv`

Submission records should include:

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

If the repo has a CLI pattern, add safe commands such as:

```bash
python -m price_action_paper_trader.cli approvals list
python -m price_action_paper_trader.cli approvals validate
```

A simulated-only submit command may be added only if it fails closed:

```bash
python -m price_action_paper_trader.cli approvals submit-simulated --approval-id <id>
```

## Acceptance criteria

- Approval model exists with explicit status/scope fields.
- `broker_action_allowed` remains false everywhere.
- Approval templates exist for all listed PTC candidates.
- Approval queue markdown and CSV artifacts are generated.
- Simulated submission queue markdown and CSV artifacts are generated.
- Service rejects expired, rejected, pending, consumed, wrong-scope, mismatched, unsafe, or non-risk-approved requests.
- No Alpaca order submission, network calls, credentials, workers, or schedulers are added.
- Tests cover happy path and fail-closed safety cases.

## Phase boundary

This phase only creates a manual approval artifact and simulated submission layer. It must not make the Alpaca scaffold capable of placing paper orders.
