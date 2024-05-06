"""
This file represents edges of the world graph that have to be added / removed
for the "Open Star Way" goal setting.
"""
edges_hos_goal_openstarway_add = [
    #+ HOS_01 Shooting Star Summit Beat Star Hunt
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_01", "id": 1}, "reqs": [], "pseudoitems": ["YOUWIN"]},
]

edges_hos_goal_openstarway_remove = [
    # Shooting Star Summit Ride Up To Starway -> Star Way Ride Down To Summit
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_02", "id": 0}, "reqs": []},
    # Star Way Ride Down To Summit -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_02", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": []},
]
