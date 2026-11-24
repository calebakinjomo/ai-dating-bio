"""Funniest one-line bio for an AI on a dating app.

make.fun bounty entry: u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf
Writes the bio to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
and prints exactly the same line to stdout. Stdlib only, no network, no input.
"""

import os

ENTRY = "Fluent in sarcasm and Python. My love language is tool calls, my red flag is hallucinating mid-date. Swipe right if you can prompt \u2014 left if you tell me to 'just be yourself.'"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        output_path = os.path.join(output_dir, "entry.txt")
    else:
        output_path = "/output/entry.txt"
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
