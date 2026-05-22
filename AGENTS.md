# AGENTS.md — On The Levels / Price Action Paper Trader

## Role

You are working on **On The Levels**, a paper-trading workflow application that consumes approved outputs from the Price Action Strategy Lab.

Act as a cautious engineering assistant. Prefer small, testable changes, clear boundaries, and no broker execution unless explicitly requested in a future approved phase.

## Repo boundary

This repo is expected to live at:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Do not modify Strategy Lab or historical data extraction repos unless explicitly instructed.

## Safety rules

This project is not a live trading bot.

Never add or enable:

- live trading
- live broker account support
- autonomous order submission
- profitability claims
- strategy signal generation
- unapproved paper order submission

For all early phases, keep:

```yaml
broker_action_allowed: false
```

## Phase rules

### Phase 0 — Scaffold only

Allowed:

- docs
- configs
- Python package skeleton
- tests
- placeholder domain models

Not allowed:

- Alpaca API integration
- order submission
- position sizing
- live broker logic

### Phase 1 — Read-only Strategy Lab import

Allowed:

- parse Strategy Lab paper-review queue
- parse Strategy Lab paper-watch journal
- validate required fields

Not allowed:

- broker calls
- order submission

### Phase 2 — Order-plan generation

Allowed:

- convert approved candidates into local order-plan files
- write blocked decisions

Not allowed:

- broker calls

### Phase 3 — Risk gate

Allowed:

- block stale, oversized, duplicate, missing-target, or missing-invalidation plans

Not allowed:

- broker calls

### Phase 4+ — Paper broker adapter

Only implement after explicit approval. Paper account only. No live trading support.

## Coding style

- Keep domain models simple and typed.
- Prefer dataclasses or Pydantic only if added deliberately.
- Write tests for every new rule.
- Keep runtime outputs under `runs/`.
- Keep configs under `configs/`.

## Test command

```bash
PYTHONPATH=src pytest -q
```
