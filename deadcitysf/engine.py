"""Game state, input dispatch, and the main loop."""

from .commands import (
    cmd_look,
    cmd_examine,
    cmd_search,
    cmd_go,
    cmd_inventory,
    cmd_health,
    cmd_use,
    cmd_help,
    cmd_map,
    intro,
)
from .save import save_game, load_game
from .utils import wrap, prompt


class GameState:
    def __init__(self):
        self.location = "house"
        self.inventory = []
        self.health = 100
        self.moves = 0
        self.hunger = 0   # moves since last ate
        self.thirst = 0   # moves since last drank
        self.visited = {"house"}
        self.game_over = False
        self.web_mode = False        # event-driven web (Pyodide) mode
        self.pending_danger = None   # (danger, origin_id) awaiting fight/flee

    def is_alive(self):
        return self.health > 0


DIRECTION_ALIASES = {
    "n": "north", "s": "south", "e": "east", "w": "west",
    "ne": "northeast", "nw": "northwest", "se": "southeast", "sw": "southwest",
    "u": "up", "d": "down",
    "out": "outside",
    "in": "inside", "enter": "inside",
}

MOVEMENT_VERBS = (
    "north", "south", "east", "west", "northeast", "northwest",
    "southeast", "southwest", "up", "down", "outside", "inside",
)


def main():
    state = GameState()
    intro()
    cmd_look(state)

    while not state.game_over:
        raw = prompt()
        if not raw:
            continue

        parts = raw.split(None, 1)
        verb = parts[0]
        arg = parts[1] if len(parts) > 1 else ""

        # Direction shortcuts
        if verb in DIRECTION_ALIASES:
            cmd_go(state, DIRECTION_ALIASES[verb])
        elif verb in MOVEMENT_VERBS:
            cmd_go(state, verb)
        elif verb == "go" and arg:
            direction = DIRECTION_ALIASES.get(arg, arg)
            cmd_go(state, direction)
        elif verb in ("examine", "x"):
            cmd_examine(state, arg)
        elif verb in ("look", "l"):
            if not arg:
                cmd_look(state)
            else:
                # "look at <thing>" / "look <thing>" -> examine
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
            break
        else:
            wrap(
                "You're not sure what to do with that. Type 'help' "
                "for commands."
            )


if __name__ == "__main__":
    main()
