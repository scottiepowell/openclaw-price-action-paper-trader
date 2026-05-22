# On The Levels

Repository: `openclaw-price-action-paper-trader`  
Python package: `price_action_paper_trader`

**On The Levels** is a paper-trading workflow application that consumes approved outputs from the Price Action Strategy Lab and turns them into manual paper-review plans, risk-gated order plans, paper-broker requests, and execution/audit journals.

## Current phase

This repo starts at **Phase 0 — scaffold only**.

Phase 0 creates the repo structure, documentation, config placeholders, package skeleton, and test harness. It does **not** connect to Alpaca, submit orders, or execute trades.

## Safety boundary

This project is **not a live trading bot**.

At this phase:

- No Alpaca order submission
- No live trading support
- No broker action enabled
- No profitability claims
- No trade recommendations
- No autonomous execution

Any future paper execution must remain paper-account only, manually approved, risk-gated, and fully journaled.

## Intended pipeline

```text
Strategy Lab outputs
        ↓
paper-review queue / journal
        ↓
paper-trader app
        ↓
paper broker adapter
        ↓
Alpaca paper account
        ↓
execution journal / audit logs
```

## Initial application layers

```text
configs/
  default.yaml
  paper.yaml

src/price_action_paper_trader/
  app.py
  config.py
  cli.py

  domain/
    candidate.py
    order_plan.py
    risk.py
    journal.py

  adapters/
    strategy_lab_reader.py
    alpaca_paper_broker.py
    file_journal.py

  services/
    paper_review_loader.py
    order_plan_builder.py
    risk_gate.py
    paper_execution_service.py
```

## Development phases

1. **Phase 0 — Scaffold only**  
   Create repo, docs, configs, package skeleton, tests.

2. **Phase 1 — Read-only Strategy Lab import**  
   Read paper-review queue and journal from Strategy Lab. No broker.

3. **Phase 2 — Order-plan generation**  
   Convert approved candidates into paper order plans. Still no Alpaca submission.

4. **Phase 3 — Risk gate**  
   Block oversized, duplicate, stale, missing-target, missing-invalidation, or non-approved candidates.

5. **Phase 4 — Paper broker adapter**  
   Connect to Alpaca paper account only. No live trading support.

6. **Phase 5 — Manual approval execution**  
   Submit paper orders only when explicitly approved.

7. **Phase 6 — Journal reconciliation**  
   Record submitted order, broker response, fills, target/invalidation outcome.

8. **Phase 7 — Reporting dashboard/CLI**  
   Summarize paper results, blocked orders, active watches, and outcomes.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src pytest -q
```

Expected Phase 0 test result:

```text
all tests pass
```

## Strategy Lab contract

This app should consume Strategy Lab outputs only after they pass the Strategy Lab evidence pipeline:

```text
replay evidence → manual review → paper readiness → paper review queue → paper watch journal
```

This app does not discover strategy candidates and does not make strategy decisions.
