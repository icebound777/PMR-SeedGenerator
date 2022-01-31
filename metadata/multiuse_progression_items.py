"""
This dict lists item requirements used for edge requirements and their
    substitute items.
The dict key describes a type of item which is used to progress in multiple
    places of the world graph. The key is to be listed within an edge
    requirement list. The item name used as key does not actually exist within
    the item pool, it is merely used a grouping term.
The dict value is a list of all actual items that can substitute for an edge
    requirement of the dict key.
This dict does not list pseudoitems or misc progression items, as both of these
    groups are considered infinitely reusable.
Example: An edge may require a "RuinsKey" item to traverse. When encountered
    by the logic module, this "RuinsKey" item must be recognized as multiuse
    progression item, and instead of searching Mario's inventory for a
    "RuinsKey" item, it is instead to be searched for any of the "RuinsKeyA"
    to "RuinsKeyD" items listed here.
"""
multiuse_progression_items = {
    "KoopaFortressKey": [
        "KoopaFortressKeyA",
        "KoopaFortressKeyB",
        "KoopaFortressKeyC",
        "KoopaFortressKeyD",
    ],
    "RuinsKey": [
        "RuinsKeyA",
        "RuinsKeyB",
        "RuinsKeyC",
        "RuinsKeyD",
    ],
    "TubbaCastleKey": [
        "TubbaCastleKeyA",
        "TubbaCastleKeyB",
        "TubbaCastleKeyC",
    ],
    "BowserCastleKey": [
        "BowserCastleKeyA",
        "BowserCastleKeyB",
        "BowserCastleKeyC",
        "BowserCastleKeyD",
        "BowserCastleKeyE",
    ],
}