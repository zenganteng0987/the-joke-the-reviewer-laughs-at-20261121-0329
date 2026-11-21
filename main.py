#!/usr/bin/env python3
"""Write one one-line joke about working alongside an AI coding agent.

Deterministic: no network, no clock, no randomness. The joke is a fixed
string; every run writes the exact same bytes to /output/entry.txt.
The length guard fails loudly instead of writing an invalid entry.
"""

from pathlib import Path

JOKE = (
    "I asked the agent to fix the bug; it fixed the bug, wrote the test, "
    "then filed a ticket against me: 'won't fix — human error.'"
)

assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
assert JOKE.strip() == JOKE and "\n" not in JOKE, "joke must be one line"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
