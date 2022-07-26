"""
This file represents edges of the world graph that have origin-nodes in the TIK
(Toad Town Tunnels) area, which have to be added / removed for the Big Chest
Shuffle setting.
"""
# Note: Remove hammer requirements due to removing the blocks guarding this
# chest completely. Makes the chest able to hold a hammer upgrade.
edges_tik_add = [
    # TIK_23 Windy Path (B3) Green Pipe -> Windy Path (B3) Exit Left
    {"from": {"map": "TIK_23", "id": 1}, "to": {"map": "TIK_23", "id": 0}, "reqs": [], "mapchange": False},

    # TIK_24 Hall to Ultra Boots (B3) Exit Right -> Hall to Ultra Boots (B3) Exit Left
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_24", "id": 0}, "reqs": [], "mapchange": False},
]

edges_tik_remove = [
    # TIK_23 Windy Path (B3) Green Pipe -> Windy Path (B3) Exit Left
    {"from": {"map": "TIK_23", "id": 1}, "to": {"map": "TIK_23", "id": 0}, "reqs": [["SuperHammer"]]},

    # TIK_24 Hall to Ultra Boots (B3) Exit Right -> Hall to Ultra Boots (B3) Exit Left
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_24", "id": 0}, "reqs": [["UltraHammer"]]},
]
