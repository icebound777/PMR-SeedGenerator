"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Forever Forest Backwards.
These edges circumvent the requirement for the RF_ForeverForestBackwards flag,
which isn't actually added to Mario's inventory ever.
"""
edges_mim_add_forever_forest_backwards = [
    #? Outside Boo's Mansion Entrance to Wasteland -> Outside Boo's Mansion Forever Forest Entrance
    {"from": {"map": "MIM_11", "id": 1}, "to": {"map": "MIM_11", "id": 0}, "reqs": [], "mapchange": False},
]
