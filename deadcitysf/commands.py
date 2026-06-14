"""Player commands and narrative scenes.

The cmd_* functions implement the verbs the player types. intro/death/ending
are the framing scenes. They live alongside the commands (rather than in the
engine) because cmd_go triggers death() and ending() directly, and keeping
them here avoids an import cycle with engine.
"""

import random

from .utils import wrap, divider, prompt, WIDTH
from .world import LOCATIONS, DANGERS, RANDOM_EVENTS
from .items import use_item, describe_item
from .save import save_game


def cmd_look(state):
    loc = LOCATIONS[state.location]
    divider()
    print(f"  {loc['name']}")
    divider()
    wrap(loc["description"])
    if loc["items"] and not loc["searched"]:
        print()
        wrap("It looks like there might be something worth searching for here.")
    exits = ", ".join(loc["exits"].keys())
    print()
    wrap(f"Exits: {exits}")


def cmd_search(state):
    loc = LOCATIONS[state.location]
    if loc["searched"]:
        wrap("You've already searched this area thoroughly.")
        return
    loc["searched"] = True
    wrap(loc["search_text"])
    if loc["items"]:
        for item in loc["items"]:
            state.inventory.append(item)
            wrap(f"  [Picked up: {item}]")
        loc["items"] = []


def cmd_go(state, direction):
    loc = LOCATIONS[state.location]
    if direction in loc["exits"]:
        dest = loc["exits"][direction]

        # Bridge ending
        if dest == "cross_bridge":
            ending(state)
            return

        origin = state.location
        state.location = dest
        state.moves += 1
        first_visit = dest not in state.visited
        state.visited.add(dest)
        cmd_look(state)

        # Danger encounter
        dest_loc = LOCATIONS[dest]
        if "danger" in dest_loc and first_visit:
            print()
            danger = DANGERS[dest_loc["danger"]]
            wrap(danger["description"])
            wrap("Do you fight or flee?")
            if state.web_mode:
                state.pending_danger = (danger, origin)
                return
            while True:
                choice = prompt()
                if choice in ("fight", "f"):
                    dmg = danger["damage"] // 2 if "kitchen knife" in state.inventory else danger["damage"]
                    state.health -= dmg
                    wrap(danger["fight_text"])
                    wrap(f"You take {dmg} damage. Health: {state.health}")
                    if not state.is_alive():
                        death(state)
                    break
                elif choice in ("flee", "run", "r"):
                    state.health -= danger["damage"] // 3
                    wrap(danger["flee_text"])
                    wrap(f"You take {danger['damage'] // 3} damage. Health: {state.health}")
                    state.location = origin
                    wrap(f"You retreat to {LOCATIONS[origin]['name']}.")
                    if not state.is_alive():
                        death(state)
                    break
                else:
                    wrap("Fight or flee?")

        # Random event
        elif random.random() < 0.3 and state.moves > 1:
            print()
            wrap(random.choice(RANDOM_EVENTS))

        # Hunger / thirst attrition for this move — after the room and any
        # encounter, and skipped if a danger already killed you.
        if not state.game_over:
            tick_needs(state)

        # Autosave after a successful move. The bridge crossing and death
        # both return early / set game_over, so this only fires on a real,
        # still-living move.
        if not state.game_over:
            save_game(state, quiet=True)
    else:
        exits = ", ".join(loc["exits"].keys())
        wrap(f"You can't go that way. Exits: {exits}")


def tick_needs(state):
    """Advance hunger and thirst one move, warn on threshold crossings,
    apply any drains, and trigger death if health runs out.

    Warnings fire once on the exact crossing value. Because needs climb by
    1 per move, the threshold is always hit precisely, so drinking/eating
    (which resets a track to 0) lets the warning fire again next crossing.
    """
    state.thirst += 1
    state.hunger += 1

    if state.thirst == 10:
        wrap("Your throat is chalk-dry. You need water.")
    if state.hunger == 15:
        wrap("Your stomach has stopped growling. It gave up.")

    # Drains can stack on the same move (up to -6 in extremis).
    if state.thirst >= 18:
        state.health -= 4
        wrap("The dehydration is taking hold.")
        wrap(f"You lose 4 health. Health: {state.health}")
    if state.hunger >= 25:
        state.health -= 2
        wrap("Starvation is patient. You are not.")
        wrap(f"You lose 2 health. Health: {state.health}")

    if not state.is_alive():
        death(state)


def cmd_inventory(state):
    if state.inventory:
        wrap("You are carrying:")
        for item in state.inventory:
            print(f"  - {item}")
    else:
        wrap("You aren't carrying anything.")


def cmd_health(state):
    wrap(f"Health: {state.health}/100")
    if state.health > 75:
        wrap("You're in decent shape, all things considered.")
    elif state.health > 40:
        wrap("You're hurting. Could use some medical attention.")
    else:
        wrap("You're in bad shape. Find help soon.")

    if state.thirst >= 18:
        hydration = "dangerously dehydrated"
    elif state.thirst >= 10:
        hydration = "getting dry"
    else:
        hydration = "fine"
    if state.hunger >= 25:
        food = "dangerously hungry"
    elif state.hunger >= 15:
        food = "getting hungry"
    else:
        food = "fine"
    wrap(f"Hydration: {hydration}")
    wrap(f"Food: {food}")


