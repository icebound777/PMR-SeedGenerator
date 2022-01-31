"""This module handles choosing random partners to start the seed with."""
import random

from metadata.partners_meta import all_partners as all_partners_imp
from optionset import OptionSet

def get_rnd_starting_partners(
    num_rnd_partners_min:int,
    num_rnd_partners_max:int,
    rando_settings:OptionSet
):
    """
    Returns a list of randomly chosen partners according to the parameters.
    Above the given minimum amount of partners there is a 50% roll to stop
    adding another partner after each one.
    """
    partners = []
    all_partners = all_partners_imp.copy()

    while len(partners) < num_rnd_partners_min:
        new_partner = random.choice(all_partners)
        all_partners.remove(new_partner)
        partners.append(new_partner)

    while len(partners) < num_rnd_partners_max:
        # Flip a coin to add another partner
        if random.randint(0, 1) == 1:
            new_partner = random.choice(all_partners)
            all_partners.remove(new_partner)
            partners.append(new_partner)
        else:
            break

    rando_settings.start_with_goombario["value"] = False
    rando_settings.start_with_kooper["value"] = False
    rando_settings.start_with_bombette["value"] = False
    rando_settings.start_with_parakarry["value"] = False
    rando_settings.start_with_bow["value"] = False
    rando_settings.start_with_watt["value"] = False
    rando_settings.start_with_sushie["value"] = False
    rando_settings.start_with_lakilester["value"] = False

    for partner in partners:
        if partner == "Goombario":
            rando_settings.start_with_goombario["value"] = True
        elif partner == "Kooper":
            rando_settings.start_with_kooper["value"] = True
        elif partner == "Bombette":
            rando_settings.start_with_bombette["value"] = True
        elif partner == "Parakarry":
            rando_settings.start_with_parakarry["value"] = True
        elif partner == "Bow":
            rando_settings.start_with_bow["value"] = True
        elif partner == "Watt":
            rando_settings.start_with_watt["value"] = True
        elif partner == "Sushie":
            rando_settings.start_with_sushie["value"] = True
        elif partner == "Lakilester":
            rando_settings.start_with_lakilester["value"] = True

    return partners
