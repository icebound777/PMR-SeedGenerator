"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Blocks to Shiver City with Kooper Shell Item Throw
"""
edges_tik_add_blocks_to_shiver_city_kooper_shell_item_throw = [
    #! note: this does not take into account actually having consumables to throw

    #* Hidden Blocks Room (B2) Top Right Door -> YBlockA (Coin)
    {"from": {"map": "TIK_21", "id": 1}, "to": {"map": "TIK_21", "id": "YBlockA"}, "reqs": [["Kooper"],["Boots"]], "mapchange": False},
    #* Hidden Blocks Room (B2) Top Right Door -> YBlockB (Coin)
    {"from": {"map": "TIK_21", "id": 1}, "to": {"map": "TIK_21", "id": "YBlockB"}, "reqs": [["Kooper"],["Boots"]], "mapchange": False},
]
