"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Hammerless Jr Playground (Laki Teleport).
"""
edges_kmr_add_hammerless_jr_playground_laki= [

    #? Bottom of the Cliff Exit Left -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 0}, "to": {"map": "KMR_03", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Bottom of the Cliff Exit Right -> Bottom of the Cliff Exit Left
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False},
]
