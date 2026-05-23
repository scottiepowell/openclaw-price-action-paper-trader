# HR-002 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-002
- related_candidate_id: PTC-002
- symbol: SPY
- date_window: 2023-05-15 to 2023-05-17
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/SPY_1Day_sample.csv
  - data_refs/google_drive/SPY_5Min_sample.csv
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-05-15 04:00:00+00:00 | O:412.27 H:413.39 L:410.26 C:413.02 V:813583 T:8458 VWAP:412.01462
- 2023-05-16 04:00:00+00:00 | O:411.85 H:412.78 L:410.25 C:410.28 V:1008235 T:9289 VWAP:411.489139
- 2023-05-17 04:00:00+00:00 | O:412.34 H:415.84 L:410.65 C:415.14 V:1343616 T:12506 VWAP:414.033074

## 5m OHLCV excerpt for the replay window
- 2023-05-15 13:30:00+00:00 | O:412.27 H:412.275 L:411.38 C:411.38 V:25488 T:245 VWAP:411.981494
- 2023-05-15 13:35:00+00:00 | O:411.4 H:411.615 L:411.26 C:411.46 V:10592 T:113 VWAP:411.445408
- 2023-05-15 13:40:00+00:00 | O:411.415 H:411.685 L:411.37 C:411.49 V:12577 T:117 VWAP:411.506932
- 2023-05-15 13:45:00+00:00 | O:411.545 H:411.68 L:411.14 C:411.19 V:11365 T:155 VWAP:411.390372
- 2023-05-15 13:50:00+00:00 | O:411.225 H:411.225 L:410.98 C:411.035 V:16212 T:168 VWAP:411.041959
- 2023-05-15 13:55:00+00:00 | O:411.085 H:411.09 L:410.8 C:410.82 V:13937 T:148 VWAP:410.928655
- 2023-05-15 14:00:00+00:00 | O:410.86 H:411.18 L:410.86 C:411.015 V:22348 T:156 VWAP:410.986829
- 2023-05-15 14:05:00+00:00 | O:411.03 H:411.125 L:410.36 C:410.42 V:20638 T:165 VWAP:410.763633
- 2023-05-15 14:10:00+00:00 | O:410.4 H:410.535 L:410.29 C:410.35 V:14247 T:128 VWAP:410.428529
- 2023-05-15 14:15:00+00:00 | O:410.295 H:410.53 L:410.26 C:410.52 V:9953 T:93 VWAP:410.368863
- 2023-05-15 14:20:00+00:00 | O:410.595 H:410.98 L:410.41 C:410.91 V:19901 T:145 VWAP:410.753418
- 2023-05-15 14:25:00+00:00 | O:410.93 H:411.225 L:410.895 C:411.015 V:13800 T:104 VWAP:411.053824
- ... 226 middle rows omitted ...
- 2023-05-17 19:10:00+00:00 | O:415.155 H:415.33 L:415.15 C:415.2 V:10704 T:186 VWAP:415.223352
- 2023-05-17 19:15:00+00:00 | O:415.24 H:415.41 L:415.13 C:415.16 V:6447 T:105 VWAP:415.264286
- 2023-05-17 19:20:00+00:00 | O:415.16 H:415.185 L:414.6 C:414.635 V:10148 T:116 VWAP:414.763462
- 2023-05-17 19:25:00+00:00 | O:414.64 H:414.75 L:414.52 C:414.62 V:18595 T:121 VWAP:414.600098
- 2023-05-17 19:30:00+00:00 | O:414.65 H:414.885 L:414.57 C:414.645 V:14101 T:164 VWAP:414.72386
- 2023-05-17 19:35:00+00:00 | O:414.645 H:414.76 L:414.485 C:414.675 V:25130 T:202 VWAP:414.591414
- 2023-05-17 19:40:00+00:00 | O:414.595 H:415.045 L:414.595 C:414.965 V:27505 T:259 VWAP:414.91146
- 2023-05-17 19:45:00+00:00 | O:414.935 H:415.38 L:414.87 C:415.325 V:26192 T:242 VWAP:415.176534
- 2023-05-17 19:50:00+00:00 | O:415.345 H:415.49 L:415.075 C:415.295 V:39066 T:347 VWAP:415.255646
- 2023-05-17 19:55:00+00:00 | O:415.285 H:415.51 L:414.94 C:415.14 V:83834 T:635 VWAP:415.213169
- 2023-05-17 20:00:00+00:00 | O:415.0 H:415.05 L:415.0 C:415.05 V:3356 T:6 VWAP:415.021692
- 2023-05-17 20:05:00+00:00 | O:415.05 H:415.05 L:415.0 C:415.0 V:2900 T:2 VWAP:415.024138

## Level interaction analysis
- support_level: 410.26
  nearest_5m_bar: 2023-05-15 14:15:00+00:00 | O:410.295 H:410.53 L:410.26 C:410.52 | distance:0.0000
- resistance_level: 415.84
  nearest_5m_bar: 2023-05-17 17:50:00+00:00 | O:415.755 H:415.84 L:415.54 C:415.615 | distance:0.0000
- target_price: 418.00
  nearest_5m_bar: 2023-05-17 17:50:00+00:00 | O:415.755 H:415.84 L:415.54 C:415.615 | distance:2.1600
- invalidation_level: 410.21
  nearest_5m_bar: 2023-05-16 20:00:00+00:00 | O:410.12 H:410.19 L:410.12 C:410.14 | distance:0.0200
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- invalidation hit before confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 410.26
- proposed resistance_level: 415.84
- proposed target_price: 418.00
- proposed invalidation_level: 410.21
- entry_candidate_price: 415.89
- room_to_target: 2.11
- higher_timeframe_obstacle_check: TBD — manual chart review required
- target_already_hit_check: false

## Candidate event summary
- resistance_touched: true
- close_above_resistance: false
- target_hit_after_confirmation: false
- invalidation_hit: true
- target_already_hit_before_confirmation: false
- suggested_classification: watch_no_trigger

## Manual visual review checklist
- [ ] Is support defensible?
- [ ] Is resistance defensible?
- [ ] Is target defensible?
- [ ] Is invalidation defensible?
- [ ] Did price close above resistance?
- [ ] Did price only wick/tap resistance?
- [ ] Did price reach target?
- [ ] Was target already hit before confirmation?
- [ ] Was there a higher-timeframe obstacle?
- [ ] Was the case confirmed, ambiguous, insufficient, contradicted, or watch/no-trigger?

## Recommended classification options
- confirmed_breakout
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
