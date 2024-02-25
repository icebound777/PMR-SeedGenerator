"""
This module is used for modifying the puzzles and minigames in various areas of
the game.
"""
import random

from db.puzzle import Puzzle


def get_puzzles_minigames(random_puzzles: bool) -> list:
    """
    Returns a list of randomly rolled data (solutions, initial setups and
    iterations) for puzzles and minigames.
    """
    puzzle_minigame_list = []

    for puzzle in Puzzle.select():
        # Fuzzy Tree Minigame Round 1 hops
        if puzzle.name == "FuzzyTreesRound1":
            num_hops = random.randint(10, 13)
            puzzle_minigame_list.append((puzzle.get_key(), num_hops))

        # Fuzzy Tree Minigame Round 2 hops
        elif puzzle.name == "FuzzyTreesRound2":
            num_hops = random.randint(9, 12)
            puzzle_minigame_list.append((puzzle.get_key(), num_hops))

        # Fuzzy Tree Minigame Round 3 hops
        elif puzzle.name == "FuzzyTreesRound3":
            num_hops = random.randint(8, 11)
            puzzle_minigame_list.append((puzzle.get_key(), num_hops))

        # Super Boots Chest Boo Ring
        elif puzzle.name == "BooRingOBK04":
            num_throws = random.randint(6, 10)
            puzzle_minigame_list.append((puzzle.get_key(), num_throws))

        # Record Boo Ring: Degrees of rotation until item drop
        elif puzzle.name == "BooRingOBK08Degrees":
            degrees = random.randint(180, 540)
            puzzle_minigame_list.append((puzzle.get_key(), degrees))

        # Record Boo Ring: Delay until main Boo stops
        elif puzzle.name == "BooRingOBK08Delay":
            delay = random.randint(360, 380)
            puzzle_minigame_list.append((puzzle.get_key(), delay))

        # Bombette Duplighosts: Actor positions
        elif puzzle.name == "BombetteDuplighosts":
            if not random_puzzles:
                positions_encoded = puzzle.default_value
            else:
                npc_ids = [0, 1, 2, 3, 4]
                random.shuffle(npc_ids)
                positions_encoded = (
                    (npc_ids[0] << 16)
                  + (npc_ids[1] << 12)
                  + (npc_ids[2] << 8)
                  + (npc_ids[3] << 4)
                  + npc_ids[4]
                )
            puzzle_minigame_list.append((puzzle.get_key(), positions_encoded))

        # Albino Dino Statues: Initial positions
        elif puzzle.name == "AlbinoDinoPositions":
            if not random_puzzles:
                positions_encoded = puzzle.default_value
            else:
                positions_encoded = _albino_dino_puzzle()
            puzzle_minigame_list.append((puzzle.get_key(), positions_encoded))

    return puzzle_minigame_list


def _albino_dino_puzzle() -> int:
    max_x_coord = 8
    max_z_coord = 2

    dino_1 = (random.randint(0, max_x_coord), random.randint(0, max_z_coord))

    # make sure the dinos don't share a space
    while True:
        dino_2 = (random.randint(0, max_x_coord), random.randint(0, max_z_coord))
        if dino_2[0] == dino_1[0] and dino_2[1] == dino_1[1]:
            continue
        else:
            break
    while True:
        dino_3 = (random.randint(0, max_x_coord), random.randint(0, max_z_coord))
        if dino_3[0] == dino_1[0] and dino_3[1] == dino_1[1]:
            continue
        elif dino_3[0] == dino_2[0] and dino_3[1] == dino_2[1]:
            continue
        else:
            break

    # Hex-Encoding: 0x00xzxzxz
    return (
        (dino_1[0] << 20)
      + (dino_1[1] << 16)
      + (dino_2[0] << 12)
      + (dino_2[1] << 8)
      + (dino_3[0] << 4)
      + dino_3[1]
    )
