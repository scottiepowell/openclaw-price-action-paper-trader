# OpenClaw Inbox Prompt: Build Order Plan Generation (Phase 2)

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
Do not add broker submission.
Do not create live trading logic.
Do not submit orders.
Do not create autonomous execution.
Do not enable paper trading.
Do not write back to Strategy Lab.

This is still a read-only/offline planning phase.

`broker_action_allowed` must remain false everywhere.

## Context

The paper-trader repo now imports a real read-only Strategy Lab snapshot.

Current imported artifacts include:

- replay evidence matrix
- paper readiness matrix
- paper review queue
- paper watch journal
- selected review plans/journal files

The Strategy Lab snapshot remains source-of-truth.

The next step is to generate:

```text
read-only simulated order plans
```

from the imported paper-review queue.

No broker.
No Alpaca.
No execution.
No fills.
No order submission.

## Goal

Implement Phase 2:

```text
candidate review queue
  ↓
order-plan generation
  ↓
offline order-plan artifacts
```

## Create domain models

Create:

```text
src/price_action_paper_trader/domain/order_plan.py
```

Suggested fields:

```python
candidate_id
symbol
side
classification
entry_reference
target_price
invalidation_level
risk_notes
plan_status
snapshot_source
broker_action_allowed
created_at_utc
```

Use lightweight dataclass/object structure only.

No broker/execution state.

## Create service

Create:

```text
src/price_action_paper_trader/services/order_plan_builder.py
```

Responsibilities:

- load imported paper-review queue
- load readiness matrix
- select READY_FOR_PAPER_REVIEW candidates only
- generate simulated order-plan objects
- keep everything read-only
- no broker interaction

Suggested functions:

```python
build_order_plan(candidate_row)
build_order_plans(snapshot_dir)
serialize_order_plan(plan)
```

## Plan behavior

For now:

- order plans are only offline planning records
- no live price lookup
- no order IDs
- no fills
- no execution timestamps
- no broker adapter calls

Every generated plan must contain:

```text
broker_action_allowed: false
plan_status: DRAFT
```

## Generated artifacts

Create:

```text
runs/order_plans/
```

Generate:

```text
runs/order_plans/order_plan_queue.md
runs/order_plans/order_plan_queue.csv
```

Optionally create:

```text
runs/order_plans/plans/PTC-*-order-plan.md
```

Each generated plan should include:

- candidate ID
- symbol
- side
- replay classification
- target
- invalidation
- readiness status
- snapshot source
- explicit no-broker boundary

## Documentation

Update:

```text
README.md
PROJECT_BRIEF.md
TODO.md
```

Add:

- Phase 2 architecture
- order-plan generation flow
- explicit offline-only boundary
- future broker adapter separation

## Tests

Add/update tests:

- only READY_FOR_PAPER_REVIEW candidates generate plans
- blocked candidates do not generate plans
- generated plans are read-only
- generated plans always set:

```text
broker_action_allowed: false
plan_status: DRAFT
```

- order-plan queue artifacts are generated
- no Alpaca/broker dependency introduced

Run:

```text
PYTHONPATH=src pytest -q
```

## Deliverable

Write the response under:

```text
.openclaw-mailbox/outbox/2026-05-22-003-build-order-plan-generation-phase2-response.md
```

Include:

1. Files created/changed.
2. Order-plan architecture summary.
3. Generated order-plan queue paths.
4. Count of generated plans.
5. Which PTC candidates generated plans.
6. Which candidates were excluded and why.
7. Confirmation all plans remain offline-only.
8. Confirmation `broker_action_allowed: false` everywhere.
9. Test results.

After committing, run:

```text
git push
```

Also reply in Discord with only:

```text
Mailbox response written and pushed: .openclaw-mailbox/outbox/2026-05-22-003-build-order-plan-generation-phase2-response.md
```