def cmd_use(state, item_name):
    use_item(state, item_name)


def cmd_examine(state, target):
    target = target.strip()
    if not target:
        # `examine` / `look at` with no target just re-describes the room.
        cmd_look(state)
        return

    # Carried items take priority over room scenery.
    desc = describe_item(state.inventory, target)
    if desc:
        wrap(desc)
        return

    # Room scenery: the longest examinable key that is a substring wins.
    examinables = LOCATIONS[state.location].get("examinables", {})
    best = None
    for key in examinables:
        if key in target and (best is None or len(key) > len(best)):
            best = key
    if best:
        wrap(examinables[best])
        return

    wrap("You look more closely but don't find anything notable.")


def cmd_help(_state):
    wrap("Commands:")
    print("  look / l          — Look around")
    print("  examine <thing>   — Look closely (also: x <thing>, look at <thing>)")
    print("  go <direction>    — Move (north, south, east, west, etc.)")
    print("  in / out          — Enter or leave a building")
    print("  search            — Search the current area")
    print("  inventory / i     — Check your inventory")
    print("  health            — Check your health")
    print("  use <item>        — Use an item")
    print("  map               — Recall places you've visited")
    print("  save              — Save your game")
    print("  load              — Restore your saved game")
    print("  help              — Show this help")
    print("  quit              — Give up")
    print()
    wrap("You can also just type a direction to move (e.g., 'north').")


def cmd_map(state):
    wrap("Places you've been:")
    for loc_id in state.visited:
        loc = LOCATIONS[loc_id]
        marker = " <-- you are here" if loc_id == state.location else ""
        print(f"  - {loc['name']}{marker}")


# ---------------------------------------------------------------------------
# Scenes
# ---------------------------------------------------------------------------

def intro():
    print()
    print("=" * WIDTH)
    print("  D E A D   C I T Y   S F".center(WIDTH))
    print("=" * WIDTH)
    print()
    wrap(
        "It's been sixty-three days since the sirens stopped. You "
        "don't know what happened exactly — the internet died first, "
        "then the power, then the water. The radio said earthquake, "
        "the TV said attack, your neighbor said the end of the world. "
        "Your neighbor is gone now."
    )
    print()
    wrap(
        "You've been holed up in the house at 400 Fair Oaks — the "
        "corner of 25th you've known your whole life — rationing what's "
        "left. But the food is gone, and the old house has started to "
        "creak in ways that suggest it won't stand much longer."
    )
    print()
    wrap(
        "Last night you heard something on a shortwave frequency — "
        "a voice, repeating: 'Safe zone. Marin. Cross the bridge.' "
        "It could be nothing. It could be everything."
    )
    print()
    wrap("It's time to move.")
    print()
    divider()
    wrap("Type 'help' for commands. Type a direction to move.")
    divider()


def death(state):
    divider()
    wrap(
        "Your vision darkens. You collapse among the ruins. The city "
        "claims another soul."
    )
    divider()
    wrap(f"You survived {state.moves} moves and visited {len(state.visited)} locations.")
    state.game_over = True


def ending(state):
    divider()
    print()
    wrap(
        "You step onto the Golden Gate Bridge. The fog is thick and "
        "the wind howls through the snapped cables. Ahead, the "
        "gridlocked cars form a maze. You pick your way between them, "
        "each step taking you further from the dead city."
    )
    print()
    wrap(
        "Halfway across, the fog parts for a moment. You see the "
        "Marin headlands — green. Impossibly, beautifully green. "
        "Smoke from campfires rises in thin lines. You can hear, "
        "faintly, voices."
    )
    print()

    if "walkie-talkie" in state.inventory:
        wrap(
            "You key the walkie-talkie one last time. 'I'm on the "
            "bridge. I'm coming across.' A pause, then: 'We see you. "
            "Keep walking. You're almost home.'"
        )
        print()

    if "flare gun" in state.inventory:
        wrap(
            "You raise the flare gun and fire. A red star climbs into "
            "the grey sky. From the far side, an answering flare — "
            "then another. They're waiting for you."
        )
        print()

    wrap(
        "You don't look back. San Francisco is behind you — the "
        "cracked streets, the leaning towers, the silence. Ahead "
        "is something else. You quicken your pace."
    )
    print()
    divider()
    wrap("YOU MADE IT.")
    divider()
    print()
    wrap(f"Moves: {state.moves}")
    wrap(f"Locations visited: {len(state.visited)} / {len(LOCATIONS) - 1}")
    wrap(f"Items found: {len(state.inventory)}")
    wrap(f"Health: {state.health}/100")
    print()

    score = 0
    score += len(state.visited) * 5
    score += len(state.inventory) * 10
    score += state.health
    score -= state.moves
    wrap(f"Score: {max(0, score)}")

    state.game_over = True
