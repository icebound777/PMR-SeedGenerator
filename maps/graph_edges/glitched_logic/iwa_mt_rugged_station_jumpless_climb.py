"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Mt. Rugged Station Jumpless Climb.
"""
edges_iwa_add_mt_rugged_station_jumpless_climb_bombette= [
    #? Train Station Ride The Train -> Train Station Exit Top Right
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": [["Bombette"], ["SpeedySpin"]], "mapchange": False},
    
    #? Train Station Exit Top Right -> Train Station Ride The Train
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": 0}, "reqs": [["Bombette"], ["SpeedySpin"]], "mapchange": False},
] 

edges_iwa_add_mt_rugged_station_jumpless_climb_laki= [
    #? Train Station Ride The Train -> Train Station Exit Top Right
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": [["Lakilester"], ["SpeedySpin"]], "mapchange": False},
    
    #? Train Station Exit Top Right -> Train Station Ride The Train
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": 0}, "reqs": [["Lakilester"], ["SpeedySpin"]], "mapchange": False},
] 
