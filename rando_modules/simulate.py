"""
This module represents Mario as an abstract object for simulating world traversal.
This is required for checking randomization logic.
"""

from metadata.multiuse_progression_items import multiuse_progression_items

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


def add_to_inventory(item_object):
    """Add something to Mario's inventory."""
    all_partners = ["Goombario", "Kooper", "Bombette", "Parakarry",
                    "Bow", "Watt", "Sushie", "Lakilester"]
    global mario
    # Overload: Single item -> Add item
    if isinstance(item_object, str):
        is_new_pseudoitem = False
    
        if (   item_object.startswith("GF")
            or item_object.startswith("MF")
            or item_object.startswith("MB")
            or item_object.startswith("RF")):
            if item_object not in mario.flags:
                mario.flags.add(item_object)
            is_new_pseudoitem = True
        elif item_object in all_partners:
            if item_object not in mario.partners:
                mario.partners.add(item_object)
                mario.item_history.append(item_object)
                is_new_pseudoitem = True
        elif item_object.find("StarPiece") != -1:
            if item_object not in mario.starpieces:
                mario.starpieces.add(item_object)
                mario.item_history.append(item_object)
                if item_object.startswith("Three"):
                    mario.starpiece_count += 3
                else:
                    mario.starpiece_count += 1
        elif item_object.startswith("FAVOR"):
            if item_object not in mario.favors:
                mario.favors.add(item_object)
                is_new_pseudoitem = True
        elif item_object.startswith("EQUIPMENT"):
            if (item_object.startswith("EQUIPMENT_Boots_Progressive")
            and item_object not in mario.boots
            ):
                mario.boots.add(item_object)
                is_new_pseudoitem = True
            if (item_object.startswith("EQUIPMENT_Hammer_Progressive")
            and item_object not in mario.hammer
            ):
                mario.hammer.add(item_object)
                is_new_pseudoitem = True
        elif item_object.startswith("STARSPIRIT"):
            if item_object not in mario.starspirits:
                mario.starspirits.add(item_object)
            is_new_pseudoitem = True
        else:
            if item_object not in mario.items:
                mario.items.add(item_object)
                mario.item_history.append(item_object)
        
        #print(f"New item: {item_object}")

        return is_new_pseudoitem
    # Overload: List of items -> Call function per item
    if isinstance(item_object, list):
        has_new_pseudoitem = False
        for singular_item in item_object:
            is_new_pseudoitem = add_to_inventory(singular_item)
            if is_new_pseudoitem:
                has_new_pseudoitem = True
        return has_new_pseudoitem

    raise TypeError('item_object argument is not of type str or list',
                    type(item_object),
                    item_object)


def clear_inventory():
    """Completely clear Mario's inventory."""
    global mario
    mario = Mario()


def get_item_history():
    """"""
    global mario
    return mario.item_history


def can_flip_panels():
    """
    Checks if Mario can currently flip hidden panels:
    * Superboots or better, or
    * UltraHammer
    """
    global mario
    return len(mario.hammer) == 3 or len(mario.boots) >= 2


def can_shake_trees():
    """
    Checks if Mario can currently shake trees:
    * Hammer or better, or
    * Bombette
    """
    global mario
    return len(mario.hammer) >= 1 or "Bombette" in mario.partners


def has_item(item_str):
    """Checks if Mario currently has a certain item."""
    global mario
    return item_str in mario.items


def has_partner(partner_str):
    """Checks if Mario currently has a certain partner."""
    global mario
    return partner_str in mario.partners


def has_parakarry_3_letters():
    """Checks if Mario has three or more different letters he can give to Parakarry."""
    global mario
    count = 0
    for item_str in mario.items:
        if item_str.startswith("Letter"):
            count += 1
            if count >= 3:
                return True
    return False


def get_starpiece_count() -> int:
    global mario
    return mario.starpiece_count


def saved_all_yoshikids():
    """Checks if Mario has saved all 5 of the Yoshi Kids"""
    global mario
    count = 0
    for flag_str in mario.flags:
        if flag_str.startswith("RF_SavedYoshiKid"):
            count += 1
            if count >= 5:
                return True
    return False


def require(**kwargs):
    # Sanity-checking kwargs
    for key in kwargs.keys():
        if key not in [
            "partner",
            "item",
            "starpieces",
            "hammer",
            "boots",
            "favor",
            "flag",
            "starspirits"
        ]:
            raise KeyError('Requirement kwargs is not valid', key)
    def func(kwargs=kwargs):
        global mario

        # Partners
        if "partner" in kwargs:
            partners = kwargs["partner"]
            if not isinstance(partners, list):
                partners = [partners]
            for partner in partners:
                if partner in mario.partners:
                    return True
        # Items
        if "item" in kwargs:
            items = kwargs["item"]
            if not isinstance(items, list):
                items = [items]
            for item in items:
                if item in multiuse_progression_items:
                    # remove single multiuse item #TODO very janky, pls rework
                    for multi_item in multiuse_progression_items[item]:
                        if multi_item in mario.items:
                            mario.items.remove(multi_item)
                            return True
                elif item in mario.items:
                    return True
        # StarPieces
        if "starpieces" in kwargs:
            starpieces = kwargs["starpieces"]
            if mario.starpiece_count >= starpieces:
                return True
        # Hammer
        if "hammer" in kwargs:
            hammer = kwargs["hammer"]
            if len(mario.hammer) >= hammer:
                return True
        # Boots
        if "boots" in kwargs:
            boots = kwargs["boots"]
            if len(mario.boots) >= boots:
                return True
        # Koopa Koot Favors
        if "favor" in kwargs:
            favor = kwargs["favor"]
            if favor in mario.favors:
                return True
        # Flags
        if "flag" in kwargs:
            flags = kwargs["flag"]
            if not isinstance(flags, list):
                flags = [flags]
            for flag in flags:
                if flag in mario.flags:
                    return True
        # Star Spirits
        if "starspirits" in kwargs:
            starspirits = kwargs["starspirits"]
            if len(mario.starspirits) >= starspirits:
                return True
                

        return False
    return func
