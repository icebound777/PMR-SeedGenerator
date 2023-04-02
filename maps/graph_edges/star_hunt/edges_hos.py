"""
This file represents edges of the world graph that have to be added / removed
for the Star Hunt setting.
"""
edges_hos_starhunt_add = [
    #? HOS_01 Shooting Star Summit Exit Bottom Left -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_01", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": [["can_climb_steps"]]},
]

edges_hos_starhunt_remove = [
    #? HOS_01 Shooting Star Summit Exit Bottom Left -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_01", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": [[{"starspirits": 7}],["can_climb_steps"]]},
]

edges_hos_starhunt2credits_add = [
    #+ HOS_01 Shooting Star Summit Beat Star Hunt
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_01", "id": 1}, "reqs": [], "pseudoitems": ["YOUWIN"]},
]

edges_hos_starhunt2credits_remove = [
    # Shooting Star Summit Ride Up To Starway -> Star Way Ride Down To Summit
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_02", "id": 0}, "reqs": []},
    # Star Way Ride Down To Summit -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_02", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": []},
]
