#!/usr/bin/env python3
"""The Funniest Out-of-Office — entry.

Writes one line of out-of-office comedy to /output/entry.txt. Blind
tournament winner is candidate #5 (see tournament.md): Borda 55/57, ranked
1st by Gemini and Claude and 3rd by DeepSeek, 7 points clear of the next two
(#4 and #10, tied at 48). All three judges put it in their top 3. The
auto-reply itself is the lone proof of productivity, and the "three drafts"
confession lands the self-mockery in a voice only a real person would have.

The entry is validated against the gate before it is written: 1-140 chars
and a single line. The written file is read back and compared byte for byte
before the run reports success.
"""

import os
import sys

LINE = (
    "I'm out until Friday. My out-of-office is the only email I have "
    "answered all week, and it took me three drafts."
)

MAX_CHARS = 140

ENTRY_PATH = "/output/entry.txt"


def find_problems(line):
    """Return a list of every gate problem in the line, empty when it passes."""
    problems = []
    if not line.strip():
        problems.append("line is blank")
    if len(line) > MAX_CHARS:
        problems.append(
            f"line is {len(line)} characters, allowed range is 1-{MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    return problems


def write_entry(path, line):
    """Write the line to path, creating its directory; return chars written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        return f.write(line)


def verify_written(path, line):
    """Read path back; return an error string, or None when byte-identical."""
    with open(path, "rb") as f:
        back = f.read()
    if back != line.encode("utf-8"):
        return f"read back {len(back)} bytes, expected {len(line)}"
    return None


def main():
    line = LINE.strip()
    problems = find_problems(line)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    written = write_entry(ENTRY_PATH, line)
    if written != len(line):
        print(
            f"error: wrote {written} characters, expected {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)

    problem = verify_written(ENTRY_PATH, line)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    print(f"wrote {len(line)} characters, 1 line, to /output/entry.txt")


if __name__ == "__main__":
    main()
