"""One word, one username: write the entrant's own make.fun username.

The entry is the entrant's own make.fun handle, "nofrizal" - one word,
7 characters, nothing else. It is written exactly as-is to
/output/entry.txt, with no trailing newline and no extra text.
"""

import os

# The entrant's own make.fun username, sent as one word.
USERNAME = "nofrizal"


def main():
    # One word, at most 30 characters per the competition gate.
    assert 1 <= len(USERNAME) <= 30 and USERNAME.strip() == USERNAME
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
