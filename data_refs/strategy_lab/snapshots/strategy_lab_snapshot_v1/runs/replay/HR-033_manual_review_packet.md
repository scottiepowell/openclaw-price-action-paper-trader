# HR-033 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-033
- related_candidate_id: PTC-033
- symbol: NVDA
- date_window: 2023-12-19 to 2023-12-19
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/NVDA/1Day/NVDA_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/NVDA/5Min/NVDA_5Min_2023.parquet

## 1D context rows
- 2023-12-14T05:00:00+00:00 | O:483.6 H:486.66 L:474.31 C:483.5 V:532517 T:9713 VWAP:481.053413
- 2023-12-15T05:00:00+00:00 | O:482.86 H:494.02 L:481.25 C:489.17 V:432889 T:7684 VWAP:489.67182
- 2023-12-18T05:00:00+00:00 | O:493.91 H:504.21 L:491.66 C:500.76 V:436298 T:8518 VWAP:499.301185
- 2023-12-19T05:00:00+00:00 | O:494.21 H:497.0 L:489.0 C:495.97 V:969126 T:15191 VWAP:493.015785

## 5m breakdown context
- prior_support: 500.66
- breakdown candle: 2023-12-19T14:30:00+00:00 | close: 493.00
- breakdown_amount: 7.66

