"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Bow-less Tubba's Castle
"""
edges_dgb_add_bowless_tubbas_castle = [
    #? Great Hall Door 1F Bottom -> Great Hall Door 1F Left
    {"from": {"map": "DGB_01", "id": 0}, "to": {"map": "DGB_01", "id": 1}, "reqs": [], "mapchange": False},
    #? Great Hall Door 1F Bottom -> Great Hall Door 1F Right
    {"from": {"map": "DGB_01", "id": 0}, "to": {"map": "DGB_01", "id": 2}, "reqs": [[{"TubbaCastleKey": 1}]], "mapchange": False},
    #? East Hall (1/2F) Door 1F Left -> East Hall (1/2F) Door 2F Left
    {"from": {"map": "DGB_08", "id": 0}, "to": {"map": "DGB_08", "id": 1}, "reqs": [], "mapchange": False},
    #* Spike Trap Room (2F) Door Bottom Left -> ChestA (CastleKey1)
    {"from": {"map": "DGB_12", "id": 0}, "to": {"map": "DGB_12", "id": "ChestA"}, "reqs": [["SpeedySpin"],["Boots"]], "mapchange": False},
]
