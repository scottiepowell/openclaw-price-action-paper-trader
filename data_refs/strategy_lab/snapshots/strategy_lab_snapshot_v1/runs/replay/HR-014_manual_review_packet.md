# HR-014 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-014
- related_candidate_id: PTC-014
- symbol: META
- date_window: 2023-11-29 to 2023-11-29
- timeframe_stack: 1D + 5m
- data files:
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/1Day/META_1Day_2023.parquet
  - /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_smoke_v1.0/symbols/META/5Min/META_5Min_2023.parquet

## 1D context rows
- 2023-11-24T05:00:00+00:00 | O:340.37 H:341.52 L:336.92 C:338.22 V:69645 T:1991 VWAP:338.450917
- 2023-11-27T05:00:00+00:00 | O:336.49 H:339.88 L:334.23 C:334.76 V:341741 T:5649 VWAP:337.689397
- 2023-11-28T05:00:00+00:00 | O:333.81 H:339.375 L:333.77 C:338.98 V:194537 T:3617 VWAP:336.308361
- 2023-11-29T05:00:00+00:00 | O:339.69 H:339.85 L:330.855 C:332.2 V:256516 T:5067 VWAP:334.351546

## 5m breakdown context
- prior_support: 336.81
- breakdown candle: 2023-11-29T14:55:00+00:00 | close: 336.75
- breakdown_amount: 0.06

