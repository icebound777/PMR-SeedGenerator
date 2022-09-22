"""
This module represents Mario's inventory as an abstract object for simulating
world traversal. This is required for checking randomization logic.
"""

from metadata.partners_meta import all_partners

class MarioInventory:
    """
    Represents a state of Mario's inventory, including items, partners and more
    abstract things that influence progression.
    """
    def __init__(
        self,
        starting_boots:int=0,
        starting_hammer:int=0,
        starting_partners:list=None,
        starting_items:list=None,
        partners_always_usable:bool=True,
        hidden_block_mode:int=1,
        magical_seeds_required:int=4,
        startwith_prologue_open:bool=False,
        startwith_bluehouse_open:bool=False,
        startwith_toybox_open:bool=False,
        startwith_whale_open:bool=False,
        startwith_speedyspin:bool=True,
        cook_without_fryingpan:bool=True
    ):
        """
        Initializes Mario's starting inventory with values depending on
        several parameters and flags.
        This includes partners (for considering their overworld abilities during
        world graph traversal), equipment, as well as additional pseudoitems
        based on chosen settings.
        Starting equipment irrelevant to world graph traversal (such as Lucky
        Star, starting coins) is ignored.
        """
        assert(isinstance(starting_boots, int) and starting_boots in range(-1,3))
        assert(isinstance(starting_hammer, int) and starting_hammer in range(-1,3))
        assert(starting_partners is None or isinstance(starting_partners, list))
        if starting_partners is None:
            starting_partners = ["Goombario"]
        assert(isinstance(partners_always_usable, bool))
        assert(starting_items is None or isinstance(starting_items, list))
        if starting_items is None:
            starting_items = []
        assert(isinstance(hidden_block_mode, int))
        assert(isinstance(magical_seeds_required, int) and magical_seeds_required in range(0,5))
        assert(isinstance(startwith_prologue_open, bool))
        assert(isinstance(startwith_bluehouse_open, bool))
        assert(isinstance(startwith_toybox_open, bool))
        assert(isinstance(startwith_whale_open, bool))
        assert(isinstance(startwith_speedyspin, bool))
        assert(isinstance(cook_without_fryingpan, bool))

        self.boots = set()
        self.hammer = set()
        self.items = set()
        self.starpieces = set()
        self.starpiece_count = 0
        self.partners = set()
        self.favors = set()
        self.flags = set()
        self.starspirits = set()
        self.item_history = []

        if starting_boots == 2:
            self.add("BootsProxy3")
        if starting_boots >= 1:
            self.add("BootsProxy2")
        if starting_boots >= 0:
            self.add("BootsProxy1")

        if starting_hammer == 2:
            self.add("HammerProxy3")
        if starting_hammer >= 1:
            self.add("HammerProxy2")
        if starting_hammer >= 0:
            self.add("HammerProxy1")

        self.add(starting_partners)
        if partners_always_usable:
            self.add(all_partners)
            self.add("RF_PartnersAlwaysUsable")

        for item in starting_items:
            self.add(item.item_name)

        if hidden_block_mode == 3:
            # hidden blocks always visible
            self.add("RF_HiddenBlocksVisible")

        if magical_seeds_required <= 3:
            self.add("RF_MagicalSeed1")
        if magical_seeds_required <= 2:
            self.add("RF_MagicalSeed2")
        if magical_seeds_required <= 1:
            self.add("RF_MagicalSeed3")
        if magical_seeds_required == 0:
            self.add("RF_MagicalSeed4")

        if startwith_prologue_open:
            self.add("RF_BeatGoombaKing")
        if startwith_bluehouse_open:
            self.add("GF_MAC02_UnlockedHouse")
        if startwith_toybox_open:
            self.add("RF_ToyboxOpen")
        if startwith_whale_open:
            self.add("RF_CanRideWhale")

        if startwith_speedyspin:
            self.add("SpeedySpin")

        if cook_without_fryingpan:
            self.add("RF_CanCook")


    def add(self, item_object):
        """Add something to Mario's inventory."""

        # Overload: Single item -> Add item
        if isinstance(item_object, str):
            is_new_pseudoitem = False

            if (   item_object.startswith("GF")
                or item_object.startswith("MF")
                or item_object.startswith("MB")
                or item_object.startswith("RF")
            ):
                if item_object not in self.flags:
                    self.flags.add(item_object)
                is_new_pseudoitem = True
            elif item_object in all_partners:
                if item_object not in self.partners:
                    self.partners.add(item_object)
                    self.item_history.append(f"+{item_object}")
                    is_new_pseudoitem = True
                else:
                    self.partners.add(f'{item_object} (Battle)')
                    self.item_history.append(f"+{item_object} (Battle)'")
                    is_new_pseudoitem = True
            elif item_object.find("StarPiece") != -1:
                if item_object not in self.starpieces:
                    if item_object.startswith("Three"):
                        self.starpiece_count += 3
                    else:
                        self.starpiece_count += 1
                    self.starpieces.add(item_object)
                    self.item_history.append(f"+{item_object}")
            elif item_object.startswith("FAVOR"):
                if item_object not in self.favors:
                    self.favors.add(item_object)
                    is_new_pseudoitem = True
            elif (    item_object in ["BootsProxy1","BootsProxy2","BootsProxy3"]
                  and item_object not in self.boots
            ):
                self.boots.add(item_object)
                is_new_pseudoitem = True
            elif (    item_object in ["HammerProxy1","HammerProxy2","HammerProxy3"]
                  and item_object not in self.hammer
            ):
                self.hammer.add(item_object)
                is_new_pseudoitem = True
            elif item_object.startswith("STARSPIRIT"):
                if item_object not in self.starspirits:
                    self.starspirits.add(item_object)
                is_new_pseudoitem = True
            else:
                if item_object not in self.items:
                    self.items.add(item_object)
                    self.item_history.append(f"+{item_object}")

            return is_new_pseudoitem

        # Overload: List of items -> Call function per item
        if isinstance(item_object, list):
            has_new_pseudoitem = False
            for singular_item in item_object:
                is_new_pseudoitem = self.add(singular_item)
                if is_new_pseudoitem:
                    has_new_pseudoitem = True
            return has_new_pseudoitem

        raise TypeError('item_object argument is not of type str or list',
                        type(item_object),
                        item_object)


    def can_flip_panels(self):
        """
        Checks if Mario can currently flip hidden panels:
        * Superboots or better, or
        * UltraHammer
        """
        return ((len(self.hammer) - 1) >= 2 or len(self.boots) - 1 >= 1)


    def can_shake_trees(self):
        """
        Checks if Mario can currently shake trees:
        * Hammer or better, or
        * Bombette
        """
        return len(self.hammer) - 1 >= 0 or "Bombette" in self.partners


    def can_hit_grounded_blocks(self):
        """Check if Mario is able to hit a block placed on the ground."""
        return (
            len(self.hammer) - 1 >= 0
         or len(self.boots) - 1 >= 1
         or "Kooper" in self.partners
         or "Bombette" in self.partners
        )


    def can_see_hidden_blocks(self):
        """Check if Mario can see hidden blocks."""
        return (
            "Watt" in self.partners
         or "RF_HiddenBlocksVisible" in self.flags
        )


    def has_parakarry_letters(self):
        """Checks if Mario has three or more different letters he can give to Parakarry."""
        count = 0
        for item_str in self.items:
            if item_str.startswith("Letter"):
                count += 1
                if count >= 3:
                    return True
        return False


    def saved_all_yoshikids(self):
        """Checks if Mario has saved all 5 of the Yoshi Kids"""
        count = 0
        for flag_str in self.flags:
            if flag_str.startswith("RF_SavedYoshiKid"):
                count += 1
                if count >= 5:
                    return True
        return False

    def can_end_sushie_glitch(self):
        """Checks if Mario is able to end the sushie glitch with another battle partner"""
        if "RF_PartnersAlwaysUsable" in self.flags:
            if len([p for p in self.partners if "Battle" in p ]) >= 2:
                return True
        else:
            if len(self.partners) >= 2:
                return True
        return False


    def requirements_fulfilled(self, all_reqs:list):
        fulfilled = True
        # For the requirements to be fulfilled, all requirement groups have
        # to be met. Each requirement group has to have at least one of its
        # conditions met to count as fulfilled.
        # This effectively ANDs all requirement groups, and ORs all conditions
        # within a given requirement group.
        for req_group in all_reqs:
            assert(isinstance(req_group, list))
            group_fulfilled = False
            for req in req_group:
                if isinstance(req, dict):
                    # Check star spirits
                    if ("starspirits" in req
                    and len(self.starspirits) >= req["starspirits"]
                    ):
                        group_fulfilled = True
                        break
                    # Check star pieces
                    if ("starpieces" in req
                    and self.starpiece_count >= req["starpieces"]
                    ):
                        group_fulfilled = True
                        break
                    # Check keys
                    for key_name, key_count in req.items():
                        keys_acquired = 0
                        for item in self.items:
                            if item.startswith(key_name):
                                keys_acquired += 1
                        if keys_acquired >= key_count:
                            group_fulfilled = True
                            break
                else:
                    # Check boots
                    if req.endswith("Boots"):
                        if req == "UltraBoots":
                            if len(self.boots) - 1 >= 2:
                                group_fulfilled = True
                                break
                        elif req == "SuperBoots":
                            if len(self.boots) - 1 >= 1:
                                group_fulfilled = True
                                break
                    # Check hammer
                    if req.endswith("Hammer"):
                        if req == "UltraHammer":
                            if len(self.hammer) - 1 >= 2:
                                group_fulfilled = True
                                break
                        elif req == "SuperHammer":
                            if len(self.hammer) - 1 >= 1:
                                group_fulfilled = True
                                break
                        elif req == "Hammer":
                            if len(self.hammer) - 1 >= 0:
                                group_fulfilled = True
                                break
                    # Check partners
                    if req in all_partners:
                        if req in self.partners:
                            group_fulfilled = True
                            break
                    # Check flags
                    if (   req.startswith("GF")
                        or req.startswith("MF")
                        or req.startswith("MB")
                        or req.startswith("RF")):
                        if req in self.flags:
                            group_fulfilled = True
                            break
                    # Check Koopa Koot favors
                    if req.startswith("FAVOR"):
                        if req in self.favors:
                            group_fulfilled = True
                            break
                    # Check panel flipping
                    if req == "can_flip_panels":
                        if self.can_flip_panels():
                            group_fulfilled = True
                            break
                    # Check tree shaking
                    if req == "can_shake_trees":
                        if self.can_shake_trees():
                            group_fulfilled = True
                            break
                    # Check letters for Parakarry
                    if req == "has_parakarry_letters":
                        if self.has_parakarry_letters():
                            group_fulfilled = True
                            break
                    # Check saved Yoshi kids
                    if req == "saved_all_yoshikids":
                        if self.saved_all_yoshikids():
                            group_fulfilled = True
                            break
                    # Check hitting grounded blocks
                    if req == "can_hit_grounded_blocks":
                        if self.can_hit_grounded_blocks():
                            group_fulfilled = True
                            break
                    # Check hidden blocks
                    if req == "can_see_hidden_blocks":
                        if self.can_see_hidden_blocks():
                            group_fulfilled = True
                            break
                    # Check can end sushie glitch
                    if req == "can_end_sushie_glitch":
                        if self.can_end_sushie_glitch():
                            group_fulfilled = True
                            break
                    # Check berries
                    if req in ["BlueBerry","RedBerry","YellowBerry","BubbleBerry"]:
                        if f"{req}Proxy1" in self.items:
                            group_fulfilled = True
                            break
                    # Check other items
                    if req in self.items:
                        group_fulfilled = True
                        break

            if not group_fulfilled:
                fulfilled = False
                break

        return fulfilled
