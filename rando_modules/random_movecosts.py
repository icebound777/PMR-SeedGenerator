"""
This module is used for modifying BP costs of badges, FP costs of both badge
and partner moves and SP costs for star power moves.
"""
import random

from db.move import Move


value_limits = {
    "BADGE":     {"BP": {"min": 1,"max": 8,}, "FP": {"min": 1,"max": 7,}},
    "PARTNER":   {"FP": {"min": 1,"max": 8,}},
    "STARPOWER": {"FP": {"min": 1,"max": 3,}}
}

def _get_shuffled_costs(movetype, costtype):
    """
    Returns a list of tuples where the first value holds the dbkey for a move
    cost and the second value holds the shuffled cost depending on which
    move type and cost type are given as parameters.
    """
    shuffled_costs = []
    db_keys = []
    db_values = []

    for move in Move \
                .select() \
                .where(Move.move_type == movetype) \
                .where(Move.cost_type == costtype):
        db_keys.append(move.get_key())
        db_values.append(move.cost_value)

    random.shuffle(db_values)

    for db_key, db_value in zip(db_keys, db_values):
        shuffled_costs.append((db_key, db_value))

    return shuffled_costs


def _get_balanced_random_costs(movetype:str, costtype:str) -> list:
    """
    Returns a list of tuples where the first value holds the dbkey for a badge
    BP cost and the second value holds its randomized BP cost.
    """
    random_costs = []

    min_value = value_limits.get(movetype).get(costtype).get("min")
    max_value = value_limits.get(movetype).get(costtype).get("max")

    for move in Move \
                .select() \
                .where(Move.move_type == movetype) \
                .where(Move.cost_type == costtype):
        default_cost = move.cost_value

        # 10% Chance to pick randomly between 1 and 8, else randomly choose
        # from -2 to +2, clamping to 1-8
        if random.randint(1, 10) == 10:
            new_cost = random.randint(min_value, max_value)
        else:
            if movetype == "STARPOWER":
                new_cost = default_cost + random.choice([-1, 0, 1])
            else:   
                new_cost = default_cost + random.choice([-2, -1, 0, 1, 2])

            if new_cost < min_value:
                new_cost = min_value
            if new_cost > max_value:
                new_cost = max_value

        random_costs.append((move.get_key(), new_cost))

    return random_costs


def _get_fully_random_costs(movetype:str, costtype:str) -> list:
    """
    Returns a list of tuples where the first value holds the dbkey for a cost
    and the second value holds its fully randomized cost value.
    """
    fully_random_costs = []

    min_value = value_limits.get(movetype).get(costtype).get("min")
    if (movetype, costtype) == ("BADGE", "BP"):
        # Special case for bp costs: 1-8 simply has too high of a median
        max_value = 6
    else:
        max_value = value_limits.get(movetype).get(costtype).get("max")

    for move in Move \
                .select() \
                .where(Move.move_type == movetype) \
                .where(Move.cost_type == costtype):
        new_cost = random.randint(min_value, max_value)
        fully_random_costs.append((move.get_key(), new_cost))
        print(f"{move.move_name}: {move.cost_value} -> {new_cost}")

    return fully_random_costs


def get_randomized_moves(
    badges_bp_setting:int,
    badges_fp_setting:int,
    partner_fp_setting:int,
    starpower_setting:int
):
    """
    Returns a list of tuples where the first value holds the dbkey for a move
    cost and the second value holds the shuffled FP,BP,SP cost.
    """
    #VANILLA = 0
    BALANCED_RANDOM = 1
    SHUFFLED = 2
    FULLY_RANDOM = 3

    rnd_cost_functions = {
        BALANCED_RANDOM: _get_balanced_random_costs,
        SHUFFLED: _get_shuffled_costs,
        FULLY_RANDOM: _get_fully_random_costs,
    }

    move_costs = []

    if (badges_bp_setting in rnd_cost_functions):
        new_cost = rnd_cost_functions.get(badges_bp_setting)("BADGE", "BP")
        move_costs.extend(new_cost)

    if (badges_fp_setting in rnd_cost_functions):
        new_cost = rnd_cost_functions.get(badges_fp_setting)("BADGE", "FP")
        move_costs.extend(new_cost)

    if (partner_fp_setting in rnd_cost_functions):
        new_cost = rnd_cost_functions.get(partner_fp_setting)("PARTNER", "FP")
        move_costs.extend(new_cost)

    if (starpower_setting in rnd_cost_functions):
        new_cost = rnd_cost_functions.get(starpower_setting)("STARPOWER", "FP")
        move_costs.extend(new_cost)

    return move_costs
