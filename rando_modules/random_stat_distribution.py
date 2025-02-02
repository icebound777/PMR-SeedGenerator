from random import randint

def generate_random_stats(level: int) -> tuple[int,int,int,int]:
    level = min(level, 27) # clamp to max level for sanity
    starting_level = level
    starting_hp = 5
    starting_fp = 5
    starting_bp = 3
    while level > 0:
        level -= 1
        stat = randint(0,2)
        while True:
            # rollover if a stat is already maxed
            if stat == 0:
                if starting_hp >= 50:
                    stat += 1
                else:
                    break
            if stat == 1:
                if starting_fp >= 50:
                    stat += 1
                else:
                    break
            if stat == 2:
                if starting_bp >= 30:
                    stat = 0
                else:
                    break

        # apply stat
        if stat == 0:
            starting_hp += 5
        elif stat == 1:
            starting_fp += 5
        else:
            starting_bp += 3
    return starting_level, starting_hp, starting_fp, starting_bp
