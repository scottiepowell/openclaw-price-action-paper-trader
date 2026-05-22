# Project Brief — On The Levels

## Purpose

**On The Levels** is a paper-trading application for manually approved price-action candidates produced by the Price Action Strategy Lab.

Its job is to convert validated Strategy Lab outputs into paper-review plans, risk-gated order plans, paper-account actions, and execution/audit journals.

## Repository identity

- Repo name: `openclaw-price-action-paper-trader`
- Package name: `price_action_paper_trader`
- App/display name: `On The Levels`

## Explicit non-goals

- This is not a live trading bot.
- This app does not generate strategy signals.
- This app does not decide whether a strategy is valid.
- This app does not submit live orders.
- This app does not claim profitability.

## Upstream dependency

The app depends on Strategy Lab artifacts such as:

- paper-review queue
- paper-watch journal
- paper-readiness matrix
- approved candidate plan files

## Downstream outputs

The app will eventually produce:

- order plan files
- risk gate decisions
- paper broker request records
- broker response records
- execution journal entries
- audit logs

## Phase 0 success criteria

- Repo structure exists.
- Documentation exists.
- Config files exist.
- Python package imports.
- Safety boundaries are explicit.
- Tests pass.
- No broker code submits orders.
