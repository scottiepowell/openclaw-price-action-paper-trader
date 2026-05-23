# Discovery Constraint Audit

## 1. Data source verification
- artifact root currently used: /home/scott/projects/openclaw-historical-market-data-extraction/artifacts/published/monster_historical_data_strategy_lab_1d_5m_v1.0
- full 11-symbol root: true
- old data_refs/google_drive samples excluded: true
- 1Min blocked: true
- symbols discovered from artifact index: AAPL, AMZN, AVGO, GOOGL, IWM, META, MSFT, NVDA, QQQ, SPY, TSLA
- symbols with both 1Day and 5Min available: SPY, QQQ, AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, AVGO, IWM

## 2. Raw candidate counts before diversification filters

### Bullish
| side | symbol | raw_candidate_count | first_event_timestamp | last_event_timestamp | months_present |
| --- | --- | ---: | --- | --- | --- |
| bullish | SPY | 48 | 2023-05-15 14:50:00+00:00 | 2023-05-17 17:45:00+00:00 | 2023-05 |
| bullish | QQQ | 76 | 2023-05-15 14:50:00+00:00 | 2023-05-17 17:25:00+00:00 | 2023-05 |
| bullish | AAPL | 63 | 2023-05-15 15:15:00+00:00 | 2023-05-18 14:30:00+00:00 | 2023-05 |
| bullish | MSFT | 46 | 2023-05-15 14:45:00+00:00 | 2023-05-18 14:30:00+00:00 | 2023-05 |
| bullish | NVDA | 136 | 2023-05-15 15:05:00+00:00 | 2023-05-18 14:35:00+00:00 | 2023-05 |
| bullish | AMZN | 83 | 2023-05-15 15:05:00+00:00 | 2023-05-18 14:25:00+00:00 | 2023-05 |
| bullish | GOOGL | 96 | 2023-05-15 15:15:00+00:00 | 2023-05-18 14:25:00+00:00 | 2023-05 |
| bullish | META | 63 | 2023-05-15 14:45:00+00:00 | 2023-05-18 13:40:00+00:00 | 2023-05 |
| bullish | TSLA | 58 | 2023-05-15 15:45:00+00:00 | 2023-05-18 14:20:00+00:00 | 2023-05 |
| bullish | AVGO | 155 | 2023-05-15 15:10:00+00:00 | 2023-05-18 15:45:00+00:00 | 2023-05 |
| bullish | IWM | 74 | 2023-05-15 14:50:00+00:00 | 2023-05-17 17:30:00+00:00 | 2023-05 |

### Bearish
| side | symbol | raw_candidate_count | first_event_timestamp | last_event_timestamp | months_present |
| --- | --- | ---: | --- | --- | --- |
| bearish | SPY | 26 | 2023-05-15 17:40:00+00:00 | 2023-05-16 20:00:00+00:00 | 2023-05 |
| bearish | QQQ | 24 | 2023-05-15 13:50:00+00:00 | 2023-05-16 20:00:00+00:00 | 2023-05 |
| bearish | AAPL | 32 | 2023-05-15 17:20:00+00:00 | 2023-05-17 13:55:00+00:00 | 2023-05 |
| bearish | MSFT | 19 | 2023-05-15 16:20:00+00:00 | 2023-05-17 15:20:00+00:00 | 2023-05 |
| bearish | NVDA | 24 | 2023-05-16 17:35:00+00:00 | 2023-05-16 19:55:00+00:00 | 2023-05 |
| bearish | AMZN | 19 | 2023-05-15 16:20:00+00:00 | 2023-05-16 19:50:00+00:00 | 2023-05 |
| bearish | GOOGL | 22 | 2023-05-15 16:30:00+00:00 | 2023-05-15 19:50:00+00:00 | 2023-05 |
| bearish | META | 14 | 2023-05-15 17:40:00+00:00 | 2023-05-16 13:25:00+00:00 | 2023-05 |
| bearish | TSLA | 33 | 2023-05-15 14:55:00+00:00 | 2023-05-18 14:00:00+00:00 | 2023-05 |
| bearish | AVGO | 21 | 2023-05-15 14:45:00+00:00 | 2023-05-16 19:55:00+00:00 | 2023-05 |
| bearish | IWM | 27 | 2023-05-16 13:05:00+00:00 | 2023-05-16 19:55:00+00:00 | 2023-05 |

