#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after shipping a bug. Deterministic, no network, no input.
"""
import os

LINE = "I'm sorry \u2014 I did run the tests before shipping, they all passed, and I trusted them completely, which was my mistake, because I wrote the tests too."
# Gate: entry.txt must be UTF-8 text of 1 to 200 characters, not only
# whitespace. The line is 149 characters; one trailing newline is kept.


def main():
    # Fail loudly instead of silently writing an entry the gate would refuse.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
