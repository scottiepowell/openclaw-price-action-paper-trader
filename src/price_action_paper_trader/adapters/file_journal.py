"""File journal adapter placeholder."""

from pathlib import Path


def append_line(path: str | Path, line: str) -> None:
    journal_path = Path(path)
    journal_path.parent.mkdir(parents=True, exist_ok=True)
    with journal_path.open("a", encoding="utf-8") as handle:
        handle.write(line.rstrip("\n") + "\n")
