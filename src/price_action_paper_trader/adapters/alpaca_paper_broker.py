"""Future Alpaca paper broker adapter.

Phase 0 placeholder only. This module must not submit orders.
"""


class AlpacaPaperBrokerDisabled:
    def submit_order(self, *_args, **_kwargs):
        raise RuntimeError("Alpaca paper order submission is disabled in Phase 0")
