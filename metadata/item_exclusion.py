"""
This file offers lists of items related to the removal of useless items
during certain randomizer settings.
"""

exclude_due_to_settings = {
    "startwith_bluehouse_open": [
        "OddKey"
    ],
    "startwith_forest_open": [
        "ForestPass"
    ],
    "magical_seeds_required": {
        0: [
            "MagicalSeed1",
            "MagicalSeed2",
            "MagicalSeed3",
            "MagicalSeed4",
        ],
        1: [
            "MagicalSeed1",
            "MagicalSeed2",
            "MagicalSeed3",
        ],
        2: [
            "MagicalSeed1",
            "MagicalSeed2",
        ],
        3: [
            "MagicalSeed1",
        ],
    },
    "shorten_bowsers_castle": [
        "BowserCastleKeyA",
        "BowserCastleKeyB",
        "BowserCastleKeyC",
        "BowserCastleKeyD",
        "BowserCastleKeyE",
    ],
    "boss_rush": [
        "PrisonKeyA",
        "PrisonKeyB",
    ],
    "always_speedyspin": [
        "SpeedySpin",
    ],
    "always_ispy": [
        "ISpy",
    ],
    "always_peekaboo": [
        "Peekaboo",
    ],
    "do_randomize_dojo": [
        "FirstDegreeCard",
        "SecondDegreeCard",
        "ThirdDegreeCard",
        "FourthDegreeCard",
        "Diploma",
    ],
    "do_progressive_badges": [
        "SmashCharge0",
        "SmashCharge",
        "SSmashChg",
        "JumpCharge0",
        "JumpCharge",
        "SJumpChg",
        "PowerJump",
        "SuperJump",
        "MegaJump",
        "PowerSmash1",
        "SuperSmash",
        "MegaSmash",
        "QuakeHammer",
        "PowerQuake",
        "MegaQuake"
    ],
    "partner_upgrade_shuffle": [
        "UltraStone",
        "Nothing", # Goombario 1
        "Nothing", # Goombario 2
        "Nothing", # Kooper 1
        "Nothing", # Kooper 2
        "Nothing", # Bombette 1
        "Nothing", # Bombette 2
        "Nothing", # Parakarry 1
        "Nothing", # Parakarry 2
        "Nothing", # Watt 1
        "Nothing", # Watt 2
        "Nothing", # Sushie 1
        "Nothing", # Sushie 2
        "Nothing", # Lakilester 1
        "Nothing", # Lakilester 2
        "Nothing", # Bow 1
        "Nothing", # Bow 2
    ]
}

exclude_from_taycet_placement = [
    0x0B5, # "Koopasta",
    0x0C1, # "Cake",
    0x0C2, # "Mistake",
    0x0C3, # "KoopaTea",
    0x0D3, # "KookyCookie",
    0x0D6, # "NuttyCake",
]
