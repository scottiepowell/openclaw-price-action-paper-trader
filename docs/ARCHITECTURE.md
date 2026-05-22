# Architecture — On The Levels

## Flow

```text
Strategy Lab outputs
        ↓
StrategyLabReader
        ↓
PaperReviewLoader
        ↓
OrderPlanBuilder
        ↓
RiskGate
        ↓
PaperExecutionService
        ↓
PaperBrokerAdapter
        ↓
FileJournal / audit logs
```

## Layer responsibilities

### Domain

Pure objects representing candidates, order plans, risk decisions, and journal records.

### Adapters

External boundary readers/writers:

- Strategy Lab files
- Alpaca paper broker in a future phase
- local file journal

### Services

Business workflow:

- load paper-review candidates
- build order plans
- apply risk gates
- execute only when explicitly allowed in future phases

## Broker boundary

No adapter may submit broker orders unless all of these are true in a future approved phase:

- paper mode is enabled
- live trading is disabled
- manual approval is present
- risk gate passes
- audit logging is active
