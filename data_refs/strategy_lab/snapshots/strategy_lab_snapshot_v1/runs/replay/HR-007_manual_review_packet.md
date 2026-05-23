# HR-007 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-007
- related_candidate_id: PTC-007
- symbol: META
- date_window: 2023-05-16 to 2023-05-16
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/META_1Day_sample.csv
  - data_refs/google_drive/META_5Min_sample.csv

## 1D context rows
- 2023-05-15 04:00:00+00:00 | O:236.89 H:240.21 L:235.39 C:238.89 V:410409 T:5892 VWAP:238.707766
- 2023-05-16 04:00:00+00:00 | O:235.63 H:239.635 L:235.56 C:238.82 V:222830 T:4051 VWAP:237.993448

## 5m breakdown context
- prior_support: 238.15
- breakdown candle: 2023-05-16 13:25:00+00:00 | close: 235.73
- breakdown_amount: 2.42

## 5m bars around the breakdown
- 2023-05-15 19:00:00+00:00 | O:238.615 H:238.98 L:238.15 C:238.98 V:3003 T:61 VWAP:238.606154
- 2023-05-15 19:05:00+00:00 | O:239.04 H:239.36 L:239.04 C:239.36 V:2174 T:47 VWAP:239.120022
- 2023-05-15 19:10:00+00:00 | O:239.39 H:239.5 L:239.22 C:239.22 V:3662 T:60 VWAP:239.341442
- 2023-05-15 19:15:00+00:00 | O:239.13 H:239.16 L:239.02 C:239.14 V:940 T:22 VWAP:239.0925
- 2023-05-15 19:20:00+00:00 | O:239.12 H:239.13 L:239.035 C:239.07 V:2888 T:42 VWAP:239.084318
- 2023-05-15 19:25:00+00:00 | O:239.05 H:239.1 L:239.01 C:239.1 V:3282 T:55 VWAP:239.046981
- 2023-05-15 19:30:00+00:00 | O:239.22 H:239.4 L:239.215 C:239.22 V:3890 T:75 VWAP:239.313113
- 2023-05-15 19:35:00+00:00 | O:239.235 H:239.25 L:239.09 C:239.18 V:3818 T:66 VWAP:239.174315
- 2023-05-15 19:40:00+00:00 | O:239.08 H:239.31 L:239.08 C:239.19 V:3523 T:73 VWAP:239.239389
- 2023-05-15 19:45:00+00:00 | O:239.25 H:239.25 L:238.65 C:238.81 V:7317 T:133 VWAP:238.894862
- 2023-05-15 19:50:00+00:00 | O:238.86 H:239.11 L:238.69 C:238.83 V:12557 T:177 VWAP:238.866147
- 2023-05-15 19:55:00+00:00 | O:238.81 H:238.89 L:238.62 C:238.89 V:24140 T:334 VWAP:238.700708
- 2023-05-16 13:25:00+00:00 | O:235.57 H:235.93 L:235.57 C:235.73 V:1328 T:36 VWAP:235.800175
- 2023-05-16 13:30:00+00:00 | O:235.63 H:236.925 L:235.56 C:236.24 V:14404 T:211 VWAP:236.487473
- 2023-05-16 13:35:00+00:00 | O:236.06 H:236.615 L:236.06 C:236.34 V:16100 T:144 VWAP:236.351466
- 2023-05-16 13:40:00+00:00 | O:236.26 H:237.7 L:236.21 C:237.7 V:8130 T:127 VWAP:236.962255
- 2023-05-16 13:45:00+00:00 | O:237.84 H:238.555 L:237.84 C:238.24 V:4488 T:77 VWAP:238.198869
- 2023-05-16 13:50:00+00:00 | O:237.79 H:237.79 L:236.95 C:236.95 V:1266 T:31 VWAP:237.445556
- 2023-05-16 13:55:00+00:00 | O:237.17 H:237.73 L:237.17 C:237.35 V:2369 T:41 VWAP:237.459688
- 2023-05-16 14:00:00+00:00 | O:237.54 H:237.78 L:237.12 C:237.78 V:2125 T:36 VWAP:237.41
- 2023-05-16 14:05:00+00:00 | O:237.79 H:238.17 L:237.77 C:237.77 V:2195 T:42 VWAP:237.974906
- 2023-05-16 14:10:00+00:00 | O:237.21 H:237.22 L:236.8 C:236.91 V:1579 T:42 VWAP:237.038182
- 2023-05-16 14:15:00+00:00 | O:236.815 H:237.52 L:236.815 C:237.48 V:1765 T:49 VWAP:237.254231
- 2023-05-16 14:20:00+00:00 | O:237.5 H:237.5 L:236.99 C:237.255 V:6357 T:92 VWAP:237.153149
- 2023-05-16 14:25:00+00:00 | O:237.145 H:237.87 L:237.09 C:237.86 V:10578 T:126 VWAP:237.517082
- 2023-05-16 14:30:00+00:00 | O:237.865 H:238.105 L:237.63 C:237.77 V:7741 T:104 VWAP:237.935145
- 2023-05-16 14:35:00+00:00 | O:237.5 H:237.6 L:237.31 C:237.31 V:639 T:18 VWAP:237.48
- 2023-05-16 14:40:00+00:00 | O:237.32 H:237.32 L:237.0 C:237.18 V:1580 T:42 VWAP:237.144583
- 2023-05-16 14:45:00+00:00 | O:237.21 H:237.625 L:237.21 C:237.625 V:701 T:22 VWAP:237.38
- 2023-05-16 14:50:00+00:00 | O:237.51 H:237.83 L:237.5 C:237.63 V:2812 T:49 VWAP:237.70381
- 2023-05-16 14:55:00+00:00 | O:237.82 H:238.265 L:237.81 C:238.08 V:2658 T:38 VWAP:238.084406
- 2023-05-16 15:00:00+00:00 | O:238.14 H:238.19 L:237.39 C:237.63 V:3236 T:68 VWAP:237.729015
- 2023-05-16 15:05:00+00:00 | O:237.66 H:237.85 L:237.66 C:237.8 V:926 T:23 VWAP:237.788333
- 2023-05-16 15:10:00+00:00 | O:237.81 H:238.05 L:237.81 C:237.97 V:2778 T:52 VWAP:237.919286
- 2023-05-16 15:15:00+00:00 | O:237.95 H:237.97 L:237.73 C:237.95 V:3104 T:33 VWAP:237.892857
- 2023-05-16 15:20:00+00:00 | O:237.95 H:237.99 L:237.855 C:237.99 V:1422 T:26 VWAP:237.937678
- 2023-05-16 15:25:00+00:00 | O:238.13 H:238.4 L:238.05 C:238.4 V:3214 T:46 VWAP:238.141129

## Downside follow-through rows
- min_low_next_6_bars: 235.56
- min_low_next_12_bars: 235.56
- min_low_next_24_bars: 235.56
- close_after_6_bars: 237.35
- close_after_12_bars: 237.86
- close_after_24_bars: 238.40

## Candidate chart-level worksheet
- proposed support_level: 238.15
- proposed resistance_level: 240.57
- proposed target_price: 233.31
- proposed invalidation_level: 240.57
- entry_candidate_price: 235.73
- target_distance: 4.84
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: false
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 235.56
- max_close_after_confirmation: 238.40
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
