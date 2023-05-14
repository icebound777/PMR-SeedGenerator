"""This module handles choosing random partners to start the seed with."""
import random

from metadata.partners_meta import all_partners as all_partners_imp
from models.options.OptionSet import OptionSet

def get_rnd_starting_partners(
    num_rnd_partners_min:int,
    num_rnd_partners_max:int,
    rando_settings:OptionSet
) -> list:
    """
    Returns a list of randomly chosen partners according to the parameters.
    """
    starting_partners = []
    all_partners = all_partners_imp.copy()

    non_guaranteed_partners = num_rnd_partners_max - num_rnd_partners_min
    randomly_added_partners = random.randint(0, non_guaranteed_partners)

    while len(starting_partners) < (num_rnd_partners_min + randomly_added_partners):
        new_partner = random.choice(all_partners)
        all_partners.remove(new_partner)
        starting_partners.append(new_partner)

    rando_settings.start_with_goombario = False
    rando_settings.start_with_kooper = False
    rando_settings.start_with_bombette = False
    rando_settings.start_with_parakarry = False
    rando_settings.start_with_bow = False
    rando_settings.start_with_watt = False
    rando_settings.start_with_sushie = False
    rando_settings.start_with_lakilester = False

    for partner in starting_partners:
        if partner == "Goombario":
            rando_settings.start_with_goombario = True
        elif partner == "Kooper":
            rando_settings.start_with_kooper = True
        elif partner == "Bombette":
            rando_settings.start_with_bombette = True
        elif partner == "Parakarry":
            rando_settings.start_with_parakarry = True
        elif partner == "Bow":
            rando_settings.start_with_bow = True
        elif partner == "Watt":
            rando_settings.start_with_watt = True
        elif partner == "Sushie":
            rando_settings.start_with_sushie = True
        elif partner == "Lakilester":
            rando_settings.start_with_lakilester = True

    return starting_partners
