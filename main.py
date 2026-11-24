#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single original office joke, one line, to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3 stdlib only, fully deterministic.
"""

import os

JOKE = (
    "HR asked for my emergency contact, so I put down the IT "
    "helpdesk - they are the only people in this office who ever "
    "actually answer the phone."
)


def main():
    line = JOKE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
