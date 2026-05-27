# Phase 12 — Read-only Delayed Market Data Snapshot Layer

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Goal

Add a read-only delayed market-data snapshot layer so the operator can compare current/recent market context against existing strategy/order-plan/approval artifacts without placing trades.

This phase is for **decision support only**:

```text
watchlist symbols
→ delayed/recent historical market data snapshot
→ local snapshot artifacts
→ human-review context report
→ no order submission
```

This phase should let a human operator ask:

- What does the recent market context look like for the current candidate symbols?
- Is a simulated candidate still coherent against recent bars?
- Is the current market context aligned, mixed, stale, invalidated, or insufficient?
- What data source/time window/freshness was used?

This phase must not trade.

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not submit real orders.
Do not submit Alpaca paper orders.
Do not use broker trading credentials.
Do not enable paper execution.
Do not set `broker_action_allowed` true.
Do not change strategy logic.
Do not create new simulated submissions.
Do not create new approvals.
Do not create new journal records.
Do not create new reconciliation records.
Do not mutate existing approval/submission/journal/reconciliation artifacts.

## Network boundary for this phase

Unlike earlier offline-only phases, this phase may add **read-only market-data fetch support**.

Allowed network behavior:

- user-triggered market-data fetch only
- no background fetch
- no scheduler
- no streaming websocket
- no autonomous refresh
- read-only HTTP calls to a market-data provider only
- no broker order endpoint calls
- no account endpoint calls
- no position endpoint calls
- no trading endpoint calls

If using Alpaca, use only market-data endpoints/classes. Do not use trading client/order submission APIs.

If credentials are needed for market data, read them from environment variables only. Do not commit credentials. Do not print secrets.

## Market data policy

Start with delayed/recent historical bars, not streaming real-time data.

Prefer conservative defaults:

- symbols: existing candidate symbols from current order-plan/approval artifacts
- timeframes: `1Min`, `5Min`, and/or `1Day`, depending on provider support
- delay: at least 15 minutes by default
- mode: manual CLI invocation only
- output: local artifacts under `runs/market_data/` and `runs/reports/`

The first implementation should be safe even if API credentials are not present. It should either:

1. skip live fetch with a clear status such as `market_data_unavailable`, or
2. use a fixture/mock provider in tests, or
3. support a provider abstraction so real fetch can be configured later.

Do not make tests depend on live network access.

## Current known repo state

The app already has a proven simulated operational chain:

```text
strategy snapshot
→ order plan
→ risk gate
→ manual approval artifact
→ simulated submission
→ simulated execution journal
→ simulated reconciliation
→ audit/report outputs
```

Recent known milestones:

- Phase 9 created one simulated submission for `APR-PTC-004 / PTC-004 / OP-PTC-004 / NVDA / bullish`
- Phase 10 journaled and reconciled the simulated submission
- Phase 10 final pushed commit: `043b40f4f42f56e08c2b34906f5ebd43308439a8`
- Phase 11 mailbox task exists for run-state traceability manifest

This Phase 12 task may be implemented after Phase 11 is complete. If Phase 11 is not complete yet, do not block unnecessarily, but avoid conflicting with Phase 11 report outputs.

## New capability

Add a read-only market data layer with provider abstraction.

Suggested files:

- `src/price_action_paper_trader/domain/market_data.py`
- `src/price_action_paper_trader/services/market_data_snapshot_service.py`
- `src/price_action_paper_trader/services/market_context_assessment_service.py`
- `src/price_action_paper_trader/adapters/market_data_provider.py`
- `src/price_action_paper_trader/adapters/alpaca_market_data_provider.py` if Alpaca data support is practical and safe
- `tests/unit/test_market_data_snapshot_service.py`
- `tests/unit/test_market_context_assessment_service.py`

If existing project structure suggests better names, follow the existing style.

## Domain model guidance

Create simple read-only market-data domain models such as:

### MarketDataBar

Fields should include:

- `symbol`
- `timeframe`
- `timestamp`
- `open`
- `high`
- `low`
- `close`
- `volume`
- `source`
- `feed`
- `fetched_at`
- `data_delay_minutes`
- `is_delayed`

### MarketDataSnapshot

Fields should include:

- `snapshot_id`
- `symbols`
- `timeframes`
- `window_start`
- `window_end`
- `fetched_at`
- `source`
- `feed`
- `data_delay_minutes`
- `is_live_execution_allowed: false`
- `broker_action_allowed: false`
- `bars`
- `snapshot_status`
- `notes`

### MarketContextAssessment

Fields should include:

- `assessment_id`
- `candidate_id`
- `order_plan_id`
- `symbol`
- `side`
- `snapshot_id`
- `latest_bar_timestamp`
- `latest_close`
- `data_freshness_status`
- `plan_context_status`: `aligned`, `mixed`, `invalidated`, `stale`, or `insufficient_data`
- `human_review_required: true`
- `broker_action_allowed: false`
- `notes`

## Snapshot artifacts

