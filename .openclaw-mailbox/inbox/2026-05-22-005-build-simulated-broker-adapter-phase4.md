# OpenClaw Inbox Prompt: Build Simulated Broker Adapter (Phase 4)

## Repo

Work in this repo only:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

GitHub repo:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Discord channel

Use:

```text
#openclaw-apps
channel id: 1507382627651555480
```

## Boundary

Do not add Alpaca integration.
Do not add real broker submission.
Do not create live trading logic.
Do not submit orders.
Do not use real credentials.
Do not create autonomous execution.
Do not enable live trading.
Do not write back to Strategy Lab.

This phase must remain:

```text
offline-only
simulated-only
non-networked
```

`broker_action_allowed` must remain `false` everywhere.

## Context

The repo currently supports:

```text
Strategy Lab snapshot import
→ readiness filtering
→ offline order-plan generation
→ risk gate validation
```

The next architectural layer is:

```text
simulated broker adapter
```

The purpose is to validate future execution architecture and journaling lifecycle *without* introducing any real broker or network dependency.

## Goal

Implement:

```text
risk-reviewed order plans
  ↓
simulated broker adapter
  ↓
simulated execution records
```

## Create domain models

Create:

```text
src/price_action_paper_trader/domain/execution_record.py
```

Suggested fields:

```python
candidate_id
symbol
side
simulated_order_id
execution_status
submission_timestamp_utc
fill_status
fill_price
notes
broker_action_allowed
```

Use lightweight dataclass/object structure only.

## Create adapter

Create:

```text
src/price_action_paper_trader/adapters/simulated_broker.py
```

This adapter must:

- be offline-only
- generate fake broker responses
- generate fake order IDs
- generate deterministic simulated execution records
- perform no network calls
- have no Alpaca dependency
- have no requests/http client dependency

Suggested functions:

```python
submit_simulated_order(plan)
submit_simulated_orders(plans)
serialize_execution_record(record)
```

## Simulation behavior

The adapter should:

- accept only risk-approved plans
- reject blocked plans
- reject malformed plans
- generate deterministic fake order IDs
- mark records as:

```text
SIMULATED_SUBMITTED
```

or:

```text
SIMULATED_REJECTED
```

Do not simulate real fills yet.
Do not simulate real market pricing.
Do not add timing loops.
Do not add async workers.

## Generated artifacts

Create:

```text
runs/simulated_execution/
```

Generate:

```text
runs/simulated_execution/simulated_execution_queue.md
runs/simulated_execution/simulated_execution_queue.csv
```

Optionally create:

```text
runs/simulated_execution/records/PTC-*-simulated-execution.md
```

Each generated execution record should include:

- candidate ID
- symbol
- side
- simulated order ID
- execution status
- snapshot source
- risk-gate status
- explicit offline-only boundary
- explicit simulated-only boundary

## Documentation

Update:

```text
README.md
PROJECT_BRIEF.md
TODO.md
```

Add:

- Phase 4 architecture
- simulated broker layer
- future real broker separation
- offline-only guarantees

Document intended future flow:

```text
Strategy Lab snapshot
  ↓
readiness filter
  ↓
order plans
  ↓
risk gate
  ↓
simulated broker adapter
  ↓
execution journal
```

## Tests

Add/update tests:

- only approved plans submit successfully
- blocked plans reject
- malformed plans reject
- deterministic simulated order IDs generate
- simulated execution artifacts generate
- broker_action_allowed remains false
- no network calls introduced
- no Alpaca dependency introduced
- no requests/http client introduced

Run:

```text
PYTHONPATH=src pytest -q
```

## Deliverable

Write the response under:

```text
.openclaw-mailbox/outbox/2026-05-22-005-build-simulated-broker-adapter-phase4-response.md
```

Include:

1. Files created/changed.
2. Simulated broker architecture summary.
3. Simulated execution artifact paths.
4. Count of simulated execution records.
5. Which PTC candidates produced simulated submissions.
6. Which candidates were rejected and why.
7. Confirmation everything remains offline-only.
8. Confirmation no Alpaca dependency exists.
9. Confirmation `broker_action_allowed: false` everywhere.
10. Test results.

After committing, run:

```text
git push
```

Also reply in Discord with only:

```text
Mailbox response written and pushed: .openclaw-mailbox/outbox/2026-05-22-005-build-simulated-broker-adapter-phase4-response.md
```
