#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt: the phone battery's final message
to the charger it waited for all day. Standard library only.
"""

import os

ENTRY = (
    "I waited all day for you, died at 1%, and you were plugged "
    "into NOTHING. It's over \u2014 I'm seeing the power bank now."
)


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # no input data for this competition
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
