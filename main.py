"""Worst AI Advice — one line of confidently terrible advice.

Writes a single line (<=140 chars) to /output/entry.txt.
Stdlib only. Deterministic.
"""

import os

LINE = "Great question! Use the same password for every account, and write it on a sticky note stuck to your monitor for safekeeping."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
