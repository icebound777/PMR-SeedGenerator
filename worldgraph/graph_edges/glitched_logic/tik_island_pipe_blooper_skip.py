"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Island Pipe Blooper Skip / Jumpless Island Pipe.

Jumpless Island Pipe (method can be used for both tricks): https://www.youtube.com/watch?v=iew-IZHxKgw
"""
edges_tik_add_island_pipe_blooper_skip = [
    #? Second Level Entry (B2) Exit Left -> Second Level Entry (B2) Exit Right
    {"from": {"map": "TIK_08", "id": 0}, "to": {"map": "TIK_08", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False}
]

edges_tik_add_jumpless_island_pipe = [
    #? Second Level Entry (B2) Exit Left -> Second Level Entry (B2) Blue Warp Pipe
    {"from": {"map": "TIK_08", "id": 0}, "to": {"map": "TIK_08", "id": 4}, "reqs": [["Lakilester"]], "pseudoitems": ["GF_TIK08_WarpPipe"], "mapchange": False}
]
