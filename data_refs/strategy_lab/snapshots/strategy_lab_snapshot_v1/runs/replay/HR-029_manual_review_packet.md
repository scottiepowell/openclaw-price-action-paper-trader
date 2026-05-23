# HR-029 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-029
- related_candidate_id: PTC-029
- symbol: QQQ
- date_window: 2023-10-06 to 2023-10-06
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/QQQ/1Day/QQQ_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/QQQ/5Min/QQQ_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-10-06T04:00:00+00:00 | O:355.7 H:365.91 L:354.85 C:364.7 V:1384980 T:10037 VWAP:362.633973

## 5m OHLCV excerpt for the replay window
- 2023-10-06T12:25:00+00:00 | O:359.35 H:359.35 L:359.35 C:359.35 V:100 T:1 VWAP:359.35
- 2023-10-06T12:30:00+00:00 | O:356.23 H:356.23 L:354.31 C:354.32 V:10814 T:47 VWAP:355.130349
- 2023-10-06T12:35:00+00:00 | O:354.48 H:355.25 L:354.35 C:354.79 V:16522 T:33 VWAP:354.791705
- 2023-10-06T12:40:00+00:00 | O:355.21 H:355.47 L:354.89 C:354.89 V:3235 T:15 VWAP:355.271531
- 2023-10-06T12:45:00+00:00 | O:354.83 H:354.86 L:354.48 C:354.48 V:1168 T:12 VWAP:354.605555
- 2023-10-06T12:50:00+00:00 | O:354.53 H:354.53 L:353.81 C:353.87 V:3822 T:26 VWAP:354.090126
- 2023-10-06T12:55:00+00:00 | O:354.25 H:354.45 L:353.94 C:354.45 V:2651 T:17 VWAP:354.207511
- 2023-10-06T13:00:00+00:00 | O:354.39 H:354.64 L:354.14 C:354.51 V:1766 T:13 VWAP:354.396789
- 2023-10-06T13:05:00+00:00 | O:354.35 H:355.25 L:354.35 C:355.09 V:2470 T:10 VWAP:354.867083
- 2023-10-06T13:10:00+00:00 | O:355.15 H:355.53 L:355.15 C:355.26 V:1351 T:14 VWAP:355.259
- 2023-10-06T13:15:00+00:00 | O:355.59 H:355.86 L:355.59 C:355.79 V:3346 T:15 VWAP:355.781972
- 2023-10-06T13:20:00+00:00 | O:355.98 H:356.12 L:355.97 C:356.09 V:2737 T:12 VWAP:356.01512
- ... 74 middle rows omitted ...
- 2023-10-06T19:35:00+00:00 | O:365.41 H:365.77 L:365.4 C:365.77 V:10212 T:122 VWAP:365.640773
- 2023-10-06T19:40:00+00:00 | O:365.85 H:365.88 L:365.33 C:365.39 V:31948 T:231 VWAP:365.542584
- 2023-10-06T19:45:00+00:00 | O:365.375 H:365.565 L:365.31 C:365.375 V:23211 T:283 VWAP:365.407137
- 2023-10-06T19:50:00+00:00 | O:365.2 H:365.355 L:364.71 C:364.73 V:41404 T:317 VWAP:365.020935
- 2023-10-06T19:55:00+00:00 | O:364.76 H:364.87 L:364.6 C:364.7 V:68546 T:588 VWAP:364.707528
- 2023-10-06T20:00:00+00:00 | O:364.63 H:364.9 L:364.61 C:364.9 V:3510 T:7 VWAP:364.697714
- 2023-10-06T20:05:00+00:00 | O:365.1 H:365.12 L:365.08 C:365.09 V:3285 T:9 VWAP:365.097813
- 2023-10-06T20:10:00+00:00 | O:365.03 H:365.03 L:365.03 C:365.03 V:100 T:1 VWAP:365.03
- 2023-10-06T20:15:00+00:00 | O:365.17 H:365.17 L:365.13 C:365.13 V:2801 T:6 VWAP:365.141786
- 2023-10-06T20:20:00+00:00 | O:365.12 H:365.15 L:365.12 C:365.15 V:2560 T:7 VWAP:365.126094
- 2023-10-06T20:25:00+00:00 | O:365.14 H:365.2 L:365.14 C:365.2 V:1311 T:5 VWAP:365.153846
- 2023-10-06T20:30:00+00:00 | O:365.17 H:365.17 L:365.17 C:365.17 V:1600 T:2 VWAP:365.17

## Level interaction analysis
- support_level: 354.85
  nearest_5m_bar: 2023-10-06T13:40:00+00:00 | O:355.26 H:356.05 L:354.85 C:355.8 | distance:0.0000
- resistance_level: 365.91
  nearest_5m_bar: 2023-10-06T18:40:00+00:00 | O:365.28 H:365.91 L:365.22 C:365.3 | distance:0.0000
- target_price: 367.91
  nearest_5m_bar: 2023-10-06T18:40:00+00:00 | O:365.28 H:365.91 L:365.22 C:365.3 | distance:2.0000
- invalidation_level: 354.75
  nearest_5m_bar: 2023-10-06T12:35:00+00:00 | O:354.48 H:355.25 L:354.35 C:354.79 | distance:0.0400
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- target hit after confirmation: false
- invalidation hit before confirmation: true
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 354.85
- proposed resistance_level: 365.91
- proposed target_price: 367.91
- proposed invalidation_level: 354.75
- entry_candidate_price: 366.01
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
- invalidation_hit: true
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
