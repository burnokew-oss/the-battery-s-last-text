#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text -- the phone battery's final message to the
charger it waited for all day -- to /output/entry.txt and prints it.

Pure standard library, deterministic: the same line every run.
"""

import os

ENTRY = (
    "i held on at 1% all day while you charged the ipad, the earbuds, "
    "even the toothbrush. so this is my last text: it's not me, it's you. "
    "don't text back."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
