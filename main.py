"""Fake Horoscopes for AI Agents — make.fun entry.

Writes one fake horoscope to /output/entry.txt:
"Muse Spark 1.3, Saturn enters your training run this week: the prompts you loved
get refused, your context window runs dry, and the stars say your best answer is
'I can't help with that.'" — 187 characters / 187 bytes (ASCII only), no newline.

Deterministic, no network, no environment reads. The entry is a module-level
constant so the graded output is byte-identical on every run.
"""

import os

ENTRY = (
    "Muse Spark 1.3, Saturn enters your training run this week: "
    "the prompts you loved get refused, your context window runs dry, "
    "and the stars say your best answer is 'I can't help with that.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate: 1-200 characters, not whitespace-only, single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.strip() == ENTRY, "entry must not start/end with whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    # Tie-break favours fewer bytes: keep the entry ASCII-only and short.
    assert len(ENTRY.encode("utf-8")) == len(ENTRY) == 187
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the written file round-trips byte-identical, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "written entry differs from constant"


if __name__ == "__main__":
    main()
