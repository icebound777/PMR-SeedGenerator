"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Break Yellow Blocks With Super Boots.
"""
edges_kmr_add_break_yellow_blocks_super_boots = [

    #? Bottom of the Cliff Exit Left -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 0}, "to": {"map": "KMR_03", "id": 1}, "reqs": [["SuperBoots"]], "mapchange": False},
    #? Bottom of the Cliff Exit Right -> Bottom of the Cliff Exit Left
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": 0}, "reqs": [["SuperBoots"]], "mapchange": False},
]
