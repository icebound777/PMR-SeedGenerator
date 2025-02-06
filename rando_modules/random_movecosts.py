"""
This module is used for modifying BP costs of badges, FP costs of both badge
and partner moves and SP costs for star power moves.
"""
import random

from db.move import Move

from rando_enums.enum_options import RandomMoveCosts


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
                # Flower Fanatic is the only badge allowed to scale to 9
                # since it's the only badge with that high of a basic cost
                if move.move_name == "FlowerFanatic":
                    new_cost = 9
                else:
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
        #print(f"{move.move_name}: {move.cost_value} -> {new_cost}")

    return fully_random_costs


def _overwrite_with_plando(
    move_costs: list[int, int],
    plando_move_costs: dict[str, dict[str, dict[str, int]]],
) -> None:
    """
    Overwrites the costs for moves with values set using the plandomizer.
    """
    # plando_move_costs:
    # dict[move_type, dict[move_name, dict[move_cost_type, move_cost]]]
    # to mimic the layout within the sqlite db's 'move' table.
    # also starpower cost are 'FP', for reasons
    move_cost_changes: list[tuple[int, int, int]] = list()

    for move in Move.select():
        lower_move_type = (move.move_type).lower()
        if (    lower_move_type in plando_move_costs
            and move.move_name in plando_move_costs[lower_move_type]
            and move.cost_type in plando_move_costs[lower_move_type][move.move_name]
        ):
            new_move_cost = plando_move_costs[lower_move_type][move.move_name][move.cost_type]
            for i, move_tuple in enumerate(move_costs):
                if move_tuple[0] == move.get_key():
                    move_cost_changes.append((
                        i,
                        move_tuple[0],
                        new_move_cost
                    ))
                    break
            else:
                # the move cost isn't randomized in the first place, so just
                # append it
                move_costs.append((move.get_key(), new_move_cost))

    for index, move_dbkey, new_move_cost in move_cost_changes:
        move_costs[index] = (move_dbkey, new_move_cost)


def get_randomized_moves(
    badges_bp_setting:int,
    badges_fp_setting:int,
    partner_fp_setting:int,
    starpower_setting:int,
    plando_move_costs: dict[str, dict[str, dict[str, int]]] | None
) -> list[tuple[int, int]]:
    """
    Returns a list of tuples where the first value holds the dbkey for a move
    cost and the second value holds the shuffled FP,BP,SP cost.
    """
    rnd_cost_functions = {
        RandomMoveCosts.BALANCED_RANDOM: _get_balanced_random_costs,
        RandomMoveCosts.SHUFFLED: _get_shuffled_costs,
        RandomMoveCosts.FULLY_RANDOM: _get_fully_random_costs,
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

    if plando_move_costs:
        _overwrite_with_plando(move_costs, plando_move_costs)

    return move_costs
