"""
This module is used for modifying the puzzles and minigames in various areas of
the game.
"""
import random

from db.puzzle import Puzzle


def get_puzzles_minigames() -> list:
    """
    Returns a list of randomly rolled data (solutions, initial setups and
    iterations) for puzzles and minigames.
    """
    puzzle_minigame_list = []

    for puzzle in Puzzle.select():
        # Super Boots Chest Boo Ring
        if puzzle.name == "BooRingOBK04":
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

    return puzzle_minigame_list
