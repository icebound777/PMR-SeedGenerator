"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Mt. Rugged Quake Hammer + Letter Partnerless.
"""
edges_iwa_add_quake_hammer_and_letter_partnerless = [
    #* ItemB (Letter01) -> ItemA (QuakeHammer)
    {"from": {"map": "IWA_01", "id": "ItemB"}, "to": {"map": "IWA_01", "id": "ItemA"}, "reqs": [["Boots"]], "mapchange": False},
    #* Mt Rugged 2 Exit Bottom Left -> ItemB (Letter01)
    {"from": {"map": "IWA_01", "id": 0}, "to": {"map": "IWA_01", "id": "ItemB"}, "reqs": [["Boots"]], "mapchange": False},
]
