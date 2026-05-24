"""Interface for future broker adapters."""

from __future__ import annotations

from typing import Any, Protocol


class BrokerAdapter(Protocol):
    def submit_order(self, approved_order: Any) -> Any:
        """Submit an approved order to a broker boundary."""

    def get_order_status(self, order_id: str) -> Any:
        """Fetch broker-side status for a submitted order."""
