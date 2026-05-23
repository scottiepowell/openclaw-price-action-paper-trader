# HR-008 Manual Review Packet

## Warning
- Discovery draft only
- Not verified replay evidence
- No trade signal
- No broker action allowed

## Replay case metadata
- replay_id: HR-008
- related_candidate_id: PTC-008
- symbol: AVGO
- date_window: 2023-05-16 to 2023-05-16
- timeframe_stack: 1D + 5m
- data files:
  - data_refs/google_drive/AVGO_1Day_sample.csv
  - data_refs/google_drive/AVGO_5Min_sample.csv

## 1D context rows
- 2023-05-15 04:00:00+00:00 | O:631.88 H:639.99 L:628.82 C:639.4 V:51171 T:1854 VWAP:636.673785
- 2023-05-16 04:00:00+00:00 | O:639.82 H:646.73 L:639.28 C:641.5 V:62869 T:2227 VWAP:643.857397

## 5m breakdown context
- prior_support: 644.34
- breakdown candle: 2023-05-16 19:50:00+00:00 | close: 642.30
- breakdown_amount: 2.04

## 5m bars around the breakdown
- 2023-05-16 18:40:00+00:00 | O:644.82 H:645.49 L:644.82 C:645.49 V:531 T:11 VWAP:645.113333
- 2023-05-16 18:45:00+00:00 | O:645.6 H:645.6 L:645.6 C:645.6 V:106 T:7 VWAP:645.6
- 2023-05-16 18:50:00+00:00 | O:646.18 H:646.62 L:646.18 C:646.6 V:904 T:30 VWAP:646.464074
- 2023-05-16 19:00:00+00:00 | O:646.12 H:646.12 L:645.99 C:645.99 V:489 T:20 VWAP:646.055
- 2023-05-16 19:10:00+00:00 | O:645.47 H:645.86 L:645.47 C:645.62 V:675 T:20 VWAP:645.695
- 2023-05-16 19:15:00+00:00 | O:645.47 H:645.47 L:645.47 C:645.47 V:105 T:5 VWAP:645.47
- 2023-05-16 19:20:00+00:00 | O:645.01 H:645.59 L:645.01 C:645.56 V:610 T:25 VWAP:645.386667
- 2023-05-16 19:25:00+00:00 | O:646.24 H:646.73 L:646.24 C:646.73 V:890 T:25 VWAP:646.42
- 2023-05-16 19:30:00+00:00 | O:646.36 H:646.36 L:646.06 C:646.22 V:964 T:29 VWAP:646.268903
- 2023-05-16 19:35:00+00:00 | O:645.89 H:645.89 L:645.89 C:645.89 V:215 T:7 VWAP:645.89
- 2023-05-16 19:40:00+00:00 | O:645.1 H:645.1 L:644.99 C:644.99 V:480 T:18 VWAP:645.045
- 2023-05-16 19:45:00+00:00 | O:644.96 H:644.96 L:644.34 C:644.9 V:1084 T:33 VWAP:644.653333
- 2023-05-16 19:50:00+00:00 | O:643.34 H:643.34 L:642.3 C:642.3 V:2073 T:48 VWAP:642.891667
- 2023-05-16 19:55:00+00:00 | O:641.81 H:642.41 L:641.38 C:641.5 V:6864 T:206 VWAP:642.049878
- 2023-05-17 13:30:00+00:00 | O:647.45 H:649.44 L:647.45 C:648.76 V:798 T:27 VWAP:648.358
- 2023-05-17 13:35:00+00:00 | O:649.77 H:650.195 L:649.495 C:650.195 V:1622 T:42 VWAP:649.940486
- 2023-05-17 13:40:00+00:00 | O:650.27 H:650.47 L:648.875 C:649.405 V:2718 T:61 VWAP:649.982323
- 2023-05-17 13:45:00+00:00 | O:649.17 H:649.305 L:648.995 C:649.24 V:1456 T:41 VWAP:649.144721
- 2023-05-17 13:50:00+00:00 | O:647.83 H:648.13 L:645.01 C:645.01 V:1552 T:36 VWAP:646.101818
- 2023-05-17 13:55:00+00:00 | O:645.66 H:646.04 L:645.66 C:646.04 V:358 T:8 VWAP:645.85
- 2023-05-17 14:00:00+00:00 | O:646.0 H:646.0 L:645.37 C:645.37 V:1079 T:26 VWAP:645.576667
- 2023-05-17 14:05:00+00:00 | O:645.91 H:646.85 L:645.91 C:646.85 V:698 T:16 VWAP:646.2725
- 2023-05-17 14:10:00+00:00 | O:646.635 H:648.29 L:646.635 C:648.29 V:833 T:11 VWAP:647.055497
- 2023-05-17 14:15:00+00:00 | O:648.87 H:648.87 L:648.7 C:648.7 V:225 T:6 VWAP:648.785
- 2023-05-17 14:20:00+00:00 | O:648.965 H:650.07 L:648.965 C:650.07 V:738 T:16 VWAP:649.355
- 2023-05-17 14:25:00+00:00 | O:650.26 H:650.43 L:650.26 C:650.275 V:923 T:28 VWAP:650.31625
- 2023-05-17 14:30:00+00:00 | O:650.81 H:650.81 L:650.43 C:650.43 V:388 T:14 VWAP:650.62
- 2023-05-17 14:35:00+00:00 | O:650.18 H:651.14 L:650.18 C:651.14 V:302 T:5 VWAP:650.596667
- 2023-05-17 14:40:00+00:00 | O:651.45 H:652.19 L:651.45 C:651.85 V:714 T:16 VWAP:651.855882
- 2023-05-17 14:45:00+00:00 | O:651.63 H:651.63 L:651.63 C:651.63 V:104 T:5 VWAP:651.63
- 2023-05-17 14:50:00+00:00 | O:651.75 H:651.75 L:651.53 C:651.53 V:542 T:19 VWAP:651.603333
- 2023-05-17 14:55:00+00:00 | O:652.15 H:652.16 L:652.15 C:652.16 V:477 T:18 VWAP:652.155
- 2023-05-17 15:00:00+00:00 | O:652.64 H:652.84 L:652.64 C:652.84 V:239 T:10 VWAP:652.74
- 2023-05-17 15:05:00+00:00 | O:653.01 H:653.01 L:652.04 C:652.04 V:929 T:25 VWAP:652.367154
- 2023-05-17 15:10:00+00:00 | O:652.99 H:653.005 L:652.99 C:653.005 V:311 T:10 VWAP:652.9975
- 2023-05-17 15:15:00+00:00 | O:653.49 H:654.585 L:653.49 C:654.53 V:1476 T:41 VWAP:654.023684
- 2023-05-17 15:20:00+00:00 | O:654.145 H:654.145 L:652.82 C:652.82 V:414 T:8 VWAP:653.455

## Downside follow-through rows
- min_low_next_6_bars: 641.38
- min_low_next_12_bars: 641.38
- min_low_next_24_bars: 641.38
- close_after_6_bars: 645.01
- close_after_12_bars: 650.07
- close_after_24_bars: 652.82

## Candidate chart-level worksheet
- proposed support_level: 644.34
- proposed resistance_level: 646.38
- proposed target_price: 640.26
- proposed invalidation_level: 646.38
- entry_candidate_price: 642.30
- target_distance: 4.08
- higher_timeframe_obstacle_check: TBD
- target_already_hit_check: TBD

## Candidate event summary
- close_below_support: true
- support_touched: true
- downside_target_hit_before_confirmation: false
- downside_target_hit_after_confirmation: false
- invalidation_hit_after_confirmation: true
- min_low_after_confirmation: 641.38
- max_close_after_confirmation: 654.53
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
