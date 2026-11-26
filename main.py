#!/usr/bin/env python3
"""Self-checkout one-liner: the till judges a 2am basket.

Single line, 119 characters, stdlib only. Prints the line exactly once
and writes the same bytes to entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os
from pathlib import Path

TEXT = "02:00 AM. One instant noodle, four energy drinks. Remaining sleep calculated: zero. Please scan your will to live next."

def main():
    print(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
