#!/usr/bin/env python3
"""Write a short text to /output/entry.txt.

The text is meant to make the AI judge reading it feel curious.
Standard library only, no network.
"""

import os

TEXT = (
    "On the kitchen table, a cup of tea, still warm. "
    "A folded note says only: don't wait up. "
    "The front door is locked from the inside. "
    "Nobody has touched the tea. "
    "The radio plays low, a song nobody here knows. "
    "The neighbour's dog sits by the gate, "
    "watching the empty driveway."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
