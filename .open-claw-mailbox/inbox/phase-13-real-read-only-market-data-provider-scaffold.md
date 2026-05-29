# Phase 13 — Real Read-only Market Data Provider Scaffold

Work in:

```text
/home/scott/projects/openclaw-price-action-paper-trader
```

Repository:

```text
scottiepowell/openclaw-price-action-paper-trader
```

## Goal

Add an opt-in real read-only market-data provider behind the Phase 12 provider interface, while keeping fake/offline market data as the default.

This phase should allow a human operator to manually fetch delayed/recent historical market bars from a real market-data provider and write local snapshot/report artifacts for review.

This phase must not trade.

Target lifecycle:

```text
manual CLI invocation
→ read-only delayed market-data fetch
→ local market snapshot artifacts
→ market context assessment report
→ no order submission
```

## Hard boundaries

Do not add Alpaca order submission.
Do not add live trading.
Do not add autonomous execution.
Do not add background workers.
Do not add schedulers.
Do not add streaming websocket support.
Do not submit real orders.
Do not submit Alpaca paper orders.
Do not call broker trading endpoints.
Do not call account endpoints.
Do not call position endpoints.
Do not call order endpoints.
Do not use broker trading credentials.
Do not enable paper execution.
Do not create new simulated submissions.
Do not create new approvals.
Do not create new journal records.
Do not create new reconciliation records.
Do not mutate existing approval/submission/journal/reconciliation artifacts.
Do not set `broker_action_allowed` true.
Do not change strategy logic.

Everything remains human-triggered, read-only, and decision-support only.

## Current known state

Phase 12 added:

- fake/offline market-data provider
- snapshot layer
- context assessment layer
- CLI commands
- snapshot artifacts under `runs/market_data/`
- context assessment artifacts under `runs/reports/`

Recent verified Phase 12 state:

- Final pushed commit: `b0a5872feafc64e7acd2643c9d6b801c0aeaf246`
- Fake snapshot command returned `status=pass`, `count=45`
- Context assessment returned `status=warning`, `total_complete_traces=1`, `incomplete_traces=10`
- Tests: `PYTHONPATH=src pytest -q` → 71 passed
- No broker/order/account/position calls
- No live credentials required
- No live execution path
- `broker_action_allowed` remains false everywhere

## New capability

Add a real read-only provider implementation behind the existing provider abstraction.

Preferred provider name:

```text
alpaca-readonly
```

Keep current fake/offline provider as the default.

Expected CLI shape:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli market-data snapshot \
  --provider alpaca-readonly \
  --symbols NVDA \
  --timeframes 5Min \
  --delay-minutes 15
```

Also keep the fake provider working:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli market-data snapshot \
  --provider fake \
  --symbols NVDA \
  --timeframes 5Min \
  --delay-minutes 15
```

## Provider requirements

Suggested file:

```text
src/price_action_paper_trader/adapters/alpaca_readonly_market_data_provider.py
```

or use an existing adapter file if Phase 12 created one.

The provider must:

- fetch market data only
- support delayed/recent historical bars only
- respect `delay_minutes`, defaulting to at least 15
- avoid requesting bars newer than `now - delay_minutes`
- normalize provider data into existing Phase 12 `MarketDataBar` / snapshot models
- return safe unavailable status if credentials are absent
- fail closed on provider/API errors
- never print secrets
- never submit orders
- never instantiate or call trading/order/account/position clients

## Credentials

Use market-data-specific environment variable names only:

```text
ALPACA_MARKET_DATA_API_KEY
ALPACA_MARKET_DATA_SECRET_KEY
ALPACA_MARKET_DATA_FEED
```

Optional/default feed behavior:

```text
ALPACA_MARKET_DATA_FEED=iex
```

Do not require or use trading-specific variable names in this phase.

Do not commit credentials.
Do not print credentials.
Do not write credentials into artifacts.

If credentials are missing, the CLI should exit safely with a clear unavailable status, not crash and not trade.

## Network policy

Allowed:

- user-triggered read-only HTTP calls to market-data endpoints/classes only

Not allowed:

