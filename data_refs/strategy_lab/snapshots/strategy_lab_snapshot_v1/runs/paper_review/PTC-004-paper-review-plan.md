# PTC-004 Paper Review Plan

- replay_id: HR-004
- symbol: NVDA
- side: bullish
- paper_review_status: pending_human_approval
- broker_action_allowed: false

## Replay evidence summary
- prior_resistance: 301.99
- breakout_amount: 3.53
- close_above_resistance: true
- target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- suggested_classification: confirmed_breakout

## Entry condition
- close_above_resistance replay supports a manual paper-review watch only; entry candidate price is 305.52.

## Target condition
- target_price: 309.05
- room_to_target: 7.06

## Invalidation condition
- invalidation_level: 298.46

## No-trade filters
- real_market_replay only
- verified replay evidence
- manual_review_status completed
- broker_action_allowed false
- no Alpaca submission
- no live trading

## Manual approval checklist
- [ ] Replay evidence is verified and real-market-backed
- [ ] Paper review status remains pending_human_approval until manually approved
- [ ] Broker action stays false
- [ ] No Alpaca submission or live execution path exists
- [ ] Target and invalidation levels are documented
- [ ] No profitability claim is made

## Boundary
- no trade signal
- no profitability claim
- no broker action
- no Alpaca submission