Generate:

- `runs/market_data/latest_market_snapshot.md`
- `runs/market_data/latest_market_snapshot.csv`

Optional if useful:

- `runs/market_data/latest_market_snapshot.json`

The snapshot artifacts should include:

- source/provider
- fetch mode: read-only
- symbols
- timeframes
- requested window
- actual data window
- fetched_at
- data_delay_minutes
- feed/source
- row count
- broker_action_allowed: false
- explicit note that this is not an order signal and not trade authorization

## Context assessment artifacts

Generate:

- `runs/reports/market_context_assessment_report.md`
- `runs/reports/market_context_assessment_report.csv`

Optional if useful:

- `runs/reports/market_context_assessment_report.json`

The assessment report should compare the market snapshot to existing candidate/order-plan artifacts and classify each candidate as one of:

- `aligned`
- `mixed`
- `invalidated`
- `stale`
- `insufficient_data`

Keep the first version simple. It does not need sophisticated trading logic. It should focus on data freshness, symbol match, side/context consistency if current order-plan fields make that possible, and human-review notes.

Every assessment must include:

```yaml
human_review_required: true
broker_action_allowed: false
```

## CLI

If consistent with existing CLI style, add safe commands such as:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli market-data snapshot --symbols NVDA,SPY,QQQ --timeframes 1Min,5Min,1Day --delay-minutes 15
PYTHONPATH=src python -m price_action_paper_trader.cli market-data assess-context
```

If the repo prefers all commands under `approvals`, use a clear safe name, but `market-data` is preferred because this is not an approval command.

CLI behavior requirements:

- manual invocation only
- no scheduler
- no background loop
- no streaming
- no trade submission
- no simulated submission creation
- no mutation of approval/submission/journal/reconciliation artifacts
- writes only market-data snapshots and assessment reports

## Provider behavior

Implement a provider interface so tests can use deterministic fake data.

If a real provider is implemented, it must be read-only and fail closed.

Expected real-provider behavior:

- If required env vars are absent, return a clear `market_data_unavailable` status instead of crashing.
- Do not print secrets.
- Do not call broker trading/order/account/position endpoints.
- Do not submit orders.
- Respect `delay_minutes` and avoid requesting data newer than the configured delay.

Suggested environment variable names if needed:

```text
ALPACA_MARKET_DATA_API_KEY
ALPACA_MARKET_DATA_SECRET_KEY
ALPACA_MARKET_DATA_FEED
```

Do not use or require trading-specific variable names for this phase.

## Safety checks

Add explicit checks or tests proving:

- `broker_action_allowed` is false in all market-data artifacts
- `human_review_required` is true in all assessments
- missing credentials do not enable execution
- provider failures do not enable execution
- no order/trading/broker client is invoked
- no approval/submission/journal/reconciliation artifacts are mutated
- tests do not require live network access

## Tests

Add or strengthen tests verifying:

- fake provider can produce deterministic bars
- snapshot artifacts are generated from fake provider data
- snapshot artifacts include provider/source/freshness/broker_action_allowed false
- missing provider credentials produce safe unavailable/stale status
- assessment report generates one row per relevant candidate/order-plan symbol where possible
- stale or missing data produces `stale` or `insufficient_data`
- `broker_action_allowed true` is never produced
- `human_review_required` is always true
- CLI snapshot command works with fake/offline mode or safely reports unavailable if live provider is not configured
- CLI assess-context command writes reports without mutating lifecycle artifacts

## Verification

Run:

```bash
PYTHONPATH=src pytest -q
```

If CLI commands are added, run safe commands that do not require live credentials, for example:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli market-data snapshot --symbols NVDA --timeframes 5Min --delay-minutes 15 --provider fake
PYTHONPATH=src python -m price_action_paper_trader.cli market-data assess-context
```

If the CLI does not use `--provider fake`, use the equivalent safe/offline mode implemented by the repo.

Then show:

```bash
git status --short
git diff --stat
```

## Commit and push

Before committing, remove Python cache files if present:

```bash
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
```

If changes are made and tests pass:

```bash
git add src tests runs .open-claw-mailbox/outbox .gitignore
 git commit -m "Add Phase 12 read-only delayed market data snapshot layer"
git push origin main
```

If tests fail, stop and report the exact failure.
If unrelated files appear, stop and report them before committing.

## Outbox response

Write the response to:

```text
.open-claw-mailbox/outbox/phase-12-read-only-delayed-market-data-snapshot-response.md
```

Include:

- files added/changed
- provider approach implemented: fake/offline only, real read-only provider, or both
- snapshot artifacts generated
- market context assessment artifacts generated
- CLI commands added and results
- pytest result
- commit SHA if committed
- whether live credentials are required: yes/no
- confirmation no broker/order/account/position endpoints are called
- confirmation no broker/network/live execution path was added
- confirmation no broker credentials were used for trading
- confirmation lifecycle artifacts were not mutated
- confirmation `broker_action_allowed` remains false everywhere
