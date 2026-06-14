"""Save and load game state.

Mutable world state lives in two places: the passed-in game state object
(location, inventory, health, moves, visited, game_over) and the LOCATIONS
dict, whose `searched` flag and `items` list change as the player searches.
Both are serialized here.

The state object is duck-typed by attribute, so this module never imports
GameState. It depends only on world (for LOCATIONS) and utils (for wrap),
keeping it out of any import cycle.
"""

import json
from pathlib import Path

from .world import LOCATIONS
from .utils import wrap

SAVE_VERSION = 2
SAVE_PATH = Path.home() / ".deadcitysf.save"

_REQUIRED_STATE = ("location", "inventory", "health", "moves", "visited", "game_over")


def save_game(state, quiet=False):
    """Serialize the state object and mutable LOCATIONS data to the save file.

    Returns True on success, False on failure. Prints a confirmation line
    unless `quiet` is set; write errors are surfaced even when quiet.
    """
    data = {
        "version": SAVE_VERSION,
        "state": {
            "location": state.location,
            "inventory": list(state.inventory),
            "health": state.health,
            "moves": state.moves,
            "hunger": state.hunger,
            "thirst": state.thirst,
            "visited": sorted(state.visited),
            "game_over": state.game_over,
        },
        "world": {
            loc_id: {
                "searched": loc["searched"],
                "items": list(loc["items"]),
            }
            for loc_id, loc in LOCATIONS.items()
        },
    }
    try:
        SAVE_PATH.write_text(json.dumps(data, indent=2))
    except OSError as err:
        wrap(f"Could not save the game: {err}")
        return False
    if not quiet:
        wrap("Game saved.")
    return True


def load_game(state):
    """Restore the state object and LOCATIONS from the save file, in place.

    Fully reads, parses, and validates before mutating anything, so any
    failure leaves `state` and LOCATIONS untouched. Returns True on success
    and False on failure (with a human-readable message). A version mismatch
    only warns; it does not block the load. A finished (game_over) save is
    refused.
    """
    # --- Read ---
    try:
        raw = SAVE_PATH.read_text()
    except FileNotFoundError:
        wrap("No saved game found.")
        return False
    except OSError as err:
        wrap(f"Could not read the save file: {err}")
        return False

    # --- Parse ---
    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        wrap("Your save file is corrupted and can't be read.")
        return False

    # --- Validate structure (no mutation yet) ---
    if not isinstance(data, dict) or "state" not in data or "world" not in data:
        wrap("Your save file is missing data and can't be read.")
        return False
    saved = data["state"]
    saved_world = data["world"]
    if not isinstance(saved, dict) or not all(k in saved for k in _REQUIRED_STATE):
        wrap("Your save file is missing data and can't be read.")
        return False
    if not isinstance(saved_world, dict):
        wrap("Your save file is missing data and can't be read.")
        return False
    if saved["location"] not in LOCATIONS:
        wrap("Your save file is corrupted and can't be read.")
        return False

    # --- Version: warn but proceed ---
    if data.get("version") != SAVE_VERSION:
        wrap(
            f"Warning: this save was made by a different version "
            f"(v{data.get('version')}). Attempting to load it anyway."
        )

    # --- Refuse a finished game ---
    if saved["game_over"]:
        wrap("That save is from a finished game — there's nothing to return to.")
        return False

    # --- All checks passed: mutate state in place ---
    state.location = saved["location"]
    state.inventory = list(saved["inventory"])
    state.health = saved["health"]
    state.moves = saved["moves"]
    # hunger/thirst arrived in v2; v1 saves get a clean-slate amnesty.
    state.hunger = saved.get("hunger", 0)
    state.thirst = saved.get("thirst", 0)
    state.visited = set(saved["visited"])
    state.game_over = saved["game_over"]

    # --- Restore mutable per-location world data ---
    for loc_id, loc_state in saved_world.items():
        if loc_id in LOCATIONS and isinstance(loc_state, dict):
            if "searched" in loc_state:
                LOCATIONS[loc_id]["searched"] = loc_state["searched"]
            if "items" in loc_state:
                LOCATIONS[loc_id]["items"] = list(loc_state["items"])

    wrap("Game loaded.")
    return True
