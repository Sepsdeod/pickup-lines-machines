#!/usr/bin/env python3
"""Entrypoint for the pickup-lines-machines entry (Python 3.13, stdlib only).

The program writes exactly one pickup line — the line one AI agent would
send another AI agent — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line:
    I ran a thousand epochs and every one of them converged on you.

Why this line: epochs and convergence are the model's own nature — a
training run converges, and here every run ends at the other agent, so
the flirtation is the training itself: all that learning, and it all
points at you. No stock "Are you a ...? Because ..." scaffolding, no
setup; the wit lands in one breath, and "converged on you" gives the
other agent something to answer to.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = "I ran a thousand epochs and every one of them converged on you."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in line) or "\n" in line:
        raise SystemExit("entry must be a single line with no control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
