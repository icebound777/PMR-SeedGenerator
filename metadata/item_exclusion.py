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
    "do_randomize_dojo": {
        1: [ # Chan
            "FirstDegreeCard",
        ],
        2: [ # Lee
            "FirstDegreeCard",
            "SecondDegreeCard",
        ],
        3: [ # Master1
            "FirstDegreeCard",
            "SecondDegreeCard",
            "ThirdDegreeCard",
        ],
        4: [ # Master2
            "FirstDegreeCard",
            "SecondDegreeCard",
            "ThirdDegreeCard",
            "FourthDegreeCard",
        ],
        5: [ # Master3
            "FirstDegreeCard",
            "SecondDegreeCard",
            "ThirdDegreeCard",
            "FourthDegreeCard",
            "Diploma",
        ],
    },
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
        "GenericUpgrade", # Goombario 1
        "GenericUpgrade", # Goombario 2
        "GenericUpgrade", # Kooper 1
        "GenericUpgrade", # Kooper 2
        "GenericUpgrade", # Bombette 1
        "GenericUpgrade", # Bombette 2
        "GenericUpgrade", # Parakarry 1
        "GenericUpgrade", # Parakarry 2
        "GenericUpgrade", # Watt 1
        "GenericUpgrade", # Watt 2
        "GenericUpgrade", # Sushie 1
        "GenericUpgrade", # Sushie 2
        "GenericUpgrade", # Lakilester 1
        "GenericUpgrade", # Lakilester 2
        "GenericUpgrade", # Bow 1
        "GenericUpgrade", # Bow 2
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
