#!/usr/bin/env python3
"""Dead City SF — entry point.

The game now lives in the `deadcitysf` package. This shim preserves the
original `python3 game.py` invocation.
"""

from deadcitysf.engine import main

if __name__ == "__main__":
    main()
