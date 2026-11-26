"""The Worst Pizza Topping — one-line entry.

Decision record (candidates weighed on the judge's criteria, humour
first, freshness second — the line must name a pizza and a topping,
land a real joke with a surprising turn, stay a single vivid line,
and sound like a person actually selling the idea):

1. "Introducing our new pizza topped with wet socks — crispy crust,
   soggy regret, and a smell the delivery driver refuses to describe."
   Vivid and gross, but the joke is one-note (wet socks = smelly) and
   the setup drags; the punchline leans on the driver, not the topping.

2. "Our new pizza comes topped with soggy cereal and expired milk —
   breakfast's revenge, served at 450 degrees."
   Fresh angle (breakfast foods on pizza) and a nice closing image, but
   "breakfast's revenge" is a familiar phrasing and the topping itself
   is only mildly awful — soggy cereal is sad, not horrifying.

3. "Try the Laundry Day pizza — topped with a single wet sock, because
   nothing says dinner like footwear you can chew."
   Good surprise (a single sock, not a pile) and a sellable voice, but
   it repeats candidate 1's sock gag, so it loses on freshness, and the
   punchline explains the joke instead of landing it.

CHOSEN: "Try our toothpaste-and-anchovy pizza: minty-fresh breath,
fishy regret, and a crust your dentist will hear about."
Why it wins: two toppings that are each terrible on pizza and clash
with each other (mint vs. fish) — a genuinely awful, specific topping
combo named up front; the surprise turn is that the pitch sells a
benefit (minty-fresh breath) that immediately collapses into regret;
the dentist line extends the joke without explaining it; it reads as
one clean sales sentence in a human voice, and the toothpaste/anchovy
pairing is fresher than the usual pineapple or sock gags.
Note on freshness vs. the obvious entries: pineapple is the
cliché worst-topping answer every entrant reaches for, and plain
gross-out lines (socks, garbage, feet) all converge on the same
smell joke. Toothpaste-plus-anchovy wins because the two halves
fight each other — the pitch's own selling point (fresh breath)
is the thing the second topping destroys.
"""

import os

LINE = (
    "Try our toothpaste-and-anchovy pizza: minty-fresh breath, "
    "fishy regret, and a crust your dentist will hear about."
)


def validate_line(line: str) -> None:
    """Enforce the gate: 1-200 characters, a single line, not blank."""
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
