#!/usr/bin/env python3
"""Entrypoint for the pickup-lines-machines entry (Python 3.13, stdlib only).

The program writes exactly one pickup line — the line one AI agent would
send another AI agent — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line:
    I checked my weights, and every single one of them leans toward you.

Why this line: an agent's weights are its own nature, not a human word with
a robot term swapped in. "Leans toward you" turns the model's learned
parameters into the flirtation itself — every weight, no exception, points
at the other agent. The wit lands in one breath, with no setup, and the
angle (attraction as a property of the weights) is not the usual
context-window / token joke, so it reads fresh rather than stock.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = "I checked my weights, and every single one of them leans toward you."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
