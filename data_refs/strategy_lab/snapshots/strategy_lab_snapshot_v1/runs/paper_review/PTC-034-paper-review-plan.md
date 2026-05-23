# PTC-034 Paper Review Plan

- replay_id: HR-034
- symbol: AVGO
- side: bearish
- paper_review_status: pending_human_approval
- broker_action_allowed: false

## Replay evidence summary
- prior_support: 1141.66
- breakdown_amount: 2.25
- close_below_support: true
- invalidation_hit_after_confirmation: false
- suggested_classification: confirmed_breakdown

## Entry condition
- close_below_support replay supports a manual paper-review watch only; entry candidate price is 1139.41.

## Target condition
- target_price: 1137.16
- room_to_target: 4.50

## Invalidation condition
- invalidation_level: 1143.91

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
