"""
This module represents Mario as an abstract object for simulating world traversal.
This is required for checking randomization logic.
"""

from metadata.partners_meta import all_partners

class Mario:
    """
    Represents a state of Mario, including items, partners and more abstract
    things that influence progression.
    """
    def __init__(self, **kwargs):
        self.boots = kwargs.get("boots", set())
        self.hammer = kwargs.get("hammer", set())
        self.items = kwargs.get("items", set())
        self.starpieces = kwargs.get("starpieces", set())
        self.partners = kwargs.get("partners", set())
        self.favors = kwargs.get("favors", set()) # https://www.mariowiki.com/Koopa_Koot%27s_favors
        self.flags = kwargs.get("flags", set())
        self.starspirits = kwargs.get("starspirits", set())
        self.item_history = []
        self.starpiece_count = 0


    def add_to_inventory(self, item_object):
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

            #print(f"New item: {item_object}")

            return is_new_pseudoitem
        # Overload: List of items -> Call function per item
        if isinstance(item_object, list):
            has_new_pseudoitem = False
            for singular_item in item_object:
                is_new_pseudoitem = self.add_to_inventory(singular_item)
                if is_new_pseudoitem:
                    has_new_pseudoitem = True
            return has_new_pseudoitem

        raise TypeError('item_object argument is not of type str or list',
                        type(item_object),
                        item_object)


    def remove_from_inventory(self, item_object):
        """Remove something from Mario's inventory."""
        # Overload: Single item -> Remove item
        if isinstance(item_object, str):

            if (   item_object.startswith("GF")
                or item_object.startswith("MF")
                or item_object.startswith("MB")
                or item_object.startswith("RF")
            ):
                self.flags.remove(item_object)
            elif item_object in all_partners:
                self.partners.remove(item_object)
                self.item_history.append(f"-{item_object}")
            elif item_object.find("StarPiece") != -1:
                if item_object.startswith("Three"):
                    self.starpiece_count -= 3
                else:
                    self.starpiece_count -= 1
                self.starpieces.remove(item_object)
                self.item_history.append(f"-{item_object}")
            elif item_object.startswith("FAVOR"):
                self.favors.remove(item_object)
            elif (item_object in ["BootsProxy1","BootsProxy2","BootsProxy3"]):
                self.boots.remove(item_object)
            elif (item_object in ["HammerProxy1","HammerProxy2","HammerProxy3"]):
                self.hammer.remove(item_object)
            elif item_object.startswith("STARSPIRIT"):
                self.starspirits.remove(item_object)
            else:
                self.items.remove(item_object)
                self.item_history.append(f"-{item_object}")
            return

        # Overload: List of items -> Call function per item
        if isinstance(item_object, list):
            for singular_item in item_object:
                self.remove_from_inventory(singular_item)
            return

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
