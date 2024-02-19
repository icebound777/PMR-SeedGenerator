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

    return puzzle_minigame_list
