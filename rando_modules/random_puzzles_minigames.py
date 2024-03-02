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

        # Koopa Village Push Block: Initial position
        elif puzzle.name == "KoopaVillagePushBlocks":
            if not random_puzzles:
                positions_encoded = puzzle.default_value
            else:
                positions_encoded = _random_pushblock_positions(
                    num_blocks = 1,
                    min_x = 0,
                    max_x = 4,
                    min_z = 0,
                    max_z = 4,
                    disallowed_positions = []
                )
            puzzle_minigame_list.append((puzzle.get_key(), positions_encoded))

        # Dry Dry Ruins: Ruins stones positions
        elif puzzle.name == "RuinsStones":
            if not random_puzzles:
                slot_order = puzzle.default_value
            else:
                slots = [0,0,1,2,3]
                random.shuffle(slots)
                slot_order = (
                    (slots[0] << 16)
                  + (slots[1] << 12)
                  + (slots[2] << 8)
                  + (slots[3] << 4)
                  + slots[4]
                )
            puzzle_minigame_list.append((
                puzzle.get_key(),
                slot_order
            ))

        # Shy Guy's Toybox: Green Station boxes order
        elif puzzle.name == "GreenStationBoxes":
            if not random_puzzles:
                boxes_order = puzzle.default_value
            else:
                # if puzzles random: mod breaks if not exactly 6 values
                boxes_order = (
                    (random.randint(1, 4) << 20)
                  + (random.randint(1, 4) << 16)
                  + (random.randint(1, 4) << 12)
                  + (random.randint(1, 4) << 8)
                  + (random.randint(1, 4) << 4)
                  + random.randint(1, 4)
                )
            puzzle_minigame_list.append((puzzle.get_key(), boxes_order))

        # Ultra Hammer room Push Blocks: Initial positions
        elif puzzle.name == "UltraHammerPushBlocks":
            if not random_puzzles:
                positions_encoded = puzzle.default_value
            else:
                positions_encoded = _random_pushblock_positions(
                    num_blocks = 2,
                    min_x = 5,
                    max_x = 14,
                    min_z = 0,
                    max_z = 4,
                    disallowed_positions = [(14, 1)]
                )
            puzzle_minigame_list.append((puzzle.get_key(), positions_encoded))

        # Lava Dam Push Blocks: Initial positions
        elif puzzle.name == "LavaDamPushBlocks":
            if not random_puzzles:
                positions_encoded = puzzle.default_value
            else:
                positions_encoded = _lavadam_pushblock_positions()
            puzzle_minigame_list.append((puzzle.get_key(), positions_encoded))

        # Kooper Duplighosts (Crystal Palace): Actor positions
        elif puzzle.name == "PRAKooperDuplighosts":
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


def _random_pushblock_positions(
    num_blocks: int,
    min_x: int,
    max_x: int,
    min_z: int,
    max_z: int,
    disallowed_positions: list
) -> int:
    if (
        not 1 <= num_blocks <= 4
     or min_x >= max_x
     or min_z >= max_z
     or min_x < 0
     or max_x > 15
     or min_z < 0
     or max_z > 15
    ):
        raise ValueError

    block_positions = []

    while len(block_positions) < num_blocks:
        new_block_pos = (random.randint(min_x, max_x), random.randint(min_z, max_z))

        if new_block_pos in disallowed_positions:
            continue
        if new_block_pos in block_positions:
            # don't place two at the same coordinates
            continue

        block_positions.append(new_block_pos)

    positions_encoded = 0

    for block in block_positions:
        positions_encoded = positions_encoded << 4
        positions_encoded += block[0]
        positions_encoded = positions_encoded << 4
        positions_encoded += block[1]

    return positions_encoded


def _lavadam_pushblock_positions() -> int:
    block_positions = []
    disallowed_positions = [(9, 0), (10, 0), (11, 0)]

    while len(block_positions) < 3:
        new_block_pos = (random.randint(0, 12), 0)

        if new_block_pos in disallowed_positions:
            continue
        if new_block_pos in block_positions:
            # don't place two at the same coordinates
            continue
        if (
            new_block_pos[0] + 1 in [x for (x, _) in block_positions]
         or new_block_pos[0] - 1 in [x for (x, _) in block_positions]
        ):
            # don't allow two blocks right next to each other, otherwise they
            # cannot be pushed
            continue

        block_positions.append(new_block_pos)

    positions_encoded = 0

    for block in block_positions:
        positions_encoded = positions_encoded << 4
        positions_encoded += block[0]
        positions_encoded = positions_encoded << 4
        positions_encoded += block[1]

    return positions_encoded
