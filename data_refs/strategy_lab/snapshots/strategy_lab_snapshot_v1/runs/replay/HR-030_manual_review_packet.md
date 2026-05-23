# HR-030 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-030
- related_candidate_id: PTC-030
- symbol: NVDA
- date_window: 2023-10-17 to 2023-10-17
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/NVDA/1Day/NVDA_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/NVDA/5Min/NVDA_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-10-17T04:00:00+00:00 | O:439.99 H:447.405 L:425.08 C:439.49 V:1061719 T:24399 VWAP:437.004799

## 5m OHLCV excerpt for the replay window
- 2023-10-17T13:10:00+00:00 | O:444.85 H:444.85 L:444.85 C:444.85 V:587 T:11 VWAP:444.85
- 2023-10-17T13:30:00+00:00 | O:439.99 H:441.62 L:434.31 C:434.76 V:106057 T:1598 VWAP:438.312734
- 2023-10-17T13:35:00+00:00 | O:435.01 H:437.02 L:433.39 C:436.45 V:74323 T:1044 VWAP:435.240426
- 2023-10-17T13:40:00+00:00 | O:436.42 H:436.47 L:434.11 C:434.8 V:54811 T:798 VWAP:435.153998
- 2023-10-17T13:45:00+00:00 | O:433.93 H:433.95 L:427.77 C:429.44 V:81086 T:1294 VWAP:429.976508
- 2023-10-17T13:50:00+00:00 | O:429.53 H:429.64 L:425.08 C:428.585 V:58983 T:862 VWAP:427.495161
- 2023-10-17T13:55:00+00:00 | O:428.63 H:430.44 L:428.57 C:429.96 V:28074 T:516 VWAP:429.460103
- 2023-10-17T14:00:00+00:00 | O:430.12 H:434.035 L:429.82 C:433.81 V:24683 T:504 VWAP:432.155424
- 2023-10-17T14:05:00+00:00 | O:433.89 H:436.09 L:432.92 C:435.91 V:31236 T:578 VWAP:435.128432
- 2023-10-17T14:10:00+00:00 | O:436.1 H:436.1 L:434.03 C:434.13 V:37978 T:678 VWAP:435.518579
- 2023-10-17T14:15:00+00:00 | O:434.19 H:437.06 L:434.19 C:436.865 V:13572 T:379 VWAP:435.667796
- 2023-10-17T14:20:00+00:00 | O:437.28 H:438.6 L:435.01 C:436.98 V:18135 T:394 VWAP:437.270006
- ... 55 middle rows omitted ...
- 2023-10-17T19:00:00+00:00 | O:437.36 H:438.1 L:436.57 C:436.97 V:3265 T:118 VWAP:437.161111
- 2023-10-17T19:05:00+00:00 | O:437.02 H:437.9 L:436.78 C:437.9 V:3523 T:147 VWAP:437.287433
- 2023-10-17T19:10:00+00:00 | O:438.4 H:438.4 L:438.29 C:438.33 V:1115 T:88 VWAP:438.34125
- 2023-10-17T19:15:00+00:00 | O:438.61 H:438.855 L:438.4 C:438.855 V:2751 T:120 VWAP:438.600625
- 2023-10-17T19:20:00+00:00 | O:438.8 H:439.49 L:438.8 C:439.07 V:4455 T:240 VWAP:439.145778
- 2023-10-17T19:25:00+00:00 | O:438.91 H:439.43 L:438.68 C:439.26 V:6076 T:182 VWAP:438.939589
- 2023-10-17T19:30:00+00:00 | O:439.49 H:439.67 L:438.8 C:438.88 V:4232 T:169 VWAP:439.333934
- 2023-10-17T19:35:00+00:00 | O:439.145 H:439.45 L:438.8 C:438.92 V:3536 T:118 VWAP:439.108605
- 2023-10-17T19:40:00+00:00 | O:439.0 H:439.1 L:438.0 C:438.07 V:4625 T:239 VWAP:438.7362
- 2023-10-17T19:45:00+00:00 | O:438.58 H:439.16 L:438.38 C:439.03 V:4316 T:184 VWAP:438.851818
- 2023-10-17T19:50:00+00:00 | O:438.89 H:439.72 L:438.63 C:439.64 V:8509 T:273 VWAP:439.182164
- 2023-10-17T19:55:00+00:00 | O:439.68 H:440.29 L:439.29 C:439.49 V:25023 T:659 VWAP:439.692546

## Level interaction analysis
- support_level: 425.08
  nearest_5m_bar: 2023-10-17T13:50:00+00:00 | O:429.53 H:429.64 L:425.08 C:428.585 | distance:0.0000
- resistance_level: 447.40
  nearest_5m_bar: 2023-10-17T16:20:00+00:00 | O:446.62 H:447.405 L:446.38 C:446.69 | distance:0.0000
- target_price: 323.00
  nearest_5m_bar: 2023-10-17T13:50:00+00:00 | O:429.53 H:429.64 L:425.08 C:428.585 | distance:102.0800
- invalidation_level: 424.98
  nearest_5m_bar: 2023-10-17T13:50:00+00:00 | O:429.53 H:429.64 L:425.08 C:428.585 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: true
- target hit before confirmation: true
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 425.08
- proposed resistance_level: 447.40
- proposed target_price: 323.00
- proposed invalidation_level: 424.98
- entry_candidate_price: 447.50
- room_to_target: -124.50
- target_distance: -124.40
- max_favorable_move: nan
- higher_timeframe_obstacle_check: TBD — manual chart review required
- target_already_hit_check: true

## Candidate event summary
- resistance_touched: true
- close_above_resistance: false
- target_hit_before_confirmation: true
- target_hit_after_confirmation: false
- invalidation_hit: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: nan
- max_close_after_confirmation: nan
- target_distance: -124.40
- max_favorable_move: nan
- target_already_hit_before_confirmation: true
- suggested_classification: contradicted

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
