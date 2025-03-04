"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Laki-less Elevator Room.
Video by JCog: https://www.youtube.com/watch?v=iZEBSnYfABg
"""
edges_flo_add_lakiless_elevator_room = [
    #? (NE) Elevators Exit Left -> (NE) Elevators Exit Right
    {"from": {"map": "FLO_16", "id": 0}, "to": {"map": "FLO_16", "id": 1}, "reqs": [["SuperBoots"]], "mapchange": False},
    #? (NE) Elevators Exit Right -> (NE) Elevators Exit Left
    # Note: this should probably be a separate trick for entrance rando or something
    {"from": {"map": "FLO_16", "id": 1}, "to": {"map": "FLO_16", "id": 0}, "reqs": [["Parakarry"]], "mapchange": False},
]
