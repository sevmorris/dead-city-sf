"""Text-output helpers and the input prompt."""

import sys
import textwrap

WIDTH = 72


def wrap(text):
    for line in text.strip().splitlines():
        if line.strip() == "":
            print()
        else:
            print(textwrap.fill(line.strip(), WIDTH))


def divider():
    print("-" * WIDTH)


def prompt():
    try:
        return input("\n> ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\n")
        wrap("You sit down in the rubble and close your eyes. The city sleeps.")
        sys.exit(0)
