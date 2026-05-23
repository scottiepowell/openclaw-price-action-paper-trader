# HR-024 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-024
- related_candidate_id: PTC-024
- symbol: MSFT
- date_window: 2023-10-24 to 2023-10-24
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/MSFT/1Day/MSFT_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/MSFT/5Min/MSFT_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-10-24T04:00:00+00:00 | O:331.12 H:331.8 L:327.6 C:330.63 V:617609 T:14380 VWAP:330.384603

## 5m OHLCV excerpt for the replay window
- 2023-10-24T13:15:00+00:00 | O:330.88 H:330.88 L:330.88 C:330.88 V:200 T:2 VWAP:330.88
- 2023-10-24T13:30:00+00:00 | O:331.12 H:331.49 L:329.985 C:331.325 V:14393 T:347 VWAP:330.738355
- 2023-10-24T13:35:00+00:00 | O:331.19 H:331.19 L:330.1 C:330.63 V:23764 T:641 VWAP:330.561274
- 2023-10-24T13:40:00+00:00 | O:331.055 H:331.525 L:330.37 C:330.95 V:14917 T:470 VWAP:330.976564
- 2023-10-24T13:45:00+00:00 | O:330.66 H:330.78 L:328.86 C:328.88 V:24367 T:415 VWAP:330.090144
- 2023-10-24T13:50:00+00:00 | O:328.865 H:330.16 L:328.79 C:330.16 V:7213 T:197 VWAP:329.231318
- 2023-10-24T13:55:00+00:00 | O:330.2 H:330.6 L:329.88 C:330.6 V:5209 T:170 VWAP:330.35119
- 2023-10-24T14:00:00+00:00 | O:330.485 H:330.87 L:329.84 C:330.05 V:7798 T:263 VWAP:330.38932
- 2023-10-24T14:05:00+00:00 | O:330.09 H:331.09 L:329.985 C:331.06 V:4393 T:177 VWAP:330.494318
- 2023-10-24T14:10:00+00:00 | O:331.15 H:331.16 L:330.66 C:330.68 V:5458 T:170 VWAP:330.89146
- 2023-10-24T14:15:00+00:00 | O:330.66 H:330.795 L:330.12 C:330.12 V:6124 T:180 VWAP:330.54431
- 2023-10-24T14:20:00+00:00 | O:330.28 H:330.72 L:329.88 C:330.56 V:10283 T:201 VWAP:330.358757
- ... 56 middle rows omitted ...
- 2023-10-24T19:05:00+00:00 | O:330.84 H:330.84 L:330.32 C:330.325 V:4255 T:149 VWAP:330.515891
- 2023-10-24T19:10:00+00:00 | O:330.345 H:330.7 L:330.345 C:330.675 V:6534 T:146 VWAP:330.576003
- 2023-10-24T19:15:00+00:00 | O:330.67 H:331.075 L:330.67 C:330.97 V:9479 T:143 VWAP:330.850234
- 2023-10-24T19:20:00+00:00 | O:330.99 H:331.38 L:330.99 C:331.38 V:8821 T:150 VWAP:331.222402
- 2023-10-24T19:25:00+00:00 | O:331.39 H:331.51 L:331.27 C:331.445 V:5611 T:126 VWAP:331.398947
- 2023-10-24T19:30:00+00:00 | O:331.5 H:331.63 L:331.39 C:331.4 V:6762 T:174 VWAP:331.498083
- 2023-10-24T19:35:00+00:00 | O:331.17 H:331.59 L:331.17 C:331.26 V:9539 T:147 VWAP:331.341095
- 2023-10-24T19:40:00+00:00 | O:331.235 H:331.535 L:331.235 C:331.52 V:9909 T:205 VWAP:331.403847
- 2023-10-24T19:45:00+00:00 | O:331.52 H:331.6 L:331.14 C:331.14 V:17319 T:273 VWAP:331.472313
- 2023-10-24T19:50:00+00:00 | O:331.2 H:331.5 L:331.04 C:331.15 V:22529 T:416 VWAP:331.231966
- 2023-10-24T19:55:00+00:00 | O:331.09 H:331.29 L:330.53 C:330.63 V:40586 T:750 VWAP:331.018611
- 2023-10-24T20:00:00+00:00 | O:346.48 H:346.48 L:346.48 C:346.48 V:3127 T:91 VWAP:346.48

## Level interaction analysis
- support_level: 327.60
  nearest_5m_bar: 2023-10-24T17:00:00+00:00 | O:328.01 H:328.025 L:327.6 C:327.95 | distance:0.0000
- resistance_level: 331.80
  nearest_5m_bar: 2023-10-24T14:35:00+00:00 | O:330.995 H:331.8 L:330.76 C:331.64 | distance:0.0000
- target_price: 333.80
  nearest_5m_bar: 2023-10-24T14:35:00+00:00 | O:330.995 H:331.8 L:330.76 C:331.64 | distance:2.0000
- invalidation_level: 327.50
  nearest_5m_bar: 2023-10-24T17:00:00+00:00 | O:328.01 H:328.025 L:327.6 C:327.95 | distance:0.1000
- any 5m close above resistance: true
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: true
- target hit before confirmation: false
- target hit after confirmation: true
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 327.60
- proposed resistance_level: 331.80
- proposed target_price: 333.80
- proposed invalidation_level: 327.50
- entry_candidate_price: 331.90
- room_to_target: 1.90
- target_distance: 2.00
- max_favorable_move: 14.68
- higher_timeframe_obstacle_check: TBD — manual chart review required
- target_already_hit_check: false

## Candidate event summary
- resistance_touched: true
- close_above_resistance: true
- target_hit_before_confirmation: false
- target_hit_after_confirmation: true
- invalidation_hit: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: 346.48
- max_close_after_confirmation: 346.48
- target_distance: 2.00
- max_favorable_move: 14.68
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
