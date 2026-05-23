# HR-028 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-028
- related_candidate_id: PTC-028
- symbol: AAPL
- date_window: 2023-09-07 to 2023-09-07
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AAPL/1Day/AAPL_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/AAPL/5Min/AAPL_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-09-07T04:00:00+00:00 | O:175.22 H:178.205 L:173.55 C:177.585 V:2208228 T:20849 VWAP:176.635416

## 5m OHLCV excerpt for the replay window
- 2023-09-07T12:35:00+00:00 | O:176.93 H:176.93 L:176.93 C:176.93 V:200 T:3 VWAP:176.93
- 2023-09-07T12:50:00+00:00 | O:176.21 H:176.21 L:176.21 C:176.21 V:357 T:8 VWAP:176.21
- 2023-09-07T12:55:00+00:00 | O:176.18 H:176.18 L:176.18 C:176.18 V:370 T:7 VWAP:176.18
- 2023-09-07T13:00:00+00:00 | O:176.07 H:176.13 L:176.07 C:176.13 V:1280 T:28 VWAP:176.1
- 2023-09-07T13:05:00+00:00 | O:176.13 H:176.13 L:176.13 C:176.13 V:158 T:4 VWAP:176.13
- 2023-09-07T13:20:00+00:00 | O:175.82 H:175.82 L:175.81 C:175.81 V:1361 T:27 VWAP:175.818333
- 2023-09-07T13:25:00+00:00 | O:175.62 H:175.62 L:174.55 C:174.55 V:1554 T:37 VWAP:174.9175
- 2023-09-07T13:30:00+00:00 | O:175.22 H:175.35 L:173.55 C:175.025 V:314142 T:1889 VWAP:174.629633
- 2023-09-07T13:35:00+00:00 | O:175.075 H:176.82 L:174.98 C:176.65 V:102494 T:856 VWAP:176.24783
- 2023-09-07T13:40:00+00:00 | O:176.6 H:177.475 L:176.42 C:176.89 V:65926 T:686 VWAP:177.040478
- 2023-09-07T13:45:00+00:00 | O:176.895 H:177.79 L:176.615 C:176.84 V:91935 T:695 VWAP:177.158509
- 2023-09-07T13:50:00+00:00 | O:176.8 H:177.63 L:176.06 C:176.085 V:63216 T:592 VWAP:176.924377
- ... 62 middle rows omitted ...
- 2023-09-07T19:05:00+00:00 | O:177.07 H:177.07 L:176.785 C:176.87 V:13906 T:208 VWAP:176.957788
- 2023-09-07T19:10:00+00:00 | O:176.88 H:177.26 L:176.88 C:177.25 V:14733 T:147 VWAP:177.121884
- 2023-09-07T19:15:00+00:00 | O:177.24 H:177.315 L:177.18 C:177.18 V:20254 T:193 VWAP:177.249147
- 2023-09-07T19:20:00+00:00 | O:177.18 H:177.18 L:176.97 C:177.035 V:11578 T:153 VWAP:177.059824
- 2023-09-07T19:25:00+00:00 | O:177.02 H:177.46 L:176.995 C:177.455 V:15691 T:187 VWAP:177.264314
- 2023-09-07T19:30:00+00:00 | O:177.455 H:177.765 L:177.445 C:177.59 V:19641 T:171 VWAP:177.63823
- 2023-09-07T19:35:00+00:00 | O:177.595 H:177.665 L:177.45 C:177.55 V:29799 T:219 VWAP:177.566653
- 2023-09-07T19:40:00+00:00 | O:177.545 H:177.955 L:177.545 C:177.94 V:22740 T:241 VWAP:177.684091
- 2023-09-07T19:45:00+00:00 | O:177.94 H:177.995 L:177.79 C:177.885 V:11398 T:195 VWAP:177.897918
- 2023-09-07T19:50:00+00:00 | O:177.915 H:178.12 L:177.85 C:178.015 V:46762 T:449 VWAP:177.972248
- 2023-09-07T19:55:00+00:00 | O:177.92 H:177.95 L:177.575 C:177.585 V:117423 T:991 VWAP:177.82709
- 2023-09-07T20:05:00+00:00 | O:178.13 H:178.13 L:178.13 C:178.13 V:100 T:1 VWAP:178.13

## Level interaction analysis
- support_level: 173.55
  nearest_5m_bar: 2023-09-07T13:30:00+00:00 | O:175.22 H:175.35 L:173.55 C:175.025 | distance:0.0000
- resistance_level: 178.21
  nearest_5m_bar: 2023-09-07T15:15:00+00:00 | O:177.865 H:178.205 L:177.715 C:177.755 | distance:0.0000
- target_price: 180.21
  nearest_5m_bar: 2023-09-07T15:15:00+00:00 | O:177.865 H:178.205 L:177.715 C:177.755 | distance:2.0000
- invalidation_level: 173.45
  nearest_5m_bar: 2023-09-07T13:30:00+00:00 | O:175.22 H:175.35 L:173.55 C:175.025 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 173.55
- proposed resistance_level: 178.21
- proposed target_price: 180.21
- proposed invalidation_level: 173.45
- entry_candidate_price: 178.31
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