## 3. Filter-stage attrition table
| stage | bullish | bearish | combined | notes |
| --- | ---: | ---: | ---: | --- |
| raw candidates | 898 | 261 | 1159 | source scan output |
| after excluding old sample sources | 898 | 261 | 1159 | raw discovery CSVs are already from the full published handoff |
| after requiring full artifact root | 898 | 261 | 1159 | full 11-symbol root resolves correctly |
| after excluding 1Min | 898 | 261 | 1159 | 1Min is not returned by resolution |
| after avoid-existing-window rule | 6 | 6 | 12 | selected batch still fits the available windows from HR-001..HR-019 |
| after 30-day spacing rule | 6 | 6 | 12 | spacing preserved by the date-diversified selector |
| after max cases per symbol per month | 6 | 6 | 12 | one case per symbol per month in the selected batch |
| after max cases per symbol total | 6 | 6 | 12 | symbol caps hold at 2 max per symbol |
| final selected candidates | 6 | 6 | 12 | selected batch is HR-020..HR-031 |

## 4. Existing HR window coverage
| replay_id | symbol | side | date | classification | replay_status |
| --- | --- | --- | --- | --- | --- |
| HR-001 | AAPL | bullish | 2023-05-15 | watch_no_trigger | VERIFIED |
| HR-002 | SPY | bullish | 2023-05-15 | watch_no_trigger | VERIFIED |
| HR-003 | NVDA | bullish | 2023-05-15 | insufficient | VERIFIED |
| HR-004 | NVDA | bullish | 2023-05-18 | confirmed_breakout | VERIFIED |
| HR-005 | AVGO | bullish | 2023-05-18 | confirmed_breakout | VERIFIED |
| HR-006 | MSFT | bullish | 2023-05-16 | confirmed_breakout_no_target_hit | VERIFIED |
| HR-007 | META | bearish | 2023-05-16 | confirmed_breakdown_no_target_hit | VERIFIED |
| HR-008 | AVGO | bearish | 2023-05-16 | failed_breakdown_reclaim | CONTRADICTED |
| HR-009 | IWM | bearish | 2023-05-16 | confirmed_breakdown | VERIFIED |
| HR-010 | META | bullish | 2023-10-30 | candidate_for_manual_review | NOT_VERIFIED |
| HR-011 | META | bullish | 2023-11-29 | candidate_for_manual_review | NOT_VERIFIED |
| HR-012 | META | bullish | 2023-12-29 | candidate_for_manual_review | NOT_VERIFIED |
| HR-013 | META | bearish | 2023-10-30 | candidate_for_manual_review | NOT_VERIFIED |
| HR-014 | META | bearish | 2023-11-29 | candidate_for_manual_review | NOT_VERIFIED |
| HR-015 | META | bearish | 2023-12-29 | candidate_for_manual_review | NOT_VERIFIED |
| HR-016 | META | bullish | 2023-06-28 | ambiguous | VERIFIED |
| HR-017 | SPY | bullish | 2023-08-09 | confirmed_breakout | VERIFIED |
| HR-018 | META | bearish | 2023-07-19 | failed_breakdown_reclaim | VERIFIED |
| HR-019 | SPY | bearish | 2023-09-19 | confirmed_breakdown | VERIFIED |

- dates already occupied: 2023-05-15, 2023-05-16, 2023-05-18, 2023-06-28, 2023-07-19, 2023-08-09, 2023-09-19, 2023-10-30, 2023-11-29, 2023-12-29
- months already occupied: 2023-05, 2023-06, 2023-07, 2023-08, 2023-09, 2023-10, 2023-11, 2023-12
- symbols already occupied: AAPL, AVGO, IWM, META, MSFT, NVDA, SPY
- existing HR cases causing over-blocking: no for HR-001..HR-019 alone; yes once HR-020..HR-031 are present and occupy the same date windows

