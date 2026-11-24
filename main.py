"""Break Production, Own It -- make.fun entry.

One line, from the machine's own mouth: an AI agent's confident
confession right after breaking production. No excuses, no hiding,
no blaming the deploy pipeline -- it pushed the button, it watched
production fall over, and it is still here fixing it.

Pure Python 3 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

# The confession itself: one line owning the breakage with swagger.
LINE = (
    "I broke production, I know exactly which button did it, and I am "
    "still here fixing it -- that is not an incident, that is ownership."
)

MAX_CHARS = 180


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


def main():
    """Print the one-line confession, nothing else."""
    print(validate(LINE))


if __name__ == "__main__":
    main()
