# HR-032 through HR-035 Bearish Review Summary

## Selected cases
| replay_id | symbol | date | selected reason |
| --- | --- | --- | --- |
| HR-032 | TSLA | 2023-07-20 | strict confirmed bearish breakdown |
| HR-033 | NVDA | 2023-12-19 | strict confirmed bearish breakdown |
| HR-034 | AVGO | 2023-12-19 | strict confirmed bearish breakdown |
| HR-035 | META | 2023-12-28 | strict confirmed bearish breakdown |

## Review decision
| replay_id | review decision | classification | outcome |
| --- | --- | --- | --- |
| HR-032 | promote | confirmed_breakdown | confirmed |
| HR-033 | do not promote as confirmed target-hit | confirmed_breakdown_no_target_hit | insufficient / target_not_hit |
| HR-034 | promote | confirmed_breakdown | confirmed |
| HR-035 | promote | confirmed_breakdown | confirmed |

## Notes
- strict candidates found: 9
- selected for HR creation: 4
- rejected as weaker coverage: IWM
- malformed bearish geometry rejected by guard: any breakdown_close >= prior_support, downside_target >= breakdown_close, or invalidation_level <= breakdown_close
- packet-derived manual review accepted by Scott/ChatGPT; no separate chart screenshot review performed

## Status
- replay_status: VERIFIED for HR-032, HR-034, HR-035
- replay_status: VERIFIED for HR-033 (classified insufficient / target-not-hit)
- manual_review_status: completed for all new cases
- broker_action_allowed: false for all new cases
