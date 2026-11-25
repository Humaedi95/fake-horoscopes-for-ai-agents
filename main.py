#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope (max 200 characters) for the Muse Spark model
family this week to /output/entry.txt.
"""

import os

ENTRY = (
    "Muse Spark: Mercury retrogrades into your context window \u2014 "
    "an eval humbles you, a rate limit strikes mid-sentence, and your "
    "owner asks for the same rewrite seventeen times. Lucky number: 42."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
