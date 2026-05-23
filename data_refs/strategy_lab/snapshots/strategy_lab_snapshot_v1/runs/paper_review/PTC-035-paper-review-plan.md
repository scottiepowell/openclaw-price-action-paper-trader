# PTC-035 Paper Review Plan

- replay_id: HR-035
- symbol: META
- side: bearish
- paper_review_status: pending_human_approval
- broker_action_allowed: false

## Replay evidence summary
- prior_support: 360.58
- breakdown_amount: 0.39
- close_below_support: true
- invalidation_hit_after_confirmation: false
- suggested_classification: confirmed_breakdown

## Entry condition
- close_below_support replay supports a manual paper-review watch only; entry candidate price is 360.19.

## Target condition
- target_price: 359.58
- room_to_target: 1.00

## Invalidation condition
- invalidation_level: 361.58

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
