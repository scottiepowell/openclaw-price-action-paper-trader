# OpenClaw Inbox Prompt: Build Risk Gate (Phase 3)

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

This remains an offline-only planning system.

`broker_action_allowed` must remain `false` everywhere.

## Context

The repo currently supports:

```text
Strategy Lab snapshot import
→ readiness filtering
→ offline order-plan generation
```

Generated order plans currently exist under:

```text
runs/order_plans/
```

The next architectural layer is:

```text
risk gate validation
```

The risk gate should block malformed, contradictory, duplicate, stale, or unsafe order plans before any future broker adapter exists.

No broker integration should be added in this phase.

## Goal

Implement:

```text
order-plan generation
  ↓
risk gate evaluation
  ↓
risk-reviewed offline plans
```

## Create domain model

Create:

```text
src/price_action_paper_trader/domain/risk_result.py
```

Suggested fields:

```python
candidate_id
symbol
risk_status
blocked
block_reasons
warnings
review_timestamp_utc
broker_action_allowed
```

Use lightweight dataclass/object structure only.

## Create service

Create:

```text
src/price_action_paper_trader/services/risk_gate.py
```

Suggested functions:

```python
validate_order_plan(plan)
validate_order_plans(plans)
serialize_risk_result(result)
```

## Risk rules

Implement offline validation rules only.

Suggested blocking rules:

```text
missing target price
missing invalidation level
missing symbol
missing side
duplicate symbol plan
non-DRAFT plan status
contradictory classification
missing readiness status
broker_action_allowed not false
```

Suggested warning-only rules:

```text
very small breakout amount
very small target distance
older snapshot metadata
ambiguous historical classification
```

Do not use live pricing.
Do not use broker APIs.
Do not use Alpaca.

## Generated artifacts

Create:

```text
runs/risk_gate/
```

Generate:

```text
runs/risk_gate/risk_gate_report.md
runs/risk_gate/risk_gate_report.csv
```

Optionally create:

```text
runs/risk_gate/plans/PTC-*-risk-review.md
```

Each report should include:

- candidate ID
- symbol
- blocked or approved
- warnings
- block reasons
- readiness source
- snapshot source
- explicit offline-only boundary

## Documentation

Update:

```text
README.md
PROJECT_BRIEF.md
TODO.md
```

Add:

- Phase 3 architecture
- risk gate role in the pipeline
- offline-only validation boundaries
- future broker adapter separation

Document intended future flow:

```text
Strategy Lab snapshot
  ↓
readiness filter
  ↓
order-plan generation
  ↓
risk gate
  ↓
future broker adapter
```

## Tests

Add/update tests:

- malformed plans are blocked
- duplicate symbol plans are blocked
- missing target/invalidation plans are blocked
- valid DRAFT plans pass
- warnings generate correctly
- generated reports exist
- broker_action_allowed remains false
- no Alpaca/broker dependency introduced

Run:

```text
PYTHONPATH=src pytest -q
```

## Deliverable

Write the response under:

```text
.openclaw-mailbox/outbox/2026-05-22-004-build-risk-gate-phase3-response.md
```

Include:

1. Files created/changed.
2. Risk-gate architecture summary.
3. Risk report artifact paths.
4. Count of validated plans.
5. Count of blocked plans.
6. Common block reasons.
7. Warning categories generated.
8. Confirmation everything remains offline-only.
9. Confirmation `broker_action_allowed: false` everywhere.
10. Test results.

After committing, run:

```text
git push
```

Also reply in Discord with only:

```text
Mailbox response written and pushed: .openclaw-mailbox/outbox/2026-05-22-004-build-risk-gate-phase3-response.md
```
