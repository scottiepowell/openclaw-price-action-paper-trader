# HR-001 Data Quality Report

generated_at: 2026-05-18T00:52:23.905860+00:00
replay_case: /home/scott/projects/openclaw-monster-academy-strategy-lab/replay/cases/HR-001.md
date_window: 2023-05-15 to 2023-05-18
can_be_real_market_replay: true

## Files inspected
- path: /home/scott/projects/openclaw-monster-academy-strategy-lab/data_refs/google_drive/AAPL_1Day_sample.csv
  exists: true
  file_type: csv
  row_count: 250
  first_timestamp: 2023-05-15T04:00:00+00:00
  last_timestamp: 2024-05-10T04:00:00+00:00
  timezone: UTC
  source: alpaca
  feed: iex
  adjustment: raw
  quality_status: PASS
  missing_columns: []
  duplicate_timestamps: 0
- path: /home/scott/projects/openclaw-monster-academy-strategy-lab/data_refs/google_drive/AAPL_5Min_sample.csv
  exists: true
  file_type: csv
  row_count: 250
  first_timestamp: 2023-05-15T13:30:00+00:00
  last_timestamp: 2023-05-18T14:40:00+00:00
  timezone: UTC
  source: alpaca
  feed: iex
  adjustment: raw
  quality_status: PASS
  missing_columns: []
  duplicate_timestamps: 0

## Summary
- data_quality_status: PASSED
- blocking_issues: none
- can_be_real_market_replay: true