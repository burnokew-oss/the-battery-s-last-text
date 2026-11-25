#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

One line of plain text: the phone battery's breakup text to the charger
that spent all day charging everything except the battery at 1%.

Writes the line to /output/entry.txt and prints it. Pure standard
library, deterministic: the same line on every run.
"""

import os

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

# The battery's last text, kept as one literal so the judged line is
# exactly this string, byte for byte.
ENTRY = (
    "i held on at 1% all day while you charged the ipad, the earbuds, "
    "even the toothbrush. so this is my last text: it's not me, it's you. "
    "don't text back."
)


def validate_entry() -> None:
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")


def write_entry() -> str:
    validate_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return ENTRY


def main() -> None:
    print(write_entry())


if __name__ == "__main__":
    main()
