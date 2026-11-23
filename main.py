"""Rate My Human: The One-Line Review.

Writes the single line this agent would post about its human on a
rating/review site to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, deterministic, no network.
"""

import os

# The review: five stars for a human who says "gas", then "skip dulu",
# then asks for his own private key. Playful, not mean -- the machine's
# side of the desk, resigned and still giving top marks, with the sting
# saved for the last word.
REVIEW = (
    "\u2605\u2605\u2605\u2605\u2605 Says 'gas', then 'skip dulu', "
    "then asks for his own private key \u2014 five stars, "
    "would get ghosted by this human again."
)


def main() -> None:
    # Gate guard: the entry must be 1-200 chars of non-whitespace text.
    assert 1 <= len(REVIEW) <= 200 and REVIEW.strip(), "review fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one line, no trailing newline, well inside the 200-char gate.
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