## 5m bars around the breakdown
- 2023-12-18T20:00:00+00:00 | O:502.06 H:502.44 L:501.71 C:502.38 V:3851 T:76 VWAP:502.008624
- 2023-12-18T20:05:00+00:00 | O:502.49 H:502.755 L:502.26 C:502.26 V:1279 T:34 VWAP:502.458182
- 2023-12-18T20:10:00+00:00 | O:502.32 H:502.65 L:502.04 C:502.65 V:1028 T:30 VWAP:502.363333
- 2023-12-18T20:15:00+00:00 | O:502.6 H:503.3 L:502.6 C:503.27 V:4848 T:123 VWAP:502.964064
- 2023-12-18T20:20:00+00:00 | O:503.175 H:503.67 L:503.14 C:503.61 V:4981 T:120 VWAP:503.480025
- 2023-12-18T20:25:00+00:00 | O:503.45 H:503.99 L:503.41 C:503.98 V:8644 T:127 VWAP:503.812355
- 2023-12-18T20:30:00+00:00 | O:503.985 H:504.21 L:503.31 C:503.32 V:7821 T:104 VWAP:503.90389
- 2023-12-18T20:35:00+00:00 | O:503.41 H:503.44 L:502.245 C:502.385 V:7669 T:128 VWAP:502.961667
- 2023-12-18T20:40:00+00:00 | O:502.705 H:502.94 L:501.93 C:502.455 V:11205 T:193 VWAP:502.353784
- 2023-12-18T20:45:00+00:00 | O:502.25 H:502.25 L:501.36 C:502.14 V:8860 T:161 VWAP:501.753238
- 2023-12-18T20:50:00+00:00 | O:502.1 H:503.05 L:502.0 C:502.85 V:21023 T:302 VWAP:502.666344
- 2023-12-18T20:55:00+00:00 | O:502.85 H:502.85 L:500.66 C:500.76 V:38957 T:564 VWAP:502.007268
- 2023-12-19T14:30:00+00:00 | O:494.21 H:497.0 L:490.5 C:493.0 V:118728 T:1285 VWAP:493.609828
- 2023-12-19T14:35:00+00:00 | O:493.07 H:495.59 L:492.28 C:494.6 V:29603 T:450 VWAP:493.583523
- 2023-12-19T14:40:00+00:00 | O:494.57 H:495.0 L:493.31 C:493.71 V:47785 T:584 VWAP:493.885471
- 2023-12-19T14:45:00+00:00 | O:493.76 H:493.76 L:489.0 C:489.66 V:75805 T:891 VWAP:491.151719
- 2023-12-19T14:50:00+00:00 | O:489.26 H:492.18 L:489.16 C:492.0 V:33640 T:600 VWAP:490.631411
- 2023-12-19T14:55:00+00:00 | O:492.0 H:493.035 L:491.13 C:492.495 V:34760 T:398 VWAP:492.268283
- 2023-12-19T15:00:00+00:00 | O:492.62 H:493.59 L:492.01 C:493.08 V:12350 T:174 VWAP:492.969302
- 2023-12-19T15:05:00+00:00 | O:492.88 H:493.84 L:492.64 C:492.88 V:7182 T:136 VWAP:493.304664
- 2023-12-19T15:10:00+00:00 | O:492.75 H:494.75 L:492.69 C:494.705 V:12318 T:168 VWAP:493.417962
- 2023-12-19T15:15:00+00:00 | O:494.515 H:494.87 L:493.725 C:494.395 V:19732 T:216 VWAP:494.325617
- 2023-12-19T15:20:00+00:00 | O:494.52 H:494.635 L:493.875 C:494.39 V:13759 T:160 VWAP:494.274725
- 2023-12-19T15:25:00+00:00 | O:494.07 H:495.47 L:494.07 C:495.47 V:19237 T:220 VWAP:495.042743
- 2023-12-19T15:30:00+00:00 | O:495.485 H:495.94 L:494.835 C:494.875 V:11707 T:150 VWAP:495.331243
- 2023-12-19T15:35:00+00:00 | O:494.9 H:494.9 L:491.92 C:491.92 V:21091 T:286 VWAP:493.756557
- 2023-12-19T15:40:00+00:00 | O:492.0 H:492.43 L:491.26 C:492.0 V:22214 T:343 VWAP:492.001825
- 2023-12-19T15:45:00+00:00 | O:492.08 H:492.13 L:489.355 C:491.51 V:25509 T:416 VWAP:490.388292
- 2023-12-19T15:50:00+00:00 | O:491.71 H:492.4 L:491.71 C:492.4 V:12676 T:216 VWAP:492.064482
- 2023-12-19T15:55:00+00:00 | O:492.43 H:493.03 L:492.06 C:492.95 V:10901 T:156 VWAP:492.492885
- 2023-12-19T16:00:00+00:00 | O:492.76 H:492.76 L:491.38 C:492.685 V:10722 T:193 VWAP:492.211412
- 2023-12-19T16:05:00+00:00 | O:492.81 H:492.81 L:492.06 C:492.065 V:12386 T:171 VWAP:492.269632
- 2023-12-19T16:10:00+00:00 | O:492.065 H:492.07 L:490.87 C:491.0 V:16653 T:249 VWAP:491.318045
- 2023-12-19T16:15:00+00:00 | O:490.98 H:491.71 L:490.98 C:491.445 V:6388 T:104 VWAP:491.444561
- 2023-12-19T16:20:00+00:00 | O:491.48 H:491.51 L:490.03 C:490.3 V:18281 T:291 VWAP:490.688762
- 2023-12-19T16:25:00+00:00 | O:490.18 H:491.37 L:490.18 C:491.29 V:11899 T:230 VWAP:490.862075
- 2023-12-19T16:30:00+00:00 | O:491.37 H:492.05 L:491.3 C:491.78 V:5667 T:128 VWAP:491.846956

## Downside follow-through rows
- min_low_next_6_bars: 489.00
- min_low_next_12_bars: 489.00
- min_low_next_24_bars: 489.00
- close_after_6_bars: 493.08
- close_after_12_bars: 494.88
- close_after_24_bars: 491.78

## Candidate chart-level worksheet
- proposed support_level: 500.66
- proposed resistance_level: 508.32
- proposed target_price: 485.34
- proposed invalidation_level: 508.32
- entry_candidate_price: 493.00
- target_distance: 15.32
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: false
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 489.00
- max_close_after_confirmation: 495.47
- suggested_classification: confirmed_breakdown_no_target_hit

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
