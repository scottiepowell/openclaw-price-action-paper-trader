# HR-034 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-034
- related_candidate_id: PTC-034
- symbol: AVGO
- date_window: 2023-12-19 to 2023-12-19
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AVGO/1Day/AVGO_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AVGO/5Min/AVGO_5Min_2023.parquet

## 1D context rows
- 2023-12-14T05:00:00+00:00 | O:1092.9 H:1121.03 L:1091.665 C:1106.05 V:144792 T:5451 VWAP:1108.938094
- 2023-12-15T05:00:00+00:00 | O:1096.86 H:1149.65 L:1096.86 C:1128.93 V:174277 T:5781 VWAP:1135.325172
- 2023-12-18T05:00:00+00:00 | O:1120.08 H:1151.195 L:1119.305 C:1147.12 V:136113 T:5128 VWAP:1137.643917
- 2023-12-19T05:00:00+00:00 | O:1141.69 H:1149.91 L:1133.17 C:1139.98 V:83996 T:3759 VWAP:1140.864254

## 5m breakdown context
- prior_support: 1141.66
- breakdown candle: 2023-12-19T20:35:00+00:00 | close: 1139.41
- breakdown_amount: 2.25

## 5m bars around the breakdown
- 2023-12-19T19:35:00+00:00 | O:1146.335 H:1146.335 L:1146.335 C:1146.335 V:153 T:5 VWAP:1146.335
- 2023-12-19T19:40:00+00:00 | O:1144.58 H:1144.84 L:1144.58 C:1144.59 V:663 T:21 VWAP:1144.683
- 2023-12-19T19:45:00+00:00 | O:1144.1 H:1144.1 L:1144.1 C:1144.1 V:523 T:14 VWAP:1144.1
- 2023-12-19T19:50:00+00:00 | O:1143.41 H:1145.01 L:1143.41 C:1144.77 V:1045 T:44 VWAP:1144.3525
- 2023-12-19T19:55:00+00:00 | O:1144.855 H:1144.855 L:1144.855 C:1144.855 V:138 T:8 VWAP:1144.855
- 2023-12-19T20:00:00+00:00 | O:1144.68 H:1144.68 L:1143.66 C:1143.66 V:599 T:36 VWAP:1144.23
- 2023-12-19T20:05:00+00:00 | O:1142.73 H:1143.07 L:1141.66 C:1142.34 V:4229 T:105 VWAP:1142.358638
- 2023-12-19T20:10:00+00:00 | O:1143.58 H:1143.85 L:1143.58 C:1143.74 V:654 T:16 VWAP:1143.705
- 2023-12-19T20:15:00+00:00 | O:1144.64 H:1144.64 L:1144.64 C:1144.64 V:154 T:6 VWAP:1144.64
- 2023-12-19T20:20:00+00:00 | O:1144.23 H:1144.23 L:1144.23 C:1144.23 V:358 T:10 VWAP:1144.23
- 2023-12-19T20:25:00+00:00 | O:1143.22 H:1143.22 L:1142.62 C:1143.0 V:779 T:36 VWAP:1143.0
- 2023-12-19T20:30:00+00:00 | O:1141.7 H:1141.9 L:1141.7 C:1141.9 V:272 T:10 VWAP:1141.8
- 2023-12-19T20:35:00+00:00 | O:1141.55 H:1141.55 L:1139.41 C:1139.41 V:1682 T:59 VWAP:1140.792273
- 2023-12-19T20:40:00+00:00 | O:1139.69 H:1139.69 L:1136.475 C:1136.475 V:1400 T:63 VWAP:1138.65
- 2023-12-19T20:45:00+00:00 | O:1135.91 H:1136.2 L:1133.17 C:1133.36 V:4249 T:115 VWAP:1134.38174
- 2023-12-19T20:50:00+00:00 | O:1135.01 H:1136.91 L:1135.01 C:1136.08 V:3425 T:115 VWAP:1136.157868
- 2023-12-19T20:55:00+00:00 | O:1137.68 H:1140.0 L:1137.68 C:1139.98 V:7253 T:263 VWAP:1138.849478
- 2023-12-20T14:30:00+00:00 | O:1131.19 H:1137.99 L:1128.545 C:1135.91 V:7231 T:153 VWAP:1132.690491
- 2023-12-20T14:35:00+00:00 | O:1135.255 H:1136.23 L:1131.84 C:1132.96 V:1718 T:32 VWAP:1134.194167
- 2023-12-20T14:40:00+00:00 | O:1136.78 H:1141.36 L:1136.78 C:1139.66 V:2900 T:54 VWAP:1140.05384
- 2023-12-20T14:45:00+00:00 | O:1136.395 H:1136.67 L:1134.3 C:1134.3 V:1383 T:49 VWAP:1135.996
- 2023-12-20T14:50:00+00:00 | O:1135.765 H:1135.765 L:1135.765 C:1135.765 V:102 T:2 VWAP:1135.765
- 2023-12-20T14:55:00+00:00 | O:1135.59 H:1135.66 L:1132.98 C:1133.815 V:904 T:33 VWAP:1134.437176
- 2023-12-20T15:00:00+00:00 | O:1134.775 H:1136.345 L:1134.775 C:1135.985 V:1318 T:32 VWAP:1135.591924
- 2023-12-20T15:05:00+00:00 | O:1135.83 H:1135.83 L:1134.385 C:1135.12 V:1160 T:37 VWAP:1135.147367
- 2023-12-20T15:10:00+00:00 | O:1133.47 H:1135.0 L:1133.11 C:1135.0 V:1841 T:63 VWAP:1134.037285
- 2023-12-20T15:15:00+00:00 | O:1135.23 H:1135.825 L:1135.23 C:1135.825 V:234 T:7 VWAP:1135.5275
- 2023-12-20T15:20:00+00:00 | O:1134.64 H:1135.5 L:1134.64 C:1135.5 V:1085 T:32 VWAP:1135.09
- 2023-12-20T15:25:00+00:00 | O:1135.525 H:1137.4 L:1134.66 C:1137.4 V:1150 T:31 VWAP:1136.448454
- 2023-12-20T15:30:00+00:00 | O:1137.525 H:1137.78 L:1136.89 C:1136.89 V:667 T:20 VWAP:1137.398333
- 2023-12-20T15:35:00+00:00 | O:1136.18 H:1136.18 L:1135.265 C:1135.265 V:377 T:11 VWAP:1135.57
- 2023-12-20T15:40:00+00:00 | O:1135.52 H:1136.68 L:1135.52 C:1136.68 V:1113 T:31 VWAP:1136.351875
- 2023-12-20T15:45:00+00:00 | O:1135.81 H:1135.81 L:1134.66 C:1135.23 V:1008 T:27 VWAP:1135.027
- 2023-12-20T15:50:00+00:00 | O:1136.3 H:1136.3 L:1134.04 C:1134.04 V:336 T:8 VWAP:1135.17
- 2023-12-20T15:55:00+00:00 | O:1133.92 H:1134.2 L:1133.92 C:1134.2 V:242 T:15 VWAP:1134.06
- 2023-12-20T16:00:00+00:00 | O:1134.68 H:1135.6 L:1134.68 C:1135.23 V:1546 T:50 VWAP:1135.126196
- 2023-12-20T16:10:00+00:00 | O:1133.62 H:1133.62 L:1132.9 C:1132.9 V:617 T:13 VWAP:1133.44

## Downside follow-through rows
- min_low_next_6_bars: 1128.55
- min_low_next_12_bars: 1128.55
- min_low_next_24_bars: 1128.55
- close_after_6_bars: 1132.96
- close_after_12_bars: 1135.12
- close_after_24_bars: 1132.90

## Candidate chart-level worksheet
- proposed support_level: 1141.66
- proposed resistance_level: 1143.91
- proposed target_price: 1137.16
- proposed invalidation_level: 1143.91
- entry_candidate_price: 1139.41
- target_distance: 4.50
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 1128.55
- max_close_after_confirmation: 1139.98
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
