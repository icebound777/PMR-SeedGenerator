"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Parakarry-less Boo's Portrait.
"""
edges_obk_add_boo_portrait_kooper = [
    #* Library Fall From Ceiling -> ItemA (BooPortrait)
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": "ItemA"},  "reqs": [["Kooper"]], "mapchange": False},
    #* ItemA (BooPortrait) -> Library Fall From Ceiling
    {"from": {"map": "OBK_06", "id": "ItemA"},  "to": {"map": "OBK_06", "id": 0}, "reqs": [], "mapchange": False},
]

edges_obk_add_boo_portrait_laki = [
    #* Library Bombable Wall -> ItemA (BooPortrait)
    {"from": {"map": "OBK_06", "id": 1}, "to": {"map": "OBK_06", "id": "ItemA"}, "reqs": [["Lakilester"],["Boots"]], "mapchange": False},
    #* ItemA (BooPortrait) -> Library Fall From Ceiling
    {"from": {"map": "OBK_06", "id": "ItemA"},  "to": {"map": "OBK_06", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False},
    #* Library Bombable Wall -> Library Fall From Ceiling
    {"from": {"map": "OBK_06", "id": 1}, "to": {"map": "OBK_06", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Library Fall From Ceiling -> Library Bombable Wall
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Pot Room Door South -> Pot Room Hole Under Planks
    {"from": {"map": "OBK_05", "id": 0}, "to": {"map": "OBK_05", "id": 1}, "reqs": [["SuperBoots"], ["Lakilester"]], "mapchange": False},
]
