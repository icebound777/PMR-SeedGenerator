"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Jumpless Koopa Village Blue Pipe.
Using Parakarry next to the tree can raise Mario high enough to land on the blue pipe.
"""
edges_nok_add_jumpless_koopa_village_blue_pipe = [
    #? Koopa Village 2 Exit Left -> Koopa Village 2 Blue Pipe
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 2}, "reqs": [["GF_TIK01_WarpPipes"],["Parakarry"]], "mapchange": False}, 
]
