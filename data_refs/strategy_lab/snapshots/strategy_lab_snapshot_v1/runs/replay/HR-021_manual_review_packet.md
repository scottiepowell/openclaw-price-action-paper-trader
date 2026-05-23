# HR-021 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-021
- related_candidate_id: PTC-021
- symbol: GOOGL
- date_window: 2023-07-25 to 2023-07-25
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/GOOGL/1Day/GOOGL_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/GOOGL/5Min/GOOGL_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-07-25T04:00:00+00:00 | O:121.345 H:123.12 L:121.03 C:122.21 V:932032 T:11601 VWAP:122.100664

## 5m OHLCV excerpt for the replay window
- 2023-07-25T13:25:00+00:00 | O:121.21 H:121.21 L:121.21 C:121.21 V:288 T:5 VWAP:121.21
- 2023-07-25T13:30:00+00:00 | O:121.345 H:122.44 L:121.345 C:121.985 V:24837 T:279 VWAP:122.058752
- 2023-07-25T13:35:00+00:00 | O:122.105 H:122.105 L:121.43 C:121.43 V:3170 T:41 VWAP:121.697017
- 2023-07-25T13:40:00+00:00 | O:121.32 H:121.71 L:121.32 C:121.66 V:7139 T:94 VWAP:121.562687
- 2023-07-25T13:45:00+00:00 | O:121.64 H:122.1 L:121.64 C:121.93 V:9632 T:76 VWAP:121.897183
- 2023-07-25T13:50:00+00:00 | O:121.91 H:121.96 L:121.605 C:121.96 V:8721 T:90 VWAP:121.789873
- 2023-07-25T13:55:00+00:00 | O:121.755 H:122.34 L:121.755 C:122.34 V:16722 T:119 VWAP:122.154323
- 2023-07-25T14:00:00+00:00 | O:122.335 H:122.34 L:121.76 C:121.76 V:10084 T:100 VWAP:122.049912
- 2023-07-25T14:05:00+00:00 | O:121.755 H:121.845 L:121.51 C:121.51 V:9613 T:92 VWAP:121.652553
- 2023-07-25T14:10:00+00:00 | O:121.555 H:121.595 L:121.32 C:121.39 V:15025 T:118 VWAP:121.495216
- 2023-07-25T14:15:00+00:00 | O:121.365 H:121.63 L:121.185 C:121.575 V:16850 T:190 VWAP:121.430514
- 2023-07-25T14:20:00+00:00 | O:121.54 H:121.71 L:121.54 C:121.655 V:18058 T:159 VWAP:121.64265
- ... 59 middle rows omitted ...
- 2023-07-25T19:20:00+00:00 | O:122.975 H:123.025 L:122.855 C:122.86 V:12959 T:126 VWAP:122.944049
- 2023-07-25T19:25:00+00:00 | O:122.86 H:122.93 L:122.82 C:122.93 V:16162 T:155 VWAP:122.874757
- 2023-07-25T19:30:00+00:00 | O:122.925 H:122.925 L:122.705 C:122.8 V:15155 T:178 VWAP:122.88159
- 2023-07-25T19:35:00+00:00 | O:122.795 H:122.85 L:122.73 C:122.73 V:11738 T:149 VWAP:122.794159
- 2023-07-25T19:40:00+00:00 | O:122.7 H:122.76 L:122.55 C:122.605 V:8336 T:131 VWAP:122.673292
- 2023-07-25T19:45:00+00:00 | O:122.655 H:122.78 L:122.625 C:122.655 V:13120 T:113 VWAP:122.687898
- 2023-07-25T19:50:00+00:00 | O:122.64 H:122.65 L:122.415 C:122.535 V:44672 T:344 VWAP:122.516789
- 2023-07-25T19:55:00+00:00 | O:122.46 H:122.46 L:122.22 C:122.22 V:42500 T:648 VWAP:122.332476
- 2023-07-25T20:00:00+00:00 | O:122.21 H:122.21 L:122.21 C:122.21 V:400 T:2 VWAP:122.21
- 2023-07-25T20:10:00+00:00 | O:128.4 H:130.67 L:128.4 C:130.37 V:19436 T:494 VWAP:129.341333
- 2023-07-25T20:15:00+00:00 | O:130.4 H:130.5 L:130.4 C:130.4 V:9055 T:130 VWAP:130.415361
- 2023-07-25T20:40:00+00:00 | O:130.32 H:130.32 L:130.32 C:130.32 V:352 T:8 VWAP:130.32

## Level interaction analysis
- support_level: 121.03
  nearest_5m_bar: 2023-07-25T14:30:00+00:00 | O:121.3 H:121.3 L:121.03 C:121.08 | distance:0.0000
- resistance_level: 123.12
  nearest_5m_bar: 2023-07-25T17:20:00+00:00 | O:122.88 H:123.12 L:122.875 C:122.99 | distance:0.0000
- target_price: 125.12
  nearest_5m_bar: 2023-07-25T17:20:00+00:00 | O:122.88 H:123.12 L:122.875 C:122.99 | distance:2.0000
- invalidation_level: 120.93
  nearest_5m_bar: 2023-07-25T14:30:00+00:00 | O:121.3 H:121.3 L:121.03 C:121.08 | distance:0.1000
- any 5m close above resistance: true
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: true
- target hit before confirmation: false
- target hit after confirmation: true
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 121.03
- proposed resistance_level: 123.12
- proposed target_price: 125.12
- proposed invalidation_level: 120.93
- entry_candidate_price: 123.22
- room_to_target: 1.90
- target_distance: 2.00
- max_favorable_move: 7.55
- higher_timeframe_obstacle_check: TBD — manual chart review required
- target_already_hit_check: false

## Candidate event summary
- resistance_touched: true
- close_above_resistance: true
- target_hit_before_confirmation: false
- target_hit_after_confirmation: true
- invalidation_hit: false
- invalidation_hit_after_confirmation: false
- max_high_after_confirmation: 130.67
- max_close_after_confirmation: 130.40
- target_distance: 2.00
- max_favorable_move: 7.55
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
