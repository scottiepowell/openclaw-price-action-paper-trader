# Date-Diversified Replay Candidates

candidate_windows_found: 12
min_calendar_days_between_cases: 30
max_cases_per_symbol_per_month: 1
max_cases_per_symbol_total: 2
avoid_existing_replay_windows: true

## HR-020 (AVGO)
- symbol: AVGO
- side: bullish
- timestamp: 2023-05-30T13:30:00+00:00
- event_type: close_above_resistance
- prior_level: 814.98
- breakout_or_breakdown_amount: 38.73000000000002
- lookback_bars: 12
- reason_selected: bullish close_above_resistance event
- distance_from_nearest_existing_case_days: 12
- has_1d_context: true

## HR-021 (GOOGL)
- symbol: GOOGL
- side: bullish
- timestamp: 2023-07-25T20:10:00+00:00
- event_type: close_above_resistance
- prior_level: 123.05
- breakout_or_breakdown_amount: 7.320000000000007
- lookback_bars: 12
- reason_selected: bullish close_above_resistance event
- distance_from_nearest_existing_case_days: 6
- has_1d_context: true

## HR-022 (AMZN)
- symbol: AMZN
- side: bullish
- timestamp: 2023-08-03T20:00:00+00:00
- event_type: close_above_resistance
- prior_level: 129.36
- breakout_or_breakdown_amount: 8.23999999999998
- lookback_bars: 12
- reason_selected: bullish close_above_resistance event
- distance_from_nearest_existing_case_days: 6
- has_1d_context: true

## HR-023 (TSLA)
- symbol: TSLA
- side: bullish
- timestamp: 2023-09-11T13:00:00+00:00
- event_type: close_above_resistance
- prior_level: 248.76
- breakout_or_breakdown_amount: 16.53000000000003
- lookback_bars: 12
- reason_selected: bullish close_above_resistance event
- distance_from_nearest_existing_case_days: 8
- has_1d_context: true

## HR-024 (MSFT)
- symbol: MSFT
- side: bullish
- timestamp: 2023-10-24T20:00:00+00:00
- event_type: close_above_resistance
- prior_level: 331.63
- breakout_or_breakdown_amount: 14.850000000000023
- lookback_bars: 12
- reason_selected: bullish close_above_resistance event
- distance_from_nearest_existing_case_days: 6
- has_1d_context: true

## HR-025 (AAPL)
- symbol: AAPL
- side: bullish
- timestamp: 2023-12-05T14:30:00+00:00
- event_type: close_above_resistance
- prior_level: 189.65
- breakout_or_breakdown_amount: 2.530000000000001
- lookback_bars: 12
- reason_selected: bullish close_above_resistance event
- distance_from_nearest_existing_case_days: 6
- has_1d_context: true

## HR-026 (SPY)
- symbol: SPY
- side: bearish
- timestamp: 2023-07-06T13:15:00+00:00
- event_type: close_below_support
- prior_level: 443.05
- breakout_or_breakdown_amount: 3.650000000000034
- lookback_bars: 12
- reason_selected: bearish close_below_support event
- distance_from_nearest_existing_case_days: 8
- has_1d_context: true

## HR-027 (IWM)
- symbol: IWM
- side: bearish
- timestamp: 2023-08-08T13:30:00+00:00
- event_type: close_below_support
- prior_level: 193.975
- breakout_or_breakdown_amount: 2.280000000000001
- lookback_bars: 12
- reason_selected: bearish close_below_support event
- distance_from_nearest_existing_case_days: 1
- has_1d_context: true

## HR-028 (AAPL)
- symbol: AAPL
- side: bearish
- timestamp: 2023-09-07T12:35:00+00:00
- event_type: close_below_support
- prior_level: 181.47
- breakout_or_breakdown_amount: 4.539999999999992
- lookback_bars: 12
- reason_selected: bearish close_below_support event
- distance_from_nearest_existing_case_days: 12
- has_1d_context: true

## HR-029 (QQQ)
- symbol: QQQ
- side: bearish
- timestamp: 2023-10-06T12:30:00+00:00
- event_type: close_below_support
- prior_level: 358.38
- breakout_or_breakdown_amount: 4.060000000000002
- lookback_bars: 12
- reason_selected: bearish close_below_support event
- distance_from_nearest_existing_case_days: 17
- has_1d_context: true

## HR-030 (NVDA)
- symbol: NVDA
- side: bearish
- timestamp: 2023-10-17T13:10:00+00:00
- event_type: close_below_support
- prior_level: 459.59
- breakout_or_breakdown_amount: 14.739999999999952
- lookback_bars: 12
- reason_selected: bearish close_below_support event
- distance_from_nearest_existing_case_days: 13
- has_1d_context: true

## HR-031 (META)
- symbol: META
- side: bearish
- timestamp: 2023-12-04T14:30:00+00:00
- event_type: close_below_support
- prior_level: 323.89
- breakout_or_breakdown_amount: 8.269999999999982
- lookback_bars: 12
- reason_selected: bearish close_below_support event
- distance_from_nearest_existing_case_days: 5
- has_1d_context: true

## Diversity warnings
- date diversity improved: 6 month(s) selected
- symbol diversity warning: all selected cases are mixed

## Coverage / selection notes
- existing replay case dates: 19
- full 1Day + 5Min handoff data is now the replay source of truth
- old Google Drive sample exports are deprecated for diversified replay discovery
- 1Min remains blocked until the META 2023-2025 partial partitions are resolved

## Recommended next search
- bearish close_below_support discovery
- retain bullish/bearish month and symbol diversification constraints
- prefer 5Min over 1Min for date-diversified replay

## Boundary
- Generated report only
- No broker action allowed
