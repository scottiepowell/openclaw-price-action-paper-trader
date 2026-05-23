# HR-005 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-005
- related_candidate_id: PTC-005
- symbol: AVGO
- date_window: 2023-05-18 to 2023-05-18
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/AVGO_1Day_sample.csv
  - data_refs/google_drive/AVGO_5Min_sample.csv

## 1D context rows
- 2023-05-15 04:00:00+00:00 | O:631.88 H:639.99 L:628.82 C:639.4 V:51171 T:1854 VWAP:636.673785
- 2023-05-16 04:00:00+00:00 | O:639.82 H:646.73 L:639.28 C:641.5 V:62869 T:2227 VWAP:643.857397
- 2023-05-17 04:00:00+00:00 | O:647.45 H:660.83 L:645.01 C:656.905 V:108694 T:3131 VWAP:656.054785
- 2023-05-18 04:00:00+00:00 | O:656.22 H:679.27 L:656.22 C:677.81 V:130911 T:3272 VWAP:671.113733

## 5m breakout context
- prior_resistance: 659.77
- breakout candle: 2023-05-18 13:35:00+00:00 | close: 662.17
- breakout_amount: 2.40

## 5m bars around the breakout
- 2023-05-17 19:05:00+00:00 | O:658.9 H:659.44 L:658.9 C:659.44 V:1403 T:42 VWAP:659.275417
- 2023-05-17 19:10:00+00:00 | O:659.26 H:659.28 L:659.16 C:659.24 V:863 T:24 VWAP:659.225
- 2023-05-17 19:15:00+00:00 | O:659.29 H:659.46 L:659.13 C:659.13 V:1742 T:41 VWAP:659.322308
- 2023-05-17 19:20:00+00:00 | O:658.84 H:659.09 L:658.495 C:658.5 V:1574 T:42 VWAP:658.794231
- 2023-05-17 19:25:00+00:00 | O:658.41 H:658.75 L:658.23 C:658.23 V:2392 T:49 VWAP:658.459714
- 2023-05-17 19:30:00+00:00 | O:658.42 H:658.42 L:657.79 C:657.79 V:1423 T:35 VWAP:658.293846
- 2023-05-17 19:35:00+00:00 | O:657.935 H:657.935 L:657.1 C:657.215 V:3637 T:77 VWAP:657.524074
- 2023-05-17 19:40:00+00:00 | O:657.23 H:658.33 L:657.23 C:658.12 V:3473 T:76 VWAP:658.027999
- 2023-05-17 19:45:00+00:00 | O:658.32 H:658.5 L:657.62 C:657.62 V:4823 T:73 VWAP:658.10962
- 2023-05-17 19:50:00+00:00 | O:657.575 H:657.92 L:657.07 C:657.7 V:5314 T:133 VWAP:657.554566
- 2023-05-17 19:55:00+00:00 | O:657.86 H:658.11 L:656.64 C:656.905 V:6922 T:231 VWAP:657.383438
- 2023-05-18 13:30:00+00:00 | O:656.22 H:659.77 L:656.22 C:659.65 V:1228 T:18 VWAP:658.804545
- 2023-05-18 13:35:00+00:00 | O:659.955 H:662.175 L:659.87 C:662.175 V:985 T:13 VWAP:660.539063
- 2023-05-18 13:40:00+00:00 | O:662.0 H:662.0 L:660.14 C:661.02 V:2586 T:44 VWAP:661.151316
- 2023-05-18 13:45:00+00:00 | O:661.15 H:663.4 L:660.85 C:662.94 V:2713 T:47 VWAP:662.12825
- 2023-05-18 13:50:00+00:00 | O:662.985 H:664.23 L:662.985 C:664.05 V:5012 T:103 VWAP:663.571746
- 2023-05-18 13:55:00+00:00 | O:663.31 H:663.495 L:662.74 C:663.305 V:2607 T:42 VWAP:663.133351
- 2023-05-18 14:00:00+00:00 | O:663.0 H:663.37 L:662.485 C:662.93 V:2354 T:56 VWAP:663.039687
- 2023-05-18 14:05:00+00:00 | O:663.46 H:665.42 L:663.36 C:665.42 V:1169 T:20 VWAP:663.915556
- 2023-05-18 14:10:00+00:00 | O:665.98 H:666.76 L:665.8 C:666.07 V:3562 T:70 VWAP:666.311333
- 2023-05-18 14:15:00+00:00 | O:665.79 H:666.1 L:665.79 C:666.09 V:1004 T:30 VWAP:665.97
- 2023-05-18 14:20:00+00:00 | O:666.265 H:667.035 L:666.265 C:666.91 V:1475 T:77 VWAP:666.743333
- 2023-05-18 14:25:00+00:00 | O:666.54 H:666.73 L:666.22 C:666.71 V:2290 T:76 VWAP:666.541539
- 2023-05-18 14:30:00+00:00 | O:666.87 H:667.49 L:666.87 C:667.48 V:1603 T:51 VWAP:667.254
- 2023-05-18 14:35:00+00:00 | O:667.75 H:667.77 L:667.69 C:667.77 V:1016 T:33 VWAP:667.73
- 2023-05-18 14:40:00+00:00 | O:667.45 H:668.1 L:667.04 C:667.16 V:2255 T:57 VWAP:667.657273
- 2023-05-18 14:45:00+00:00 | O:667.225 H:668.37 L:667.225 C:668.28 V:1342 T:23 VWAP:667.847917
- 2023-05-18 14:50:00+00:00 | O:668.255 H:669.27 L:668.24 C:669.27 V:2441 T:49 VWAP:668.579737
- 2023-05-18 14:55:00+00:00 | O:669.71 H:670.74 L:669.59 C:670.54 V:2305 T:52 VWAP:669.959
- 2023-05-18 15:00:00+00:00 | O:670.64 H:672.46 L:670.64 C:672.43 V:3978 T:64 VWAP:671.673182
- 2023-05-18 15:05:00+00:00 | O:672.63 H:673.32 L:672.63 C:672.82 V:3441 T:86 VWAP:672.993809
- 2023-05-18 15:10:00+00:00 | O:672.77 H:672.84 L:672.205 C:672.205 V:1099 T:48 VWAP:672.585834
- 2023-05-18 15:15:00+00:00 | O:672.46 H:672.49 L:671.93 C:671.93 V:1317 T:32 VWAP:672.253333
- 2023-05-18 15:20:00+00:00 | O:672.06 H:672.68 L:671.66 C:671.97 V:1917 T:36 VWAP:672.308065
- 2023-05-18 15:25:00+00:00 | O:671.57 H:673.26 L:671.48 C:672.98 V:1226 T:68 VWAP:672.402857
- 2023-05-18 15:30:00+00:00 | O:672.93 H:672.93 L:672.03 C:672.64 V:2434 T:66 VWAP:672.315281
- 2023-05-18 15:35:00+00:00 | O:672.58 H:674.14 L:672.58 C:673.58 V:1821 T:35 VWAP:673.578462

## Follow-through rows
- max_high_next_6_bars: 665.42
- max_high_next_12_bars: 667.77
- max_high_next_24_bars: 674.14
- close_after_6_bars: 665.42
- close_after_12_bars: 667.77
- close_after_24_bars: 673.58

## Candidate chart-level worksheet
- proposed support_level: 657.37
- proposed resistance_level: 659.77
- proposed target_price: 664.58
- proposed invalidation_level: 657.37
- entry_candidate_price: 662.17
- room_to_target: 4.81
- target_distance: 4.81
- max_favorable_move: 14.37
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- resistance_touched: true
- close_above_resistance: true
- target_hit_before_confirmation: false
- target_hit_after_confirmation: true
- invalidation_hit_before_confirmation: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: 674.14
- max_close_after_confirmation: 673.58
- suggested_classification: confirmed_breakout

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
