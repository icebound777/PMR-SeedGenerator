"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Mt. Rugged Station Jumpless Climb.
"""
edges_iwa_add_mt_rugged_station_jumpless_climb_bombette= [
    #? Train Station Ride The Train -> Train Station Exit Top Right
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": [["Bombette"], ["SpeedySpin"], ["Parakarry"]], "mapchange": False},
]

edges_iwa_add_mt_rugged_station_jumpless_climb_laki_block_clip= [
    #* Train Station Ride The Train -> RandomBlockItemA (GenericUpgrade)
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": "RandomBlockItemA"}, "reqs": [["Lakilester"], ["can_hit_floating_blocks"]], "mapchange": False},
    #? RandomBlockItemA (GenericUpgrade) -> Train Station Exit Top Right
    {"from": {"map": "IWA_10", "id": "RandomBlockItemA"}, "to": {"map": "IWA_10", "id": 1}, "reqs": [["Lakilester"], ["SpeedySpin"], ["Hammer"]], "mapchange": False},
]

edges_iwa_add_mt_rugged_station_jumpless_climb_laki= [
    #* Train Station Ride The Train -> RandomBlockItemA (GenericUpgrade)
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": "RandomBlockItemA"}, "reqs": [["Lakilester"], ["can_hit_floating_blocks"]], "mapchange": False},
    #? Train Station Ride The Train -> Train Station Exit Top Right
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": [["Lakilester"], ["SpeedySpin"]], "mapchange": False},
]
