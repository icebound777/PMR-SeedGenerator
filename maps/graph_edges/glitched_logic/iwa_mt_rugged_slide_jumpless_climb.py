"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Mt. Rugged Slide Jumpless Climb.
"""

edges_iwa_add_mt_rugged_slide_jumpless_climb_laki= [
    #? Mt Rugged 1 Exit Left -> Mt Rugged 1 Exit Right
    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},

    #* Mt Rugged 1 Exit Left -> ItemB (Coin)
    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": "ItemB"}, "reqs": [["Lakilester"]], "mapchange": False},
    #* Mt Rugged 1 Exit Right -> ItemB (Coin)
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": "ItemB"}, "reqs": [["Lakilester"]], "mapchange": False},
    #* Mt Rugged 1 Exit Left -> ItemC (Coin)
    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": "ItemC"}, "reqs": [["Lakilester"]], "mapchange": False}, 
    #* Mt Rugged 1 Exit Right -> ItemC (Coin)
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": "ItemC"}, "reqs": [["Lakilester"]], "mapchange": False},

] 
