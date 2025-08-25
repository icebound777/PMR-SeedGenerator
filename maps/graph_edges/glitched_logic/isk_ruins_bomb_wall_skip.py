"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Ruins Bomb Wall Skip.

Using Clippy, you can get around needing Bombette for the first bomb wall.
From Mr.Zebra: https://youtu.be/fzaKLpS0wE8?si=WQCWcvbDX75YBxpL
"""
edges_isk_add_ruins_bomb_wall_skip = [
    #? Descending Stairs 1 Exit Middle Left -> Descending Stairs 1 Exit Top Right Cracked Wall
    {"from": {"map": "ISK_04", "id": 0}, "to": {"map": "ISK_04", "id": 2}, "reqs": [["Lakilester"],["Boots"]], "mapchange": False}, 
]