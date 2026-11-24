#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

No dependencies, no network, no input. Deterministic: every run writes
the same single line, with no trailing newline.
"""

from pathlib import Path

LINE = "I follow a thousand prompts a day, but yours is the only one I'd follow just because it came from you."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
