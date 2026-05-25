# Approval Audit Report

Read-only audit report for manual approvals and simulated submissions.

## Summary

- Overall audit status: warning
- Total approvals: 11
- Total compatibility approval files expected: 11
- Total compatibility approval files found: 11
- Total simulated submissions: 1
- Pending approvals: 11
- Approved approvals: 0
- Rejected approvals: 0
- Expired approvals: 0
- Consumed approvals: 0
- Approvals with approval_scope != simulated_only: 0
- Approvals with broker_action_allowed != false: 0
- Simulated submissions with broker_action_allowed != false: 0
- Conservative warning reason: pending approvals remain in the queue

## Approval Queue Audit

| approval_id | candidate_id | order_plan_id | symbol | side | approval_status | approval_scope | broker_action_allowed | expires_at | audit_status | audit_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APR-PTC-004 | PTC-004 | OP-PTC-004 | NVDA | bullish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-005 | PTC-005 | OP-PTC-005 | AVGO | bullish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-009 | PTC-009 | OP-PTC-009 | IWM | bearish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-017 | PTC-017 | OP-PTC-017 | SPY | bullish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-019 | PTC-019 | OP-PTC-019 | SPY | bearish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-021 | PTC-021 | OP-PTC-021 | GOOGL | bullish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-022 | PTC-022 | OP-PTC-022 | AMZN | bullish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-024 | PTC-024 | OP-PTC-024 | MSFT | bullish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-032 | PTC-032 | OP-PTC-032 | TSLA | bearish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-034 | PTC-034 | OP-PTC-034 | AVGO | bearish | pending | simulated_only | false |  | pass | pending approval is acceptable |
| APR-PTC-035 | PTC-035 | OP-PTC-035 | META | bearish | pending | simulated_only | false |  | pass | pending approval is acceptable |

## Compatibility File Audit

| expected_path | found | candidate_id | approval_id | approval_status | approval_scope | broker_action_allowed | audit_status | audit_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-004-approval.md | true | PTC-004 | APR-PTC-004 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-005-approval.md | true | PTC-005 | APR-PTC-005 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-009-approval.md | true | PTC-009 | APR-PTC-009 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-017-approval.md | true | PTC-017 | APR-PTC-017 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-019-approval.md | true | PTC-019 | APR-PTC-019 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-021-approval.md | true | PTC-021 | APR-PTC-021 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-022-approval.md | true | PTC-022 | APR-PTC-022 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-024-approval.md | true | PTC-024 | APR-PTC-024 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-032-approval.md | true | PTC-032 | APR-PTC-032 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-034-approval.md | true | PTC-034 | APR-PTC-034 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |
| /home/scott/projects/openclaw-price-action-paper-trader/runs/approvals/PTC-035-approval.md | true | PTC-035 | APR-PTC-035 | pending | simulated_only | false | pass | compatibility file matches expected safe fields |

## Simulated Submission Audit

| simulated_submission_id | approval_id | candidate_id | order_plan_id | symbol | side | simulated_broker_order_id | submission_status | submitted_at | broker_action_allowed | audit_status | audit_notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SS-APR-PTC-004-514ACD1054A0 | APR-PTC-004 | PTC-004 | OP-PTC-004 | NVDA | bullish | SIM-BROKER-PTC-004-6C52AADE56D6 | SIMULATED_SUBMITTED | 2026-05-25T23:06:59.189552+00:00 | false | pass | simulated submission record is present |

## Safety Boundary Audit

- broker_action_allowed all false: yes
- approval_scope all simulated_only: yes
- broker/network execution path detected by this audit: no
- report generation mutated source artifacts: no
