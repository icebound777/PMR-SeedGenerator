"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Goomba Village Hammerless Exit.
"""
edges_kmr_add_goomba_village_hammerless_exit_super_boots= [
    # Logic Hack: Since the logic doesn't support homeward shroom, we add a pseudoitem when breaking the block with super boots.
    # This is necessary for Toad Town Start to work, because marking it as no requirements would make entry possible without requirements,
    #  which is part of a separate trick.

    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1 },  "to": {"map": "KMR_02", "id": 0 },  "reqs": [["SuperBoots"]], "pseudoitems": ["RF_BrokeGoombaVillageYellowBlock"], "mapchange": False}, 

    #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 0 },  "to": {"map": "KMR_02", "id": 1 },  "reqs": [["RF_BrokeGoombaVillageYellowBlock"]], "mapchange": False}, 
]

edges_kmr_add_goomba_village_hammerless_exit_laki= [
    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1 },  "to": {"map": "KMR_02", "id": 0 },  "reqs": [["Lakilester"]], "mapchange": False}, 

    #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 0 },  "to": {"map": "KMR_02", "id": 1 },  "reqs": [["Lakilester"]], "mapchange": False}, 
]
