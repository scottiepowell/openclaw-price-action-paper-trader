# Safety Boundaries

This project is not a live trading bot.

## Always prohibited unless future docs explicitly change it

- Live trading
- Live account support
- Autonomous order submission
- Profitability claims
- Strategy signal generation

## Phase 0 boundary

Phase 0 is scaffold only. It must not import Alpaca or submit orders.

## Required default flags

```yaml
broker_action_allowed: false
live_trading_allowed: false
alpaca_order_submission_allowed: false
require_manual_approval: true
```
