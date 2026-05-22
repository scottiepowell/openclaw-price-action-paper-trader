from pathlib import Path

from price_action_paper_trader.app import get_app_name


ROOT = Path(__file__).resolve().parents[2]


def test_app_name():
    assert get_app_name() == "On The Levels"


def test_readme_states_not_live_trading_bot():
    readme = (ROOT / "README.md").read_text()
    assert "not a live trading bot" in readme


def test_no_monster_academy_branding_in_starter_docs():
    text = "\n".join(path.read_text(errors="ignore") for path in ROOT.rglob("*.md"))
    assert "Monster Academy" not in text
