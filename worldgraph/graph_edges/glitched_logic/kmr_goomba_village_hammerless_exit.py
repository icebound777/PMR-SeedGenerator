"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Goomba Village Hammerless Exit.
"""
edges_kmr_add_goomba_village_hammerless_exit_npc_lure = [
    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1 },  "to": {"map": "KMR_02", "id": 0 },  "reqs": [], "mapchange": False},
]

edges_kmr_add_goomba_village_hammerless_exit_laki = [
    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1 },  "to": {"map": "KMR_02", "id": 0 },  "reqs": [["Lakilester"]], "mapchange": False},

    #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 0 },  "to": {"map": "KMR_02", "id": 1 },  "reqs": [["Lakilester"]], "mapchange": False},
]
