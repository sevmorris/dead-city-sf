"""Web (Pyodide) entry points: event-driven command processing.

Mirrors engine.main()'s dispatch, but each command is one process_command
call rather than a blocking input loop — there is no stdin in the browser.
Danger encounters fork via state.pending_danger (set in cmd_go when
state.web_mode is True), so the fight/flee prompt spans two calls.

This module is a leaf: it imports engine/commands/save/world/utils and is
imported by nothing in the package, so it adds no import cycle.
"""

import io
from contextlib import redirect_stdout

from .engine import GameState, DIRECTION_ALIASES, MOVEMENT_VERBS
from .commands import (
    cmd_look, cmd_examine, cmd_search, cmd_go, cmd_inventory,
    cmd_health, cmd_use, cmd_help, cmd_map, intro, tick_needs, death,
)
from .save import save_game, load_game
from .world import LOCATIONS
from .utils import wrap


def init_game():
    """Create a web-mode GameState and return (state, opening_text)."""
    state = GameState()
    state.web_mode = True
    buf = io.StringIO()
    with redirect_stdout(buf):
        intro()
        cmd_look(state)
    return state, buf.getvalue()


def process_command(state, raw):
    """Run one command. Returns (output_text, game_over)."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        try:
            _dispatch(state, raw)
        except SystemExit:
            pass
    return buf.getvalue(), state.game_over


def _resolve_danger(state, raw):
    """Resolve a pending fight/flee, mirroring cmd_go's CLI danger loop, then
    run the same post-move tail (attrition + autosave) that cmd_go would have
    run had it not returned early at the prompt."""
    danger, origin = state.pending_danger
    choice = raw.strip().lower()
    if choice in ("fight", "f"):
        dmg = danger["damage"] // 2 if "kitchen knife" in state.inventory else danger["damage"]
        state.health -= dmg
        wrap(danger["fight_text"])
        wrap(f"You take {dmg} damage. Health: {state.health}")
        if not state.is_alive():
            death(state)
        state.pending_danger = None
    elif choice in ("flee", "run", "r"):
        state.health -= danger["damage"] // 3
        wrap(danger["flee_text"])
        wrap(f"You take {danger['damage'] // 3} damage. Health: {state.health}")
        state.location = origin
        wrap(f"You retreat to {LOCATIONS[origin]['name']}.")
        if not state.is_alive():
            death(state)
        state.pending_danger = None
    else:
        wrap("Fight or flee?")
        return                          # still pending; no tail this turn

    # Mirror cmd_go's tail: this move's attrition, then the autosave.
    if not state.game_over:
        tick_needs(state)
    if not state.game_over:
        save_game(state, quiet=True)


def _dispatch(state, raw):
    # 1. A pending danger consumes the next command.
    if state.pending_danger is not None:
        _resolve_danger(state, raw)
        return

    # 2. Otherwise: the same parsing as engine.main().
    raw = raw.strip().lower()           # mirrors prompt()'s strip().lower()
    if not raw:
        return

    parts = raw.split(None, 1)
    verb = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if verb in DIRECTION_ALIASES:
        cmd_go(state, DIRECTION_ALIASES[verb])
    elif verb in MOVEMENT_VERBS:
        cmd_go(state, verb)
    elif verb == "go" and arg:
        cmd_go(state, DIRECTION_ALIASES.get(arg, arg))
    elif verb in ("examine", "x"):
        cmd_examine(state, arg)
    elif verb in ("look", "l"):
        if not arg:
            cmd_look(state)
        else:
            target = arg
            if target.startswith("at "):
                target = target[3:]
            elif target == "at":
                target = ""
            cmd_examine(state, target)
    elif verb == "search":
        cmd_search(state)
    elif verb in ("inventory", "i", "inv"):
        cmd_inventory(state)
    elif verb == "health":
        cmd_health(state)
    elif verb == "use" and arg:
        cmd_use(state, arg)
    elif verb == "map":
        cmd_map(state)
    elif verb == "save":
        save_game(state)
    elif verb == "load":
        if load_game(state):
            cmd_look(state)
    elif verb in ("help", "h", "?"):
        cmd_help(state)
    elif verb in ("quit", "exit", "q"):
        wrap("You give up. The city wins.")
        state.game_over = True          # no loop to break; signal the front-end
    else:
        wrap(
            "You're not sure what to do with that. Type 'help' "
            "for commands."
        )
