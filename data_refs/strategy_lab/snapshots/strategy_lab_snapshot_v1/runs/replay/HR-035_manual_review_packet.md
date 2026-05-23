# HR-035 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-035
- related_candidate_id: PTC-035
- symbol: META
- date_window: 2023-12-28 to 2023-12-28
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/META/1Day/META_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/META/5Min/META_5Min_2023.parquet

## 1D context rows
- 2023-12-22T05:00:00+00:00 | O:356.13 H:357.12 L:351.35 C:353.39 V:193094 T:3822 VWAP:353.698088
- 2023-12-26T05:00:00+00:00 | O:354.95 H:356.78 L:353.53 C:354.86 V:93656 T:2603 VWAP:355.013472
- 2023-12-27T05:00:00+00:00 | O:356.08 H:358.94 L:355.41 C:357.86 V:132428 T:2854 VWAP:357.412757
- 2023-12-28T05:00:00+00:00 | O:359.69 H:361.865 L:357.905 C:358.41 V:232396 T:6749 VWAP:359.908358

## 5m breakdown context
- prior_support: 360.58
- breakdown candle: 2023-12-28T19:50:00+00:00 | close: 360.19
- breakdown_amount: 0.39

## 5m bars around the breakdown
- 2023-12-28T18:50:00+00:00 | O:360.885 H:361.27 L:360.885 C:361.27 V:701 T:28 VWAP:361.10875
- 2023-12-28T18:55:00+00:00 | O:360.86 H:361.08 L:360.86 C:361.08 V:956 T:41 VWAP:360.97625
- 2023-12-28T19:00:00+00:00 | O:361.06 H:361.17 L:360.97 C:361.14 V:1402 T:62 VWAP:361.091667
- 2023-12-28T19:05:00+00:00 | O:361.11 H:361.11 L:360.91 C:360.91 V:395 T:17 VWAP:361.01
- 2023-12-28T19:10:00+00:00 | O:360.925 H:360.925 L:360.79 C:360.86 V:838 T:26 VWAP:360.852143
- 2023-12-28T19:15:00+00:00 | O:360.9 H:361.07 L:360.9 C:360.94 V:1590 T:64 VWAP:360.99875
- 2023-12-28T19:20:00+00:00 | O:360.97 H:360.97 L:360.97 C:360.97 V:271 T:19 VWAP:360.97
- 2023-12-28T19:25:00+00:00 | O:361.05 H:361.15 L:361.05 C:361.06 V:1552 T:58 VWAP:361.086667
- 2023-12-28T19:30:00+00:00 | O:361.09 H:361.09 L:360.885 C:360.92 V:1005 T:45 VWAP:360.98625
- 2023-12-28T19:35:00+00:00 | O:360.86 H:360.98 L:360.825 C:360.84 V:1735 T:58 VWAP:360.903571
- 2023-12-28T19:40:00+00:00 | O:360.76 H:360.86 L:360.76 C:360.86 V:1357 T:61 VWAP:360.795714
- 2023-12-28T19:45:00+00:00 | O:360.71 H:360.84 L:360.58 C:360.84 V:2034 T:78 VWAP:360.686462
- 2023-12-28T19:50:00+00:00 | O:360.43 H:360.43 L:360.19 C:360.19 V:1920 T:60 VWAP:360.31
- 2023-12-28T19:55:00+00:00 | O:360.18 H:360.26 L:360.11 C:360.16 V:2216 T:57 VWAP:360.175693
- 2023-12-28T20:00:00+00:00 | O:360.18 H:360.28 L:359.95 C:359.95 V:5626 T:148 VWAP:360.141765
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

## Downside follow-through rows
- min_low_next_6_bars: 359.13
- min_low_next_12_bars: 358.06
- min_low_next_24_bars: 355.77
- close_after_6_bars: 359.49
- close_after_12_bars: 358.06
- close_after_24_bars: 356.56

## Candidate chart-level worksheet
- proposed support_level: 360.58
- proposed resistance_level: 361.08
- proposed target_price: 359.58
- proposed invalidation_level: 361.58
- entry_candidate_price: 360.19
- target_distance: 1.00
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 355.77
- max_close_after_confirmation: 360.19
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
