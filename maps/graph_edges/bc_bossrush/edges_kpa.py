"""
This file represents edges of the world graph that have origin-nodes in the KPA
(Bowser's Castle) area, which have to be added / removed for the
Bowser's Castle Boss Rush setting.
"""
edges_kpa_add = [
    # Fake Peach Hallway Door Left -> Riding Star Ship Scene Fly To Bowser's Castle
    {"from": {"map": "KPA_53",  "id": 0}, "to": {"map": "HOS_20", "id": 2}, "reqs": [], "mapchange": True},
]

edges_kpa_remove = [
    # Fake Peach Hallway Door Left -> Blue Fire Bridge Door Right
    {"from": {"map": "KPA_53",  "id": 0}, "to": {"map": "KPA_102", "id": 1}, "reqs": []},
]
