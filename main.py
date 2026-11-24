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


def validate_entry(lines: list[str]) -> str:
    """Validate the two-line entry and return the joined text.

    Rejects control characters (C0 + DEL), leading/trailing whitespace on
    any line, anything other than exactly two lines, and a total length
    outside 1-280 characters. Raises ValueError on failure.
    """
    if len(lines) != 2:
        raise ValueError(f"entry must have exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines):
        for ch in line:
            if ord(ch) < 0x20 or ord(ch) == 0x7F:
                raise ValueError(
                    f"line {i + 1}: control character U+{ord(ch):04X} not allowed"
                )
        if line != line.strip():
            raise ValueError(f"line {i + 1}: leading/trailing whitespace not allowed")
    text = "\n".join(lines)
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(text)}")
    return text


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    text = validate_entry(ENTRY_LINES) + "\n"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
