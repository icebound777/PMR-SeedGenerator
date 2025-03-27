"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Pleasant Path Clippy Traversal
Pleasant Path ledges can be clipped around without the need for climbing the steps.
Video by mrzebra: https://youtu.be/gXbGPqkf4Lg
"""
edges_nok_add_pleasant_path_clippy_traversal = [
    #? Pleasant Path Bridge Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": [["MF_NOK12_BuiltBridge"], ["Lakilester"]], "mapchange": False},
]
