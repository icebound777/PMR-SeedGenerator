"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Goomba Village Entry Fence Clip.
"""
edges_kmr_add_goomba_village_entry_fence_clip = [
    # Logic Hack: Since the logic doesn't support homeward shroom, we add a pseudoitem when entering the village from the right.
    # This is necessary for Goomba Village Start to work, because marking it as no requirements would mean that itemless village exit is possible,
    # and it's not.

    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1 },  "to": {"map": "KMR_02", "id": 0 },  "reqs": [["RF_EnteredGoombaVillage"]], "mapchange": False}, 

    #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 0 },  "to": {"map": "KMR_02", "id": 1 },  "reqs": [], "pseudoitems": ["RF_EnteredGoombaVillage"], "mapchange": False}, 
]
