# HR-025 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-025
- related_candidate_id: PTC-025
- symbol: AAPL
- date_window: 2023-12-05 to 2023-12-05
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AAPL/1Day/AAPL_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AAPL/5Min/AAPL_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-12-05T05:00:00+00:00 | O:190.21 H:194.4 L:190.18 C:193.5 V:1450126 T:14612 VWAP:193.269987

## 5m OHLCV excerpt for the replay window
- 2023-12-05T14:30:00+00:00 | O:190.21 H:192.49 L:190.18 C:192.18 V:125722 T:992 VWAP:191.839827
- 2023-12-05T14:35:00+00:00 | O:192.06 H:192.93 L:192.01 C:192.445 V:53740 T:527 VWAP:192.53628
- 2023-12-05T14:40:00+00:00 | O:192.435 H:193.35 L:192.38 C:193.24 V:55661 T:526 VWAP:192.908069
- 2023-12-05T14:45:00+00:00 | O:193.22 H:193.22 L:192.75 C:192.855 V:28625 T:310 VWAP:192.988437
- 2023-12-05T14:50:00+00:00 | O:192.845 H:192.915 L:192.55 C:192.635 V:38687 T:182 VWAP:192.721812
- 2023-12-05T14:55:00+00:00 | O:192.56 H:192.95 L:192.56 C:192.82 V:24577 T:203 VWAP:192.819566
- 2023-12-05T15:00:00+00:00 | O:192.75 H:194.28 L:192.74 C:194.16 V:93834 T:640 VWAP:193.711374
- 2023-12-05T15:05:00+00:00 | O:194.2 H:194.255 L:193.33 C:193.335 V:51026 T:361 VWAP:193.745675
- 2023-12-05T15:10:00+00:00 | O:193.335 H:193.66 L:193.145 C:193.66 V:29684 T:274 VWAP:193.398277
- 2023-12-05T15:15:00+00:00 | O:193.725 H:193.89 L:193.44 C:193.89 V:16304 T:193 VWAP:193.664449
- 2023-12-05T15:20:00+00:00 | O:193.885 H:194.08 L:193.66 C:193.73 V:21077 T:249 VWAP:193.888169
- 2023-12-05T15:25:00+00:00 | O:193.78 H:193.86 L:193.225 C:193.57 V:23420 T:281 VWAP:193.449825
- ... 54 middle rows omitted ...
- 2023-12-05T20:00:00+00:00 | O:193.225 H:193.3 L:193.18 C:193.205 V:5632 T:67 VWAP:193.24781
- 2023-12-05T20:05:00+00:00 | O:193.18 H:193.23 L:193.145 C:193.185 V:9538 T:98 VWAP:193.18035
- 2023-12-05T20:10:00+00:00 | O:193.2 H:193.47 L:193.2 C:193.36 V:11649 T:130 VWAP:193.371122
- 2023-12-05T20:15:00+00:00 | O:193.36 H:193.385 L:193.325 C:193.375 V:9380 T:82 VWAP:193.349269
- 2023-12-05T20:20:00+00:00 | O:193.38 H:193.405 L:193.23 C:193.31 V:5400 T:77 VWAP:193.317352
- 2023-12-05T20:25:00+00:00 | O:193.28 H:193.345 L:193.13 C:193.195 V:38282 T:234 VWAP:193.248724
- 2023-12-05T20:30:00+00:00 | O:193.215 H:193.24 L:193.125 C:193.155 V:16382 T:198 VWAP:193.177177
- 2023-12-05T20:35:00+00:00 | O:193.15 H:193.17 L:193.065 C:193.09 V:9016 T:106 VWAP:193.110596
- 2023-12-05T20:40:00+00:00 | O:193.065 H:193.085 L:192.87 C:192.87 V:12836 T:173 VWAP:193.014323
- 2023-12-05T20:45:00+00:00 | O:192.895 H:193.08 L:192.87 C:193.025 V:11255 T:180 VWAP:192.96627
- 2023-12-05T20:50:00+00:00 | O:193.015 H:193.2 L:192.98 C:193.025 V:26875 T:327 VWAP:193.073174
- 2023-12-05T20:55:00+00:00 | O:193.02 H:193.53 L:193.02 C:193.5 V:67170 T:805 VWAP:193.302243

## Level interaction analysis
- support_level: 190.18
  nearest_5m_bar: 2023-12-05T14:30:00+00:00 | O:190.21 H:192.49 L:190.18 C:192.18 | distance:0.0000
- resistance_level: 194.40
  nearest_5m_bar: 2023-12-05T16:05:00+00:00 | O:194.155 H:194.4 L:194.135 C:194.22 | distance:0.0000
- target_price: 196.40
  nearest_5m_bar: 2023-12-05T16:05:00+00:00 | O:194.155 H:194.4 L:194.135 C:194.22 | distance:2.0000
- invalidation_level: 190.08
  nearest_5m_bar: 2023-12-05T14:30:00+00:00 | O:190.21 H:192.49 L:190.18 C:192.18 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 190.18
- proposed resistance_level: 194.40
- proposed target_price: 196.40
- proposed invalidation_level: 190.08
- entry_candidate_price: 194.50
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
