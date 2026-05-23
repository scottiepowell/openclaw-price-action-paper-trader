# HR-023 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-023
- related_candidate_id: PTC-023
- symbol: TSLA
- date_window: 2023-09-11 to 2023-09-11
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/TSLA/1Day/TSLA_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/TSLA/5Min/TSLA_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-09-11T04:00:00+00:00 | O:264.21 H:274.825 L:260.67 C:273.63 V:1167982 T:16941 VWAP:268.615997

## 5m OHLCV excerpt for the replay window
- 2023-09-11T13:00:00+00:00 | O:265.17 H:265.43 L:265.15 C:265.29 V:2359 T:50 VWAP:265.292222
- 2023-09-11T13:05:00+00:00 | O:265.09 H:265.09 L:264.35 C:264.41 V:1877 T:32 VWAP:264.661429
- 2023-09-11T13:10:00+00:00 | O:264.29 H:264.43 L:264.23 C:264.27 V:1265 T:22 VWAP:264.346667
- 2023-09-11T13:15:00+00:00 | O:264.21 H:264.57 L:263.99 C:264.55 V:3439 T:65 VWAP:264.248823
- 2023-09-11T13:20:00+00:00 | O:264.61 H:264.75 L:264.57 C:264.71 V:1737 T:29 VWAP:264.641429
- 2023-09-11T13:30:00+00:00 | O:264.21 H:264.71 L:260.67 C:261.96 V:97643 T:1377 VWAP:262.586265
- 2023-09-11T13:35:00+00:00 | O:262.1 H:263.58 L:261.01 C:261.12 V:43155 T:522 VWAP:262.439641
- 2023-09-11T13:40:00+00:00 | O:261.09 H:263.0 L:261.09 C:262.18 V:18392 T:305 VWAP:262.013162
- 2023-09-11T13:45:00+00:00 | O:262.44 H:264.48 L:261.18 C:264.48 V:30263 T:450 VWAP:263.033192
- 2023-09-11T13:50:00+00:00 | O:264.6 H:264.81 L:262.51 C:264.39 V:38649 T:484 VWAP:263.95546
- 2023-09-11T13:55:00+00:00 | O:264.48 H:265.89 L:263.65 C:264.375 V:21806 T:392 VWAP:264.913212
- 2023-09-11T14:00:00+00:00 | O:264.345 H:265.66 L:264.345 C:265.185 V:24935 T:314 VWAP:264.918131
- ... 60 middle rows omitted ...
- 2023-09-11T19:05:00+00:00 | O:274.46 H:274.62 L:274.31 C:274.475 V:6926 T:90 VWAP:274.457517
- 2023-09-11T19:10:00+00:00 | O:274.44 H:274.45 L:273.795 C:274.22 V:16299 T:175 VWAP:274.08121
- 2023-09-11T19:15:00+00:00 | O:274.17 H:274.27 L:273.96 C:273.98 V:7986 T:132 VWAP:274.168142
- 2023-09-11T19:20:00+00:00 | O:274.115 H:274.57 L:273.99 C:274.57 V:5937 T:134 VWAP:274.178261
- 2023-09-11T19:25:00+00:00 | O:274.47 H:274.825 L:274.375 C:274.57 V:7134 T:125 VWAP:274.61566
- 2023-09-11T19:30:00+00:00 | O:274.63 H:274.63 L:273.92 C:274.245 V:11255 T:152 VWAP:274.391097
- 2023-09-11T19:35:00+00:00 | O:274.29 H:274.29 L:273.42 C:273.42 V:12055 T:146 VWAP:273.956533
- 2023-09-11T19:40:00+00:00 | O:273.34 H:273.38 L:272.98 C:273.35 V:20106 T:266 VWAP:273.150618
- 2023-09-11T19:45:00+00:00 | O:273.265 H:273.45 L:273.045 C:273.36 V:17515 T:228 VWAP:273.29515
- 2023-09-11T19:50:00+00:00 | O:273.46 H:273.81 L:272.7 C:272.95 V:17123 T:298 VWAP:273.354156
- 2023-09-11T19:55:00+00:00 | O:272.91 H:273.7 L:272.58 C:273.63 V:60121 T:617 VWAP:273.366135
- 2023-09-11T20:00:00+00:00 | O:273.77 H:273.77 L:273.77 C:273.77 V:100 T:1 VWAP:273.77

## Level interaction analysis
- support_level: 260.67
  nearest_5m_bar: 2023-09-11T13:30:00+00:00 | O:264.21 H:264.71 L:260.67 C:261.96 | distance:0.0000
- resistance_level: 274.82
  nearest_5m_bar: 2023-09-11T19:25:00+00:00 | O:274.47 H:274.825 L:274.375 C:274.57 | distance:0.0000
- target_price: 276.82
  nearest_5m_bar: 2023-09-11T19:25:00+00:00 | O:274.47 H:274.825 L:274.375 C:274.57 | distance:2.0000
- invalidation_level: 260.57
  nearest_5m_bar: 2023-09-11T13:30:00+00:00 | O:264.21 H:264.71 L:260.67 C:261.96 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 260.67
- proposed resistance_level: 274.82
- proposed target_price: 276.82
- proposed invalidation_level: 260.57
- entry_candidate_price: 274.93
- room_to_target: 1.90
- target_distance: 2.00
- max_favorable_move: nan
- higher_timeframe_obstacle_check: TBD — manual chart review required
- target_already_hit_check: false

## Candidate event summary
- resistance_touched: true
- close_above_resistance: false
- target_hit_before_confirmation: false
- target_hit_after_confirmation: false
- invalidation_hit: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: nan
- max_close_after_confirmation: nan
- target_distance: 2.00
- max_favorable_move: nan
- target_already_hit_before_confirmation: false
- suggested_classification: watch_no_trigger

## Manual promotion workflow
- manual_review_status: pending
- manual_review_outcome: pending
- manual_review_classification: pending
- manual_reviewer_notes: pending
- broker_action_allowed: false

## Manual visual review checklist
- [ ] Is support defensible?
- [ ] Is resistance defensible?
- [ ] Is target defensible?
- [ ] Is invalidation defensible?
- [ ] Did price close above resistance?
- [ ] Did price only wick/tap resistance?
- [ ] Did price reach target?
- [ ] Was target already hit before confirmation?
- [ ] Did target hit after confirmation?
- [ ] Did invalidation hit after confirmation?
- [ ] Was there a higher-timeframe obstacle?
- [ ] Was the case confirmed, ambiguous, insufficient, contradicted, or watch/no-trigger?

## Recommended classification options
- confirmed_breakout
- confirmed_breakout_no_target_hit
- failed_breakout
- watch_no_trigger
- ambiguous
- insufficient
- contradicted
- blocked_data_quality

## Boundary
- No trade signal
- No profitability claim
- No execution readiness
- No broker action allowed
