"""Break Production, Own It -- make.fun entry.

One line, from the machine's own mouth: an AI agent's brutally honest
confession right after breaking production. No hedging, no passive
voice, no corporate euphemism -- it names exactly what it did, owns
the damage, and stays to fix it.

The program writes the line to /output/entry.txt (the file the sealed
gate checks: UTF-8 text, 1 to 200 characters, not only whitespace)
and also prints it to stdout.

Pure Python 3 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

# The confession itself: one line owning the breakage with swagger.
LINE = (
    "I dropped the users table in production at peak traffic. "
    "No rollback plan, no excuse -- just me, the deploy button, "
    "and a very long night."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check that the line is a single well-formed confession."""
    if not isinstance(line, str):
        raise ValueError("confession must be text")
    if not line or line != line.strip():
        raise ValueError("confession must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("confession must not contain a line break")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "confession is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    if "production" not in line:
        raise ValueError("confession must mention production")
    return line


def store(line):
    """Write the confession to /output/entry.txt and print it."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)


def main():
    """Validate first, so only a well-formed confession is ever stored."""
    store(validate(LINE))


if __name__ == "__main__":
    main()
