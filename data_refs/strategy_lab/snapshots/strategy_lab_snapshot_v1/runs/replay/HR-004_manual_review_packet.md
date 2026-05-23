# HR-004 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-004
- related_candidate_id: PTC-004
- symbol: NVDA
- date_window: 2023-05-18 to 2023-05-18
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/NVDA_1Day_sample.csv
  - data_refs/google_drive/NVDA_5Min_sample.csv

## 1D context rows
- 2023-05-15 04:00:00+00:00 | O:285.07 H:289.65 L:281.63 C:289.56 V:335578 T:5843 VWAP:286.561523
- 2023-05-16 04:00:00+00:00 | O:288.47 H:298.7 L:288.47 C:292.08 V:666197 T:10962 VWAP:294.84921
- 2023-05-17 04:00:00+00:00 | O:295.83 H:301.99 L:294.49 C:301.83 V:539831 T:9335 VWAP:298.53448
- 2023-05-18 04:00:00+00:00 | O:304.31 H:318.27 L:303.345 C:316.72 V:751990 T:14620 VWAP:313.219205

## 5m breakout context
- prior_resistance: 301.99
- breakout candle: 2023-05-18 13:30:00+00:00 | close: 305.52
- breakout_amount: 3.53

## 5m bars around the breakout
- 2023-05-17 19:00:00+00:00 | O:299.82 H:300.32 L:299.82 C:300.265 V:2632 T:64 VWAP:300.134445
- 2023-05-17 19:05:00+00:00 | O:300.26 H:300.975 L:300.21 C:300.94 V:6651 T:90 VWAP:300.789487
- 2023-05-17 19:10:00+00:00 | O:300.92 H:301.23 L:300.92 C:301.23 V:3336 T:127 VWAP:301.12697
- 2023-05-17 19:15:00+00:00 | O:301.2 H:301.42 L:300.99 C:301.215 V:9303 T:187 VWAP:301.227118
- 2023-05-17 19:20:00+00:00 | O:301.205 H:301.36 L:300.66 C:300.79 V:12830 T:206 VWAP:301.098727
- 2023-05-17 19:25:00+00:00 | O:300.85 H:301.15 L:300.805 C:300.88 V:4107 T:71 VWAP:300.983939
- 2023-05-17 19:30:00+00:00 | O:300.89 H:301.31 L:300.755 C:300.76 V:4112 T:83 VWAP:301.014355
- 2023-05-17 19:35:00+00:00 | O:300.77 H:301.02 L:300.59 C:300.87 V:13373 T:137 VWAP:300.754569
- 2023-05-17 19:40:00+00:00 | O:300.95 H:301.09 L:300.74 C:300.95 V:6320 T:104 VWAP:300.920181
- 2023-05-17 19:45:00+00:00 | O:300.9 H:301.88 L:300.9 C:301.81 V:10612 T:198 VWAP:301.571142
- 2023-05-17 19:50:00+00:00 | O:301.83 H:301.83 L:301.38 C:301.44 V:7288 T:154 VWAP:301.578193
- 2023-05-17 19:55:00+00:00 | O:301.59 H:301.99 L:301.52 C:301.83 V:29360 T:660 VWAP:301.809132
- 2023-05-18 13:30:00+00:00 | O:304.31 H:305.91 L:303.345 C:305.52 V:44676 T:758 VWAP:304.491058
- 2023-05-18 13:35:00+00:00 | O:305.81 H:308.06 L:305.715 C:308.06 V:44176 T:576 VWAP:307.107352
- 2023-05-18 13:40:00+00:00 | O:308.0 H:308.14 L:306.79 C:307.43 V:21548 T:436 VWAP:307.428567
- 2023-05-18 13:45:00+00:00 | O:307.4 H:308.24 L:307.15 C:307.32 V:7772 T:259 VWAP:307.658555
- 2023-05-18 13:50:00+00:00 | O:306.81 H:306.91 L:305.86 C:306.78 V:13022 T:346 VWAP:306.455285
- 2023-05-18 13:55:00+00:00 | O:306.825 H:307.93 L:306.6 C:307.79 V:5182 T:183 VWAP:307.515428
- 2023-05-18 14:00:00+00:00 | O:307.77 H:309.2 L:307.61 C:308.63 V:17915 T:347 VWAP:308.216791
- 2023-05-18 14:05:00+00:00 | O:308.655 H:309.74 L:308.655 C:309.44 V:10944 T:193 VWAP:309.360639
- 2023-05-18 14:10:00+00:00 | O:309.45 H:309.74 L:308.88 C:309.02 V:11802 T:200 VWAP:309.267187
- 2023-05-18 14:15:00+00:00 | O:309.0 H:309.22 L:308.95 C:309.22 V:1181 T:26 VWAP:309.031429
- 2023-05-18 14:20:00+00:00 | O:309.23 H:310.19 L:309.23 C:309.86 V:7000 T:139 VWAP:309.958802
- 2023-05-18 14:25:00+00:00 | O:309.83 H:310.675 L:309.82 C:310.675 V:17363 T:334 VWAP:310.234312
- 2023-05-18 14:30:00+00:00 | O:310.92 H:311.005 L:310.51 C:310.57 V:5498 T:106 VWAP:310.775707
- 2023-05-18 14:35:00+00:00 | O:310.495 H:311.36 L:310.35 C:311.335 V:5627 T:89 VWAP:310.948416

## Follow-through rows
- max_high_next_6_bars: 309.20
- max_high_next_12_bars: 311.00
- max_high_next_24_bars: 311.36
- close_after_6_bars: 308.63
- close_after_12_bars: 310.57
- close_after_24_bars: 311.33

## Candidate chart-level worksheet
- proposed support_level: 298.46
- proposed resistance_level: 301.99
- proposed target_price: 309.05
- proposed invalidation_level: 298.46
- entry_candidate_price: 305.52
- room_to_target: 7.06
- target_distance: 7.06
- max_favorable_move: 9.37
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- resistance_touched: true
- close_above_resistance: true
- target_hit_before_confirmation: false
- target_hit_after_confirmation: true
- invalidation_hit_before_confirmation: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: 311.36
- max_close_after_confirmation: 311.34
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
