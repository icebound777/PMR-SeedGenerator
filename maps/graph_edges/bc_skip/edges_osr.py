"""
This file represents edges of the world graph that have origin-nodes in the OSR
(Peach's Castle Grounds) area, which have to be added / removed for the
Bowser's Castle Bowsers Only setting.
"""
edges_osr_add = [
    # Hijacked Castle Entrance Door West -> Riding Star Ship Scene Fly To Bowser's Castle
    {"from": {"map": "OSR_02",  "id": 0}, "to": {"map": "HOS_20", "id": 2}, "reqs": [], "mapchange": True},
]

edges_osr_remove = [
    # Hijacked Castle Entrance Door West -> Exit to Peach's Castle
    {"from": {"map": "OSR_02",  "id": 0}, "to": {"map": "KPA_121", "id": 1}, "reqs": []},
]
