# Strategy Lab Contract

The paper trader consumes Strategy Lab outputs. It does not create strategy candidates.

## Expected upstream files

- paper-review queue CSV/Markdown
- paper-watch journal CSV/Markdown
- candidate-specific paper-review plans
- readiness matrix

## Required candidate fields

- candidate_id
- replay_id
- symbol
- side
- setup_type
- readiness_status
- entry_candidate_price
- target_price
- invalidation_level
- broker_action_allowed

## Required gates

Only candidates marked `READY_FOR_PAPER_REVIEW` should be loaded for order-plan generation.

Blocked candidates must remain excluded.
