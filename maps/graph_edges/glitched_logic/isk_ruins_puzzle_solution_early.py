"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Ruins Puzzle Solution Early.
This trick uses Lakilester to clip into the stairs of the lower part of the room,
and fall out of bounds, landing in the upper part where the switch is located.
"""
edges_isk_add_ruins_puzzle_solution_early= [
    #? Sand Drainage Room 3 Exit Top Left -> Sand Drainage Room 3 Exit Upper Room Left
    {"from": {"map": "ISK_12", "id": 1}, "to": {"map": "ISK_12", "id": 0}, "reqs": [["Lakilester"], ["Boots"]], "mapchange": False},
]
