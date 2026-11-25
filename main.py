#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — make.fun entry.

Writes one line of plain text to $ENTRY_OUTPUT_DIR/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

LINE = "I waited all day next to the outlet, burned my last 2% texting you, and you spent the night charging your AirPods."

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