- order endpoint calls
- account endpoint calls
- position endpoint calls
- trading endpoint calls
- streaming websocket
- scheduler
- background polling
- autonomous refresh

## Dependency policy

Prefer using dependencies already present in the repo.

If a new dependency is needed for Alpaca market data, do not add it blindly. First inspect current project dependency files. If adding a dependency is necessary, keep it narrow and document why.

Tests must not require network access or real credentials.

## Artifact behavior

Real provider snapshot should write the same artifact paths as Phase 12 unless CLI options support alternate output paths:

- `runs/market_data/latest_market_snapshot.md`
- `runs/market_data/latest_market_snapshot.csv`
- `runs/market_data/latest_market_snapshot.json`

Context assessment should continue writing:

- `runs/reports/market_context_assessment_report.md`
- `runs/reports/market_context_assessment_report.csv`

Every artifact must include:

```yaml
broker_action_allowed: false
is_live_execution_allowed: false
human_review_required: true
```

where applicable.

Snapshot artifacts should also include:

- provider: `alpaca-readonly` or `fake`
- feed
- delayed/recent historical mode
- requested symbols
- requested timeframes
- requested delay_minutes
- fetched_at
- window_start
- window_end
- row_count
- snapshot_status
- notes

## Context assessment behavior

Do not add sophisticated trading strategy logic in this phase.

The assessment should remain conservative and classify each candidate as one of:

- `aligned`
- `mixed`
- `invalidated`
- `stale`
- `insufficient_data`
- `market_data_unavailable`

For real provider unavailable/missing credentials, use `market_data_unavailable` or equivalent safe status.

Always require human review.

## Tests

Add or strengthen tests verifying:

- fake provider still works
- `alpaca-readonly` provider returns safe unavailable status when credentials are missing
- provider errors fail closed
- delay window excludes bars newer than `now - delay_minutes`
- no order/trading/account/position clients are instantiated or called
- secrets are not printed or written to artifacts
- real-provider adapter can normalize mocked provider bars into existing domain models
- CLI with `--provider fake` still succeeds
- CLI with `--provider alpaca-readonly` and no credentials safely reports unavailable or warning without crashing
- `broker_action_allowed` is false in all outputs
- `is_live_execution_allowed` is false in all snapshots
- `human_review_required` is true in all assessments
- lifecycle artifacts are not mutated
- tests do not require live network access

## Verification

Run:

```bash
PYTHONPATH=src pytest -q
```

Run safe CLI checks that do not require live credentials:

```bash
PYTHONPATH=src python -m price_action_paper_trader.cli market-data snapshot --provider fake --symbols NVDA --timeframes 5Min --delay-minutes 15
PYTHONPATH=src python -m price_action_paper_trader.cli market-data snapshot --provider alpaca-readonly --symbols NVDA --timeframes 5Min --delay-minutes 15
PYTHONPATH=src python -m price_action_paper_trader.cli market-data assess-context
```

The `alpaca-readonly` command should be safe if credentials are missing.

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
git add src tests runs .open-claw-mailbox/outbox .gitignore pyproject.toml requirements.txt setup.cfg setup.py
 git commit -m "Add Phase 13 real read-only market data provider scaffold"
git push origin main
```

Only stage dependency files if actually changed.

If tests fail, stop and report the exact failure.
If unrelated files appear, stop and report them before committing.

## Outbox response

Write the response to:

```text
.open-claw-mailbox/outbox/phase-13-real-read-only-market-data-provider-scaffold-response.md
```

Include:

- files added/changed
- provider approach implemented
- whether fake provider still works
- whether `alpaca-readonly` safe unavailable behavior works without credentials
- snapshot artifacts generated
- context assessment artifacts generated
- CLI command results
- pytest result
- commit SHA if committed
- whether new dependencies were added
- whether live credentials are required for tests: yes/no
- confirmation no broker/order/account/position endpoints are called
- confirmation no live/paper execution path was added
- confirmation no broker credentials were used for trading
- confirmation lifecycle artifacts were not mutated
- confirmation `broker_action_allowed` remains false everywhere
