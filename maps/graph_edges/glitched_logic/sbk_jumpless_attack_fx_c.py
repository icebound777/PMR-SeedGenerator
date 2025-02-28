"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Jumpless Attack FX C
Mario can just walk on the rock from a corner: https://youtu.be/OdVf73KLaZE
"""
edges_sbk_add_jumpless_attack_fx_c = [
    #* S3W2 Hidden AttackFX Exit West -> HiddenRBlockA (AttackFXC)]
    {"from": {"map": "SBK_61", "id": 0}, "to": {"map": "SBK_61", "id": "HiddenRBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, 
]
