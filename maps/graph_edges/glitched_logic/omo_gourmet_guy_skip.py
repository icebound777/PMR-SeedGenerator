"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Gourmet Guy Skip
"""
edges_omo_add_gourmet_guy_skip_laki = [
    #? PNK Station Exit West -> PNK Station Exit West (Switch Area)
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? PNK Station Exit West (Switch Area) -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_06", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False},
]

edges_omo_add_gourmet_guy_skip_parakarry = [
    #? PNK Station Exit West -> PNK Station Exit West (Switch Area)
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 1}, "reqs": [["Parakarry"], ["Boots"]], "mapchange": False},
    #? PNK Station Exit West (Switch Area) -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_06", "id": 0}, "reqs": [], "mapchange": False},
]

edges_omo_add_gourmet_guy_skip_jump = [
    #? PNK Station Exit West -> PNK Station Exit West (Switch Area)
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 1}, "reqs": [["Boots"]], "mapchange": False},
    #? PNK Station Exit West (Switch Area) -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_06", "id": 0}, "reqs": [], "mapchange": False},
]
