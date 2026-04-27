"""Simple CLI for LegalEase"""
import sys
from pathlib import Path
from typing import Optional

from .simplify import simplify_text


def _read_input(path: Optional[Path]) -> str:
    if path:
        return path.read_text(encoding="utf-8")
    return sys.stdin.read()


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python -m legal_ease.cli <input-file> [--api-key KEY]")
        return 2

    path = Path(argv[0])
    api_key = None
    if len(argv) > 2 and argv[1] == "--api-key":
        api_key = argv[2]

    text = _read_input(path)
    simplified = simplify_text(text, api_key=api_key)
    print(simplified)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
