"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Hammer-less Pleasant Path Bridge Skip.
"""
edges_nok_add_hammerless_bridge_skip_ultra_boots_parakarry= [
    #? Pleasant Path Bridge Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": [["UltraBoots"],["Parakarry"]], "mapchange": False},

    #* Pleasant Path Bridge Exit Left -> ItemA (StarPiece)
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": "ItemA"}, "reqs": [["UltraBoots"],["Parakarry"]], "mapchange": False},
]
