# PTC-022 Paper Review Plan

- replay_id: HR-022
- symbol: AMZN
- side: bullish
- paper_review_status: pending_human_approval
- broker_action_allowed: false

## Replay evidence summary
- close_above_resistance: true
- target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- suggested_classification: confirmed_breakout

## Entry condition
- close_above_resistance replay supports a manual paper-review watch only; entry candidate price is 129.92.

## Target condition
- target_price: 131.82
- room_to_target: 1.90

## Invalidation condition
- invalidation_level: 126.34

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
