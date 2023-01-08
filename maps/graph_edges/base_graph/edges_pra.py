"""This file represents all edges of the world graph that have origin-nodes in the PRA (Crystal Palace) area."""
edges_pra = [
    # PRA_01 Entrance
    {"from": {"map": "PRA_01", "id": 0}, "to": {"map": "SAM_10", "id": 1}, "reqs": []}, # Entrance Exit West -> Shiver Mountain Peaks Exit East
    {"from": {"map": "PRA_01", "id": 1}, "to": {"map": "PRA_02", "id": 0}, "reqs": []}, # Entrance Front Door -> Entry Hall Entrance Door
    {"from": {"map": "PRA_01", "id": 2}, "to": {"map": "PRA_02", "id": 5}, "reqs": []}, # Entrance Front Door (Mirror Side) -> Entry Hall Entrance Door (Mirror Side)
    {"from": {"map": "PRA_01", "id": 3}, "to": {"map": "PRA_15", "id": 0}, "reqs": []}, # Entrance Cave Entrance -> Star Piece Cave Cave Entrance

    {"from": {"map": "PRA_01", "id": 0}, "to": {"map": "PRA_01", "id": 1}, "reqs": []}, #? Entrance Exit West -> Entrance Front Door
    {"from": {"map": "PRA_01", "id": 1}, "to": {"map": "PRA_01", "id": 0}, "reqs": []}, #? Entrance Front Door -> Entrance Exit West
    {"from": {"map": "PRA_01", "id": 2}, "to": {"map": "PRA_01", "id": 3}, "reqs": []}, #? Entrance Front Door (Mirror Side) -> Entrance Cave Entrance
    {"from": {"map": "PRA_01", "id": 3}, "to": {"map": "PRA_01", "id": 2}, "reqs": []}, #? Entrance Cave Entrance -> Entrance Front Door (Mirror Side)

    # PRA_02 Entry Hall
    {"from": {"map": "PRA_02", "id": 0}, "to": {"map": "PRA_01", "id": 1}, "reqs": []}, # Entry Hall Entrance Door -> Entrance Front Door
    {"from": {"map": "PRA_02", "id": 1}, "to": {"map": "PRA_03", "id": 0}, "reqs": []}, # Entry Hall Hallway Door -> Save Room Door West
    {"from": {"map": "PRA_02", "id": 6}, "to": {"map": "PRA_13", "id": 0}, "reqs": [["BlueKey"],["SuperBoots"]]}, # Entry Hall Blue/Red Door -> Blue Mirror Hall 1 Door West
    {"from": {"map": "PRA_02", "id": 2}, "to": {"map": "PRA_16", "id": 0}, "reqs": [["RedKey"]]}, # Entry Hall Blue/Red Door -> Red Mirror Hall Door West
    {"from": {"map": "PRA_02", "id": 7}, "to": {"map": "PRA_13", "id": 3}, "reqs": [["BlueKey"],["SuperBoots"]]}, # Entry Hall Blue/Red Door (Mirror Side) -> Blue Mirror Hall 1 Door West (Mirror Side)
    {"from": {"map": "PRA_02", "id": 3}, "to": {"map": "PRA_16", "id": 3}, "reqs": [["RedKey"]]}, # Entry Hall Blue/Red Door (Mirror Side) -> Red Mirror Hall Door West (Mirror Side)
    {"from": {"map": "PRA_02", "id": 4}, "to": {"map": "PRA_04", "id": 0}, "reqs": []}, # Entry Hall Hallway Door (Mirror Side) -> Reflected Save Room Door West
    {"from": {"map": "PRA_02", "id": 5}, "to": {"map": "PRA_01", "id": 2}, "reqs": []}, # Entry Hall Entrance Door (Mirror Side) -> Entrance Front Door (Mirror Side)

    {"from": {"map": "PRA_02", "id": 0}, "to": {"map": "PRA_02", "id": 1}, "reqs": []}, #? Entry Hall Entrance Door -> Entry Hall Hallway Door
    {"from": {"map": "PRA_02", "id": 1}, "to": {"map": "PRA_02", "id": 0}, "reqs": []}, #? Entry Hall Hallway Door -> Entry Hall Entrance Door
    {"from": {"map": "PRA_02", "id": 0}, "to": {"map": "PRA_02", "id": 2}, "reqs": []}, #? Entry Hall Entrance Door -> Entry Hall Red Door
    {"from": {"map": "PRA_02", "id": 0}, "to": {"map": "PRA_02", "id": 6}, "reqs": []}, #? Entry Hall Entrance Door -> Entry Hall Blue Door
    {"from": {"map": "PRA_02", "id": 2}, "to": {"map": "PRA_02", "id": 0}, "reqs": []}, #? Entry Hall Red Door -> Entry Hall Entrance Door
    {"from": {"map": "PRA_02", "id": 6}, "to": {"map": "PRA_02", "id": 0}, "reqs": []}, #? Entry Hall Blue Door -> Entry Hall Entrance Door
    {"from": {"map": "PRA_02", "id": 5}, "to": {"map": "PRA_02", "id": 4}, "reqs": []}, #? Entry Hall Entrance Door (Mirror Side) -> Entry Hall Hallway Door (Mirror Side)
    {"from": {"map": "PRA_02", "id": 4}, "to": {"map": "PRA_02", "id": 5}, "reqs": []}, #? Entry Hall Hallway Door (Mirror Side) -> Entry Hall Entrance Door (Mirror Side)
    {"from": {"map": "PRA_02", "id": 3}, "to": {"map": "PRA_02", "id": 5}, "reqs": []}, #? Entry Hall Red Door (Mirror Side) -> Entry Hall Entrance Door (Mirror Side)
    {"from": {"map": "PRA_02", "id": 7}, "to": {"map": "PRA_02", "id": 5}, "reqs": []}, #? Entry Hall Blue Door (Mirror Side) -> Entry Hall Entrance Door (Mirror Side)
    {"from": {"map": "PRA_02", "id": 5}, "to": {"map": "PRA_02", "id": 3}, "reqs": []}, #? Entry Hall Entrance Door (Mirror Side) -> Entry Hall Red Door (Mirror Side)
    {"from": {"map": "PRA_02", "id": 5}, "to": {"map": "PRA_02", "id": 7}, "reqs": []}, #? Entry Hall Entrance Door (Mirror Side) -> Entry Hall Blue Door (Mirror Side)

    # PRA_03 Save Room
    {"from": {"map": "PRA_03", "id": 0}, "to": {"map": "PRA_02", "id": 1}, "reqs": []}, # Save Room Door West -> Entry Hall Hallway Door
    {"from": {"map": "PRA_03", "id": 1}, "to": {"map": "PRA_38", "id": 0}, "reqs": []}, # Save Room Door East -> Blue Key Hall Door West
    {"from": {"map": "PRA_03", "id": 2}, "to": {"map": "PRA_09", "id": 0}, "reqs": []}, # Save Room Basement Door -> Red Key Hall Door West

    {"from": {"map": "PRA_03", "id": 0}, "to": {"map": "PRA_03", "id": 1}, "reqs": []}, #? Save Room Door West -> Save Room Door East
    {"from": {"map": "PRA_03", "id": 1}, "to": {"map": "PRA_03", "id": 0}, "reqs": []}, #? Save Room Door East -> Save Room Door West
    {"from": {"map": "PRA_03", "id": 0}, "to": {"map": "PRA_03", "id": 2}, "reqs": [["GF_PRA04_BoardedFloor"]]}, #? Save Room Door West -> Save Room Basement Door
    {"from": {"map": "PRA_03", "id": 2}, "to": {"map": "PRA_03", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Save Room Basement Door -> Save Room Door West

    # PRA_04 Reflected Save Room
    {"from": {"map": "PRA_04", "id": 0}, "to": {"map": "PRA_02", "id": 4}, "reqs": []}, # Reflected Save Room Door West -> Entry Hall Hallway Door (Mirror Side)
    {"from": {"map": "PRA_04", "id": 1}, "to": {"map": "PRA_39", "id": 0}, "reqs": []}, # Reflected Save Room Door East -> Shooting Star Hall Door West
    {"from": {"map": "PRA_04", "id": 2}, "to": {"map": "PRA_10", "id": 0}, "reqs": []}, # Reflected Save Room Basement Door -> P-Down, D-Up Hall Door West

    {"from": {"map": "PRA_04", "id": 0}, "to": {"map": "PRA_04", "id": 1}, "reqs": []}, #? Reflected Save Room Door West -> Reflected Save Room Door East
    {"from": {"map": "PRA_04", "id": 1}, "to": {"map": "PRA_04", "id": 0}, "reqs": []}, #? Reflected Save Room Door East -> Reflected Save Room Door West
    {"from": {"map": "PRA_04", "id": 0}, "to": {"map": "PRA_04", "id": 2}, "reqs": [["SuperBoots"]], "pseudoitems": ["GF_PRA04_BoardedFloor"]}, #? Reflected Save Room Door West -> Reflected Save Room Basement Door
    {"from": {"map": "PRA_04", "id": 2}, "to": {"map": "PRA_04", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Reflected Save Room Basement Door -> Reflected Save Room Door West

    {"from": {"map": "PRA_04", "id": 0}, "to": {"map": "PRA_04", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Reflected Save Room Door West -> YBlockA (SuperShroom)

    # PRA_05 Blue Key Room
    {"from": {"map": "PRA_05", "id": 0}, "to": {"map": "PRA_38", "id": 1}, "reqs": []}, # Blue Key Room Door West -> Blue Key Hall Door East

    {"from": {"map": "PRA_05", "id": 0}, "to": {"map": "PRA_05", "id": "ChestA"}, "reqs": [["can_climb_steps"]]}, #* Blue Key Room Door West -> ChestA (BlueKey)

    # PRA_06 Shooting Star Room
    {"from": {"map": "PRA_06", "id": 0}, "to": {"map": "PRA_39", "id": 1}, "reqs": []}, # Shooting Star Room Door West -> Shooting Star Hall Door East

    {"from": {"map": "PRA_06", "id": 0}, "to": {"map": "PRA_06", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Shooting Star Room Door West -> ItemA (ShootingStar)

    # PRA_09 Red Key Hall
    {"from": {"map": "PRA_09", "id": 0}, "to": {"map": "PRA_03", "id": 2}, "reqs": [["Hammer"]]}, # Red Key Hall Door West -> Save Room Basement Door
    {"from": {"map": "PRA_09", "id": 1}, "to": {"map": "PRA_11", "id": 0}, "reqs": [["Bombette"],["Hammer"]]}, # Red Key Hall Bombable Wall -> Red Key Room Bombable Wall

    {"from": {"map": "PRA_09", "id": 0}, "to": {"map": "PRA_09", "id": 1}, "reqs": []}, #? Red Key Hall Door West -> Red Key Hall Bombable Wall
    {"from": {"map": "PRA_09", "id": 1}, "to": {"map": "PRA_09", "id": 0}, "reqs": []}, #? Red Key Hall Bombable Wall -> Red Key Hall Door West

    # PRA_10 P-Down, D-Up Hall
    {"from": {"map": "PRA_10", "id": 0}, "to": {"map": "PRA_04", "id": 2}, "reqs": []}, # P-Down, D-Up Hall Door West -> Reflected Save Room Basement Door
    {"from": {"map": "PRA_10", "id": 1}, "to": {"map": "PRA_12", "id": 0}, "reqs": []}, # P-Down, D-Up Hall Door East -> P-Down, D-Up Room Door West

    {"from": {"map": "PRA_10", "id": 0}, "to": {"map": "PRA_10", "id": 1}, "reqs": []}, #? P-Down, D-Up Hall Door West -> P-Down, D-Up Hall Door East
    {"from": {"map": "PRA_10", "id": 1}, "to": {"map": "PRA_10", "id": 0}, "reqs": []}, #? P-Down, D-Up Hall Door East -> P-Down, D-Up Hall Door West

    # PRA_11 Red Key Room
    {"from": {"map": "PRA_11", "id": 0}, "to": {"map": "PRA_09", "id": 1}, "reqs": []}, # Red Key Room Bombable Wall -> Red Key Hall Bombable Wall

    {"from": {"map": "PRA_11", "id": 0}, "to": {"map": "PRA_11", "id": "ChestA"}, "reqs": [["can_climb_steps"]]}, #* Red Key Room Bombable Wall -> ChestA (RedKey)

    # PRA_12 P-Down, D-Up Room
    {"from": {"map": "PRA_12", "id": 0}, "to": {"map": "PRA_10", "id": 1}, "reqs": []}, # P-Down, D-Up Room Door West -> P-Down, D-Up Hall Door East

    {"from": {"map": "PRA_12", "id": 0}, "to": {"map": "PRA_12", "id": "ChestA"}, "reqs": [["can_climb_steps"]]}, #* P-Down, D-Up Room Door West -> ChestA (PDownDUp)

    # PRA_13 Blue Mirror Hall 1
    {"from": {"map": "PRA_13", "id": 0}, "to": {"map": "PRA_02", "id": 6}, "reqs": []}, # Blue Mirror Hall 1 Door West -> Entry Hall Blue/Red Door
    {"from": {"map": "PRA_13", "id": 1}, "to": {"map": "PRA_14", "id": 0}, "reqs": [["Bombette"]]}, # Blue Mirror Hall 1 Bombable Wall -> Blue Mirror Hall 2 Bombable Wall
    {"from": {"map": "PRA_13", "id": 2}, "to": {"map": "PRA_14", "id": 1}, "reqs": [["Bombette"]]}, # Blue Mirror Hall 1 Bombable Wall (Mirror Side) -> Blue Mirror Hall 2 Bombable Wall (Mirror Side)
    {"from": {"map": "PRA_13", "id": 3}, "to": {"map": "PRA_02", "id": 7}, "reqs": []}, # Blue Mirror Hall 1 Door West (Mirror Side) -> Entry Hall Blue/Red Door (Mirror Side)

    {"from": {"map": "PRA_13", "id": 0}, "to": {"map": "PRA_13", "id": 1}, "reqs": []}, #? Blue Mirror Hall 1 Door West -> Blue Mirror Hall 1 Bombable Wall
    {"from": {"map": "PRA_13", "id": 1}, "to": {"map": "PRA_13", "id": 0}, "reqs": []}, #? Blue Mirror Hall 1 Bombable Wall -> Blue Mirror Hall 1 Door West
    {"from": {"map": "PRA_13", "id": 2}, "to": {"map": "PRA_13", "id": 3}, "reqs": []}, #? Blue Mirror Hall 1 Bombable Wall (Mirror Side) -> Blue Mirror Hall 1 Door West (Mirror Side)
    {"from": {"map": "PRA_13", "id": 3}, "to": {"map": "PRA_13", "id": 2}, "reqs": []}, #? Blue Mirror Hall 1 Door West (Mirror Side) -> Blue Mirror Hall 1 Bombable Wall (Mirror Side)

    # PRA_14 Blue Mirror Hall 2
    {"from": {"map": "PRA_14", "id": 0}, "to": {"map": "PRA_13", "id": 1}, "reqs": [["Bombette"]]}, # Blue Mirror Hall 2 Bombable Wall -> Blue Mirror Hall 1 Bombable Wall
    {"from": {"map": "PRA_14", "id": 1}, "to": {"map": "PRA_13", "id": 2}, "reqs": [["Bombette"]]}, # Blue Mirror Hall 2 Bombable Wall (Mirror Side) -> Blue Mirror Hall 1 Bombable Wall (Mirror Side)

    {"from": {"map": "PRA_14", "id": 0}, "to": {"map": "PRA_14", "id": 1}, "reqs": []}, #? Blue Mirror Hall 2 Bombable Wall -> Blue Mirror Hall 2 Bombable Wall (Mirror Side)
    {"from": {"map": "PRA_14", "id": 1}, "to": {"map": "PRA_14", "id": 0}, "reqs": []}, #? Blue Mirror Hall 2 Bombable Wall (Mirror Side) -> Blue Mirror Hall 2 Bombable Wall

    # PRA_15 Star Piece Cave
    {"from": {"map": "PRA_15", "id": 0}, "to": {"map": "PRA_01", "id": 3}, "reqs": []}, # Star Piece Cave Cave Entrance -> Entrance Cave Entrance

    {"from": {"map": "PRA_15", "id": 0}, "to": {"map": "PRA_15", "id": "ItemA"}, "reqs": []}, #* Star Piece Cave Cave Entrance -> ItemA (StarPiece)

    # PRA_16 Red Mirror Hall
    {"from": {"map": "PRA_16", "id": 0}, "to": {"map": "PRA_02", "id": 2}, "reqs": []}, # Red Mirror Hall Door West -> Entry Hall Blue/Red Door
    {"from": {"map": "PRA_16", "id": 1}, "to": {"map": "PRA_18", "id": 0}, "reqs": []}, # Red Mirror Hall Door East -> Bridge Mirror Hall Bridge Mirror Hall Door West
    {"from": {"map": "PRA_16", "id": 2}, "to": {"map": "PRA_18", "id": 2}, "reqs": []}, # Red Mirror Hall Door East (Mirror Side) -> Bridge Mirror Hall
    {"from": {"map": "PRA_16", "id": 3}, "to": {"map": "PRA_02", "id": 3}, "reqs": []}, # Red Mirror Hall Door West (Mirror Side) -> Entry Hall Blue/Red Door (Mirror Side)

    {"from": {"map": "PRA_16", "id": 0}, "to": {"map": "PRA_16", "id": 1}, "reqs": []}, #? Red Mirror Hall Door West -> Red Mirror Hall Door East
    {"from": {"map": "PRA_16", "id": 1}, "to": {"map": "PRA_16", "id": 0}, "reqs": []}, #? Red Mirror Hall Door East -> Red Mirror Hall Door West
    {"from": {"map": "PRA_16", "id": 0}, "to": {"map": "PRA_16", "id": 2}, "reqs": []}, #? Red Mirror Hall Door West -> Red Mirror Hall Door East (Mirror Side)
    {"from": {"map": "PRA_16", "id": 2}, "to": {"map": "PRA_16", "id": 0}, "reqs": []}, #? Red Mirror Hall Door East (Mirror Side) -> Red Mirror Hall Door West
    {"from": {"map": "PRA_16", "id": 0}, "to": {"map": "PRA_16", "id": 3}, "reqs": []}, #? Red Mirror Hall Door West -> Red Mirror Hall Door West (Mirror Side)
    {"from": {"map": "PRA_16", "id": 3}, "to": {"map": "PRA_16", "id": 0}, "reqs": []}, #? Red Mirror Hall Door West (Mirror Side) -> Red Mirror Hall Door West

    # PRA_18 Bridge Mirror Hall
    {"from": {"map": "PRA_18", "id": 0}, "to": {"map": "PRA_16", "id": 1}, "reqs": []}, # Bridge Mirror Hall Door West -> Red Mirror Hall Door East
    {"from": {"map": "PRA_18", "id": 1}, "to": {"map": "PRA_33", "id": 1}, "reqs": [["MF_PRA_18_DefeatedClubbas"]]}, # Bridge Mirror Hall Door East (Mirror Side) -> Turnstyle Room Door West
    {"from": {"map": "PRA_18", "id": 2}, "to": {"map": "PRA_16", "id": 2}, "reqs": []}, # Bridge Mirror Hall Door West (Mirror Side) -> Red Mirror Hall Door East (Mirror Side)

    {"from": {"map": "PRA_18", "id": 1}, "to": {"map": "PRA_18", "id": 2}, "reqs": [["MF_PRA_18_DefeatedClubbas"]]}, #? Bridge Mirror Hall Door East (Mirror Side) -> Bridge Mirror Hall Door West (Mirror Side)
    {"from": {"map": "PRA_18", "id": 2}, "to": {"map": "PRA_18", "id": 1}, "reqs": []}, #? Bridge Mirror Hall Door West (Mirror Side) -> Bridge Mirror Hall Door East (Mirror Side)

    {"from": {"map": "PRA_18", "id": 0}, "to": {"map": "PRA_18", "id": 0}, "reqs": [], "pseudoitems": ["MF_PRA_18_DefeatedClubbas"]}, #+ Bridge Mirror Hall Door West

    # PRA_19 Reflection Mimic Room
    {"from": {"map": "PRA_19", "id": 0}, "to": {"map": "PRA_35", "id": 1}, "reqs": [["Hammer"]]}, # Reflection Mimic Room Door West -> Triple Dip Room Door East
    {"from": {"map": "PRA_19", "id": 1}, "to": {"map": "PRA_20", "id": 0}, "reqs": [["Kooper"],["Hammer"]]}, # Reflection Mimic Room Bombable Wall -> Mirrored Door Room Bombable Wall

    {"from": {"map": "PRA_19", "id": 0}, "to": {"map": "PRA_19", "id": 1}, "reqs": []}, #? Reflection Mimic Room Door West -> Reflection Mimic Room Bombable Wall
    {"from": {"map": "PRA_19", "id": 1}, "to": {"map": "PRA_19", "id": 0}, "reqs": []}, #? Reflection Mimic Room Bombable Wall -> Reflection Mimic Room Door West

    # PRA_20 Mirrored Door Room
    {"from": {"map": "PRA_20", "id": 0}, "to": {"map": "PRA_19", "id": 1}, "reqs": []}, # Mirrored Door Room Bombable Wall -> Reflection Mimic Room Bombable Wall
    {"from": {"map": "PRA_20", "id": 1}, "to": {"map": "PRA_21", "id": 0}, "reqs": []}, # Mirrored Door Room Hallway Door -> Huge Statue Room Door West
    {"from": {"map": "PRA_20", "id": 2}, "to": {"map": "PRA_29", "id": 0}, "reqs": []}, # Mirrored Door Room Door East -> Hidden Bridge Room Door West
    {"from": {"map": "PRA_20", "id": 3}, "to": {"map": "PRA_29", "id": 3}, "reqs": []}, # Mirrored Door Room Door East (Mirror Side) -> Hidden Bridge Room Door West (Mirror Side)
    {"from": {"map": "PRA_20", "id": 4}, "to": {"map": "PRA_22", "id": 0}, "reqs": []}, # Mirrored Door Room Hallway Door (Mirror Side) -> Small Statue Room Door West

    {"from": {"map": "PRA_20", "id": 0}, "to": {"map": "PRA_20", "id": 1}, "reqs": []}, #? Mirrored Door Room Bombable Wall -> Mirrored Door Room Hallway Door
    {"from": {"map": "PRA_20", "id": 1}, "to": {"map": "PRA_20", "id": 0}, "reqs": []}, #? Mirrored Door Room Hallway Door -> Mirrored Door Room Bombable Wall
    {"from": {"map": "PRA_20", "id": 0}, "to": {"map": "PRA_20", "id": 2}, "reqs": []}, #? Mirrored Door Room Bombable Wall -> Mirrored Door Room Door East
    {"from": {"map": "PRA_20", "id": 2}, "to": {"map": "PRA_20", "id": 0}, "reqs": []}, #? Mirrored Door Room Door East -> Mirrored Door Room Bombable Wall
    {"from": {"map": "PRA_20", "id": 3}, "to": {"map": "PRA_20", "id": 4}, "reqs": []}, #? Mirrored Door Room Door East (Mirror Side) -> Mirrored Door Room Hallway Door (Mirror Side)
    {"from": {"map": "PRA_20", "id": 4}, "to": {"map": "PRA_20", "id": 3}, "reqs": []}, #? Mirrored Door Room Hallway Door (Mirror Side) -> Mirrored Door Room Door East (Mirror Side)

    # PRA_21 Huge Statue Room
    {"from": {"map": "PRA_21", "id": 0}, "to": {"map": "PRA_20", "id": 1}, "reqs": []}, # Huge Statue Room Door West -> Mirrored Door Room Hallway Door
    {"from": {"map": "PRA_21", "id": 1}, "to": {"map": "PRA_36", "id": 0}, "reqs": []}, # Huge Statue Room Basement Door -> Palace Key Hall Door West

    {"from": {"map": "PRA_21", "id": 0}, "to": {"map": "PRA_21", "id": 1}, "reqs": [["MF_PRA_22_FoundHiddenRoomUnderStatue"]]}, #? Huge Statue Room Door West -> Huge Statue Room Basement Door
    {"from": {"map": "PRA_21", "id": 1}, "to": {"map": "PRA_21", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Huge Statue Room Basement Door -> Huge Statue Room Door West

    {"from": {"map": "PRA_21", "id": 0}, "to": {"map": "PRA_21", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Huge Statue Room Door West -> HiddenPanel (StarPiece)
    {"from": {"map": "PRA_21", "id": 0}, "to": {"map": "PRA_21", "id": "YBlockA"},     "reqs": [["UltraBoots"]]}, #* Huge Statue Room Door West -> YBlockA (MapleSyrup)

    # PRA_22 Small Statue Room
    {"from": {"map": "PRA_22", "id": 0}, "to": {"map": "PRA_20", "id": 4}, "reqs": []}, # Small Statue Room Door West -> Mirrored Door Room Hallway Door (Mirror Side)
    {"from": {"map": "PRA_22", "id": 1}, "to": {"map": "PRA_37", "id": 0}, "reqs": []}, # Small Statue Room Basement Door -> P-Up, D-Down Hall Door West

    {"from": {"map": "PRA_22", "id": 0}, "to": {"map": "PRA_22", "id": 1}, "reqs": []}, #? Small Statue Room Door West -> Small Statue Room Basement Door
    {"from": {"map": "PRA_22", "id": 1}, "to": {"map": "PRA_22", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Small Statue Room Basement Door -> Small Statue Room Door West

    {"from": {"map": "PRA_22", "id": 0}, "to": {"map": "PRA_22", "id": 1}, "reqs": [], "pseudoitems": ["MF_PRA_22_FoundHiddenRoomUnderStatue"]}, #+ Small Statue Room Door West

    {"from": {"map": "PRA_22", "id": 0}, "to": {"map": "PRA_22", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* Small Statue Room Door West -> HiddenPanel (StarPiece)
    {"from": {"map": "PRA_22", "id": 0}, "to": {"map": "PRA_22", "id": "HiddenYBlockA"}, "reqs": [["UltraBoots"],["can_see_hidden_blocks"]]}, #* Small Statue Room Door West -> HiddenYBlockA (JamminJelly)

    # PRA_27 Palace Key Room
    {"from": {"map": "PRA_27", "id": 0}, "to": {"map": "PRA_36", "id": 1}, "reqs": []}, # Palace Key Room Door West -> Palace Key Hall Door East

    {"from": {"map": "PRA_27", "id": 0}, "to": {"map": "PRA_27", "id": "ChestA"}, "reqs": [["can_climb_steps"]]}, #* Palace Key Room Door West -> ChestA (CrystalPalaceKey)

    # PRA_28 P-Up, D-Down Room
    {"from": {"map": "PRA_28", "id": 0}, "to": {"map": "PRA_37", "id": 1}, "reqs": []}, # P-Up, D-Down Room Door West -> P-Up, D-Down Hall Door East

    {"from": {"map": "PRA_28", "id": 0}, "to": {"map": "PRA_28", "id": "ChestA"}, "reqs": [["can_climb_steps"]]}, #* P-Up, D-Down Room Door West -> ChestA (PUpDDown)

    # PRA_29 Hidden Bridge Room
    {"from": {"map": "PRA_29", "id": 0}, "to": {"map": "PRA_20", "id": 2}, "reqs": []}, # Hidden Bridge Room Door West -> Mirrored Door Room Door East
    {"from": {"map": "PRA_29", "id": 1}, "to": {"map": "PRA_34", "id": 0}, "reqs": []}, # Hidden Bridge Room Door East -> Mirror Hole Room Door West
    {"from": {"map": "PRA_29", "id": 2}, "to": {"map": "PRA_34", "id": 3}, "reqs": []}, # Hidden Bridge Room Door East (Mirror Side) -> Mirror Hole Room Door West (Mirror Side)
    {"from": {"map": "PRA_29", "id": 3}, "to": {"map": "PRA_20", "id": 3}, "reqs": []}, # Hidden Bridge Room Door West (Mirror Side) -> Mirrored Door Room Door East (Mirror Side)

    {"from": {"map": "PRA_29", "id": 0}, "to": {"map": "PRA_29", "id": 1}, "reqs": [["RF_PRA_29_ExtendedBridge","Kooper"]], "pseudoitems": ["RF_PRA_29_ExtendedBridge"]}, #? Hidden Bridge Room Door West -> Hidden Bridge Room Door East
    {"from": {"map": "PRA_29", "id": 1}, "to": {"map": "PRA_29", "id": 0}, "reqs": [["RF_PRA_29_ExtendedBridge","can_climb_steps","Hammer","Kooper","Bombette"]], "pseudoitems": ["RF_PRA_29_ExtendedBridge"]}, #? Hidden Bridge Room Door East -> Hidden Bridge Room Door West
    {"from": {"map": "PRA_29", "id": 2}, "to": {"map": "PRA_29", "id": 3}, "reqs": [["RF_PRA_29_ExtendedBridge","can_climb_steps","Hammer","Kooper","Bombette"]], "pseudoitems": ["RF_PRA_29_ExtendedBridge"]}, #? Hidden Bridge Room Door East (Mirror Side) -> Hidden Bridge Room Door West (Mirror Side)
    {"from": {"map": "PRA_29", "id": 3}, "to": {"map": "PRA_29", "id": 2}, "reqs": [["RF_PRA_29_ExtendedBridge","Kooper"]], "pseudoitems": ["RF_PRA_29_ExtendedBridge"]}, #? Hidden Bridge Room Door West (Mirror Side) -> Hidden Bridge Room Door East (Mirror Side)

    # PRA_31 Dino Puzzle Room
    {"from": {"map": "PRA_31", "id": 0}, "to": {"map": "PRA_34", "id": 1}, "reqs": []}, # Dino Puzzle Room Door West -> Mirror Hole Room Door East
    {"from": {"map": "PRA_31", "id": 1}, "to": {"map": "PRA_40", "id": 0}, "reqs": []}, # Dino Puzzle Room Door East -> Boss Antechamber Door West
    {"from": {"map": "PRA_31", "id": 2}, "to": {"map": "PRA_34", "id": 2}, "reqs": []}, # Dino Puzzle Room Door West (Mirror Side) -> Mirror Hole Room Door East (Mirror Side)

    {"from": {"map": "PRA_31", "id": 1}, "to": {"map": "PRA_31", "id": 2}, "reqs": []}, #? Dino Puzzle Room Door East -> Dino Puzzle Room Door West (Mirror Side)
    {"from": {"map": "PRA_31", "id": 2}, "to": {"map": "PRA_31", "id": 1}, "reqs": []}, #? Dino Puzzle Room Door West (Mirror Side) -> Dino Puzzle Room Door East

    # PRA_32 Crystal Summit
    {"from": {"map": "PRA_32", "id": 0}, "to": {"map": "PRA_40", "id": 1}, "reqs": []}, # Crystal Summit Door West -> Boss Antechamber Door East

    {"from": {"map": "PRA_32", "id": 0}, "to": {"map": "PRA_32", "id": 0}, "reqs": [], "pseudoitems": ["STARSPIRIT_7"]}, #+ Crystal Summit Door West

    # PRA_33 Turnstyle Room
    {"from": {"map": "PRA_33", "id": 0}, "to": {"map": "PRA_35", "id": 0}, "reqs": []}, # Turnstyle Room Door East -> Triple Dip Room Door West
    {"from": {"map": "PRA_33", "id": 1}, "to": {"map": "PRA_18", "id": 1}, "reqs": []}, # Turnstyle Room Door West -> Bridge Mirror Hall Door East (Mirror Side)
    {"from": {"map": "PRA_33", "id": 2}, "to": {"map": "PRA_35", "id": 2}, "reqs": [["Bombette"]]}, # Turnstyle Room Bombable Wall (Mirror Side) -> Triple Dip Room Bombable Wall (Mirror Side)

    {"from": {"map": "PRA_33", "id": 0}, "to": {"map": "PRA_33", "id": 1}, "reqs": [["Bombette"]]}, #? Turnstyle Room Door East -> Turnstyle Room Door West
    {"from": {"map": "PRA_33", "id": 1}, "to": {"map": "PRA_33", "id": 0}, "reqs": [["Bombette"]]}, #? Turnstyle Room Door West -> Turnstyle Room Door East
    {"from": {"map": "PRA_33", "id": 1}, "to": {"map": "PRA_33", "id": 2}, "reqs": []}, #? Turnstyle Room Door West -> Turnstyle Room Bombable Wall (Mirror Side)
    {"from": {"map": "PRA_33", "id": 2}, "to": {"map": "PRA_33", "id": 1}, "reqs": []}, #? Turnstyle Room Bombable Wall (Mirror Side) -> Turnstyle Room Door West

    # PRA_34 Mirror Hole Room
    {"from": {"map": "PRA_34", "id": 0}, "to": {"map": "PRA_29", "id": 1}, "reqs": []}, # Mirror Hole Room Door West -> Hidden Bridge Room Door East
    {"from": {"map": "PRA_34", "id": 1}, "to": {"map": "PRA_31", "id": 0}, "reqs": [["CrystalPalaceKey"]]}, # Mirror Hole Room Door East -> Dino Puzzle Room Door West
    {"from": {"map": "PRA_34", "id": 2}, "to": {"map": "PRA_31", "id": 2}, "reqs": [["CrystalPalaceKey"]]}, # Mirror Hole Room Door East (Mirror Side) -> Dino Puzzle Room Door West (Mirror Side)
    {"from": {"map": "PRA_34", "id": 3}, "to": {"map": "PRA_29", "id": 2}, "reqs": []}, # Mirror Hole Room Door West (Mirror Side) -> Hidden Bridge Room Door East (Mirror Side)

    {"from": {"map": "PRA_34", "id": 0}, "to": {"map": "PRA_34", "id": 1}, "reqs": []}, #? Mirror Hole Room Door West -> Mirror Hole Room Door East
    {"from": {"map": "PRA_34", "id": 1}, "to": {"map": "PRA_34", "id": 0}, "reqs": []}, #? Mirror Hole Room Door East -> Mirror Hole Room Door West
    {"from": {"map": "PRA_34", "id": 0}, "to": {"map": "PRA_34", "id": 2}, "reqs": []}, #? Mirror Hole Room Door West -> Mirror Hole Room Door East (Mirror Side)
    {"from": {"map": "PRA_34", "id": 2}, "to": {"map": "PRA_34", "id": 0}, "reqs": []}, #? Mirror Hole Room Door East (Mirror Side) -> Mirror Hole Room Door West
    {"from": {"map": "PRA_34", "id": 0}, "to": {"map": "PRA_34", "id": 3}, "reqs": []}, #? Mirror Hole Room Door West -> Mirror Hole Room Door West (Mirror Side)
    {"from": {"map": "PRA_34", "id": 3}, "to": {"map": "PRA_34", "id": 0}, "reqs": []}, #? Mirror Hole Room Door West (Mirror Side) -> Mirror Hole Room Door West

    # PRA_35 Triple Dip Room
    {"from": {"map": "PRA_35", "id": 0}, "to": {"map": "PRA_33", "id": 0}, "reqs": []}, # Triple Dip Room Door West -> Turnstyle Room Door East
    {"from": {"map": "PRA_35", "id": 1}, "to": {"map": "PRA_19", "id": 0}, "reqs": []}, # Triple Dip Room Door East -> Reflection Mimic Room Door West
    {"from": {"map": "PRA_35", "id": 2}, "to": {"map": "PRA_33", "id": 2}, "reqs": [["Bombette"]]}, # Triple Dip Room Bombable Wall (Mirror Side) -> Turnstyle Room Bombable Wall (Mirror Side)

    {"from": {"map": "PRA_35", "id": 0}, "to": {"map": "PRA_35", "id": 1}, "reqs": []}, #? Triple Dip Room Door West -> Triple Dip Room Door East
    {"from": {"map": "PRA_35", "id": 1}, "to": {"map": "PRA_35", "id": 0}, "reqs": []}, #? Triple Dip Room Door East -> Triple Dip Room Door West

    {"from": {"map": "PRA_35", "id": 2}, "to": {"map": "PRA_35", "id": "ChestA"}, "reqs": []}, #* Triple Dip Room Bombable Wall (Mirror Side) -> ChestA (TripleDip)

    # PRA_36 Palace Key Hall
    {"from": {"map": "PRA_36", "id": 0}, "to": {"map": "PRA_21", "id": 1}, "reqs": []}, # Palace Key Hall Door West -> Huge Statue Room Basement Door
    {"from": {"map": "PRA_36", "id": 1}, "to": {"map": "PRA_27", "id": 0}, "reqs": []}, # Palace Key Hall Door East -> Palace Key Room Door West

    {"from": {"map": "PRA_36", "id": 0}, "to": {"map": "PRA_36", "id": 1}, "reqs": []}, #? Palace Key Hall Door West -> Palace Key Hall Door East
    {"from": {"map": "PRA_36", "id": 1}, "to": {"map": "PRA_36", "id": 0}, "reqs": []}, #? Palace Key Hall Door East -> Palace Key Hall Door West

    # PRA_37 P-Up, D-Down Hall
    {"from": {"map": "PRA_37", "id": 0}, "to": {"map": "PRA_22", "id": 1}, "reqs": []}, # P-Up, D-Down Hall Door West -> Small Statue Room Basement Door
    {"from": {"map": "PRA_37", "id": 1}, "to": {"map": "PRA_28", "id": 0}, "reqs": []}, # P-Up, D-Down Hall Door East -> P-Up, D-Down Room Door West

    {"from": {"map": "PRA_37", "id": 0}, "to": {"map": "PRA_37", "id": 1}, "reqs": []}, #? P-Up, D-Down Hall Door West -> P-Up, D-Down Hall Door East
    {"from": {"map": "PRA_37", "id": 1}, "to": {"map": "PRA_37", "id": 0}, "reqs": []}, #? P-Up, D-Down Hall Door East -> P-Up, D-Down Hall Door West

    # PRA_38 Blue Key Hall
    {"from": {"map": "PRA_38", "id": 0}, "to": {"map": "PRA_03", "id": 1}, "reqs": []}, # Blue Key Hall Door West -> Save Room Door East
    {"from": {"map": "PRA_38", "id": 1}, "to": {"map": "PRA_05", "id": 0}, "reqs": []}, # Blue Key Hall Door East -> Blue Key Room Door West

    {"from": {"map": "PRA_38", "id": 0}, "to": {"map": "PRA_38", "id": 1}, "reqs": []}, #? Blue Key Hall Door West -> Blue Key Hall Door East
    {"from": {"map": "PRA_38", "id": 1}, "to": {"map": "PRA_38", "id": 0}, "reqs": []}, #? Blue Key Hall Door East -> Blue Key Hall Door West

    # PRA_39 Shooting Star Hall
    {"from": {"map": "PRA_39", "id": 0}, "to": {"map": "PRA_04", "id": 1}, "reqs": []}, # Shooting Star Hall Door West -> Reflected Save Room Door East
    {"from": {"map": "PRA_39", "id": 1}, "to": {"map": "PRA_06", "id": 0}, "reqs": []}, # Shooting Star Hall Door East -> Shooting Star Room Door West

    {"from": {"map": "PRA_39", "id": 0}, "to": {"map": "PRA_39", "id": 1}, "reqs": []}, #? Shooting Star Hall Door West -> Shooting Star Hall Door East
    {"from": {"map": "PRA_39", "id": 1}, "to": {"map": "PRA_39", "id": 0}, "reqs": []}, #? Shooting Star Hall Door East -> Shooting Star Hall Door West

    # PRA_40 Boss Antechamber
    {"from": {"map": "PRA_40", "id": 0}, "to": {"map": "PRA_31", "id": 1}, "reqs": []}, # Boss Antechamber Door West -> Dino Puzzle Room Door East
    {"from": {"map": "PRA_40", "id": 1}, "to": {"map": "PRA_32", "id": 0}, "reqs": []}, # Boss Antechamber Door East -> Crystal Summit Door West

    {"from": {"map": "PRA_40", "id": 0}, "to": {"map": "PRA_40", "id": 1}, "reqs": []}, #? Boss Antechamber Door West -> Boss Antechamber Door East
    {"from": {"map": "PRA_40", "id": 1}, "to": {"map": "PRA_40", "id": 0}, "reqs": []}, #? Boss Antechamber Door East -> Boss Antechamber Door West
]
