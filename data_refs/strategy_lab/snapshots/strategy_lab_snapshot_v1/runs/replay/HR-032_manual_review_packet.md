# HR-032 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-032
- related_candidate_id: PTC-032
- symbol: TSLA
- date_window: 2023-07-20 to 2023-07-20
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/TSLA/1Day/TSLA_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0/symbols/TSLA/5Min/TSLA_5Min_2023.parquet

## 1D context rows
- 2023-07-17T04:00:00+00:00 | O:286.73 H:292.15 L:283.63 C:290.33 V:584520 T:9652 VWAP:288.224727
- 2023-07-18T04:00:00+00:00 | O:290.24 H:295.21 L:286.08 C:293.26 V:570523 T:9436 VWAP:290.376366
- 2023-07-19T04:00:00+00:00 | O:296.05 H:299.25 L:289.57 C:291.2 V:838129 T:14839 VWAP:294.818164
- 2023-07-20T04:00:00+00:00 | O:279.48 H:280.93 L:261.2 C:263.02 V:1248437 T:18565 VWAP:271.388516

## 5m breakdown context
- prior_support: 291.06
- breakdown candle: 2023-07-20T13:30:00+00:00 | close: 280.48
- breakdown_amount: 10.58

## 5m bars around the breakdown
- 2023-07-19T19:05:00+00:00 | O:291.79 H:292.505 L:291.785 C:292.505 V:7806 T:117 VWAP:292.051124
- 2023-07-19T19:10:00+00:00 | O:292.51 H:293.0 L:292.51 C:292.72 V:5331 T:97 VWAP:292.739386
- 2023-07-19T19:15:00+00:00 | O:292.82 H:293.49 L:292.82 C:293.49 V:4866 T:87 VWAP:293.132252
- 2023-07-19T19:20:00+00:00 | O:293.47 H:293.76 L:293.11 C:293.32 V:4796 T:119 VWAP:293.412733
- 2023-07-19T19:25:00+00:00 | O:293.35 H:293.75 L:293.26 C:293.72 V:9004 T:122 VWAP:293.445317
- 2023-07-19T19:30:00+00:00 | O:293.64 H:293.975 L:293.38 C:293.71 V:7272 T:119 VWAP:293.729916
- 2023-07-19T19:35:00+00:00 | O:293.69 H:293.69 L:292.62 C:292.62 V:7164 T:145 VWAP:293.015615
- 2023-07-19T19:40:00+00:00 | O:292.82 H:293.16 L:292.18 C:292.36 V:8516 T:143 VWAP:292.797669
- 2023-07-19T19:45:00+00:00 | O:292.6 H:292.68 L:291.72 C:292.27 V:12766 T:200 VWAP:292.359546
- 2023-07-19T19:50:00+00:00 | O:292.06 H:292.27 L:291.81 C:291.92 V:11209 T:220 VWAP:292.090231
- 2023-07-19T19:55:00+00:00 | O:291.91 H:292.11 L:291.06 C:291.2 V:40445 T:625 VWAP:291.690847
- 2023-07-19T20:35:00+00:00 | O:293.0 H:293.0 L:293.0 C:293.0 V:510 T:10 VWAP:293.0
- 2023-07-20T13:30:00+00:00 | O:279.48 H:280.93 L:276.6 C:280.48 V:181813 T:2278 VWAP:278.56263
- 2023-07-20T13:35:00+00:00 | O:280.38 H:280.39 L:279.13 C:279.21 V:56097 T:855 VWAP:279.871392
- 2023-07-20T13:40:00+00:00 | O:279.21 H:279.21 L:276.2 C:278.17 V:35759 T:466 VWAP:277.712724
- 2023-07-20T13:45:00+00:00 | O:277.95 H:278.53 L:276.8 C:276.8 V:25805 T:337 VWAP:277.776725
- 2023-07-20T13:50:00+00:00 | O:276.85 H:277.34 L:276.0 C:276.45 V:32108 T:347 VWAP:276.719567
- 2023-07-20T13:55:00+00:00 | O:276.25 H:277.45 L:275.26 C:275.63 V:43835 T:466 VWAP:276.367964
- 2023-07-20T14:00:00+00:00 | O:275.56 H:275.96 L:272.77 C:272.955 V:34199 T:476 VWAP:274.206811
- 2023-07-20T14:05:00+00:00 | O:272.79 H:273.58 L:272.11 C:272.62 V:35523 T:404 VWAP:272.846104
- 2023-07-20T14:10:00+00:00 | O:272.61 H:274.12 L:272.52 C:274.12 V:12597 T:227 VWAP:273.452901
- 2023-07-20T14:15:00+00:00 | O:274.0 H:274.575 L:273.19 C:274.19 V:27298 T:321 VWAP:273.95604
- 2023-07-20T14:20:00+00:00 | O:274.24 H:274.24 L:272.89 C:272.89 V:14069 T:229 VWAP:273.56196
- 2023-07-20T14:25:00+00:00 | O:272.98 H:273.33 L:272.51 C:272.57 V:12126 T:174 VWAP:272.900446
- 2023-07-20T14:30:00+00:00 | O:272.5 H:272.5 L:270.67 C:271.125 V:18919 T:273 VWAP:271.695101
- 2023-07-20T14:35:00+00:00 | O:270.9 H:271.53 L:270.13 C:270.13 V:10913 T:163 VWAP:270.917728
- 2023-07-20T14:40:00+00:00 | O:270.12 H:270.88 L:269.5 C:270.76 V:21162 T:339 VWAP:270.25317
- 2023-07-20T14:45:00+00:00 | O:270.675 H:271.95 L:270.36 C:271.92 V:11787 T:174 VWAP:270.929542
- 2023-07-20T14:50:00+00:00 | O:271.78 H:272.215 L:271.15 C:271.44 V:15960 T:259 VWAP:271.785383
- 2023-07-20T14:55:00+00:00 | O:271.4 H:271.4 L:269.89 C:269.97 V:17578 T:284 VWAP:270.577476
- 2023-07-20T15:00:00+00:00 | O:270.07 H:271.54 L:269.72 C:271.31 V:13219 T:212 VWAP:270.487795
- 2023-07-20T15:05:00+00:00 | O:271.28 H:271.78 L:270.34 C:270.47 V:7608 T:122 VWAP:271.028817
- 2023-07-20T15:10:00+00:00 | O:270.505 H:271.17 L:270.41 C:270.925 V:3983 T:62 VWAP:270.765491
- 2023-07-20T15:15:00+00:00 | O:270.82 H:270.9 L:269.59 C:270.545 V:14311 T:245 VWAP:270.243856
- 2023-07-20T15:20:00+00:00 | O:270.41 H:271.45 L:270.41 C:271.45 V:6410 T:82 VWAP:270.825349
- 2023-07-20T15:25:00+00:00 | O:271.4 H:271.59 L:270.74 C:270.9 V:10294 T:127 VWAP:271.144495
- 2023-07-20T15:30:00+00:00 | O:270.865 H:271.855 L:270.795 C:271.82 V:10425 T:135 VWAP:271.341882

## Downside follow-through rows
- min_low_next_6_bars: 272.77
- min_low_next_12_bars: 270.67
- min_low_next_24_bars: 269.50
- close_after_6_bars: 272.95
- close_after_12_bars: 271.12
- close_after_24_bars: 271.82

## Candidate chart-level worksheet
- proposed support_level: 291.06
- proposed resistance_level: 301.64
- proposed target_price: 269.90
- proposed invalidation_level: 301.64
- entry_candidate_price: 280.48
- target_distance: 21.16
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 269.50
- max_close_after_confirmation: 280.48
- suggested_classification: confirmed_breakdown

## Manual promotion workflow
- manual_review_status: pending
- manual_review_outcome: TBD
- manual_review_classification: TBD
- manual_reviewer_notes: TBD
- broker_action_allowed: false

## Recommended classification options
- confirmed_breakdown
- confirmed_breakdown_no_target_hit
- support_touch_no_trigger
- failed_breakdown_reclaim
- ambiguous
- insufficient
- contradicted
- blocked_data_quality

## Boundary
- No trade signal
- No profitability claim
- No execution readiness
- No broker action allowed
