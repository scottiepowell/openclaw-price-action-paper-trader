# HR-009 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-009
- related_candidate_id: PTC-009
- symbol: IWM
- date_window: 2023-05-16 to 2023-05-16
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/IWM_1Day_sample.csv
  - data_refs/google_drive/IWM_5Min_sample.csv

## 1D context rows
- 2023-05-15 04:00:00+00:00 | O:173.29 H:175.705 L:172.89 C:174.89 V:538190 T:4638 VWAP:174.473051
- 2023-05-16 04:00:00+00:00 | O:173.61 H:173.71 L:172.23 C:172.25 V:580216 T:4836 VWAP:172.82025

## 5m breakdown context
- prior_support: 174.72
- breakdown candle: 2023-05-16 13:05:00+00:00 | close: 173.69
- breakdown_amount: 1.03

## 5m bars around the breakdown
- 2023-05-15 19:05:00+00:00 | O:174.86 H:174.95 L:174.86 C:174.875 V:2457 T:31 VWAP:174.92
- 2023-05-15 19:10:00+00:00 | O:174.86 H:174.92 L:174.86 C:174.88 V:2058 T:22 VWAP:174.898947
- 2023-05-15 19:15:00+00:00 | O:174.875 H:174.88 L:174.81 C:174.87 V:1980 T:26 VWAP:174.851053
- 2023-05-15 19:20:00+00:00 | O:174.81 H:174.88 L:174.73 C:174.875 V:3178 T:38 VWAP:174.850577
- 2023-05-15 19:25:00+00:00 | O:174.8 H:174.84 L:174.795 C:174.83 V:4476 T:56 VWAP:174.820516
- 2023-05-15 19:30:00+00:00 | O:174.82 H:174.92 L:174.805 C:174.85 V:6072 T:71 VWAP:174.850867
- 2023-05-15 19:35:00+00:00 | O:174.81 H:174.865 L:174.78 C:174.835 V:17165 T:134 VWAP:174.835823
- 2023-05-15 19:40:00+00:00 | O:174.82 H:174.875 L:174.72 C:174.78 V:21735 T:163 VWAP:174.803303
- 2023-05-15 19:45:00+00:00 | O:174.765 H:174.885 L:174.75 C:174.79 V:13126 T:151 VWAP:174.802778
- 2023-05-15 19:50:00+00:00 | O:174.775 H:174.915 L:174.775 C:174.815 V:16140 T:156 VWAP:174.835361
- 2023-05-15 19:55:00+00:00 | O:174.765 H:174.9 L:174.72 C:174.89 V:28394 T:275 VWAP:174.788127
- 2023-05-15 20:00:00+00:00 | O:174.86 H:174.86 L:174.86 C:174.86 V:500 T:1 VWAP:174.86
- 2023-05-16 13:05:00+00:00 | O:173.69 H:173.69 L:173.69 C:173.69 V:500 T:1 VWAP:173.69
- 2023-05-16 13:30:00+00:00 | O:173.61 H:173.71 L:173.39 C:173.55 V:7145 T:77 VWAP:173.519685
- 2023-05-16 13:35:00+00:00 | O:173.54 H:173.54 L:173.08 C:173.11 V:6624 T:89 VWAP:173.280748
- 2023-05-16 13:40:00+00:00 | O:173.16 H:173.67 L:173.05 C:173.56 V:8676 T:76 VWAP:173.375216
- 2023-05-16 13:45:00+00:00 | O:173.645 H:173.65 L:173.09 C:173.09 V:9656 T:79 VWAP:173.409288
- 2023-05-16 13:50:00+00:00 | O:173.045 H:173.045 L:172.64 C:172.77 V:14235 T:139 VWAP:172.787011
- 2023-05-16 13:55:00+00:00 | O:172.735 H:172.885 L:172.61 C:172.86 V:11069 T:88 VWAP:172.757558
- 2023-05-16 14:00:00+00:00 | O:172.83 H:172.845 L:172.65 C:172.68 V:5874 T:64 VWAP:172.737596
- 2023-05-16 14:05:00+00:00 | O:172.715 H:172.87 L:172.6 C:172.61 V:6730 T:63 VWAP:172.777898
- 2023-05-16 14:10:00+00:00 | O:172.55 H:172.55 L:172.27 C:172.33 V:5677 T:48 VWAP:172.36917
- 2023-05-16 14:15:00+00:00 | O:172.285 H:172.55 L:172.25 C:172.55 V:7313 T:56 VWAP:172.362011
- 2023-05-16 14:20:00+00:00 | O:172.55 H:172.595 L:172.39 C:172.39 V:3132 T:37 VWAP:172.507126
- 2023-05-16 14:25:00+00:00 | O:172.465 H:172.74 L:172.44 C:172.74 V:4532 T:48 VWAP:172.584131
- 2023-05-16 14:30:00+00:00 | O:172.825 H:172.91 L:172.74 C:172.78 V:6710 T:55 VWAP:172.844898
- 2023-05-16 14:35:00+00:00 | O:172.845 H:172.895 L:172.64 C:172.73 V:16213 T:102 VWAP:172.736806
- 2023-05-16 14:40:00+00:00 | O:172.71 H:172.8 L:172.59 C:172.8 V:8355 T:59 VWAP:172.676821
- 2023-05-16 14:45:00+00:00 | O:172.82 H:173.06 L:172.82 C:173.06 V:23731 T:65 VWAP:172.974105
- 2023-05-16 14:50:00+00:00 | O:173.005 H:173.04 L:172.93 C:173.025 V:5416 T:43 VWAP:172.988185
- 2023-05-16 14:55:00+00:00 | O:173.04 H:173.145 L:172.89 C:172.93 V:11663 T:95 VWAP:173.038302
- 2023-05-16 15:00:00+00:00 | O:173.07 H:173.07 L:172.95 C:172.99 V:1978 T:24 VWAP:173.013938
- 2023-05-16 15:05:00+00:00 | O:173.09 H:173.115 L:172.94 C:172.94 V:5169 T:31 VWAP:173.013333
- 2023-05-16 15:10:00+00:00 | O:172.96 H:173.035 L:172.82 C:172.865 V:4405 T:36 VWAP:172.958659
- 2023-05-16 15:15:00+00:00 | O:172.88 H:172.92 L:172.68 C:172.8 V:6200 T:59 VWAP:172.798868
- 2023-05-16 15:20:00+00:00 | O:172.84 H:172.87 L:172.74 C:172.84 V:3159 T:31 VWAP:172.803119
- 2023-05-16 15:25:00+00:00 | O:172.84 H:172.995 L:172.83 C:172.995 V:5043 T:36 VWAP:172.930306

## Downside follow-through rows
- min_low_next_6_bars: 172.61
- min_low_next_12_bars: 172.25
- min_low_next_24_bars: 172.25
- close_after_6_bars: 172.86
- close_after_12_bars: 172.74
- close_after_24_bars: 173.00

## Candidate chart-level worksheet
- proposed support_level: 174.72
- proposed resistance_level: 175.75
- proposed target_price: 172.66
- proposed invalidation_level: 175.75
- entry_candidate_price: 173.69
- target_distance: 2.06
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 172.25
- max_close_after_confirmation: 173.69
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
