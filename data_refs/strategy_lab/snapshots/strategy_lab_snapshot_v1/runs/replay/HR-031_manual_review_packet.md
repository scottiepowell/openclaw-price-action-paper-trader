# HR-031 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-031
- related_candidate_id: PTC-031
- symbol: META
- date_window: 2023-12-04 to 2023-12-04
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/META/1Day/META_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/META/5Min/META_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-12-04T05:00:00+00:00 | O:317.24 H:320.805 L:313.83 C:320.0 V:362112 T:6376 VWAP:316.75315

## 5m OHLCV excerpt for the replay window
- 2023-12-04T14:30:00+00:00 | O:317.24 H:317.25 L:314.945 C:315.62 V:27783 T:373 VWAP:315.724393
- 2023-12-04T14:35:00+00:00 | O:316.09 H:317.1 L:314.33 C:316.72 V:14591 T:221 VWAP:315.953498
- 2023-12-04T14:40:00+00:00 | O:316.615 H:316.615 L:315.14 C:315.25 V:9963 T:150 VWAP:315.716902
- 2023-12-04T14:45:00+00:00 | O:315.24 H:315.57 L:314.12 C:314.12 V:21191 T:262 VWAP:314.921899
- 2023-12-04T14:50:00+00:00 | O:313.95 H:315.13 L:313.83 C:314.77 V:11347 T:168 VWAP:314.642779
- 2023-12-04T14:55:00+00:00 | O:314.88 H:316.18 L:314.88 C:315.91 V:8308 T:133 VWAP:315.691775
- 2023-12-04T15:00:00+00:00 | O:315.93 H:317.92 L:315.79 C:317.92 V:10683 T:157 VWAP:317.059219
- 2023-12-04T15:05:00+00:00 | O:318.08 H:318.355 L:317.48 C:317.765 V:6974 T:124 VWAP:317.955568
- 2023-12-04T15:10:00+00:00 | O:317.5 H:317.6 L:315.92 C:315.95 V:5564 T:124 VWAP:316.86337
- 2023-12-04T15:15:00+00:00 | O:316.0 H:316.48 L:315.485 C:316.3 V:8839 T:262 VWAP:315.804402
- 2023-12-04T15:20:00+00:00 | O:316.45 H:316.63 L:315.445 C:315.445 V:5031 T:144 VWAP:316.066676
- 2023-12-04T15:25:00+00:00 | O:315.715 H:315.795 L:315.04 C:315.04 V:8054 T:164 VWAP:315.273832
- ... 54 middle rows omitted ...
- 2023-12-04T20:00:00+00:00 | O:317.9 H:318.315 L:317.9 C:318.075 V:2074 T:74 VWAP:318.146429
- 2023-12-04T20:05:00+00:00 | O:318.31 H:318.59 L:318.31 C:318.58 V:3403 T:82 VWAP:318.484357
- 2023-12-04T20:10:00+00:00 | O:318.565 H:318.565 L:318.31 C:318.31 V:1178 T:40 VWAP:318.417143
- 2023-12-04T20:15:00+00:00 | O:318.52 H:318.52 L:318.34 C:318.45 V:2090 T:64 VWAP:318.45073
- 2023-12-04T20:20:00+00:00 | O:318.52 H:318.71 L:318.52 C:318.64 V:936 T:28 VWAP:318.595246
- 2023-12-04T20:25:00+00:00 | O:318.69 H:318.87 L:318.56 C:318.865 V:1763 T:53 VWAP:318.730714
- 2023-12-04T20:30:00+00:00 | O:319.02 H:319.6 L:319.02 C:319.57 V:2949 T:56 VWAP:319.297665
- 2023-12-04T20:35:00+00:00 | O:319.55 H:319.6 L:319.32 C:319.46 V:2355 T:51 VWAP:319.448736
- 2023-12-04T20:40:00+00:00 | O:319.54 H:319.565 L:319.3 C:319.31 V:4044 T:80 VWAP:319.397674
- 2023-12-04T20:45:00+00:00 | O:319.42 H:320.26 L:319.365 C:320.215 V:3049 T:67 VWAP:319.813504
- 2023-12-04T20:50:00+00:00 | O:320.68 H:320.805 L:319.86 C:319.86 V:11542 T:176 VWAP:320.493775
- 2023-12-04T20:55:00+00:00 | O:319.86 H:320.06 L:319.78 C:320.0 V:11830 T:280 VWAP:319.946877

## Level interaction analysis
- support_level: 313.83
  nearest_5m_bar: 2023-12-04T14:50:00+00:00 | O:313.95 H:315.13 L:313.83 C:314.77 | distance:0.0000
- resistance_level: 320.81
  nearest_5m_bar: 2023-12-04T20:50:00+00:00 | O:320.68 H:320.805 L:319.86 C:319.86 | distance:0.0000
- target_price: 322.81
  nearest_5m_bar: 2023-12-04T20:50:00+00:00 | O:320.68 H:320.805 L:319.86 C:319.86 | distance:2.0000
- invalidation_level: 313.73
  nearest_5m_bar: 2023-12-04T14:50:00+00:00 | O:313.95 H:315.13 L:313.83 C:314.77 | distance:0.1000
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: false
- target hit before confirmation: false
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 313.83
- proposed resistance_level: 320.81
- proposed target_price: 322.81
- proposed invalidation_level: 313.73
- entry_candidate_price: 320.91
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
