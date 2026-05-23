# HR-006 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-006
- related_candidate_id: PTC-006
- symbol: MSFT
- date_window: 2023-05-16 to 2023-05-16
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/MSFT_1Day_sample.csv
  - data_refs/google_drive/MSFT_5Min_sample.csv

## 1D context rows
- 2023-05-15 04:00:00+00:00 | O:309.02 H:309.86 L:307.625 C:309.51 V:234575 T:4240 VWAP:308.904982
- 2023-05-16 04:00:00+00:00 | O:309.91 H:313.675 L:309.89 C:311.745 V:451351 T:7294 VWAP:312.632646

## 5m breakout context
- prior_resistance: 309.60
- breakout candle: 2023-05-16 13:30:00+00:00 | close: 312.53
- breakout_amount: 2.93

## 5m bars around the breakout
- 2023-05-15 19:00:00+00:00 | O:308.97 H:309.2 L:308.95 C:309.1 V:2344 T:65 VWAP:309.041875
- 2023-05-15 19:05:00+00:00 | O:308.895 H:309.205 L:308.895 C:309.205 V:1537 T:35 VWAP:309.042917
- 2023-05-15 19:10:00+00:00 | O:309.155 H:309.545 L:309.155 C:309.36 V:5183 T:86 VWAP:309.314735
- 2023-05-15 19:15:00+00:00 | O:309.22 H:309.25 L:309.14 C:309.21 V:1424 T:34 VWAP:309.193182
- 2023-05-15 19:20:00+00:00 | O:309.44 H:309.495 L:309.425 C:309.495 V:938 T:30 VWAP:309.457143
- 2023-05-15 19:25:00+00:00 | O:309.41 H:309.455 L:309.4 C:309.41 V:776 T:33 VWAP:309.415833
- 2023-05-15 19:30:00+00:00 | O:309.38 H:309.595 L:309.295 C:309.565 V:1739 T:48 VWAP:309.428462
- 2023-05-15 19:35:00+00:00 | O:309.35 H:309.395 L:309.245 C:309.245 V:1116 T:34 VWAP:309.338571
- 2023-05-15 19:40:00+00:00 | O:309.325 H:309.395 L:308.99 C:308.99 V:1749 T:71 VWAP:309.135357
- 2023-05-15 19:45:00+00:00 | O:309.06 H:309.24 L:309.06 C:309.22 V:2402 T:93 VWAP:309.164063
- 2023-05-15 19:50:00+00:00 | O:309.2 H:309.435 L:309.16 C:309.16 V:5549 T:110 VWAP:309.332663
- 2023-05-15 19:55:00+00:00 | O:309.09 H:309.51 L:309.015 C:309.51 V:26781 T:378 VWAP:309.269149
- 2023-05-16 13:30:00+00:00 | O:309.91 H:312.53 L:309.89 C:312.53 V:14562 T:305 VWAP:311.401575
- 2023-05-16 13:35:00+00:00 | O:312.61 H:312.63 L:312.04 C:312.07 V:13536 T:172 VWAP:312.392327
- 2023-05-16 13:40:00+00:00 | O:312.11 H:312.58 L:311.905 C:312.495 V:8073 T:104 VWAP:312.303435
- 2023-05-16 13:45:00+00:00 | O:312.58 H:313.67 L:312.58 C:313.195 V:14551 T:209 VWAP:313.06439
- 2023-05-16 13:50:00+00:00 | O:313.07 H:313.18 L:312.31 C:313.11 V:11365 T:166 VWAP:312.885473
- 2023-05-16 13:55:00+00:00 | O:312.94 H:313.025 L:312.235 C:312.235 V:5624 T:103 VWAP:312.573403
- 2023-05-16 14:00:00+00:00 | O:312.115 H:312.295 L:311.455 C:311.68 V:9496 T:142 VWAP:311.819936
- 2023-05-16 14:05:00+00:00 | O:311.73 H:311.99 L:311.53 C:311.585 V:8328 T:88 VWAP:311.717202
- 2023-05-16 14:10:00+00:00 | O:311.68 H:311.68 L:311.13 C:311.61 V:7855 T:131 VWAP:311.5025
- 2023-05-16 14:15:00+00:00 | O:311.505 H:312.2 L:311.36 C:312.09 V:6950 T:130 VWAP:311.865696
- 2023-05-16 14:20:00+00:00 | O:312.07 H:312.59 L:312.07 C:312.41 V:9014 T:133 VWAP:312.28597
- 2023-05-16 14:25:00+00:00 | O:312.37 H:312.625 L:312.05 C:312.22 V:4734 T:89 VWAP:312.306714
- 2023-05-16 14:30:00+00:00 | O:312.335 H:312.335 L:311.93 C:312.03 V:7701 T:114 VWAP:312.114839
- 2023-05-16 14:35:00+00:00 | O:312.11 H:312.26 L:312.03 C:312.085 V:3773 T:69 VWAP:312.095598
- 2023-05-16 14:40:00+00:00 | O:312.025 H:312.37 L:312.025 C:312.25 V:3254 T:53 VWAP:312.127503
- 2023-05-16 14:45:00+00:00 | O:312.335 H:312.335 L:312.05 C:312.105 V:6625 T:70 VWAP:312.172123
- 2023-05-16 14:50:00+00:00 | O:312.09 H:312.31 L:311.97 C:312.3 V:5682 T:103 VWAP:312.120867
- 2023-05-16 14:55:00+00:00 | O:312.33 H:313.24 L:312.33 C:312.74 V:7376 T:117 VWAP:312.97486
- 2023-05-16 15:00:00+00:00 | O:312.82 H:313.165 L:312.64 C:313.165 V:2948 T:45 VWAP:312.912934
- 2023-05-16 15:05:00+00:00 | O:313.13 H:313.54 L:312.89 C:313.34 V:6889 T:74 VWAP:313.238216
- 2023-05-16 15:10:00+00:00 | O:313.185 H:313.19 L:312.705 C:312.705 V:6400 T:138 VWAP:313.00004
- 2023-05-16 15:15:00+00:00 | O:312.46 H:312.71 L:312.22 C:312.69 V:4737 T:85 VWAP:312.443076
- 2023-05-16 15:20:00+00:00 | O:312.89 H:313.32 L:312.85 C:313.22 V:3735 T:68 VWAP:313.101621
- 2023-05-16 15:25:00+00:00 | O:313.075 H:313.4 L:313.01 C:313.385 V:2163 T:72 VWAP:313.202279
- 2023-05-16 15:30:00+00:00 | O:313.48 H:313.48 L:312.77 C:312.82 V:4407 T:63 VWAP:313.050657

## Follow-through rows
- max_high_next_6_bars: 313.67
- max_high_next_12_bars: 313.67
- max_high_next_24_bars: 313.67
- close_after_6_bars: 311.68
- close_after_12_bars: 312.03
- close_after_24_bars: 312.82

## Candidate chart-level worksheet
- proposed support_level: 306.66
- proposed resistance_level: 309.60
- proposed target_price: 315.46
- proposed invalidation_level: 306.66
- entry_candidate_price: 312.53
- room_to_target: 5.87
- target_distance: 5.86
- max_favorable_move: 4.07
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- resistance_touched: true
- close_above_resistance: true
- target_hit_before_confirmation: false
- target_hit_after_confirmation: false
- invalidation_hit_before_confirmation: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: 313.67
- max_close_after_confirmation: 313.39
- suggested_classification: confirmed_breakout_no_target_hit

## Manual promotion workflow
- manual_review_status: pending
- manual_review_outcome: TBD
- manual_review_classification: TBD
- manual_reviewer_notes: TBD
- broker_action_allowed: false

## Boundary
- No trade signal
- No profitability claim
- No execution readiness
- No broker action allowed

## Status
- Not verified
