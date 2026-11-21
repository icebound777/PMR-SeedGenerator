"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Blue Station Take Train Jumpless.
"""
edges_omo_add_blue_station_train_jumpless = [
    # Can hit the buttons, reach the conductor, and take the train
    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_03", "id": 0}, "reqs": [["MF_Ch4_CanThrowInTrain"],["ToyTrain"],["Lakilester"]], "pseudoitems": ["RF_CanTakeTrain"]},
]
