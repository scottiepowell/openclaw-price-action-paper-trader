# HR-027 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-027
- related_candidate_id: PTC-027
- symbol: IWM
- date_window: 2023-08-08 to 2023-08-08
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/IWM/1Day/IWM_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/IWM/5Min/IWM_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-08-08T04:00:00+00:00 | O:192.1 H:193.28 L:190.55 C:193.16 V:319488 T:3149 VWAP:191.977953

## 5m OHLCV excerpt for the replay window
- 2023-08-08T13:30:00+00:00 | O:192.1 H:192.1 L:191.03 C:191.695 V:30853 T:275 VWAP:191.482428
- 2023-08-08T13:35:00+00:00 | O:191.71 H:191.71 L:191.16 C:191.25 V:23228 T:169 VWAP:191.347758
- 2023-08-08T13:40:00+00:00 | O:191.16 H:191.36 L:191.08 C:191.15 V:11604 T:86 VWAP:191.181081
- 2023-08-08T13:45:00+00:00 | O:191.19 H:191.29 L:190.96 C:191.01 V:6198 T:63 VWAP:191.125207
- 2023-08-08T13:50:00+00:00 | O:190.98 H:191.46 L:190.93 C:191.46 V:6970 T:67 VWAP:191.185078
- 2023-08-08T13:55:00+00:00 | O:191.39 H:191.605 L:191.34 C:191.48 V:7008 T:96 VWAP:191.480318
- 2023-08-08T14:00:00+00:00 | O:191.435 H:191.435 L:191.1 C:191.18 V:7022 T:93 VWAP:191.267837
- 2023-08-08T14:05:00+00:00 | O:191.185 H:191.53 L:191.115 C:191.53 V:5067 T:65 VWAP:191.260455
- 2023-08-08T14:10:00+00:00 | O:191.49 H:191.49 L:190.91 C:190.91 V:5695 T:62 VWAP:191.2002
- 2023-08-08T14:15:00+00:00 | O:190.855 H:190.9 L:190.64 C:190.81 V:10065 T:107 VWAP:190.75022
- 2023-08-08T14:20:00+00:00 | O:190.81 H:190.87 L:190.55 C:190.87 V:3765 T:49 VWAP:190.695645
- 2023-08-08T14:25:00+00:00 | O:190.86 H:191.32 L:190.86 C:191.32 V:2163 T:27 VWAP:191.12725
- ... 58 middle rows omitted ...
- 2023-08-08T19:25:00+00:00 | O:193.22 H:193.255 L:193.08 C:193.08 V:3560 T:37 VWAP:193.130734
- 2023-08-08T19:30:00+00:00 | O:193.075 H:193.13 L:192.96 C:192.97 V:2380 T:31 VWAP:193.026438
- 2023-08-08T19:35:00+00:00 | O:193.02 H:193.03 L:192.935 C:192.99 V:10304 T:72 VWAP:192.985601
- 2023-08-08T19:40:00+00:00 | O:193.05 H:193.24 L:193.035 C:193.06 V:18773 T:130 VWAP:193.098379
- 2023-08-08T19:45:00+00:00 | O:193.1 H:193.28 L:193.09 C:193.23 V:9306 T:82 VWAP:193.214926
- 2023-08-08T19:50:00+00:00 | O:193.2 H:193.27 L:193.09 C:193.09 V:11418 T:99 VWAP:193.183563
- 2023-08-08T19:55:00+00:00 | O:193.075 H:193.23 L:193.075 C:193.16 V:29292 T:246 VWAP:193.168192
- 2023-08-08T20:05:00+00:00 | O:193.13 H:193.13 L:193.13 C:193.13 V:500 T:1 VWAP:193.13
- 2023-08-08T20:10:00+00:00 | O:193.08 H:193.08 L:193.08 C:193.08 V:500 T:1 VWAP:193.08
- 2023-08-08T20:20:00+00:00 | O:193.07 H:193.07 L:193.07 C:193.07 V:500 T:1 VWAP:193.07
- 2023-08-08T20:40:00+00:00 | O:193.06 H:193.06 L:193.06 C:193.06 V:300 T:1 VWAP:193.06
- 2023-08-08T20:50:00+00:00 | O:193.02 H:193.02 L:193.02 C:193.02 V:500 T:1 VWAP:193.02

## Level interaction analysis
- support_level: 190.55
  nearest_5m_bar: 2023-08-08T14:20:00+00:00 | O:190.81 H:190.87 L:190.55 C:190.87 | distance:0.0000
- resistance_level: 193.28
  nearest_5m_bar: 2023-08-08T19:45:00+00:00 | O:193.1 H:193.28 L:193.09 C:193.23 | distance:0.0000
- target_price: 195.28
  nearest_5m_bar: 2023-08-08T19:45:00+00:00 | O:193.1 H:193.28 L:193.09 C:193.23 | distance:2.0000
- invalidation_level: 190.45
  nearest_5m_bar: 2023-08-08T14:20:00+00:00 | O:190.81 H:190.87 L:190.55 C:190.87 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 190.55
- proposed resistance_level: 193.28
- proposed target_price: 195.28
- proposed invalidation_level: 190.45
- entry_candidate_price: 193.38
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
