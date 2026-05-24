# OpenClaw Inbox Prompt: Plan and Scaffold Alpaca Paper Adapter (Phase 6)

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

This phase is allowed to scaffold a future Alpaca paper adapter, but it must not submit real orders yet.

Do not submit orders.
Do not create autonomous execution.
Do not enable live trading.
Do not add scheduler loops.
Do not add polling daemons.
Do not add background workers.
Do not use real credentials in the repo.
Do not hardcode secrets.
Do not enable live Alpaca endpoints.
Do not write back to Strategy Lab.

This phase must remain:

```text
manual-only
paper-only
config-gated
safe-by-default
```

`broker_action_allowed` must remain `false` by default.

If a future code path can ever set `broker_action_allowed` true, it must require explicit manual approval and must be paper-only.

## Context

The repo currently supports an offline end-to-end paper-trader simulation pipeline:

```text
Strategy Lab snapshot import
→ readiness filtering
→ offline order plans
→ risk gate
→ simulated broker adapter
→ simulated execution records
→ execution journal
→ reconciliation reports
```

Recent state:

- Phase 5 execution journal and reconciliation completed
- Tests reported: `30 passed`
- Current artifacts live under `runs/execution_journal/`
- No Alpaca dependency exists yet
- No broker/network execution exists yet

The next step is to safely prepare for a future Alpaca paper adapter, without submitting orders.

## Goal

Create a Phase 6 scaffold and safety plan for Alpaca paper integration.

This should include:

```text
configuration validation
paper-only broker interface
disabled-by-default adapter stub
manual approval contract
safety tests
architecture docs
```

Do not submit an Alpaca paper order in this phase.

## Create broker interface

Create:

```text
src/price_action_paper_trader/adapters/broker_interface.py
```

Define a simple interface/protocol for future broker adapters, such as:

```python
class BrokerAdapter:
    def submit_order(self, approved_order): ...
    def get_order_status(self, order_id): ...
```

This should be an interface only. No network calls.

## Create Alpaca paper adapter scaffold

Create:

```text
src/price_action_paper_trader/adapters/alpaca_paper_broker.py
```

For now this should be a disabled scaffold only.

It may define:

```python
class AlpacaPaperBroker:
    def __init__(self, config): ...
    def validate_config(self): ...
    def submit_order(self, approved_order): ...
```

But `submit_order()` must raise a safe exception or return a blocked result unless all future manual approval gates are explicitly satisfied.

Do not install or import real Alpaca SDK unless strictly necessary. Prefer no Alpaca dependency in this phase.

Do not perform network calls.

## Create manual approval model

Create:

```text
src/price_action_paper_trader/domain/manual_approval.py
```

Suggested fields:

```python
candidate_id
approved_by
approval_timestamp_utc
approval_scope
approval_status
paper_only
broker_action_allowed
notes
```

Default behavior:

```text
approval_status: NOT_APPROVED
paper_only: true
broker_action_allowed: false
```

## Create config files

Update or create:

```text
configs/paper.yaml
configs/default.yaml
```

Add safe defaults:

```yaml
broker:
  provider: alpaca
  mode: paper
  enabled: false
  allow_live_trading: false
  require_manual_approval: true
  submit_orders: false
  broker_action_allowed_default: false
```

Do not include credentials.

Use environment variable names only, for future use:

```text
ALPACA_PAPER_API_KEY
ALPACA_PAPER_SECRET_KEY
ALPACA_PAPER_BASE_URL
```

Do not read real env vars unless config validation needs to check their presence in disabled mode.

## Create safety validation service

Create:

```text
src/price_action_paper_trader/services/broker_safety_gate.py
```

It should validate:

- broker enabled is false by default
- live trading is false
- mode is paper
- submit_orders is false unless explicit future manual approval exists
- broker_action_allowed is false unless all safety checks pass
- no live endpoint is configured
- no missing target/invalidation plan gets through
- no blocked risk gate plan gets through

For now, all real submission attempts should be blocked.

## Documentation

Update:

```text
README.md
PROJECT_BRIEF.md
TODO.md
docs/ARCHITECTURE.md
docs/DEVELOPMENT_PHASES.md
```

Add a new doc:

```text
docs/ALPACA_PAPER_ADAPTER_PLAN.md
```

Include:

- Phase 6 scope
- why Alpaca is scaffolded but disabled
- manual approval model
- required environment variables for future use
- paper-only endpoint policy
- live-trading prohibition
- safety checks before any future submission
- how simulated broker differs from real paper adapter

## Tests

Add/update tests:

- Alpaca adapter scaffold cannot submit by default
- broker enabled defaults to false
- live trading cannot be enabled by default
- missing manual approval blocks submission
- non-paper mode blocks submission
- submit_orders false blocks submission
- broker_action_allowed remains false by default
- no real Alpaca dependency required
- no network calls are made
- simulated broker tests still pass
- execution journal/reconciliation tests still pass

Run:

```text
PYTHONPATH=src pytest -q
```

## Deliverable

Write the response under:

```text
.openclaw-mailbox/outbox/2026-05-22-007-plan-alpaca-paper-adapter-phase6-response.md
```

Include:

1. Files created/changed.
2. Broker interface summary.
3. Alpaca paper adapter scaffold summary.
4. Manual approval model summary.
5. Config safety defaults.
6. Safety gate summary.
7. Documentation paths.
8. Confirmation no orders can be submitted.
9. Confirmation no live trading path exists.
10. Confirmation no secrets were committed.
11. Confirmation `broker_action_allowed` remains false by default.
12. Test results.

After committing, run:

```text
git push
```

Also reply in Discord with only:

```text
Mailbox response written and pushed: .openclaw-mailbox/outbox/2026-05-22-007-plan-alpaca-paper-adapter-phase6-response.md
```
