# HR-019 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-019
- related_candidate_id: PTC-019
- symbol: SPY
- date_window: 2023-09-19 to 2023-09-19
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/SPY/1Day/SPY_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/SPY/5Min/SPY_5Min_2023.parquet

## 1D context rows
- 2023-09-14T04:00:00+00:00 | O:449.08 H:451.06 L:447.72 C:450.4 V:1294030 T:11776 VWAP:449.895849
- 2023-09-15T04:00:00+00:00 | O:447.245 H:447.42 L:443.02 C:443.305 V:2127873 T:16601 VWAP:444.438466
- 2023-09-18T04:00:00+00:00 | O:443.04 H:444.965 L:442.57 C:443.63 V:934550 T:9194 VWAP:443.811236
- 2023-09-19T04:00:00+00:00 | O:442.78 H:443.22 L:439.97 C:442.62 V:1070394 T:9669 VWAP:441.737185

## 5m breakdown context
- prior_support: 443.18
- breakdown candle: 2023-09-19T13:30:00+00:00 | close: 442.75
- breakdown_amount: 0.43

## 5m bars around the breakdown
- 2023-09-18T19:15:00+00:00 | O:443.635 H:443.715 L:443.48 C:443.565 V:25794 T:201 VWAP:443.572128
- 2023-09-18T19:20:00+00:00 | O:443.54 H:443.54 L:443.23 C:443.265 V:15961 T:145 VWAP:443.417789
- 2023-09-18T19:25:00+00:00 | O:443.28 H:443.54 L:443.265 C:443.53 V:18101 T:165 VWAP:443.394594
- 2023-09-18T19:30:00+00:00 | O:443.47 H:443.48 L:443.205 C:443.22 V:15292 T:145 VWAP:443.356227
- 2023-09-18T19:35:00+00:00 | O:443.23 H:443.32 L:443.19 C:443.22 V:19762 T:187 VWAP:443.238361
- 2023-09-18T19:40:00+00:00 | O:443.23 H:443.45 L:443.19 C:443.265 V:16034 T:169 VWAP:443.316719
- 2023-09-18T19:45:00+00:00 | O:443.25 H:443.455 L:443.175 C:443.37 V:24733 T:263 VWAP:443.297973
- 2023-09-18T19:50:00+00:00 | O:443.31 H:443.495 L:443.26 C:443.3 V:49599 T:373 VWAP:443.36998
- 2023-09-18T19:55:00+00:00 | O:443.32 H:443.725 L:443.32 C:443.63 V:50124 T:511 VWAP:443.574993
- 2023-09-18T20:00:00+00:00 | O:443.73 H:443.73 L:443.63 C:443.63 V:4333 T:7 VWAP:443.673845
- 2023-09-18T20:05:00+00:00 | O:443.63 H:443.66 L:443.63 C:443.66 V:1700 T:2 VWAP:443.656471
- 2023-09-18T20:10:00+00:00 | O:443.74 H:443.74 L:443.74 C:443.74 V:100 T:1 VWAP:443.74
- 2023-09-19T13:30:00+00:00 | O:442.78 H:442.85 L:442.4 C:442.75 V:18614 T:129 VWAP:442.623454
- 2023-09-19T13:35:00+00:00 | O:442.735 H:442.93 L:442.63 C:442.9 V:8872 T:69 VWAP:442.774893
- 2023-09-19T13:40:00+00:00 | O:442.83 H:443.005 L:442.66 C:442.71 V:9565 T:110 VWAP:442.884764
- 2023-09-19T13:45:00+00:00 | O:442.94 H:443.09 L:442.77 C:442.88 V:6418 T:70 VWAP:442.915271
- 2023-09-19T13:50:00+00:00 | O:442.71 H:442.88 L:442.44 C:442.62 V:9788 T:89 VWAP:442.662861
- 2023-09-19T13:55:00+00:00 | O:442.51 H:442.68 L:442.15 C:442.19 V:12667 T:165 VWAP:442.334913
- 2023-09-19T14:00:00+00:00 | O:442.2 H:442.2 L:441.39 C:441.43 V:25087 T:153 VWAP:441.736401
- 2023-09-19T14:05:00+00:00 | O:441.4 H:441.64 L:441.33 C:441.41 V:21958 T:174 VWAP:441.489072
- 2023-09-19T14:10:00+00:00 | O:441.44 H:441.565 L:441.38 C:441.44 V:28779 T:200 VWAP:441.483484
- 2023-09-19T14:15:00+00:00 | O:441.46 H:441.62 L:441.095 C:441.57 V:23776 T:181 VWAP:441.353058
- 2023-09-19T14:20:00+00:00 | O:441.57 H:441.715 L:441.525 C:441.61 V:13302 T:137 VWAP:441.624625
- 2023-09-19T14:25:00+00:00 | O:441.67 H:441.765 L:441.37 C:441.56 V:12387 T:146 VWAP:441.542827
- 2023-09-19T14:30:00+00:00 | O:441.475 H:441.55 L:441.15 C:441.18 V:17330 T:181 VWAP:441.328867
- 2023-09-19T14:35:00+00:00 | O:441.15 H:441.31 L:440.68 C:440.68 V:20355 T:184 VWAP:441.109841
- 2023-09-19T14:40:00+00:00 | O:440.69 H:440.975 L:440.56 C:440.91 V:18271 T:143 VWAP:440.787401
- 2023-09-19T14:45:00+00:00 | O:441.0 H:441.1 L:440.75 C:440.79 V:6664 T:87 VWAP:440.912786
- 2023-09-19T14:50:00+00:00 | O:440.77 H:440.78 L:440.565 C:440.63 V:24936 T:235 VWAP:440.650419
- 2023-09-19T14:55:00+00:00 | O:440.645 H:440.72 L:440.51 C:440.6 V:27405 T:163 VWAP:440.632254
- 2023-09-19T15:00:00+00:00 | O:440.52 H:440.78 L:440.495 C:440.65 V:13116 T:167 VWAP:440.640979
- 2023-09-19T15:05:00+00:00 | O:440.7 H:440.75 L:440.59 C:440.74 V:8977 T:128 VWAP:440.64845
- 2023-09-19T15:10:00+00:00 | O:440.69 H:440.81 L:440.57 C:440.81 V:8318 T:114 VWAP:440.721051
- 2023-09-19T15:15:00+00:00 | O:440.85 H:440.865 L:440.555 C:440.63 V:12049 T:110 VWAP:440.687943
- 2023-09-19T15:20:00+00:00 | O:440.7 H:440.73 L:440.52 C:440.54 V:8761 T:117 VWAP:440.618633
- 2023-09-19T15:25:00+00:00 | O:440.55 H:440.865 L:440.55 C:440.855 V:14970 T:114 VWAP:440.766588
- 2023-09-19T15:30:00+00:00 | O:440.86 H:441.005 L:440.755 C:440.93 V:14434 T:169 VWAP:440.926863

## Downside follow-through rows
- min_low_next_6_bars: 441.39
- min_low_next_12_bars: 441.10
- min_low_next_24_bars: 440.50
- close_after_6_bars: 441.43
- close_after_12_bars: 441.18
- close_after_24_bars: 440.93

## Candidate chart-level worksheet
- proposed support_level: 443.18
- proposed resistance_level: 443.68
- proposed target_price: 442.18
- proposed invalidation_level: 444.18
- entry_candidate_price: 442.75
- target_distance: 1.00
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: false
- min_low_after_confirmation: 440.50
- max_close_after_confirmation: 442.90
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
