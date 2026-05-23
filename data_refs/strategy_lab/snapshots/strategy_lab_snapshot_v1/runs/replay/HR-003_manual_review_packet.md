# HR-003 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-003
- related_candidate_id: PTC-003
- symbol: NVDA
- date_window: 2023-05-15 to 2023-05-18
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/NVDA_1Day_sample.csv
  - data_refs/google_drive/NVDA_5Min_sample.csv
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-05-15 04:00:00+00:00 | O:285.07 H:289.65 L:281.63 C:289.56 V:335578 T:5843 VWAP:286.561523
- 2023-05-16 04:00:00+00:00 | O:288.47 H:298.7 L:288.47 C:292.08 V:666197 T:10962 VWAP:294.84921
- 2023-05-17 04:00:00+00:00 | O:295.83 H:301.99 L:294.49 C:301.83 V:539831 T:9335 VWAP:298.53448
- 2023-05-18 04:00:00+00:00 | O:304.31 H:318.27 L:303.345 C:316.72 V:751990 T:14620 VWAP:313.219205

## 5m OHLCV excerpt for the replay window
- 2023-05-15 13:25:00+00:00 | O:285.17 H:285.17 L:285.17 C:285.17 V:159 T:3 VWAP:285.17
- 2023-05-15 13:30:00+00:00 | O:285.07 H:285.07 L:283.96 C:284.81 V:9278 T:155 VWAP:284.469208
- 2023-05-15 13:35:00+00:00 | O:284.74 H:284.76 L:282.86 C:283.14 V:10006 T:160 VWAP:283.941259
- 2023-05-15 13:40:00+00:00 | O:283.2 H:283.89 L:283.2 C:283.79 V:7926 T:111 VWAP:283.615671
- 2023-05-15 13:45:00+00:00 | O:284.185 H:285.12 L:284.185 C:284.43 V:21005 T:356 VWAP:284.611786
- 2023-05-15 13:50:00+00:00 | O:284.49 H:284.49 L:282.79 C:283.44 V:8033 T:125 VWAP:283.392004
- 2023-05-15 13:55:00+00:00 | O:283.405 H:283.405 L:282.73 C:282.73 V:3476 T:77 VWAP:283.001502
- 2023-05-15 14:00:00+00:00 | O:282.8 H:283.39 L:282.8 C:282.95 V:3224 T:103 VWAP:283.072647
- 2023-05-15 14:05:00+00:00 | O:283.08 H:283.08 L:281.9 C:282.04 V:4551 T:65 VWAP:282.105936
- 2023-05-15 14:10:00+00:00 | O:282.035 H:282.43 L:282.01 C:282.03 V:4163 T:90 VWAP:282.18125
- 2023-05-15 14:15:00+00:00 | O:281.96 H:282.12 L:281.63 C:282.12 V:5750 T:90 VWAP:281.837834
- 2023-05-15 14:20:00+00:00 | O:282.04 H:282.285 L:281.86 C:281.93 V:4195 T:79 VWAP:282.010167
- ... 226 middle rows omitted ...
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

## Level interaction analysis
- support_level: 281.63
  nearest_5m_bar: 2023-05-15 14:15:00+00:00 | O:281.96 H:282.12 L:281.63 C:282.12 | distance:0.0000
- resistance_level: 318.27
  nearest_5m_bar: 2023-05-18 14:35:00+00:00 | O:310.495 H:311.36 L:310.35 C:311.335 | distance:6.9100
- target_price: 323.00
  nearest_5m_bar: 2023-05-18 14:35:00+00:00 | O:310.495 H:311.36 L:310.35 C:311.335 | distance:11.6400
- invalidation_level: 281.53
  nearest_5m_bar: 2023-05-15 14:15:00+00:00 | O:281.96 H:282.12 L:281.63 C:282.12 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: false
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- invalidation hit before confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 281.63
- proposed resistance_level: 318.27
- proposed target_price: 323.00
- proposed invalidation_level: 281.53
- entry_candidate_price: 318.37
- room_to_target: 4.63
- higher_timeframe_obstacle_check: TBD — manual chart review required
- target_already_hit_check: false

## Candidate event summary
- resistance_touched: false
- close_above_resistance: false
- target_hit_after_confirmation: false
- invalidation_hit: false
- target_already_hit_before_confirmation: false
- suggested_classification: insufficient

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
