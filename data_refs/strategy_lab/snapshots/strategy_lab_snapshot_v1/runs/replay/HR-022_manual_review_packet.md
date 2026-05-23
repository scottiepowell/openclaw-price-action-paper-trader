# HR-022 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-022
- related_candidate_id: PTC-022
- symbol: AMZN
- date_window: 2023-08-03 to 2023-08-03
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AMZN/1Day/AMZN_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AMZN/5Min/AMZN_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-08-03T04:00:00+00:00 | O:127.55 H:129.825 L:126.44 C:128.91 V:1175235 T:13495 VWAP:128.703527

## 5m OHLCV excerpt for the replay window
- 2023-08-03T13:05:00+00:00 | O:128.32 H:128.32 L:128.32 C:128.32 V:150 T:2 VWAP:128.32
- 2023-08-03T13:30:00+00:00 | O:127.55 H:127.58 L:126.46 C:126.59 V:64014 T:672 VWAP:126.984659
- 2023-08-03T13:35:00+00:00 | O:126.58 H:127.82 L:126.44 C:127.76 V:33239 T:304 VWAP:127.497065
- 2023-08-03T13:40:00+00:00 | O:127.68 H:127.7 L:127.14 C:127.51 V:13064 T:196 VWAP:127.45506
- 2023-08-03T13:45:00+00:00 | O:127.575 H:128.66 L:127.55 C:128.405 V:23268 T:292 VWAP:128.153448
- 2023-08-03T13:50:00+00:00 | O:128.435 H:128.6 L:128.21 C:128.42 V:16179 T:223 VWAP:128.40962
- 2023-08-03T13:55:00+00:00 | O:128.45 H:128.71 L:128.28 C:128.48 V:7499 T:106 VWAP:128.51254
- 2023-08-03T14:00:00+00:00 | O:128.485 H:128.83 L:128.465 C:128.545 V:28255 T:210 VWAP:128.655259
- 2023-08-03T14:05:00+00:00 | O:128.545 H:128.55 L:127.81 C:127.83 V:18312 T:178 VWAP:128.315842
- 2023-08-03T14:10:00+00:00 | O:127.73 H:128.44 L:127.59 C:128.35 V:7966 T:87 VWAP:128.138809
- 2023-08-03T14:15:00+00:00 | O:128.37 H:128.375 L:128.15 C:128.22 V:6605 T:86 VWAP:128.279179
- 2023-08-03T14:20:00+00:00 | O:128.24 H:128.24 L:127.78 C:127.865 V:13055 T:117 VWAP:128.034017
- ... 63 middle rows omitted ...
- 2023-08-03T19:40:00+00:00 | O:128.655 H:128.905 L:128.57 C:128.88 V:9854 T:123 VWAP:128.695092
- 2023-08-03T19:45:00+00:00 | O:128.86 H:128.945 L:128.645 C:128.925 V:26516 T:282 VWAP:128.819562
- 2023-08-03T19:50:00+00:00 | O:128.98 H:129.24 L:128.765 C:129.055 V:51461 T:447 VWAP:128.984999
- 2023-08-03T19:55:00+00:00 | O:129.075 H:129.36 L:128.84 C:128.91 V:142565 T:983 VWAP:129.147681
- 2023-08-03T20:00:00+00:00 | O:137.18 H:138.51 L:137.18 C:137.6 V:27840 T:681 VWAP:137.744426
- 2023-08-03T20:05:00+00:00 | O:137.36 H:138.24 L:135.59 C:138.08 V:49090 T:769 VWAP:137.089835
- 2023-08-03T20:10:00+00:00 | O:138.26 H:138.38 L:136.82 C:137.11 V:34345 T:551 VWAP:137.708211
- 2023-08-03T20:15:00+00:00 | O:137.16 H:137.22 L:137.0 C:137.22 V:6942 T:126 VWAP:137.073036
- 2023-08-03T20:20:00+00:00 | O:138.71 H:138.71 L:138.52 C:138.52 V:2863 T:93 VWAP:138.595
- 2023-08-03T20:25:00+00:00 | O:138.26 H:138.26 L:138.26 C:138.26 V:1446 T:46 VWAP:138.26
- 2023-08-03T20:30:00+00:00 | O:138.33 H:138.38 L:138.33 C:138.38 V:1544 T:45 VWAP:138.36
- 2023-08-03T20:40:00+00:00 | O:137.33 H:137.33 L:137.33 C:137.33 V:914 T:29 VWAP:137.33

## Level interaction analysis
- support_level: 126.44
  nearest_5m_bar: 2023-08-03T13:35:00+00:00 | O:126.58 H:127.82 L:126.44 C:127.76 | distance:0.0000
- resistance_level: 129.82
  nearest_5m_bar: 2023-08-03T16:50:00+00:00 | O:129.765 H:129.825 L:129.605 C:129.655 | distance:0.0000
- target_price: 131.82
  nearest_5m_bar: 2023-08-03T16:50:00+00:00 | O:129.765 H:129.825 L:129.605 C:129.655 | distance:2.0000
- invalidation_level: 126.34
  nearest_5m_bar: 2023-08-03T13:35:00+00:00 | O:126.58 H:127.82 L:126.44 C:127.76 | distance:0.1000
- any 5m close above resistance: true
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: true
- target hit before confirmation: false
- target hit after confirmation: true
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 126.44
- proposed resistance_level: 129.82
- proposed target_price: 131.82
- proposed invalidation_level: 126.34
- entry_candidate_price: 129.92
- room_to_target: 1.90
- target_distance: 2.00
- max_favorable_move: 8.89
- higher_timeframe_obstacle_check: TBD — manual chart review required
- target_already_hit_check: false

## Candidate event summary
- resistance_touched: true
- close_above_resistance: true
- target_hit_before_confirmation: false
- target_hit_after_confirmation: true
- invalidation_hit: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: 138.71
- max_close_after_confirmation: 138.52
- target_distance: 2.00
- max_favorable_move: 8.89
- target_already_hit_before_confirmation: false
- suggested_classification: confirmed_breakout

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
