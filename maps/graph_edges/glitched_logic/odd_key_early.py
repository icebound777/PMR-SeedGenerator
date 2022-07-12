"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Odd Key Early.
"""
edges_mac_odd_key_early = [
    # TODO: Find a proper fix for the error that logic could think you can go from Item A to Blue Pipe when obtaining ItemA with OddKeyEarly
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": "ItemA"}, "reqs": [["Hammer"]], "mapchange": False}, #* Southern District Exit Top -> ItemA (OddKey)
    {"from": {"map": "MAC_02", "id": "ItemA"}, "to": {"map": "MAC_02", "id": 2}, "reqs": [], "mapchange": False} #* ItemA (OddKey) -> Southern District Exit Top
]

