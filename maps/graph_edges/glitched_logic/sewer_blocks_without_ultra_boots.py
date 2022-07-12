"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Sewer Blocks Without Ultra Boots.
"""
edges_tik_add_sewer_blocks_without_ultra_boots = [
    {"from": {"map": "TIK_20", "id": 1}, "to": {"map": "TIK_20", "id": "YBlockA"}, "reqs": []}, #* Room with Spikes (B2) Exit Right -> YBlockA (ShootingStar)
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_24", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"]]}, #* Hall to Ultra Boots (B3) Exit Right -> HiddenYBlockA (LifeShroom)
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_24", "id": "YBlockA"}, "reqs": []}, #* Hall to Ultra Boots (B3) Exit Right -> YBlockA (Coin)
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_24", "id": "YBlockB"}, "reqs": []}, #* Hall to Ultra Boots (B3) Exit Right -> YBlockB (Coin)
]
