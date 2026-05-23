# HR-026 Manual Visual Review Packet

## Replay case metadata
- replay_id: HR-026
- related_candidate_id: PTC-026
- symbol: SPY
- date_window: 2023-07-06 to 2023-07-06
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/SPY/1Day/SPY_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/SPY/5Min/SPY_5Min_2023.parquet
- data_quality_status: PASSED

## 1D OHLCV rows for the replay window
- 2023-07-06T04:00:00+00:00 | O:439.39 H:440.07 L:437.07 C:439.69 V:1061407 T:10275 VWAP:438.643062

## 5m OHLCV excerpt for the replay window
- 2023-07-06T13:15:00+00:00 | O:439.4 H:439.4 L:439.4 C:439.4 V:500 T:1 VWAP:439.4
- 2023-07-06T13:30:00+00:00 | O:439.39 H:439.615 L:438.57 C:438.81 V:34613 T:313 VWAP:439.300658
- 2023-07-06T13:35:00+00:00 | O:438.8 H:439.075 L:438.61 C:439.005 V:39068 T:278 VWAP:438.738668
- 2023-07-06T13:40:00+00:00 | O:438.94 H:439.04 L:438.565 C:438.64 V:19451 T:190 VWAP:438.742217
- 2023-07-06T13:45:00+00:00 | O:438.57 H:439.065 L:438.4 C:438.83 V:18495 T:220 VWAP:438.778978
- 2023-07-06T13:50:00+00:00 | O:438.81 H:438.9 L:438.22 C:438.25 V:8573 T:125 VWAP:438.641104
- 2023-07-06T13:55:00+00:00 | O:438.27 H:438.41 L:438.06 C:438.275 V:19685 T:188 VWAP:438.177725
- 2023-07-06T14:00:00+00:00 | O:438.2 H:438.33 L:437.85 C:437.85 V:27398 T:250 VWAP:438.044919
- 2023-07-06T14:05:00+00:00 | O:437.83 H:437.97 L:437.505 C:437.63 V:14860 T:166 VWAP:437.696975
- 2023-07-06T14:10:00+00:00 | O:437.66 H:437.98 L:437.49 C:437.98 V:22943 T:221 VWAP:437.76025
- 2023-07-06T14:15:00+00:00 | O:438.02 H:438.135 L:437.61 C:437.72 V:17618 T:141 VWAP:437.953226
- 2023-07-06T14:20:00+00:00 | O:437.665 H:437.73 L:437.46 C:437.56 V:26565 T:201 VWAP:437.562568
- ... 59 middle rows omitted ...
- 2023-07-06T19:20:00+00:00 | O:439.745 H:439.93 L:439.705 C:439.86 V:11578 T:105 VWAP:439.833274
- 2023-07-06T19:25:00+00:00 | O:439.885 H:439.935 L:439.72 C:439.74 V:7769 T:95 VWAP:439.851507
- 2023-07-06T19:30:00+00:00 | O:439.74 H:439.74 L:439.555 C:439.685 V:11399 T:143 VWAP:439.625888
- 2023-07-06T19:35:00+00:00 | O:439.665 H:439.81 L:439.505 C:439.605 V:14513 T:125 VWAP:439.622939
- 2023-07-06T19:40:00+00:00 | O:439.51 H:439.675 L:439.495 C:439.615 V:12896 T:137 VWAP:439.564228
- 2023-07-06T19:45:00+00:00 | O:439.61 H:439.75 L:439.48 C:439.75 V:13622 T:177 VWAP:439.597336
- 2023-07-06T19:50:00+00:00 | O:439.93 H:439.93 L:439.525 C:439.535 V:52618 T:321 VWAP:439.734666
- 2023-07-06T19:55:00+00:00 | O:439.565 H:439.98 L:439.555 C:439.69 V:44777 T:433 VWAP:439.830837
- 2023-07-06T20:00:00+00:00 | O:439.69 H:439.87 L:439.69 C:439.87 V:3100 T:3 VWAP:439.710323
- 2023-07-06T20:05:00+00:00 | O:439.79 H:439.79 L:439.79 C:439.79 V:1432 T:1 VWAP:439.79
- 2023-07-06T20:10:00+00:00 | O:439.86 H:439.86 L:439.86 C:439.86 V:3678 T:4 VWAP:439.86
- 2023-07-06T20:15:00+00:00 | O:439.74 H:439.79 L:439.72 C:439.72 V:5543 T:5 VWAP:439.74812

## Level interaction analysis
- support_level: 437.07
  nearest_5m_bar: 2023-07-06T15:25:00+00:00 | O:437.205 H:437.49 L:437.07 C:437.38 | distance:0.0000
- resistance_level: 440.07
  nearest_5m_bar: 2023-07-06T19:00:00+00:00 | O:440.07 H:440.07 L:439.91 C:440.02 | distance:0.0000
- target_price: 418.00
  nearest_5m_bar: 2023-07-06T15:25:00+00:00 | O:437.205 H:437.49 L:437.07 C:437.38 | distance:19.0700
- invalidation_level: 437.02
  nearest_5m_bar: 2023-07-06T15:25:00+00:00 | O:437.205 H:437.49 L:437.07 C:437.38 | distance:0.0500
- any 5m close above resistance: false
- any 5m high touched/exceeded resistance: true
- any 5m close reached/exceeded target: true
- target hit before confirmation: true
- target hit after confirmation: false
- invalidation hit before confirmation: false
- invalidation hit after confirmation: false

## Candidate chart-level worksheet
- proposed support_level: 437.07
- proposed resistance_level: 440.07
- proposed target_price: 418.00
- proposed invalidation_level: 437.02
- entry_candidate_price: 440.12
- room_to_target: -22.12
- target_distance: -22.07
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
- target_distance: -22.07
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
