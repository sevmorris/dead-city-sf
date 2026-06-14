"""World data: LOCATIONS, DANGERS, RANDOM_EVENTS.

Pure data, no logic. Each location is a dict:
    name        — display title
    description — prose shown on look
    exits       — {direction: location_id}
    items       — items found on a successful search
    searched    — whether the area has been searched yet
    search_text — prose shown on search
    examinables — {trigger_substring: close-up flavor} for the examine verb
    danger      — (optional) key into DANGERS, triggered on first entry
"""

LOCATIONS = {
    "house": {
        "name": "Your House — 400 Fair Oaks St",
        "description": (
            "Your house — a two-story Victorian on the corner of 25th, one "
            "of the bay-windowed wooden boxes they threw up all over Noe "
            "Valley a century ago. The windows are cracked and a film of "
            "ash coats every surface. A faded MUNI map is thumbtacked to "
            "the wall above the staircase. Through the broken front-room "
            "glass, Fair Oaks Street runs north, lined with dead trees and "
            "abandoned cars. In the kitchen, the tap drips a slow brown "
            "thread into a sink gone to rust-rings."
        ),
        "exits": {"north": "fair_oaks", "outside": "fair_oaks"},
        "items": ["kitchen knife", "bottled water"],
        "searched": False,
        "search_text": (
            "You rummage through the drawers and cabinets. Under the sink you "
            "find a dusty bottle of water and a dull kitchen knife."
        ),
        "examinables": {
            "map": (
                "The MUNI map, thumbtacked above the stairs, curling at the "
                "corners. In "
                "your own pen, a route is circled — a transfer out to Marin "
                "you kept meaning to take and never did. The ink has gone as "
                "brown as the tapwater."
            ),
            "sink": (
                "The faucet ticks out its slow brown drip into the stained "
                "basin. You stopped drinking from it weeks ago. You still "
                "catch yourself reaching for the handle out of habit."
            ),
            "window": (
                "Ash has settled on the glass thick enough to write in. "
                "Someone already has — a single word, traced by a fingertip. "
                "You're fairly sure it was you."
            ),
        },
    },
    "fair_oaks": {
        "name": "Fair Oaks Street — Noe Valley",
        "description": (
            "Fair Oaks slopes downhill between rows of collapsed Victorians. "
            "A rusted Prius sits on four flats in the middle of the road. "
            "Somewhere south, a dog is barking — the first animal sound "
            "you've heard in weeks. The street continues north toward "
            "the Mission, and south back to 25th Street. To the east, "
            "Guerrero Street runs toward Dolores Park. Westward, 24th "
            "Street climbs into the heart of Noe Valley — its awnings "
            "sagging, its shopfronts dark."
        ),
        "exits": {
            "south": "house",
            "north": "mission_24th",
            "east": "dolores_park",
            "west": "noe_24th_church",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You check the Prius. The glove box has a crumpled map of the "
            "city and a dead phone. Nothing useful."
        ),
        "examinables": {
            "prius": (
                "A COEXIST sticker on the bumper, a residential parking "
                "permit in the window — Zone S, renewed through next year. "
                "The little laws the street used to run on, still solemnly in "
                "force, enforced by no one."
            ),
            "victorian": (
                "Bay windows, gingerbread trim, a century of paint now "
                "peeling in long curls. On one set of steps, a child's "
                "hopscotch grid in chalk, rained almost to nothing."
            ),
            "dog": (
                "You scan south for the barking. You never find it. It's "
                "always a block further down the hill, and it never once "
                "comes closer."
            ),
        },
    },
    "dolores_park": {
        "name": "Dolores Park",
        "description": (
            "The once-green hillside is brown and scorched. The palm trees "
            "still stand, skeletal against the grey sky. Downtown's shattered "
            "skyline is visible to the northeast — the Salesforce Tower leans "
            "at a sickening angle. A makeshift camp of tarps and shopping "
            "carts sits near the playground. It looks recently abandoned. "
            "Paths lead west to Fair Oaks, north toward the Mission, and "
            "a trail heads east to the Castro. To the south, Church Street "
            "and the J-line tracks descend into Noe Valley."
        ),
        "exits": {
            "west": "fair_oaks",
            "north": "mission_24th",
            "east": "castro",
            "south": "noe_24th_church",
        },
        "items": ["canned beans"],
        "searched": False,
        "search_text": (
            "You dig through the abandoned camp. Under a tarp you find a "
            "dented can of beans — still sealed."
        ),
        "examinables": {
            "palm": (
                "The palms came through what the lawn didn't — scorched "
                "along their trunks but still standing, ragged crowns against "
                "the grey. Everything tall in this city has the same "
                "stubbornness."
            ),
            "tower": (
                "Salesforce Tower leans against the skyline at an angle that "
                "hurts to look at. When the wind comes up you can hear it a "
                "mile off — a low structural groan, like the building "
                "clearing its throat to fall."
            ),
            "playground": (
                "The swings hang dead still. In the sandbox, someone has "
                "lined up the plastic toys in a neat row: bucket, shovel, a "
                "faded dump truck. Tidied. That's the part that gets you."
            ),
        },
    },

    # -----------------------------------------------------------------------
    # Noe Valley cluster — the 24th Street commercial strip and its blocks,
    # branching west off Fair Oaks. Two re-entry points into the existing
    # map: north to Dolores Park (via Church St), and up Castro to the Castro.
    # -----------------------------------------------------------------------
    "noe_24th_church": {
        "name": "24th & Church — J-Church Stop",
        "description": (
            "The J-Church streetcar sits dead on its tracks where they run "
            "down the middle of Church Street, doors folded open, a single "
            "rider's tote bag still slumped on a seat. The boarding island "
            "is heaped with wind-blown trash and a tangle of bicycles "
            "nobody came back for. Church Street climbs north toward "
            "Dolores Park and the broken skyline; west, 24th Street opens "
            "into the gutted heart of Noe Valley. Overhead, the catenary "
            "wires have come down in places and lie across the asphalt "
            "like dropped stitches. Fair Oaks is back east."
        ),
        "exits": {
            "east": "fair_oaks",
            "west": "noe_24th_strip",
            "north": "dolores_park",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You step up into the dead streetcar. The fare box has been "
            "pried open and emptied. On the floor: a child's mitten and a "
            "transfer ticket dated the week everything stopped."
        ),
        "examinables": {
            "sign": (
                "The streetcar's destination roll-sign has jammed mid-scroll: "
                "J — CHURCH & — and then a blank stretch of tape where the "
                "rest of the route should be. A line to nowhere, and still, "
                "somehow, perfectly on time."
            ),
            "bicycle": (
                "A dozen bikes are still locked to the rack and the pole and "
                "each other, tires gone flat, frames freckling with rust. "
                "Their owners locked them up carefully against a theft that "
                "turned out to be the least of it."
            ),
            "bag": (
                "A tote bag slumps on a streetcar seat where its owner left "
                "it. Inside: a library book due three days after the sirens, "
                "and a banana long since gone to black liquid in its skin."
            ),
        },
    },
    "noe_24th_strip": {
        "name": "24th Street — Noe Valley",
        "description": (
            "This was the spine of the neighborhood — three cafes, two "
            "florists, a cheese shop, the wine merchants, the bakery that "
            "perfumed the whole block at dawn. Now the awnings sag with ash "
            "and the sidewalk tables lie overturned. Noe Valley Bakery's "
            "window is a cobweb of cracked glass; inside, the pastry cases "
            "are empty and furred with mold. Across the street, a One "
            "Medical clinic — frosted glass and a sans-serif logo dropped "
            "into the shell of the hardware store that anchored the block "
            "for a century — stands gutted, its waiting-room screens dark. "
            "The strip runs east to the streetcar tracks and west toward "
            "Castro; the Town Square gap opens north; the Whole Foods "
            "storefront gapes smashed just off the sidewalk; Sanchez Street "
            "climbs south into the houses."
        ),
        "exits": {
            "east": "noe_24th_church",
            "west": "noe_24th_castro",
            "north": "noe_town_square",
            "south": "sanchez_street",
            "inside": "bell_market",
        },
        "items": ["crowbar"],
        "searched": False,
        "search_text": (
            "You pick through the clinic. The drug lockers were emptied "
            "first, of course — but in a back utility closet, behind a dead "
            "water cooler, a contractor's crowbar lies where someone "
            "dropped it mid-pry."
        ),
        "examinables": {
            "sign": (
                "Where the One Medical logo has peeled away, the old paint "
                "bleeds through underneath: TUGG—, and part of a painted "
                "key. The hardware store stood here a hundred and fourteen "
                "years. The clinic that replaced it lasted eight. Neither "
                "outlived the city by much."
            ),
            "bakery": (
                "Through Noe Valley Bakery's cracked window, a single "
                "croissant sits petrified in the case. The ovens have been "
                "cold for months, but the building still holds onto the smell "
                "of morning and won't quite let it go."
            ),
            "wine": (
                "The wine merchant's racks have been cleared — most bottles "
                "taken, a few smashed underfoot, the good vintages gone first "
                "by the look of the empty slots. Even at the end of "
                "everything, people apparently had standards."
            ),
        },
    },
    "bell_market": {
        "name": "Whole Foods Market — 24th Street",
        "description": (
            "The neighborhood Whole Foods, crammed into half the floor "
            "space of a normal one and twice as dear for it. The automatic "
            "doors are wedged half-open and you squeeze through into a "
            "cavern of toppled shelving and the sweet-rot stink of a "
            "thousand spoiled things — the prepared-foods bar a particular "
            "horror. Most aisles were stripped in the first weeks — you can "
            "read the panic in the wreckage: carts abandoned mid-aisle, a "
            "register drawer flung across the floor. But the picked-over "
            "chaos has its mercies. Cans roll underfoot, and the back of "
            "the store, where the looters lost their nerve in the dark, "
            "looks untouched. The way out is back to 24th Street."
        ),
        "exits": {"outside": "noe_24th_strip"},
        "items": ["bottled water", "canned beans"],
        "searched": False,
        "search_text": (
            "You feel your way to the dark back aisles. Under a fallen "
            "shelf you turn up a dusty four-pack of bottled water and a can "
            "of beans the looters missed. Real food. Real water."
        ),
        "examinables": {
            "terminal": (
                "The checkout still has its Amazon One palm-reader bolted "
                "beside the register — a little glowing dish that used to "
                "take your handprint as payment. The glow is dead now. A "
                "faded decal promises PRIME MEMBERS SAVE MORE to a store "
                "with no members and no power left to read a palm."
            ),
            "register": (
                "The register drawer lies flung clear across the floor, coins "
                "fanned out in the muck. Of everything in this store worth "
                "grabbing, cash was the one thing nobody bothered to take."
            ),
            "cart": (
                "A shopping cart sits abandoned mid-aisle, still half-loaded: "
                "diapers, a bag of dog food, a single birthday candle. "
                "Somebody's perfectly ordinary Tuesday, parked here and never "
                "finished."
            ),
        },
    },
    "noe_town_square": {
        "name": "Noe Valley Town Square — 24th & Vicksburg",
        "description": (
            "The little plaza that used to host the Saturday farmers' "
            "market — once a gas station, then the neighborhood's proudest "
            "patch of public ground. The market stalls are still here, "
            "their canopies shredded to ribbons, tables tipped over crates "
            "of produce gone to black slime and flies. The children's play "
            "structure stands untouched and gleaming, which is somehow the "
            "worst part — the bright primary colors, the empty swings "
            "turning a little in the wind. A community bulletin board by the "
            "entrance is layered with curled flyers: lost pets, lost people, "
            "a hand-lettered MEET HERE IF SEPARATED that nobody met at. "
            "24th Street is back south."
        ),
        "exits": {"south": "noe_24th_strip"},
        "items": ["wool blanket"],
        "searched": False,
        "search_text": (
            "You search the collapsed market stalls. Under a shredded "
            "canopy you find a folded wool blanket — damp, but intact — "
            "and a paper sack of someone's forgotten shopping."
        ),
        "examinables": {
            "board": (
                "The community bulletin board sags under layers of curled "
                "flyers — lost cats, lost dogs, lost people. Dead center, in "
                "marker: MEET HERE IF SEPARATED. The meeting never happened, "
                "though names kept getting added underneath it anyway. Near "
                "the bottom, in tight blue-pen capitals gone faint at the "
                "ends, a later hand: WAITED 3 DAYS. NOBODY CAME. GOING "
                "NORTH. — D"
            ),
            "swing": (
                "The kids' play structure stands bright and untouched, "
                "primary colors gleaming through the ash. You give one swing "
                "a push, just to do it, and the squeak of the chain is the "
                "loudest thing for blocks in any direction."
            ),
            "stall": (
                "The farmers'-market stalls still stand under their shredded "
                "canopies. A chalkboard leans against one: HEIRLOOM TOMATOES "
                "— $4/LB, in a cheerful hand. The tomatoes themselves have "
                "become a black tide across the crates below."
            ),
        },
    },
    "sanchez_street": {
        "name": "Sanchez Street — Noe Valley",
        "description": (
            "A steep residential block of bay-windowed Victorians and "
            "Edwardians, paint peeling in long curls, every garage door "
            "tagged or kicked in. The hill is quiet in the particular way "
            "that means recently quiet — a screen door bangs somewhere, "
            "regular as a clock. Up the rise stands the old Noe Valley "
            "Ministry, its 1888 shingled tower leaning into the fog, the "
            "rose window a black socket. The street pitches north back down "
            "to 24th; south it runs toward Jersey Street and the branch "
            "library."
        ),
        "exits": {
            "north": "noe_24th_strip",
            "south": "noe_library",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You try a few front doors. Most are bolted, but one hangs open "
            "on a dark hallway that smells of cold ash and something worse "
            "beneath it. You don't go in."
        ),
        "examinables": {
            "ministry": (
                "Up the rise, the old Noe Valley Ministry leans its 1888 "
                "shingled tower into the fog. A cloth banner still hangs over "
                "the doors — ALL ARE WELCOME — lifting and falling against a "
                "nave gone black and empty behind it."
            ),
            "window": (
                "The Ministry's rose window is a black socket now, every pane "
                "of colored glass blown out and lying in pieces on the "
                "sidewalk below — a stained-glass mosaic that no one "
                "assembled on purpose."
            ),
            "garage": (
                "Every garage door on the block has been tagged or kicked in, "
                "each in a different hand. Most are gang signs and gibberish. "
                "One, in foot-high dripping letters, just says SORRY."
            ),
        },
    },
    "noe_library": {
        "name": "Noe Valley Library — Jersey Street",
        "description": (
            "The Sally Brunn branch — a squat 1916 Carnegie library, brick "
            "and arched windows, named for the woman who twice fought the "
            "city to keep it open. The front doors are chained, but a side "
            "window has been forced. Inside, the reading room is dim and "
            "swollen with damp; the books have fattened on their shelves and "
            "burst their bindings, and the card-catalogue drawers hang out "
            "like tongues. Someone has been sleeping here — a nest of "
            "blankets in the local-history corner, a stub of candle, a wall "
            "of newspaper clippings pinned up by someone trying to "
            "understand. A brass plaque by the door still reads IN MEMORY "
            "OF SALLY BRUNN. Sanchez Street is back north."
        ),
        "exits": {"north": "sanchez_street"},
        "items": ["city map", "folded note"],
        "searched": False,
        "search_text": (
            "You go through the squatter's clippings and the swollen "
            "reference shelves. Tucked inside an atlas, a folded city map — "
            "water-stained but readable, every bridge and tunnel still "
            "marked. Pressed flat beside it, a page torn from a notebook and "
            "folded into a tight square, set where the next person through "
            "would be sure to find it."
        ),
        "examinables": {
            "clippings": (
                "Newspaper — the last week anyone bothered to print one. "
                "EVACUATION ROUTES. BOIL WATER. The headlines that still "
                "believed in instructions. Someone has gone over them in blue "
                "ballpoint, a small careful hand, underlining, drawing lines "
                "from one page to the next, hunting for the thread. In the "
                "margin, a tally kept like a prisoner's: DAY 51, DAY 52, "
                "DAY 53, each struck through. Keeping the date long after the "
                "date stopped mattering."
            ),
            "plaque": (
                "A brass plaque by the door: IN MEMORY OF SALLY BRUNN. Twice "
                "she fought the city to keep this branch from closing. She'd "
                "have hated to see how, in the end, the doors finally got "
                "left open for good."
            ),
            "catalogue": (
                "The old wooden card catalogue stands with half its drawers "
                "pulled out like tongues. The cards inside are still in "
                "strict alphabetical order — somebody's small, stubborn "
                "insistence that things stay where they belong."
            ),
            "candle": (
                "In the local-history corner, a squatter's nest: a few damp "
                "blankets, a paperback, a candle burned down to a coin of "
                "wax. The wax is recent. Whoever reads here at night cleared "
                "out before you arrived."
            ),
        },
    },
    "noe_24th_castro": {
        "name": "24th & Castro — West Noe Valley",
        "description": (
            "The western end of the strip, where 24th Street meets Castro "
            "and the 24 and 48 buses used to loop. A 48 coach is slewed "
            "across the intersection, every window starred white. Contigo's "
            "corner restaurant sits dark behind a roll-down gate, the "
            "wood-burning oven inside long cold; a chalkboard menu still "
            "advertises a Catalan flatbread special in a confident cursive "
            "hand. Castro Street rises steeply north, climbing out of the "
            "valley toward the Castro proper; just west, on Diamond, the "
            "bulk of St. Philip's church breaks the fog. 24th Street runs "
            "back east into the ruined shops."
        ),
        "exits": {
            "east": "noe_24th_strip",
            "north": "castro",
            "west": "st_philip",
        },
        "items": ["box of matches"],
        "searched": False,
        "search_text": (
            "You force the gate at Contigo and slip into the cold kitchen. "
            "The walk-in is spoiled and the pantry bare, but beside the dead "
            "wood oven you find a dry box of long matches."
        ),
        "examinables": {
            "bus": (
                "The 48 coach sits slewed across the intersection, every "
                "window starred white. Its destination sign still reads "
                "QUINTARA & 24TH ST — a run out to the cold edge of the "
                "Sunset that it is never, now, going to make."
            ),
            "menu": (
                "Contigo's chalkboard menu is still propped in the window, "
                "the day's flatbread special written out in a confident "
                "looping cursive, priced in dollars that stopped meaning "
                "anything weeks ago."
            ),
            "gate": (
                "The restaurant's roll-down gate has been forced up at one "
                "corner, just far enough to crawl under. The same bright "
                "pry-marks scar every gate down the block — the whole street, "
                "methodically trying the same locked doors."
            ),
        },
    },
    "st_philip": {
        "name": "St. Philip the Apostle — Diamond Street",
        "description": (
            "The Catholic parish on Diamond, brick and stucco, its doors "
            "standing open on a long cold nave. Pigeons have got into the "
            "rafters and the floor is white with them. The rows of votive "
            "candles below the side altar have burned down to puddles of "
            "wax — but a few are fresh, relit, which means someone has been "
            "here, praying to whatever's left to pray to. The bell came down "
            "in a quake and lies cracked in the vestibule, big as a bathtub. "
            "A sheet of butcher paper is taped across the holy-water font, "
            "covered edge to edge in names and dates in a dozen different "
            "hands. The way out leads east, back to 24th and Castro."
        ),
        "exits": {"east": "noe_24th_castro"},
        "items": ["votive candle"],
        "searched": False,
        "search_text": (
            "You walk the side altars beneath the saints' chipped faces. "
            "The poor box is long empty, but from the rack of lights you "
            "lift a fat unburned votive candle, still in its red glass cup."
        ),
        "examinables": {
            "font": (
                "A sheet of butcher paper has been taped across the "
                "holy-water font and filled, edge to edge, with names and "
                "dates in a dozen different hands. The missing, or the lost, "
                "or the dead — nobody thought to write down which, and now "
                "nobody can say."
            ),
            "names": (
                "A sheet of butcher paper has been taped across the "
                "holy-water font and filled, edge to edge, with names and "
                "dates in a dozen different hands. The missing, or the lost, "
                "or the dead — nobody thought to write down which, and now "
                "nobody can say."
            ),
            "bell": (
                "The tower bell came down in one of the quakes and lies in "
                "the vestibule, cracked clean across its lip, big as a "
                "bathtub. It rang a hundred years of Sundays, and then it "
                "rang once, for the last one, and stopped."
            ),
            "candle": (
                "Most of the votive candles below the side altar have burned "
                "down to flat puddles of wax — but three of them are lit, "
                "fresh, the flames steady. Someone was here this morning to "
                "light them. Someone may still be."
            ),
            "altar": (
                "The side altar, where the three fresh votives still burn. "
                "Someone knelt here a while — the leather kneeler holds the "
                "dents of it — and left a library card face-down on the rail. "
                "On the back, in the same dry blue capitals: DAY 57. LIT ONE "
                "FOR EVERYONE I'VE GOT LEFT. THAT'S WHY THREE. Below that, "
                "smaller: NORTH IN THE MORNING."
            ),
        },
    },

    "mission_24th": {
        "name": "24th Street Mission — Mission District",
        "description": (
            "The old commercial strip is gutted. La Palma Mexicatessen's "
            "sign hangs by one bolt. The BART entrance at 24th is a dark "
            "mouth in the sidewalk — you can hear water echoing below. "
            "Murals still cover the walls, bright paint peeling in long "
            "strips. The air smells like smoke and wet concrete. Streets "
            "lead south to Fair Oaks, southeast to Dolores Park, and north "
            "deeper into the Mission toward 16th Street."
        ),
        "exits": {
            "south": "fair_oaks",
            "southeast": "dolores_park",
            "north": "mission_16th",
            "down": "bart_tunnel",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You poke through La Palma. The shelves are stripped clean. "
            "Someone got here long before you."
        ),
        "examinables": {
            "mural": (
                "The murals layer the walls decades deep, peeling now in long "
                "curls. A painted row of faces — abuelas, saints, a half-gone "
                "Quetzalcoatl — watches the empty street with the patience "
                "only paint has."
            ),
            "bart": (
                "The stairwell down to the platform is a dark mouth in the "
                "sidewalk. Cold air breathes up out of it, and under that, "
                "the steady echo of water, rising."
            ),
            "sign": (
                "La Palma's sign hangs by its one last bolt. Every so often "
                "it swings, a slow creak — though down here, between the "
                "buildings, there's no wind to move it."
            ),
        },
    },
    "bart_tunnel": {
        "name": "24th Street BART Station — Underground",
        "description": (
            "The escalators are frozen. Ankle-deep water covers the "
            "platform, black and cold. Emergency lights flicker in a slow "
            "dying rhythm. The tunnel stretches north and south into "
            "absolute darkness. Something metallic clangs deep in the "
            "southbound tube. You should not stay here long."
        ),
        "exits": {"up": "mission_24th"},
        "items": ["flashlight"],
        "searched": False,
        "search_text": (
            "You wade along the platform edge. Your hand finds a heavy "
            "MagLite flashlight wedged behind a bench. It still works."
        ),
        "examinables": {
            "water": (
                "Black water stands over the whole platform, ankle-deep and "
                "cold as a well. Now and then something disturbs the surface "
                "a few feet off. You decide, firmly, not to look directly "
                "at it."
            ),
            "escalator": (
                "The escalators have frozen mid-flight, steel teeth bared, "
                "gone back to being an awkward staircase that resents the job."
            ),
            "light": (
                "The emergency lights turn over in a slow dying rhythm. You "
                "catch yourself counting the dark between flickers — and the "
                "count is getting longer."
            ),
        },
        "danger": "rats",
    },
    "castro": {
        "name": "Castro Street",
        "description": (
            "The rainbow crosswalks are faded under grime. The Castro "
            "Theatre's marquee reads 'FINAL SHOW' in crooked letters — "
            "whatever was playing, nobody saw the end. A pharmacy on the "
            "corner has its security gate half-raised. Twin Peaks looms "
            "to the west, and the Mission is to the east. Castro Street "
            "runs south, downhill, toward 24th Street and Noe Valley."
        ),
        "exits": {
            "west": "twin_peaks",
            "east": "dolores_park",
            "south": "noe_24th_castro",
        },
        "items": ["first aid kit"],
        "searched": False,
        "search_text": (
            "You squeeze under the pharmacy gate. Most shelves are "
            "ransacked, but behind the counter you find a first aid kit "
            "with bandages and antiseptic."
        ),
        "examinables": {
            "marquee": (
                "The Castro Theatre marquee still reads FINAL SHOW in crooked "
                "black letters. Whatever was actually playing is gone from the "
                "board. Just the verdict left."
            ),
            "crosswalk": (
                "The rainbow crosswalks have gone grey under grime. You scuff "
                "one with your boot and the color's still under there, bright "
                "as ever. You only do it the once."
            ),
            "gate": (
                "The pharmacy's security gate is frozen half-raised. A square "
                "of cardboard is taped inside the glass, hand-lettered: NO "
                "PILLS NO POINT."
            ),
        },
    },
    "twin_peaks": {
        "name": "Twin Peaks Summit",
        "description": (
            "The wind up here is vicious and cold. You can see the whole "
            "city — or what's left of it. The Bay Bridge is collapsed at "
            "its midpoint, sagging into dark water. Alcatraz sits in fog. "
            "The Golden Gate is still standing, barely, its cables snapped "
            "and swaying. Smoke rises from somewhere in the Sunset. To the "
            "north you can make out the Haight. The Castro is back east "
            "downhill."
        ),
        "exits": {
            "east": "castro",
            "north": "haight",
        },
        "items": ["binoculars"],
        "searched": False,
        "search_text": (
            "Near the overlook railing you find a pair of binoculars. "
            "Through them the Golden Gate resolves into terrifying detail — "
            "vehicles still frozen on the deck."
        ),
        "examinables": {
            "bay": (
                "The Bay Bridge has let go at the midspan, the suspension "
                "half-sunk into dark water, the cantilever simply gone. Of "
                "the two bridges, it was always the one that carried the "
                "most. It's the one that broke."
            ),
            "golden": (
                "The Golden Gate is still up — just. Through the murk its main "
                "cables hang slack and combed apart, swaying like cut harp "
                "strings. Your entire plan, swinging in the wind."
            ),
            "alcatraz": (
                "Alcatraz sits in its collar of fog. The one place in the bay "
                "built to keep people in is now the safest empty rock for "
                "miles."
            ),
        },
    },
    "mission_16th": {
        "name": "16th & Mission",
        "description": (
            "This intersection was rough before the collapse. Now it's "
            "a maze of overturned dumpsters and improvised barricades. "
            "Someone has spray-painted 'ALIVE NORTH' on the side of a "
            "bus shelter with an arrow pointing up Mission Street. The "
            "16th Street BART entrance is sealed with welded steel plates. "
            "You can go south to 24th, or continue north toward Market "
            "Street. Valencia Street runs west toward the Haight."
        ),
        "exits": {
            "south": "mission_24th",
            "north": "market_street",
            "west": "haight",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "Behind a barricade you find graffiti: crude maps drawn right on "
            "the tile in dry blue pen — Mission to Market to the bridge, the "
            "safe blocks linked, the flooded ones crossed out. Warnings "
            "about 'the water.' Tally marks counting days. Somebody was here "
            "for a while — and this time they signed it, scored into the "
            "grout hard enough to outlast them, the same careful hand from "
            "the library given a name at last: DANA REYES. DAY 59."
        ),
        "examinables": {
            "alive": (
                "ALIVE NORTH, spray-painted across the bus shelter, an arrow "
                "jabbing up Mission. The paint's fresh enough that someone "
                "meant it, and old enough now that you can't help doubting it."
            ),
            "barricade": (
                "The barricade is built of overturned dumpsters, chained "
                "together from the inside — by people who aren't here "
                "anymore, against something they thought might be."
            ),
            "bart": (
                "The 16th Street BART entrance is sealed under welded steel "
                "plates, the seams still bright. Whatever they were keeping "
                "in, or out, they were deadly serious about it."
            ),
        },
    },
    "haight": {
        "name": "Haight-Ashbury",
        "description": (
            "The Summer of Love is long over. Head shops and vintage "
            "stores have been gutted. A VW bus rusts at the corner of "
            "Haight and Ashbury, flowers still painted on its side. "
            "Golden Gate Park stretches to the west — vast and overgrown. "
            "The road east leads toward the Mission, and south to Twin "
            "Peaks."
        ),
        "exits": {
            "west": "golden_gate_park",
            "east": "mission_16th",
            "south": "twin_peaks",
        },
        "items": ["rope"],
        "searched": False,
        "search_text": (
            "Inside the VW bus you find a coil of climbing rope. Still "
            "strong."
        ),
        "examinables": {
            "bus": (
                "The flower-painted VW microbus sits on four flats at the "
                "corner. A bumper sticker has bleached almost white in the "
                "sun; you can just make out IF THIS VAN'S ROCKIN' before the "
                "rest gives up."
            ),
            "sign": (
                "The HAIGHT & ASHBURY street signs, once the most-"
                "photographed corner in the city, now photograph no one. "
                "Someone has wired a single dead flower to the pole beneath "
                "them."
            ),
            "shop": (
                "The head shops and vintage stores are gutted to the studs, "
                "mannequins toppled in looted tie-dye. Even the patchouli's "
                "been cleaned out. Especially the patchouli."
            ),
        },
    },
    "golden_gate_park": {
        "name": "Golden Gate Park",
        "description": (
            "The park has gone feral. Trees have swallowed the paths, "
            "and the botanical garden is an impassable jungle. The "
            "de Young Museum is a burnt shell. Bison still roam the "
            "western paddock — you can hear them. A faded sign points "
            "north toward the Richmond District and the bridge. The "
            "Haight is back east."
        ),
        "exits": {
            "east": "haight",
            "north": "richmond",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You push through the undergrowth near the museum. Nothing "
            "but broken glass and charred beams."
        ),
        "examinables": {
            "museum": (
                "The de Young's copper skin has burned and peeled back in "
                "long twisted sheets, the observation tower above it now just "
                "a chimney for smoke that won't quit rising."
            ),
            "bison": (
                "You can hear the bison off in the paddock — a heavy shuffle, "
                "a snort — but never see them through the overgrowth. The herd "
                "has outlived its keepers and its fences and sounds, frankly, "
                "content."
            ),
            "sign": (
                "A parks-department sign points the way: RICHMOND DISTRICT, an "
                "arrow north. Beneath it, scratched into the wood by a later "
                "hand: GO. JUST GO."
            ),
        },
    },
    "richmond": {
        "name": "Richmond District — Geary Boulevard",
        "description": (
            "Fog presses down on rows of pastel houses. Geary Boulevard "
            "stretches east-west, empty except for military vehicles "
            "that never made it out. A checkpoint barrier blocks the road "
            "west toward the coast — razor wire and sandbags. To the north "
            "you can see the approach to the Golden Gate Bridge. The park "
            "is south."
        ),
        "exits": {
            "south": "golden_gate_park",
            "north": "golden_gate_bridge",
            "east": "market_street",
        },
        "items": ["gas mask"],
        "searched": False,
        "search_text": (
            "You search a military Humvee. In the back seat: a gas mask "
            "with a cracked but functional filter."
        ),
        "examinables": {
            "checkpoint": (
                "Razor wire, sandbags, a barrier across Geary. A stencilled "
                "sign still holds the road: TURN BACK — QUARANTINE. The "
                "soldiers who painted it are long gone. The word does its "
                "work on you anyway."
            ),
            "humvee": (
                "The military vehicles sit nose-to-tail, doors hanging open, "
                "keys still in one ignition. Nobody drove them out. Which "
                "tells you the road out was never the part that failed."
            ),
            "house": (
                "Pastel row houses climb away into the fog, identical, "
                "curtains all drawn. You catch yourself imagining someone "
                "behind each one, holding their breath until you've passed."
            ),
        },
    },
    "market_street": {
        "name": "Market Street — Downtown",
        "description": (
            "The grand boulevard is a canyon of broken glass. The Ferry "
            "Building clock tower stopped at 3:47. Streetcar tracks "
            "buckle out of the pavement. The Salesforce Tower's top "
            "floors are gone, sheared off and scattered across blocks. "
            "A massive sinkhole has swallowed the intersection at 5th. "
            "The financial district is to the northeast, and Mission "
            "Street runs south. The Richmond is far west."
        ),
        "exits": {
            "south": "mission_16th",
            "northeast": "financial_district",
            "west": "richmond",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You step carefully around the sinkhole. Down in the gap "
            "you can see flooded MUNI tunnels. The water is rising."
        ),
        "examinables": {
            "clock": (
                "The Ferry Building clock tower stopped at 3:47. Not the "
                "moment it all ended — just the moment the gears finally quit "
                "pretending otherwise."
            ),
            "tower": (
                "Salesforce Tower stands with its crown sheared clean off. "
                "The great LED 'eye' that used to glow over the city at night "
                "is a dead grey socket now, staring at nothing."
            ),
            "track": (
                "The old streetcar tracks have heaved up out of the asphalt "
                "in long buckled ribbons. A vintage F-line car lies on its "
                "side a block down — wood and brass, a museum piece twice "
                "over now."
            ),
        },
    },
    "financial_district": {
        "name": "Financial District — Montgomery Street",
        "description": (
            "Skyscrapers lean against each other like drunks. Paper — "
            "millions of sheets — carpets the streets, fluttering in "
            "the wind. The Transamerica Pyramid's top spike is bent but "
            "it still stands. A ham radio crackles from somewhere above — "
            "you catch fragments: '...safe zone... Marin... bridge still "
            "passable...' The Embarcadero and the waterfront are to the "
            "east. Market Street is southwest."
        ),
        "exits": {
            "southwest": "market_street",
            "east": "embarcadero",
        },
        "items": ["walkie-talkie"],
        "searched": False,
        "search_text": (
            "You follow the radio signal into a lobby. On a security "
            "desk you find a walkie-talkie, still tuned to a frequency. "
            "A voice repeats: 'Marin safe zone. Cross the bridge. Bring "
            "supplies.'"
        ),
        "examinables": {
            "pyramid": (
                "The Transamerica Pyramid's spire is bent like a struck "
                "match, but the thing still stands. Every child's drawing of "
                "this skyline needed that shape. It seems to know it, and "
                "refuses to fall."
            ),
            "paper": (
                "Paper drifts ankle-deep along the canyon — contracts, memos, "
                "quarterly projections. A printed boarding pass tumbles past "
                "your boot, for a flight that never boarded."
            ),
            "radio": (
                "You can hear the ham radio but never find it, somewhere up "
                "in the leaning towers, reciting the same safe-zone message "
                "on a loop. Either a recording, or someone very patient. "
                "Maybe both."
            ),
            "desk": (
                "The security desk the radio signal leads down to. Someone "
                "got here before you — a chair dragged up close, a candle "
                "burned to a stub, a Whole Foods receipt flipped over and "
                "filled in dry blue capitals. DAY 60. HEARD THE VOICE "
                "MYSELF. MARIN. IT'S REAL. The last two words gone over "
                "twice, hard enough to tear the paper. Then, smaller: ONE "
                "MORE DAY. — D.R."
            ),
        },
    },
    "embarcadero": {
        "name": "The Embarcadero — Waterfront",
        "description": (
            "The bay is grey and choppy. The piers are half-submerged — "
            "sea level has risen enough to flood the promenade at high "
            "tide. Fisherman's Wharf is to the north, a long walk along "
            "the crumbling seawall. Seagulls wheel overhead — the only "
            "things thriving. The Financial District is west."
        ),
        "exits": {
            "west": "financial_district",
            "north": "fishermans_wharf",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You check the Ferry Building. The artisan food stalls are "
            "smashed and looted. A rat scurries over your boot."
        ),
        "examinables": {
            "pier": (
                "The piers stand half-drowned, decking awash at the tide "
                "line. Offshore, the tops of parking meters break the surface "
                "in a neat row — a street you could have driven down, once."
            ),
            "gull": (
                "The gulls are fat and loud and absolutely everywhere. "
                "They've inherited the whole waterfront, and from the way "
                "they strut the seawall, they know exactly what they've come "
                "into."
            ),
            "bay": (
                "The bay is grey and shouldering higher than it used to. It's "
                "closer to the roadway than it was last week, and closer than "
                "that the week before — patient, the way only the tide gets "
                "to be."
            ),
        },
    },
    "fishermans_wharf": {
        "name": "Fisherman's Wharf — Pier 39",
        "description": (
            "The sea lions are gone. The carousel is frozen mid-turn, "
            "horses with chipped paint staring at nothing. Alcatraz is "
            "a grey smudge in the fog. From here the road runs west "
            "along the Marina toward the Golden Gate Bridge. The "
            "Embarcadero stretches back south."
        ),
        "exits": {
            "south": "embarcadero",
            "west": "golden_gate_bridge",
        },
        "items": ["flare gun"],
        "searched": False,
        "search_text": (
            "In a harbormaster's shack you find a flare gun with two "
            "charges. Could be useful as a signal — or a weapon."
        ),
        "examinables": {
            "carousel": (
                "The Pier 39 carousel has frozen mid-turn, painted horses "
                "caught mid-gallop and going nowhere. One has lost a glass "
                "eye somewhere along the way. It stares anyway."
            ),
            "lion": (
                "The floating docks where the sea lions used to pile and bark "
                "and stink are bare, boards bleached pale. There's a silence "
                "out there now with a sea-lion shape to it."
            ),
            "alcatraz": (
                "Alcatraz is a grey smudge in the fog. Out past it a foghorn "
                "still sounds on its automated cycle, faithfully warning "
                "ships that aren't coming, won't come, can't."
            ),
        },
    },
    "golden_gate_bridge": {
        "name": "Golden Gate Bridge — South Approach",
        "description": (
            "The bridge towers vanish into fog. Cables hang loose, "
            "swaying and groaning in the wind. The roadway is cracked "
            "but walkable — vehicles are gridlocked bumper to bumper, "
            "doors hanging open, belongings scattered. A hand-painted "
            "sign reads: 'MARIN SAFE ZONE — 2 MI NORTH — BRING WHAT "
            "YOU CAN CARRY.' This is it. The way out."
        ),
        "exits": {
            "south": "richmond",
            "east": "fishermans_wharf",
            "north": "cross_bridge",
        },
        "items": [],
        "searched": False,
        "search_text": (
            "You check a few cars. Personal belongings, a child's "
            "backpack, a paperback novel face-down on a dashboard. "
            "People left in a hurry."
        ),
        "examinables": {
            "sign": (
                "MARIN SAFE ZONE — 2 MI NORTH — BRING WHAT YOU CAN CARRY. The "
                "letters drip where the paint ran, brushed on fast, by a hand "
                "that very badly wanted you to believe it."
            ),
            "cable": (
                "The great cables hang slack and swaying, snapped strands "
                "fanned out into the fog like combed hair. When the wind "
                "leans on them they groan in a register you feel in your "
                "teeth more than hear."
            ),
            "car": (
                "Bumper to bumper, doors flung wide, keys still in the "
                "ignitions — a leash with no dog, a wedding photo face-up on "
                "a dash. On the hood of a grey sedan, scratched deep through "
                "the paint with a key, the pen finally given out: the same "
                "hand you've followed since the library. DANA REYES WAS "
                "HERE. DAY 61. Below it, smaller, pressed in like an "
                "afterthought or a prayer, one more word: ONWARD. The "
                "scratches end there. The fog takes the rest of the span, and "
                "the far end with it. Everyone here got out and walked. So "
                "will you."
            ),
        },
    },
    "cross_bridge": {
        "name": "Golden Gate Bridge — The Crossing",
        "description": "ENDING",
        "exits": {},
        "items": [],
        "searched": False,
        "search_text": "",
        "examinables": {},
    },
}

