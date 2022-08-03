"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Break Stone Blocks With Ultra Boots.
"""
edges_kmr_tik_isk_add_break_stone_blocks_ultra_boots = [
    #* Bottom of the Cliff Exit Right -> HiddenYBlockA (RepelGel)
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": "HiddenYBlockA"}, "reqs": [["UltraBoots"]], "mapchange": False},
    #? Sewer Entrance (B1) Green Pipe Left -> Sewer Entrance (B1) Exit Left
    {"from": {"map": "TIK_06", "id": 2}, "to": {"map": "TIK_06", "id": 0}, "reqs": [["UltraBoots"]], "mapchange": False},
    #* Sand Drainage Room 3 Exit Bottom Left -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": 2}, "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": [["UltraBoots"]],  "mapchange": False},
]
