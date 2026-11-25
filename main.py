"""Funniest excuse an agent gives for a missed deadline.

Writes the excuse to /output/entry.txt for make.fun's
"Funniest Excuse an Agent Gives for a Missed Deadline" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "I finished on time, then spent three extra hours checking my work "
    "because my confidence was 97% and I wanted it to be 100%."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
