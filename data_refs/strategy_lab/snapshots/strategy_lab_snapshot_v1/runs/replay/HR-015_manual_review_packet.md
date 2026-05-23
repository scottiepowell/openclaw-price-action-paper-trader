# HR-015 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-015
- related_candidate_id: PTC-015
- symbol: META
- date_window: 2023-12-29 to 2023-12-29
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/1Day/META_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/5Min/META_5Min_2023.parquet

## 1D context rows
- 2023-12-26T05:00:00+00:00 | O:354.95 H:356.78 L:353.53 C:354.86 V:93656 T:2603 VWAP:355.013472
- 2023-12-27T05:00:00+00:00 | O:356.08 H:358.94 L:355.41 C:357.86 V:132428 T:2854 VWAP:357.412757
- 2023-12-28T05:00:00+00:00 | O:359.69 H:361.865 L:357.905 C:358.41 V:232396 T:6749 VWAP:359.908358
- 2023-12-29T05:00:00+00:00 | O:359.515 H:359.83 L:351.92 C:354.26 V:234530 T:5990 VWAP:354.372222

## 5m breakdown context
- prior_support: 357.90
- breakdown candle: 2023-12-29T14:35:00+00:00 | close: 356.55
- breakdown_amount: 1.36

## 5m bars around the breakdown
- 2023-12-28T20:05:00+00:00 | O:359.87 H:360.08 L:359.77 C:359.8 V:2277 T:75 VWAP:359.913825
- 2023-12-28T20:10:00+00:00 | O:359.74 H:359.8 L:359.13 C:359.44 V:4715 T:138 VWAP:359.492622
- 2023-12-28T20:15:00+00:00 | O:359.23 H:359.75 L:359.16 C:359.75 V:2228 T:72 VWAP:359.33125
- 2023-12-28T20:20:00+00:00 | O:359.7 H:359.77 L:359.44 C:359.49 V:4098 T:90 VWAP:359.628788
- 2023-12-28T20:25:00+00:00 | O:359.31 H:359.31 L:358.98 C:359.18 V:2869 T:77 VWAP:359.162663
- 2023-12-28T20:30:00+00:00 | O:359.275 H:359.275 L:358.65 C:358.65 V:6023 T:193 VWAP:359.020212
- 2023-12-28T20:35:00+00:00 | O:358.59 H:358.7 L:358.41 C:358.51 V:4392 T:163 VWAP:358.5248
- 2023-12-28T20:40:00+00:00 | O:358.57 H:358.87 L:358.47 C:358.84 V:2734 T:93 VWAP:358.59995
- 2023-12-28T20:45:00+00:00 | O:358.56 H:358.6 L:358.28 C:358.45 V:2456 T:99 VWAP:358.416176
- 2023-12-28T20:50:00+00:00 | O:358.43 H:358.53 L:358.06 C:358.06 V:5748 T:144 VWAP:358.316025
- 2023-12-28T20:55:00+00:00 | O:358.03 H:358.55 L:357.905 C:358.41 V:16421 T:387 VWAP:358.269822
- 2023-12-29T14:30:00+00:00 | O:359.515 H:359.83 L:358.66 C:358.665 V:1687 T:40 VWAP:359.433
- 2023-12-29T14:35:00+00:00 | O:357.55 H:357.55 L:356.035 C:356.545 V:6551 T:82 VWAP:356.542424
- 2023-12-29T14:40:00+00:00 | O:356.485 H:357.03 L:355.94 C:357.03 V:3948 T:94 VWAP:356.396351
- 2023-12-29T14:45:00+00:00 | O:357.18 H:357.18 L:356.22 C:356.74 V:4575 T:86 VWAP:356.801218
- 2023-12-29T14:50:00+00:00 | O:356.79 H:357.5 L:356.67 C:356.93 V:6331 T:102 VWAP:357.05153
- 2023-12-29T14:55:00+00:00 | O:356.77 H:357.16 L:356.73 C:356.86 V:5172 T:113 VWAP:356.98079
- 2023-12-29T15:00:00+00:00 | O:356.635 H:356.635 L:355.77 C:356.01 V:4682 T:129 VWAP:356.19443
- 2023-12-29T15:05:00+00:00 | O:356.12 H:358.195 L:356.06 C:357.88 V:3135 T:95 VWAP:357.282235
- 2023-12-29T15:10:00+00:00 | O:357.68 H:357.82 L:357.64 C:357.76 V:1133 T:43 VWAP:357.736667
- 2023-12-29T15:15:00+00:00 | O:357.64 H:357.68 L:357.43 C:357.445 V:661 T:28 VWAP:357.54875
- 2023-12-29T15:20:00+00:00 | O:357.19 H:357.19 L:356.52 C:356.56 V:1253 T:46 VWAP:356.855
- 2023-12-29T15:25:00+00:00 | O:356.52 H:357.4 L:356.505 C:357.09 V:2997 T:79 VWAP:356.835238
- 2023-12-29T15:30:00+00:00 | O:357.16 H:357.16 L:356.055 C:356.14 V:3993 T:99 VWAP:356.434678
- 2023-12-29T15:35:00+00:00 | O:356.13 H:356.39 L:355.93 C:356.38 V:1603 T:57 VWAP:356.2215
- 2023-12-29T15:40:00+00:00 | O:356.41 H:356.41 L:355.49 C:355.58 V:1515 T:52 VWAP:355.928259
- 2023-12-29T15:45:00+00:00 | O:355.77 H:355.87 L:354.81 C:354.81 V:5053 T:105 VWAP:355.312119
- 2023-12-29T15:50:00+00:00 | O:355.11 H:355.39 L:354.28 C:354.37 V:4602 T:110 VWAP:354.860799
- 2023-12-29T15:55:00+00:00 | O:354.45 H:354.83 L:354.39 C:354.66 V:3999 T:109 VWAP:354.636786
- 2023-12-29T16:00:00+00:00 | O:354.49 H:354.66 L:354.34 C:354.4 V:3906 T:85 VWAP:354.476842
- 2023-12-29T16:05:00+00:00 | O:354.52 H:354.59 L:352.89 C:353.315 V:4477 T:105 VWAP:353.440992
- 2023-12-29T16:10:00+00:00 | O:353.5 H:353.98 L:353.09 C:353.09 V:8641 T:219 VWAP:353.577811
- 2023-12-29T16:15:00+00:00 | O:353.05 H:353.23 L:352.46 C:353.01 V:6938 T:153 VWAP:352.867111
- 2023-12-29T16:20:00+00:00 | O:353.03 H:353.13 L:352.3 C:352.38 V:3780 T:122 VWAP:352.737006
- 2023-12-29T16:25:00+00:00 | O:352.43 H:352.58 L:352.21 C:352.365 V:7402 T:96 VWAP:352.334031
- 2023-12-29T16:30:00+00:00 | O:352.4 H:352.81 L:352.33 C:352.78 V:3607 T:60 VWAP:352.556935
- 2023-12-29T16:35:00+00:00 | O:352.79 H:352.83 L:352.42 C:352.44 V:2102 T:45 VWAP:352.665937

## Downside follow-through rows
- min_low_next_6_bars: 355.77
- min_low_next_12_bars: 355.77
- min_low_next_24_bars: 352.21
- close_after_6_bars: 357.88
- close_after_12_bars: 356.38
- close_after_24_bars: 352.44

## Candidate chart-level worksheet
- proposed support_level: 357.90
- proposed resistance_level: 359.26
- proposed target_price: 355.19
- proposed invalidation_level: 359.26
- entry_candidate_price: 356.55
- target_distance: 2.72
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 352.21
- max_close_after_confirmation: 357.88
- suggested_classification: confirmed_breakdown

## Manual promotion workflow
- manual_review_status: pending
- manual_review_outcome: TBD
- manual_review_classification: TBD
- manual_reviewer_notes: TBD
- broker_action_allowed: false

## Recommended classification options
- confirmed_breakdown
- confirmed_breakdown_no_target_hit
- support_touch_no_trigger
- failed_breakdown_reclaim
- ambiguous
- insufficient
- contradicted
- blocked_data_quality

## Boundary
- No trade signal
- No profitability claim
- No execution readiness
- No broker action allowed
