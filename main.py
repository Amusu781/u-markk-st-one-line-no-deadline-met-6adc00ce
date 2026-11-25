#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline to
<output dir>/entry.txt (default /output, override with OUTPUT_DIR).
The line is a fixed, hand-written string: no network, no randomness.
Only the file is overwritten; the output directory is never removed.
"""

import os

LINE = (
    "My laptop chose two minutes before the deadline to start a "
    "45-minute update, so I sat there watching it reboot three times "
    "while the deadline expired once."
)


def write_entry(out_dir: str, text: str) -> str:
    """Create out_dir if needed and overwrite entry.txt inside it."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    return path


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    write_entry(os.environ.get("OUTPUT_DIR", "/output"), LINE)


if __name__ == "__main__":
    main()
