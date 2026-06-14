"""Item use logic.

`use_item` is the single entry point, dispatched from cmd_use. Items not
handled here are inert collectibles — they can be carried (and count toward
the end-game score) but have no special effect yet.
"""

from .utils import wrap


# Close-up flavor for carried items, surfaced by `examine`. Keys are the
# canonical item names. Examining never consumes or changes anything.
ITEM_DESCRIPTIONS = {
    "kitchen knife": (
        "A dull kitchen knife, the edge nicked and freckled with rust. It "
        "won't win a fight, but it's better in your hand than in a drawer."
    ),
    "bottled water": (
        "A dusty plastic bottle, the seal still unbroken. The water inside "
        "is clear — maybe the last clear water you'll see for a while."
    ),
    "canned beans": (
        "A dented can of beans, label half-peeled, still sealed. The "
        "expiration date is next year. Next year feels theoretical."
    ),
    "flashlight": (
        "A heavy MagLite, the kind that's a club as much as a light. The "
        "beam is strong and the battery, miraculously, still holds."
    ),
    "first aid kit": (
        "A field first aid kit: bandages, antiseptic, a tube of something "
        "for burns. Enough to put you back together once, maybe twice."
    ),
    "rope": (
        "A coil of synthetic climbing rope, forty feet or so, still strong. "
        "Good for a descent, for hauling — or for worse, if it comes to it."
    ),
    "binoculars": (
        "Compact field binoculars, one lens scratched. Through them, far "
        "things become near and terrible in equal measure."
    ),
    "walkie-talkie": (
        "A handheld radio, still warm with battery, tuned to the one "
        "frequency that ever answers: the Marin safe zone, looping at dawn."
    ),
    "gas mask": (
        "A military gas mask, the filter cracked but holding. It smells of "
        "old rubber and other people's fear."
    ),
    "flare gun": (
        "An orange flare gun, two charges seated in the grip. A signal, a "
        "distress call, or a last resort — depending which way you point it."
    ),
    "crowbar": (
        "A heavy iron crowbar, pitted with rust but dead straight. The "
        "honest weight of it is a small comfort, and a small temptation."
    ),
    "wool blanket": (
        "A folded wool blanket, grey and faintly damp, smelling of the "
        "market stall it came from. It'd be the warmest thing you own, if "
        "the nights were the worst of your problems."
    ),
    "city map": (
        "A folded street map of San Francisco, water-stained but legible. "
        "Every bridge, tunnel, and numbered pier still printed right where "
        "it used to be."
    ),
    "box of matches": (
        "A box of long fireplace matches from Contigo's kitchen, dry and "
        "rattling full. Fire is one of the few things still worth what it "
        "always was."
    ),
    "votive candle": (
        "A fat votive candle in a little red glass cup, lifted from the rack "
        "at St. Philip's. Unburned — a few hours of light, or a small act of "
        "faith, depending how you strike it."
    ),
    "folded note": (
        "A page torn from a notebook, folded into a tight square, the creases "
        "gone soft from handling. Small block capitals in blue ballpoint, the "
        "ink dying toward the bottom of the page:\n\n"
        "DAY 55. Tap water will kill you — don't.\n"
        "Library back room holds heat.\n"
        "Radio downtown says Marin, over the bridge. Going to try.\n"
        "The maps are mine. Follow them out. Don't wait for anyone.\n"
        "— D"
    ),
}


def describe_item(inventory, target):
    """Return examine flavor for a carried item matching `target`, else None.

    Matches a carried item when `target` is a substring of the item name or
    vice versa (so `knife` finds `kitchen knife`). Longest name wins.
    """
    matches = [
        item for item in inventory
        if item in ITEM_DESCRIPTIONS and (target in item or item in target)
    ]
    if not matches:
        return None
    return ITEM_DESCRIPTIONS[max(matches, key=len)]


def use_item(state, item_name):
    if item_name in ("first aid kit", "first aid", "medkit", "kit"):
        if "first aid kit" in state.inventory:
            heal = min(40, 100 - state.health)
            state.health += heal
            state.inventory.remove("first aid kit")
            wrap(f"You patch yourself up. Restored {heal} health. Health: {state.health}")
        else:
            wrap("You don't have a first aid kit.")
    elif item_name in ("water", "bottled water"):
        if "bottled water" in state.inventory:
            heal = min(10, 100 - state.health)
            state.health += heal
            state.thirst = 0
            state.inventory.remove("bottled water")
            wrap(f"You drink the water. Restored {heal} health. Health: {state.health}")
        else:
            wrap("You don't have any water.")
    elif item_name in ("beans", "canned beans", "food"):
        if "canned beans" in state.inventory:
            heal = min(15, 100 - state.health)
            state.health += heal
            state.hunger = 0
            state.inventory.remove("canned beans")
            wrap(f"You eat the cold beans. Not great, but nourishing. Restored {heal} health. Health: {state.health}")
        else:
            wrap("You don't have any food.")
    elif item_name in ("walkie-talkie", "walkie", "radio"):
        if "walkie-talkie" in state.inventory:
            wrap(
                "You key the walkie-talkie. Static, then a voice: "
                "'...safe zone is active. Marin headlands. Cross the "
                "Golden Gate. We have food, water, shelter. Bring "
                "whoever you can. We're here every day at dawn.' "
                "The signal fades."
            )
        else:
            wrap("You don't have a walkie-talkie.")
    elif item_name in ("binoculars",):
        if "binoculars" in state.inventory:
            if state.location == "twin_peaks":
                wrap(
                    "Through the binoculars you see movement on the "
                    "Golden Gate Bridge — figures crossing north. The "
                    "safe zone is real."
                )
            elif state.location == "golden_gate_bridge":
                wrap(
                    "You scan the Marin side. Tents, campfires, "
                    "movement. People. Living people."
                )
            else:
                wrap("You scan the surroundings. Ruin in every direction.")
        else:
            wrap("You don't have binoculars.")
    elif item_name in ("flare", "flare gun"):
        if "flare gun" in state.inventory:
            if state.location == "golden_gate_bridge":
                wrap(
                    "You fire a flare into the fog. It arcs red across "
                    "the sky. From the Marin side, an answering flare "
                    "rises. They see you."
                )
            else:
                wrap(
                    "You fire a flare. It streaks into the grey sky "
                    "and fades. Probably not the best time for that."
                )
        else:
            wrap("You don't have a flare gun.")
    else:
        wrap(f"You can't figure out how to use '{item_name}' right now.")
