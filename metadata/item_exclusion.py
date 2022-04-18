"""
This file offers lists of items related to the removal of useless items
during certain randomizer settings.
"""

exclude_due_to_settings = {
    "startwith_bluehouse_open": [
        "OddKey"
    ],
    "startwith_flowergate_open": [
        "MagicalSeed1",
        "MagicalSeed2",
        "MagicalSeed3",
        "MagicalSeed4",
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
}

exclude_from_taycet_placement = [
    0x0B5, # "Koopasta",
    0x0C1, # "Cake",
    0x0C2, # "Mistake",
    0x0C3, # "KoopaTea",
    0x0D3, # "KookyCookie",
    0x0D6, # "NuttyCake",
]