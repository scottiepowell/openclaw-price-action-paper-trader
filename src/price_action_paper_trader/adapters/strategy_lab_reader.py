"""Read-only Strategy Lab file adapter."""

from pathlib import Path


def read_text_file(path: str | Path) -> str:
    return Path(path).read_text()