## 5m bars around the breakdown
- 2023-11-28T20:25:00+00:00 | O:336.82 H:337.22 L:336.81 C:337.215 V:1151 T:29 VWAP:337.037857
- 2023-11-28T20:30:00+00:00 | O:337.12 H:337.57 L:337.12 C:337.425 V:1908 T:39 VWAP:337.414235
- 2023-11-28T20:35:00+00:00 | O:337.435 H:337.715 L:337.435 C:337.61 V:2228 T:52 VWAP:337.601287
- 2023-11-28T20:40:00+00:00 | O:337.675 H:337.765 L:337.53 C:337.64 V:4529 T:67 VWAP:337.631457
- 2023-11-28T20:45:00+00:00 | O:337.6 H:338.11 L:337.6 C:338.1 V:5666 T:102 VWAP:337.8519
- 2023-11-28T20:50:00+00:00 | O:338.31 H:338.795 L:338.31 C:338.795 V:11939 T:179 VWAP:338.536041
- 2023-11-28T20:55:00+00:00 | O:338.785 H:339.375 L:338.715 C:338.98 V:13216 T:229 VWAP:339.1573
- 2023-11-29T14:30:00+00:00 | O:339.69 H:339.85 L:338.29 C:338.29 V:20336 T:244 VWAP:338.951669
- 2023-11-29T14:35:00+00:00 | O:338.16 H:339.0 L:337.915 C:338.685 V:6576 T:95 VWAP:338.439995
- 2023-11-29T14:40:00+00:00 | O:338.645 H:338.855 L:338.125 C:338.35 V:5031 T:69 VWAP:338.503606
- 2023-11-29T14:45:00+00:00 | O:338.395 H:338.71 L:337.65 C:337.65 V:10499 T:164 VWAP:338.24827
- 2023-11-29T14:50:00+00:00 | O:337.55 H:337.93 L:336.91 C:337.93 V:3432 T:88 VWAP:337.473571
- 2023-11-29T14:55:00+00:00 | O:337.86 H:338.035 L:336.73 C:336.745 V:5068 T:75 VWAP:337.273488
- 2023-11-29T15:00:00+00:00 | O:336.82 H:337.08 L:334.68 C:334.87 V:12190 T:177 VWAP:335.894127
- 2023-11-29T15:05:00+00:00 | O:334.79 H:335.035 L:334.35 C:334.39 V:7152 T:126 VWAP:334.661407
- 2023-11-29T15:10:00+00:00 | O:334.275 H:334.7 L:334.14 C:334.65 V:3615 T:68 VWAP:334.392568
- 2023-11-29T15:15:00+00:00 | O:334.79 H:334.79 L:333.86 C:333.86 V:3530 T:58 VWAP:334.583793
- 2023-11-29T15:20:00+00:00 | O:333.865 H:333.975 L:332.685 C:332.685 V:7303 T:118 VWAP:333.253898
- 2023-11-29T15:25:00+00:00 | O:332.81 H:333.29 L:332.81 C:332.92 V:7039 T:159 VWAP:333.0651
- 2023-11-29T15:30:00+00:00 | O:332.88 H:333.385 L:332.67 C:332.67 V:10111 T:134 VWAP:332.9848
- 2023-11-29T15:35:00+00:00 | O:332.87 H:332.87 L:331.82 C:332.085 V:8797 T:174 VWAP:332.480045
- 2023-11-29T15:40:00+00:00 | O:332.5 H:332.685 L:332.43 C:332.67 V:3407 T:111 VWAP:332.528663
- 2023-11-29T15:45:00+00:00 | O:332.52 H:332.52 L:332.04 C:332.28 V:2163 T:59 VWAP:332.305833
- 2023-11-29T15:50:00+00:00 | O:332.46 H:333.17 L:332.4 C:333.11 V:4463 T:105 VWAP:332.814909
- 2023-11-29T15:55:00+00:00 | O:333.315 H:333.825 L:333.315 C:333.59 V:4782 T:73 VWAP:333.669878
- 2023-11-29T16:00:00+00:00 | O:333.29 H:333.95 L:333.27 C:333.95 V:2787 T:42 VWAP:333.585416
- 2023-11-29T16:05:00+00:00 | O:333.975 H:334.035 L:333.48 C:333.52 V:2648 T:58 VWAP:333.788571
- 2023-11-29T16:10:00+00:00 | O:333.28 H:333.48 L:332.75 C:332.79 V:4013 T:63 VWAP:333.139394
- 2023-11-29T16:15:00+00:00 | O:333.135 H:333.42 L:332.71 C:332.995 V:2625 T:37 VWAP:333.058479
- 2023-11-29T16:20:00+00:00 | O:332.29 H:332.32 L:331.9 C:331.98 V:1904 T:61 VWAP:332.130534
- 2023-11-29T16:25:00+00:00 | O:331.91 H:331.92 L:331.24 C:331.24 V:8734 T:217 VWAP:331.597699
- 2023-11-29T16:30:00+00:00 | O:331.37 H:331.37 L:330.855 C:331.15 V:7144 T:197 VWAP:331.173875
- 2023-11-29T16:35:00+00:00 | O:331.23 H:331.89 L:331.19 C:331.89 V:2199 T:77 VWAP:331.474231
- 2023-11-29T16:40:00+00:00 | O:331.85 H:332.04 L:331.75 C:332.04 V:2284 T:49 VWAP:331.881765
- 2023-11-29T16:45:00+00:00 | O:332.05 H:332.27 L:332.03 C:332.155 V:2264 T:30 VWAP:332.14975
- 2023-11-29T16:50:00+00:00 | O:332.145 H:332.715 L:332.025 C:332.705 V:2557 T:55 VWAP:332.2875
- 2023-11-29T16:55:00+00:00 | O:332.73 H:332.73 L:332.425 C:332.43 V:1074 T:23 VWAP:332.516429

## Downside follow-through rows
- min_low_next_6_bars: 332.69
- min_low_next_12_bars: 331.82
- min_low_next_24_bars: 330.86
- close_after_6_bars: 332.92
- close_after_12_bars: 333.59
- close_after_24_bars: 332.43

## Candidate chart-level worksheet
- proposed support_level: 336.81
- proposed resistance_level: 337.31
- proposed target_price: 335.81
- proposed invalidation_level: 337.81
- entry_candidate_price: 336.75
- target_distance: 1.00
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: true
- invalidation_hit_after_confirmation: true
- min_low_after_confirmation: 330.86
- max_close_after_confirmation: 336.75
- suggested_classification: ambiguous

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
