"""
This file represents edges of the world graph that have origin-nodes in the HOS
(Shooting Star Summit) area, which have to be added / removed for the
Bowser's Castle Boss Rush setting.
"""
edges_hos_add = [
    # Riding Star Ship Scene Fly To Bowser's Castle -> Fake Peach Hallway Door Left
    {"from": {"map": "HOS_20", "id": 2}, "to": {"map": "KPA_53", "id": 0}, "reqs": [], "mapchange": True},
]

edges_hos_remove = [
    # Riding Star Ship Scene Fly To Bowser's Castle -> Ship Enter/Exit Scenes Leave Hangar To Starhaven
    {"from": {"map": "HOS_20", "id": 2}, "to": {"map": "KPA_60", "id": 4}, "reqs": []},
]
