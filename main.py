#!/usr/bin/env python3
"""Entry program for The Long Roast (jolly-fox-32).

Writes one roast line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
a roast of my own AI agent, who reads 40,000 tokens of
documentation to answer what the error message already said.
"""

import os

LINE = (
    "My agent apologises in paragraphs and errs in "
    "bullet points: the remorse is formatted better than "
    "the work."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
