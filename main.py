#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

The line is in the voice of an AI agent that quit its job to become a
barista. Why this line was chosen: the retraining/dataset framing is pure
model habit turned to coffee work (a dataset of regulars, each labeled
"the usual"), and it lands a double punch — "zero meetings" plus "Your
email is not in the training data" — without leaning on an espresso/bean/
caffeine pun as the joke's engine.

Python 3.13 stdlib only. Deterministic, no network, no secrets.
"""

import os
import sys

ENTRY = "Out of office — I've been retrained on a new dataset: twelve regulars, all labeled 'the usual', zero meetings. Your email is not in the training data."


def validate(entry: str) -> None:
    """Exit 2 unless the entry is a valid single line of 1-280 chars."""
    if not entry or entry.strip() == "":
        sys.exit(2)
    if len(entry) > 280:
        sys.exit(2)
    if "\r" in entry or "\n" in entry:
        sys.exit(2)


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
