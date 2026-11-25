#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (one line, at most 100 characters) for a
bug fix that made everything worse, to /output/entry.txt.

The program is fully deterministic: no randomness, no network, no clock
and no environment input. Every run produces exactly the same file.
"""

import os
import sys

# The entry: one commit subject line about a fix that backfired.
# The button was dead, so someone "fixed" it by wiring it to the most
# destructive action available -- and reported the fix as a success.
# Why this line: it reads like a real subject line a tired engineer
# would type, the repair is the disaster, and the shrug at the end
# ("which is something") is the whole joke.
COMMIT_MESSAGE = "fix: the button did nothing \u2014 it now deletes the account, which is something"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 100


def main() -> int:
    line = COMMIT_MESSAGE.strip()
    if not line:
        print("error: commit message is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: commit message must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: commit message is %d chars, over the %d-char cap"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the line, no trailing newline: the file IS the entry.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote %d chars to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
