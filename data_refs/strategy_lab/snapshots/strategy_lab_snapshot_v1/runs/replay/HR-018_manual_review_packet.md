# HR-018 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-018
- related_candidate_id: PTC-018
- symbol: META
- date_window: 2023-07-19 to 2023-07-19
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/1Day/META_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/5Min/META_5Min_2023.parquet

## 1D context rows
- 2023-07-14T04:00:00+00:00 | O:311.45 H:314.6 L:307.38 C:308.53 V:746894 T:11146 VWAP:311.833638
- 2023-07-17T04:00:00+00:00 | O:307.22 H:311.35 L:304.76 C:310.56 V:922784 T:11297 VWAP:308.101016
- 2023-07-18T04:00:00+00:00 | O:310.77 H:314.05 L:307.63 C:312.12 V:621530 T:11515 VWAP:310.777793
- 2023-07-19T04:00:00+00:00 | O:312.91 H:318.67 L:310.57 C:316.15 V:425512 T:8556 VWAP:314.930067

## 5m breakdown context
- prior_support: 311.13
- breakdown candle: 2023-07-19T13:30:00+00:00 | close: 311.01
- breakdown_amount: 0.12

## 5m bars around the breakdown
- 2023-07-18T19:00:00+00:00 | O:312.55 H:312.64 L:312.43 C:312.555 V:5621 T:151 VWAP:312.541091
- 2023-07-18T19:05:00+00:00 | O:312.5 H:312.57 L:312.15 C:312.21 V:8187 T:160 VWAP:312.363147
- 2023-07-18T19:10:00+00:00 | O:312.18 H:312.28 L:311.95 C:312.27 V:5820 T:165 VWAP:312.128627
- 2023-07-18T19:15:00+00:00 | O:312.37 H:312.375 L:312.02 C:312.05 V:5530 T:146 VWAP:312.151765
- 2023-07-18T19:20:00+00:00 | O:311.98 H:311.98 L:311.59 C:311.77 V:6692 T:152 VWAP:311.763294
- 2023-07-18T19:25:00+00:00 | O:311.77 H:311.93 L:311.63 C:311.93 V:3432 T:107 VWAP:311.836837
- 2023-07-18T19:30:00+00:00 | O:311.91 H:312.065 L:311.79 C:312.01 V:6349 T:145 VWAP:311.930069
- 2023-07-18T19:35:00+00:00 | O:311.85 H:311.95 L:311.36 C:311.36 V:7683 T:156 VWAP:311.694349
- 2023-07-18T19:40:00+00:00 | O:311.41 H:311.55 L:311.18 C:311.26 V:7209 T:213 VWAP:311.389348
- 2023-07-18T19:45:00+00:00 | O:311.34 H:312.175 L:311.13 C:311.9 V:10609 T:255 VWAP:311.729134
- 2023-07-18T19:50:00+00:00 | O:311.91 H:312.14 L:311.49 C:312.01 V:18998 T:347 VWAP:311.836976
- 2023-07-18T19:55:00+00:00 | O:311.925 H:312.16 L:311.765 C:312.12 V:37484 T:558 VWAP:311.989878
- 2023-07-19T13:30:00+00:00 | O:312.91 H:312.95 L:310.57 C:311.01 V:17761 T:332 VWAP:311.959756
- 2023-07-19T13:35:00+00:00 | O:311.295 H:312.66 L:311.295 C:312.22 V:4902 T:156 VWAP:312.206572
- 2023-07-19T13:40:00+00:00 | O:312.86 H:313.475 L:312.52 C:313.21 V:16796 T:253 VWAP:313.105143
- 2023-07-19T13:45:00+00:00 | O:313.345 H:313.56 L:312.93 C:313.05 V:15123 T:177 VWAP:313.10162
- 2023-07-19T13:50:00+00:00 | O:313.05 H:313.2 L:312.6 C:312.99 V:9139 T:160 VWAP:312.938856
- 2023-07-19T13:55:00+00:00 | O:312.97 H:314.02 L:312.735 C:313.98 V:8539 T:159 VWAP:313.48567
- 2023-07-19T14:00:00+00:00 | O:314.04 H:314.26 L:313.83 C:313.83 V:6545 T:174 VWAP:314.052436
- 2023-07-19T14:05:00+00:00 | O:313.98 H:314.39 L:313.93 C:314.28 V:4408 T:142 VWAP:314.150165
- 2023-07-19T14:10:00+00:00 | O:314.47 H:314.65 L:314.17 C:314.39 V:4236 T:139 VWAP:314.398958
- 2023-07-19T14:15:00+00:00 | O:313.7 H:314.08 L:313.7 C:314.03 V:5971 T:138 VWAP:313.969893
- 2023-07-19T14:20:00+00:00 | O:314.04 H:314.41 L:313.77 C:313.9 V:3821 T:111 VWAP:314.129256
- 2023-07-19T14:25:00+00:00 | O:313.725 H:313.81 L:312.9 C:312.9 V:3929 T:126 VWAP:313.412955
- 2023-07-19T14:30:00+00:00 | O:312.945 H:313.34 L:312.68 C:313.27 V:6132 T:106 VWAP:312.949767
- 2023-07-19T14:35:00+00:00 | O:313.53 H:314.02 L:313.51 C:313.96 V:4457 T:99 VWAP:313.788454
- 2023-07-19T14:40:00+00:00 | O:313.98 H:314.27 L:313.9 C:314.27 V:3499 T:77 VWAP:314.056458
- 2023-07-19T14:45:00+00:00 | O:314.41 H:314.695 L:314.08 C:314.695 V:5841 T:101 VWAP:314.389391
- 2023-07-19T14:50:00+00:00 | O:314.66 H:316.57 L:314.52 C:315.07 V:27781 T:306 VWAP:315.270433
- 2023-07-19T14:55:00+00:00 | O:315.11 H:315.18 L:314.78 C:314.93 V:8584 T:170 VWAP:314.964252
- 2023-07-19T15:00:00+00:00 | O:314.88 H:314.88 L:314.14 C:314.14 V:3285 T:69 VWAP:314.246739
- 2023-07-19T15:05:00+00:00 | O:314.5 H:314.95 L:314.49 C:314.89 V:7286 T:101 VWAP:314.713913
- 2023-07-19T15:10:00+00:00 | O:315.01 H:315.7 L:315.0 C:315.7 V:4361 T:87 VWAP:315.322933
- 2023-07-19T15:15:00+00:00 | O:315.85 H:316.625 L:315.76 C:316.44 V:9233 T:140 VWAP:316.35481
- 2023-07-19T15:20:00+00:00 | O:316.43 H:317.26 L:316.3 C:317.17 V:12324 T:208 VWAP:316.865077
- 2023-07-19T15:25:00+00:00 | O:317.45 H:318.18 L:317.34 C:317.495 V:9478 T:159 VWAP:317.742513
- 2023-07-19T15:30:00+00:00 | O:317.35 H:317.7 L:317.14 C:317.32 V:3135 T:89 VWAP:317.429333

## Downside follow-through rows
- min_low_next_6_bars: 311.30
- min_low_next_12_bars: 311.30
- min_low_next_24_bars: 311.30
- close_after_6_bars: 313.83
- close_after_12_bars: 313.27
- close_after_24_bars: 317.32

## Candidate chart-level worksheet
- proposed support_level: 311.13
- proposed resistance_level: 311.63
- proposed target_price: 310.13
- proposed invalidation_level: 312.13
- entry_candidate_price: 311.01
- target_distance: 1.00
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: false
- invalidation_hit_after_confirmation: true
- min_low_after_confirmation: 310.57
- max_close_after_confirmation: 317.50
- suggested_classification: failed_breakdown_reclaim

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