DANGERS = {
    "rats": {
        "description": (
            "A swarm of rats boils out of the darkness, red eyes "
            "catching the light. They're not afraid of you."
        ),
        "damage": 15,
        "fight_text": "You swing wildly, scattering the swarm.",
        "flee_text": "You splash back to the stairs, rats nipping at your heels.",
    },
}

RANDOM_EVENTS = [
    (
        "A distant explosion echoes across the city. A pillar of smoke "
        "rises from somewhere in the Sunset."
    ),
    "The wind shifts and carries the smell of the ocean — salt and rot.",
    (
        "You hear footsteps on a parallel street. They stop when you "
        "stop. Then nothing."
    ),
    "A crow lands on a fire hydrant and watches you pass.",
    (
        "The ground trembles for a few seconds. Aftershock. Dust sifts "
        "down from above."
    ),
    "You find a faded missing-persons flyer stapled to a pole. Hundreds of names.",
    (
        "Rain begins to fall — grey and oily. It stops after a few "
        "minutes."
    ),
    "A shopping cart rolls slowly down the middle of the street, pushed by the wind.",
    "You step on broken glass. The crunch is deafening in the silence.",
    (
        "For a moment you smell coffee. Impossible. The wind shifts "
        "and it's gone."
    ),
    (
        "Fog pours down off the hill in a slow grey tide and swallows "
        "the block behind you."
    ),
    (
        "An empty stroller has rolled to rest against a curb, one wheel "
        "still lazily turning."
    ),
]
