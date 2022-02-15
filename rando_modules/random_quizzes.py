"""
This module is used for modifying the questions asked by Chuck Quizmo in
various areas of the game.
"""
import random

from db.quiz import Quiz


def get_randomized_quizzes() -> list:
    """
    Returns a list of tuples where the first value holds the dbkey for a quiz
    question and the second value holds the shuffled quiz question index. Also
    includes key/value pairs for the number of questions per area.
    """
    quiz_list = []
    db_keys = []
    db_values = []

    for quiz in Quiz.select():
        if quiz.name.endswith("Num"):
            # Do not mess with quiz numbers per area
            quiz_list.append((quiz.get_key(), quiz.value))
        else:
            db_keys.append(quiz.get_key())
            db_values.append(quiz.value)

    random.shuffle(db_values)

    for db_key, db_value in zip(db_keys, db_values):
        quiz_list.append((db_key, db_value))

    return quiz_list
