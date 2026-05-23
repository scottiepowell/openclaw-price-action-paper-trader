# HR-016 through HR-019 Manual Review Decision Sheet

All cases remain `manual_review_status: pending` until explicitly approved.

| replay_id | symbol | side | date | setup type | support/resistance level | confirmation candle | target price | target_hit_after_confirmation | invalidation_hit_after_confirmation | suggested_classification | recommendation | reason |
|---|---|---|---|---|---:|---|---:|---|---|---|---|---|
| HR-016 | META | bullish | 2023-06-28 | close_above_resistance | 288.37 | 2023-06-28T14:35:00+00:00 @ 288.70 | 289.37 | true | true | ambiguous | ambiguous | target and invalidation both hit; needs manual judgment |
| HR-017 | SPY | bullish | 2023-08-09 | close_above_resistance | 446.37 | 2023-08-09T16:30:00+00:00 @ 446.56 | 447.37 | true | true | ambiguous | ambiguous | breakout followed by both target and invalidation conditions; unclear outcome |
| HR-018 | META | bearish | 2023-07-19 | close_below_support | 311.13 | 2023-07-19T13:30:00+00:00 @ 311.01 | 310.13 | false | true | failed_breakdown_reclaim | failed/reclaim | breakdown failed and support reclaimed immediately after confirmation |
| HR-019 | SPY | bearish | 2023-09-19 | close_below_support | 443.18 | 2023-09-19T13:30:00+00:00 @ 442.75 | 442.18 | true | false | confirmed_breakdown | confirm | clean breakdown with target hit and no invalidation after confirmation |

## Notes
- No Alpaca order submission.
- No broker APIs.
- No profitability claim.
- No automatic promotion.
- Broker action remains disabled.
