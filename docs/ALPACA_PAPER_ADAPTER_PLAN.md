# Alpaca Paper Adapter Plan

This is a disabled scaffold for a future paper-only integration.

## Phase 6 scope

- broker interface definition
- manual approval model
- disabled-by-default Alpaca scaffold
- broker safety gate
- config validation
- docs and tests

## Required environment variable names (future use only)

- `ALPACA_PAPER_API_KEY`
- `ALPACA_PAPER_SECRET_KEY`
- `ALPACA_PAPER_BASE_URL`

## Manual approval model

- `approval_status: NOT_APPROVED` by default
- `paper_only: true` by default
- `broker_action_allowed: false` by default
- future approval must be explicit and paper-only

## Safety rules

- paper account only
- no live account support
- no default order submission
- no live-trading endpoint
- `submit_orders: false` by default
- `broker_action_allowed: false` by default
- all broker responses must be journaled when future approval exists
- all submissions require explicit approval

## Difference from the simulated broker

- simulated broker emits offline-only execution records
- this scaffold is only a broker boundary and safety gate
- no network calls
- no Alpaca SDK dependency required
- no order submission in this phase
