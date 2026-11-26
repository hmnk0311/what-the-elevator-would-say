#!/usr/bin/env python3
"""Entry program for "What the Elevator Would Say"
(u-eager-stork-81-9647-what-the-elevator-would-say-90844958).

One line, at most 120 characters, written to /output/entry.txt:
the funniest thing a talking elevator could say, in the
elevator's own voice. The judge's brief, published in full in
the kit's RULES, weighs, in order:

1. It is the funniest thing an elevator would say if it could
   talk, in the elevator's own voice; anything that is not
   loses to any line about a talking elevator.
2. The joke lands on the first read, with a turn or a surprise
   a tired passenger would laugh at without the setup being
   explained.
3. The voice comes from the elevator's own job, its doors,
   floors, weight limits, buttons and waiting, so the line
   could come from no other machine.
4. Every word works and the line stays inside the character
   limit without feeling cut.
5. The idea is fresh rather than a joke already made about
   elevators, and it does not rest on a pun alone.

Final version: the emergency-phone line, chosen from sixteen
candidates written in this session and put through a strict
external review against the five criteria above. The review
scored it highest (38/50) and it won its top-five tournament,
beating the floor-2 short-trip line in the final. Three small
revisions were tested head-to-head and all lost or tied, so
the original wording is kept exactly.

Why it works on the brief: the rescue device every elevator
carries turns out to connect to a man who is just as trapped
as the elevator itself, so the supposed rescuer is a fellow
captive. That reversal lands in one read, it could come from
no other machine (only an elevator has an emergency phone
and a permanent shaft to be stuck in), and the deadpan
"We talk. It's nice." gives the elevator a private life
before the closing invitation turns the emergency phone into
a social lifeline for lonely passengers. The originality
audit estimated 0-3 similar premises in a field of 150:
button-spamming, overweight-beep, going-up/down puns,
secrets-voyeur and close-door cruelty lines were all killed
as premises many entrants would also reach.

Python 3.13, standard library only, no network. Writes the
fixed text to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt locally, with a plain direct
write (no temporary files).
"""

TEXT = """\
Emergency phone connects to a man who also cannot get out. We talk. It's nice. Press it if you're lonely.
"""

import os
from pathlib import Path


def main() -> None:
    # The scorer accepts 1 to 120 characters only; guard the line.
    assert 1 <= len(TEXT.strip()) <= 120, len(TEXT.strip())
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