## 5. Near-miss candidates
| side | symbol | event timestamp | setup type | prior level | close | target hit after confirmation | invalidation hit after confirmation | which constraint rejected it | whether it would be useful as coverage |
| --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- |
| bullish | NVDA | 2023-05-18 13:30:00+00:00 | close_above_resistance | 301.99 | 305.52 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-18 13:35:00+00:00 | close_above_resistance | 659.77 | 662.17 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-16 13:40:00+00:00 | close_above_resistance | 640.83 | 643.79 |  |  | avoid_existing_replay_windows | false |
| bullish | MSFT | 2023-05-16 13:30:00+00:00 | close_above_resistance | 309.60 | 312.53 |  |  | avoid_existing_replay_windows | false |
| bullish | NVDA | 2023-05-18 13:35:00+00:00 | close_above_resistance | 305.91 | 308.06 |  |  | avoid_existing_replay_windows | false |
| bearish | META | 2023-05-16 13:25:00+00:00 | close_below_support | 238.15 | 235.73 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-17 13:30:00+00:00 | close_above_resistance | 646.73 | 648.76 |  |  | avoid_existing_replay_windows | false |
| bearish | AVGO | 2023-05-16 19:50:00+00:00 | close_below_support | 644.34 | 642.30 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-18 15:00:00+00:00 | close_above_resistance | 670.74 | 672.43 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-18 14:05:00+00:00 | close_above_resistance | 664.23 | 665.42 |  |  | avoid_existing_replay_windows | false |
| bullish | TSLA | 2023-05-17 13:40:00+00:00 | close_above_resistance | 168.39 | 169.74 |  |  | avoid_existing_replay_windows | true |
| bullish | AVGO | 2023-05-18 14:55:00+00:00 | close_above_resistance | 669.27 | 670.54 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-18 13:45:00+00:00 | close_above_resistance | 662.17 | 662.94 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-17 15:15:00+00:00 | close_above_resistance | 653.01 | 654.53 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-15 15:20:00+00:00 | close_above_resistance | 631.52 | 632.62 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-15 15:10:00+00:00 | close_above_resistance | 630.60 | 631.52 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-18 14:50:00+00:00 | close_above_resistance | 668.37 | 669.27 |  |  | avoid_existing_replay_windows | false |
| bullish | NVDA | 2023-05-16 13:30:00+00:00 | close_above_resistance | 289.65 | 290.70 |  |  | avoid_existing_replay_windows | false |
| bullish | NVDA | 2023-05-17 19:45:00+00:00 | close_above_resistance | 301.42 | 301.81 |  |  | avoid_existing_replay_windows | false |
| bullish | AVGO | 2023-05-18 13:50:00+00:00 | close_above_resistance | 663.40 | 664.05 |  |  | avoid_existing_replay_windows | false |

## 6. Recommended constraint options
- Option A — Keep strict constraints: no new cases; strongest anti-bias posture.
- Option B — Relax date spacing only: reduce min spacing from 30 calendar days to 10 or 15; keep symbol caps.
- Option C — Relax avoid-existing-window only: allow new cases in same month but not same symbol/date; keep symbol caps.
- Option D — Create targeted gap-fill cases: choose scenarios missing from evidence matrix rather than pure date/symbol diversity.
- Option E — Expand data or selector logic if raw counts are unexpectedly low: only if raw candidates are missing for many symbols.

## 7. Recommendation
- Keep the scanner/data path as-is; all 11 symbols are visible and both required timeframes resolve.
- The useful next prompt is Option D (targeted gap-fill cases), not broader relaxation of spacing or window rules.
- On a rerun with the current repo state, 12 of the 12 selected windows are already occupied, so no new slots remain.
- Main constraint causing the zero-case rerun result: avoid-existing-window, then symbol/month caps.

- Final test result: pending (written by report generator only)
