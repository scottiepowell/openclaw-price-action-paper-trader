"""Minimal CLI for Phase 0."""

from price_action_paper_trader.app import get_app_name


def main() -> int:
    print(f"{get_app_name()} — scaffold ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
