"""This meta file houses misc. data about partners."""

all_partners = [
    "Goombario",
    "Kooper",
    "Bombette",
    "Parakarry",
    "Bow",
    "Watt",
    "Sushie",
    "Lakilester",
]

partner_moves = {
    "Goombario": [
        "Headbonk",
        "Tattle",
        "Charge",
        "Multibonk",
    ],
    "Kooper": [
        "ShellToss",
        "PowerShell",
        "DizzyShell",
        "FireShell",
    ],
    "Bombette": [
        "BodySlam",
        "Bomb",
        "PowerBomb",
        "MegaBomb",
    ],
    "Parakarry": [
        "SkyDive",
        "ShellShot",
        "AirLift",
        "AirRaid",
    ],
    "Bow": [
        "Smack",
        "OuttaSight",
        "Spook",
        "FanSmack",
    ],
    "Watt": [
        "ElectroShock",
        "PowerShock",
        "TurboCharge",
        "MegaShock",
    ],
    "Sushie": [
        "BellyFlop",
        "Squirt",
        "WaterBlock",
        "TidalWave",
    ],
    "Lakilester": [
        "SpinyFlip",
        "SpinySurge",
        "CloudNine",
        "Hurricane",
    ],
}

all_progressive_partners = [
    f"{x}Proxy{y+1}"
    for x in all_partners
    for y in range(3)
]
