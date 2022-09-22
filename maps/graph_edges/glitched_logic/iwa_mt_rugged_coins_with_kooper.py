"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Mt. Rugged Coins with Kooper.
"""
edges_iwa_add_mt_rugged_coins_with_kooper = [
    #* Mt Rugged 4 Exit Bottom Right -> ItemC (Coin) (circle-right)
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_03", "id": "ItemC"}, "reqs": [["Kooper"]], "mapchange": False},
    
    #* Mt Rugged 4 Exit Bottom Right -> ItemE (Coin) (circle-bottom-right)
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_03", "id": "ItemE"}, "reqs": [["Kooper"]], "mapchange": False},
    
    #* Mt Rugged 4 Exit Bottom Right -> ItemG (Coin) (circle-top-right)
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_03", "id": "ItemG"}, "reqs": [["Kooper"]], "mapchange": False},
]
