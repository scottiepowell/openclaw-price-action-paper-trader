# HR-020 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-020
- related_candidate_id: PTC-020
- symbol: AVGO
- date_window: 2023-05-30 to 2023-05-30
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AVGO/1Day/AVGO_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AVGO/5Min/AVGO_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-05-30T04:00:00+00:00 | O:835.83 H:920.0 L:799.61 C:803.44 V:734303 T:15658 VWAP:847.135164

## 5m OHLCV excerpt for the replay window
- 2023-05-30T13:30:00+00:00 | O:835.83 H:854.0 L:821.97 C:853.71 V:29089 T:439 VWAP:840.296296
- 2023-05-30T13:35:00+00:00 | O:853.985 H:860.89 L:844.44 C:860.08 V:15830 T:204 VWAP:852.101261
- 2023-05-30T13:40:00+00:00 | O:859.62 H:883.79 L:859.62 C:883.79 V:31884 T:445 VWAP:869.484595
- 2023-05-30T13:45:00+00:00 | O:883.515 H:917.8 L:881.88 C:902.43 V:39740 T:738 VWAP:899.074521
- 2023-05-30T13:50:00+00:00 | O:901.855 H:920.0 L:888.995 C:893.3 V:27625 T:427 VWAP:901.750125
- 2023-05-30T13:55:00+00:00 | O:892.05 H:893.045 L:879.78 C:882.47 V:20304 T:353 VWAP:887.18473
- 2023-05-30T14:00:00+00:00 | O:877.735 H:881.61 L:871.99 C:873.825 V:18375 T:379 VWAP:876.26226
- 2023-05-30T14:05:00+00:00 | O:875.39 H:879.27 L:869.96 C:874.76 V:19827 T:348 VWAP:874.728191
- 2023-05-30T14:10:00+00:00 | O:874.55 H:878.15 L:866.13 C:870.0 V:12212 T:244 VWAP:872.759517
- 2023-05-30T14:15:00+00:00 | O:873.08 H:874.31 L:864.7 C:873.86 V:10199 T:182 VWAP:869.723045
- 2023-05-30T14:20:00+00:00 | O:874.68 H:876.12 L:868.0 C:869.45 V:20839 T:252 VWAP:873.960951
- 2023-05-30T14:25:00+00:00 | O:868.46 H:870.4 L:864.29 C:867.0 V:5594 T:111 VWAP:867.268501
- ... 54 middle rows omitted ...
- 2023-05-30T19:00:00+00:00 | O:807.96 H:809.71 L:806.11 C:809.59 V:7458 T:236 VWAP:807.929531
- 2023-05-30T19:05:00+00:00 | O:810.03 H:811.34 L:809.09 C:811.34 V:11409 T:265 VWAP:810.138786
- 2023-05-30T19:10:00+00:00 | O:810.99 H:811.87 L:809.67 C:811.87 V:5878 T:178 VWAP:810.585321
- 2023-05-30T19:15:00+00:00 | O:811.64 H:811.64 L:809.92 C:811.52 V:2851 T:126 VWAP:810.96582
- 2023-05-30T19:20:00+00:00 | O:811.75 H:814.405 L:811.75 C:814.06 V:6174 T:156 VWAP:813.631167
- 2023-05-30T19:25:00+00:00 | O:813.24 H:814.105 L:812.24 C:812.25 V:3683 T:126 VWAP:813.460964
- 2023-05-30T19:30:00+00:00 | O:812.32 H:812.47 L:807.8 C:807.8 V:8398 T:217 VWAP:810.446892
- 2023-05-30T19:35:00+00:00 | O:809.31 H:809.43 L:806.41 C:808.63 V:8824 T:226 VWAP:807.910266
- 2023-05-30T19:40:00+00:00 | O:808.6 H:808.84 L:806.725 C:807.18 V:3709 T:86 VWAP:808.027953
- 2023-05-30T19:45:00+00:00 | O:806.93 H:808.685 L:806.93 C:807.18 V:13338 T:210 VWAP:807.458755
- 2023-05-30T19:50:00+00:00 | O:807.17 H:807.6 L:799.61 C:801.37 V:17965 T:426 VWAP:803.533865
- 2023-05-30T19:55:00+00:00 | O:801.74 H:805.37 L:801.74 C:803.44 V:43311 T:719 VWAP:804.338262

## Level interaction analysis
- support_level: 799.61
  nearest_5m_bar: 2023-05-30T19:50:00+00:00 | O:807.17 H:807.6 L:799.61 C:801.37 | distance:0.0000
- resistance_level: 920.00
  nearest_5m_bar: 2023-05-30T13:50:00+00:00 | O:901.855 H:920.0 L:888.995 C:893.3 | distance:0.0000
- target_price: 922.00
  nearest_5m_bar: 2023-05-30T13:50:00+00:00 | O:901.855 H:920.0 L:888.995 C:893.3 | distance:2.0000
- invalidation_level: 799.51
  nearest_5m_bar: 2023-05-30T19:50:00+00:00 | O:807.17 H:807.6 L:799.61 C:801.37 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 799.61
- proposed resistance_level: 920.00
- proposed target_price: 922.00
- proposed invalidation_level: 799.51
- entry_candidate_price: 920.10
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
