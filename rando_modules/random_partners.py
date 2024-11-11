"""This module handles choosing random partners to start the seed with."""
import random

from metadata.partners_meta import all_partners as all_partners_imp
from models.options.LogicOptionSet import LogicOptionSet

def get_rnd_starting_partners(
    num_rnd_partners_min:int,
    num_rnd_partners_max:int,
    logic_settings:LogicOptionSet
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

    logic_settings.start_with_goombario = False
    logic_settings.start_with_kooper = False
    logic_settings.start_with_bombette = False
    logic_settings.start_with_parakarry = False
    logic_settings.start_with_bow = False
    logic_settings.start_with_watt = False
    logic_settings.start_with_sushie = False
    logic_settings.start_with_lakilester = False

    for partner in starting_partners:
        if partner == "Goombario":
            logic_settings.start_with_goombario = True
        elif partner == "Kooper":
            logic_settings.start_with_kooper = True
        elif partner == "Bombette":
            logic_settings.start_with_bombette = True
        elif partner == "Parakarry":
            logic_settings.start_with_parakarry = True
        elif partner == "Bow":
            logic_settings.start_with_bow = True
        elif partner == "Watt":
            logic_settings.start_with_watt = True
        elif partner == "Sushie":
            logic_settings.start_with_sushie = True
        elif partner == "Lakilester":
            logic_settings.start_with_lakilester = True

    return starting_partners
