# ACTIONS

GO = {
    "proceed",
    "tiptoe",
    "travel",
    "crawl",
    "lead",
    "move",
    "swim",
    "turn",
    "walk",
    "run",
    "go",
}
PUT = {
    "position",
    "apply",
    "place",
    "lay",
    "put",
    "set",
}
OPEN = {
    "unlock",
    "open",
}
CLOS = {
    "close",
    "lock",
    "shut",
}
TALK = {
    "talk",
    "tell",
    "ask",
    "say",
}
LOOK = {
    "look",
    "view",
    "see",
    "l",
}
INSP = {
    "examine",
    "inspect",
    "search",
    "x",
}
GIVE = {
    "present",
    "grant",
    "throw",
    "feed",
    "gift",
    "give",
    "hand",
    "pass",
}
TAKE = {
    "acquire",
    "choose",
    "select",
    "carry",
    "claim",
    "grab",
    "hold",
    "pack",
    "pick",
    "take",
    "get",
}
ATAK = {
    "assault",
    "attack",
    "defeat",
    "squash",
    "squish",
    "slice",
    "smack",
    "chop",
    "kill",
    "poke",
    "stab",
    "jab",
}
CAST = {
    "conjure",
    "enchant",
    "incant",
    "invoke",
    "cast",
}

# COMMANDS

UNDO = {
    "undo",
    "u",
}
AGAIN = {
    "repeat",
    "again",
    "g",
}
INVEN = {
    "inventory",
    "backpack",
    "items",
    "i",
}
SAVE = {
    "backup",
    "save",
    "b",
}
LOAD = {
    "restore",
    "load",
    "r",
}
QUIT = {
    "quit",
    "q",
}
MAP = {
    "map",
    "m",
}

# ACCEPTABLE COMMANDS

ACTIONS = (
    ATAK
    | CAST
    | CLOS
    | GIVE
    | INSP
    | LOOK
    | OPEN
    | TAKE
    | TALK
    | PUT
    | GO
)
MENU = (
    AGAIN
    | INVEN
    | LOAD
    | QUIT
    | SAVE
    | UNDO
    | MAP
)
DIRS = {
    "north",
    "south",
    "east",
    "west",
    "n",
    "s",
    "e",
    "w",
}
CMDS = ACTIONS | DIRS | MENU
CHART = dict(
    zip(
        (
            "inventory",
            "inspect",
            "attack",
            "again",
            "close",
            "cast",
            "give",
            "load",
            "look",
            "open",
            "quit",
            "save",
            "take",
            "talk",
            "undo",
            "map",
            "put",
            "go",
        ),
        (
            INVEN,
            INSP,
            ATAK,
            AGAIN,
            CLOS,
            CAST,
            GIVE,
            LOAD,
            LOOK,
            OPEN,
            QUIT,
            SAVE,
            TAKE,
            TALK,
            UNDO,
            MAP,
            PUT,
            GO,
        ),
    )
)

# PARTS OF SPEECH

ARTS = {
    "these",
    "those",
    "that",
    "this",
    "the",
    "an",
    "a",
}
PREP = {
    "considering",
    "concerning",
    "throughout",
    "underneath",
    "regarding",
    "against",
    "athwart",
    "beneath",
    "besides",
    "between",
    "betwixt",
    "despite",
    "outside",
    "through",
    "without",
    "across",
    "around",
    "before",
    "behind",
    "beside",
    "beyond",
    "during",
    "except",
    "inside",
    "toward",
    "within",
    "about",
    "above",
    "after",
    "along",
    "among",
    "below",
    "circa",
    "minus",
    "round",
    "since",
    "under",
    "until",
    "amid",
    "down",
    "from",
    "into",
    "like",
    "near",
    "onto",
    "over",
    "past",
    "plus",
    "save",
    "than",
    "unto",
    "upon",
    "with",
    "but",
    "for",
    "off",
    "out",
    "per",
    "via",
    "as",
    "at",
    "by",
    "in",
    "of",
    "on",
    "to",
    "up",
}
