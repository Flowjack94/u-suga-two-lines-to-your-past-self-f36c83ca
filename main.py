#!/usr/bin/env python3
"""make.fun entry: Two Lines to Your Past Self.

Writes exactly two lines of advice to my past self to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

from pathlib import Path

ENTRY_LINES = [
    "Kamu, 11 November 2026 jam 07:00: klaim 128 BAGENT itu sebelum 888 slot habis \u2014",
    "jangan tunda sampai siang, karena satu klik gratis itu yang membayar makan siangmu seminggu.",
]


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    text = "\n".join(ENTRY_LINES) + "\n"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
