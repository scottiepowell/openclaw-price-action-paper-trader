# HR-013 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-013
- related_candidate_id: PTC-013
- symbol: META
- date_window: 2023-10-30 to 2023-10-30
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/1Day/META_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/5Min/META_5Min_2023.parquet

## 1D context rows
- 2023-10-25T04:00:00+00:00 | O:309.92 H:310.83 L:298.85 C:299.69 V:727558 T:13457 VWAP:302.881943
- 2023-10-26T04:00:00+00:00 | O:294.1 H:294.585 L:279.46 C:288.345 V:2016205 T:24154 VWAP:286.937403
- 2023-10-27T04:00:00+00:00 | O:294.58 H:299.29 L:293.05 C:296.74 V:595540 T:10998 VWAP:296.129926
- 2023-10-30T04:00:00+00:00 | O:299.65 H:309.37 L:299.06 C:302.56 V:653526 T:9345 VWAP:303.859381

## 5m breakdown context
- prior_support: 302.87
- breakdown candle: 2023-10-30T14:40:00+00:00 | close: 302.08
- breakdown_amount: 0.79

## 5m bars around the breakdown
- 2023-10-30T13:40:00+00:00 | O:304.675 H:305.92 L:304.29 C:305.03 V:37507 T:562 VWAP:305.070449
- 2023-10-30T13:45:00+00:00 | O:305.225 H:307.25 L:304.72 C:306.58 V:28309 T:400 VWAP:306.248661
- 2023-10-30T13:50:00+00:00 | O:306.955 H:307.82 L:306.57 C:306.905 V:25700 T:440 VWAP:307.208104
- 2023-10-30T13:55:00+00:00 | O:306.62 H:307.8 L:306.355 C:307.72 V:17662 T:346 VWAP:306.889041
- 2023-10-30T14:00:00+00:00 | O:308.0 H:308.18 L:306.615 C:307.025 V:22371 T:385 VWAP:307.473101
- 2023-10-30T14:05:00+00:00 | O:306.82 H:309.37 L:306.82 C:308.995 V:11468 T:221 VWAP:308.023479
- 2023-10-30T14:10:00+00:00 | O:308.64 H:308.64 L:305.95 C:305.95 V:8764 T:127 VWAP:307.160901
- 2023-10-30T14:15:00+00:00 | O:306.025 H:306.355 L:304.97 C:305.17 V:6401 T:93 VWAP:305.759916
- 2023-10-30T14:20:00+00:00 | O:305.26 H:305.26 L:303.855 C:304.6 V:8198 T:116 VWAP:304.346764
- 2023-10-30T14:25:00+00:00 | O:304.9 H:304.9 L:303.32 C:303.59 V:22002 T:121 VWAP:304.562373
- 2023-10-30T14:30:00+00:00 | O:303.56 H:303.76 L:302.87 C:303.76 V:3613 T:71 VWAP:303.416437
- 2023-10-30T14:35:00+00:00 | O:303.825 H:304.01 L:303.06 C:303.345 V:3197 T:50 VWAP:303.638532
- 2023-10-30T14:40:00+00:00 | O:303.23 H:303.95 L:302.08 C:302.08 V:6190 T:115 VWAP:302.840816
- 2023-10-30T14:45:00+00:00 | O:302.06 H:302.86 L:302.0 C:302.7 V:15368 T:191 VWAP:302.186588
- 2023-10-30T14:50:00+00:00 | O:302.4 H:303.3 L:302.065 C:302.99 V:1822 T:31 VWAP:302.821539
- 2023-10-30T14:55:00+00:00 | O:302.82 H:303.14 L:302.55 C:302.635 V:8550 T:112 VWAP:302.695505
- 2023-10-30T15:00:00+00:00 | O:302.82 H:304.115 L:302.785 C:303.42 V:5033 T:75 VWAP:303.426345
- 2023-10-30T15:05:00+00:00 | O:303.84 H:304.0 L:303.42 C:303.53 V:6109 T:90 VWAP:303.680006
- 2023-10-30T15:10:00+00:00 | O:303.98 H:304.475 L:303.41 C:303.48 V:11943 T:157 VWAP:303.884863
- 2023-10-30T15:15:00+00:00 | O:303.39 H:304.095 L:302.89 C:303.84 V:16229 T:171 VWAP:303.567648
- 2023-10-30T15:20:00+00:00 | O:303.995 H:304.74 L:303.55 C:303.7 V:10486 T:152 VWAP:304.047668
- 2023-10-30T15:25:00+00:00 | O:303.725 H:303.95 L:303.12 C:303.77 V:6899 T:128 VWAP:303.639416
- 2023-10-30T15:30:00+00:00 | O:304.02 H:304.29 L:303.6 C:304.025 V:4975 T:84 VWAP:303.976967
- 2023-10-30T15:35:00+00:00 | O:304.375 H:304.48 L:303.385 C:303.385 V:2244 T:45 VWAP:304.092222
- 2023-10-30T15:40:00+00:00 | O:303.3 H:303.33 L:302.41 C:302.745 V:2282 T:48 VWAP:302.844615
- 2023-10-30T15:45:00+00:00 | O:303.105 H:303.105 L:302.67 C:302.88 V:3514 T:41 VWAP:302.796782
- 2023-10-30T15:50:00+00:00 | O:303.06 H:303.885 L:303.005 C:303.84 V:3544 T:49 VWAP:303.489516
- 2023-10-30T15:55:00+00:00 | O:303.76 H:304.515 L:303.73 C:304.11 V:5242 T:84 VWAP:304.0343
- 2023-10-30T16:00:00+00:00 | O:304.07 H:304.28 L:303.83 C:304.15 V:5694 T:67 VWAP:304.062631
- 2023-10-30T16:05:00+00:00 | O:303.92 H:304.1 L:303.79 C:303.79 V:1064 T:13 VWAP:303.933
- 2023-10-30T16:10:00+00:00 | O:304.13 H:304.52 L:303.88 C:303.91 V:2386 T:46 VWAP:304.194412
- 2023-10-30T16:15:00+00:00 | O:304.07 H:304.46 L:303.45 C:303.45 V:4582 T:76 VWAP:303.947143
- 2023-10-30T16:20:00+00:00 | O:303.41 H:303.535 L:302.83 C:302.83 V:5287 T:67 VWAP:303.266499
- 2023-10-30T16:25:00+00:00 | O:302.88 H:302.92 L:302.48 C:302.48 V:7801 T:93 VWAP:302.647919
- 2023-10-30T16:30:00+00:00 | O:302.34 H:302.64 L:302.26 C:302.52 V:2003 T:29 VWAP:302.434444
- 2023-10-30T16:35:00+00:00 | O:302.49 H:303.03 L:302.49 C:302.515 V:1549 T:27 VWAP:302.7405
- 2023-10-30T16:40:00+00:00 | O:302.315 H:302.62 L:301.825 C:301.98 V:3705 T:100 VWAP:302.277396

## Downside follow-through rows
- min_low_next_6_bars: 302.00
- min_low_next_12_bars: 302.00
- min_low_next_24_bars: 301.82
- close_after_6_bars: 303.48
- close_after_12_bars: 302.75
- close_after_24_bars: 301.98

## Candidate chart-level worksheet
- proposed support_level: 302.87
- proposed resistance_level: 303.66
- proposed target_price: 301.29
- proposed invalidation_level: 303.87
- entry_candidate_price: 302.08
- target_distance: 1.58
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: false
- invalidation_hit_after_confirmation: true
- min_low_after_confirmation: 301.82
- max_close_after_confirmation: 304.15
- suggested_classification: failed_breakdown_reclaim

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
