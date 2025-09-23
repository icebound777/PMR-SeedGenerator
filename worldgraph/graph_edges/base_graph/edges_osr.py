"""This file represents all edges of the world graph that have origin-nodes in the OSR (Peach's Castle Grounds) area."""
edges_osr = [
    # OSR_01 Ruined Castle Grounds
    {"from": {"map": "OSR_01", "id": 0}, "to": {"map": "MAC_01",  "id": 2}, "reqs": []}, # Ruined Castle Grounds Exit South -> Plaza District Exit North
    {"from": {"map": "OSR_01", "id": 1}, "to": {"map": "HOS_00",  "id": 0}, "reqs": []}, # Ruined Castle Grounds Exit East -> Shooting Star Path Exit West

    {"from": {"map": "OSR_01", "id": 0}, "to": {"map": "OSR_01",  "id": 1}, "reqs": []}, #? Ruined Castle Grounds Exit South -> Ruined Castle Grounds Exit East
    {"from": {"map": "OSR_01", "id": 1}, "to": {"map": "OSR_01",  "id": 0}, "reqs": []}, #? Ruined Castle Grounds Exit East -> Ruined Castle Grounds Exit South

    {"from": {"map": "OSR_01", "id": 0}, "to": {"map": "OSR_01",  "id": "GiftA"}, "reqs": [["Parakarry"],["Letter13"]]}, #* Ruined Castle Grounds Exit South -> GiftA (Letter14)

    # OSR_02 Hijacked Castle Entrance
    {"from": {"map": "OSR_02", "id": 0}, "to": {"map": "KPA_121", "id": 1}, "reqs": []}, # Hijacked Castle Entrance Door West -> Exit to Peach's Castle Exit East
    {"from": {"map": "OSR_02", "id": 1}, "to": {"map": "KKJ_10",  "id": 0}, "reqs": []}, # Hijacked Castle Entrance Door North -> Entry Hall (1F) Exit South

    {"from": {"map": "OSR_02", "id": 0}, "to": {"map": "OSR_02", "id": 1}, "reqs": []}, #? Hijacked Castle Entrance Door West -> Hijacked Castle Entrance Door North
    {"from": {"map": "OSR_02", "id": 1}, "to": {"map": "OSR_02", "id": 0}, "reqs": []}, #? Hijacked Castle Entrance Door North -> Hijacked Castle Entrance Door West

    {"from": {"map": "OSR_02", "id": 0}, "to": {"map": "OSR_02", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* Hijacked Castle Entrance Door West -> HiddenYBlockA (UltraShroom)
]
