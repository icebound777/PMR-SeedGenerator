"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Jumpless Dane T Letters.
From the train station platform, Parakarry can be used to climb the opposite ledge before
the camera finishes turning, allowing Dane T's two letters to be delivered without boots.

Jumpless Ledge: https://youtu.be/uhiUKmlG3VY 
"""
edges_mac_jumpless_dane_t_letters = [
    #* Station District -> Dane T letter turn in
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_03", "id": "GiftA"}, "reqs": [["Parakarry"],["Letter20"]], "mapchange": False},
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_03", "id": "GiftB"}, "reqs": [["Parakarry"],["Letter22"]], "mapchange": False}
]
