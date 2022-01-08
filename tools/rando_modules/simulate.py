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
        self.boots = kwargs.get("boots", 0)
        self.hammer = kwargs.get("hammer", -1)
        self.items = kwargs.get("items", [])
        self.partners = kwargs.get("partners", [])
        self.favors = kwargs.get("favors", []) # https://www.mariowiki.com/Koopa_Koot%27s_favors
        self.flags = kwargs.get("flags", [])
        self.starspirits = kwargs.get("starspirits", 0)


def add_to_inventory(item_object):
    """Add something to Mario's inventory."""
    all_partners = ["Goombario", "Kooper", "Bombette", "Parakarry",
                    "Bow", "Watt", "Sushie", "Lakilester"]
    global mario
    # Overload: Single item -> Add item
    if isinstance(item_object, str):
        is_new_pseudoitem = False
    
        if (  item_object.startswith("GF")
            or item_object.startswith("MF")
            or item_object.startswith("MB")
            or item_object.startswith("RF")):
            mario.flags.append(item_object)
            is_new_pseudoitem = True
        elif item_object in all_partners and item_object not in mario.partners:
            mario.partners.append(item_object)
            is_new_pseudoitem = True
        elif item_object.startswith("FAVOR") and item_object not in mario.favors:
            mario.favors.append(item_object)
            is_new_pseudoitem = True
        elif item_object.startswith("EQUIPMENT"):
            if item_object == "EQUIPMENT_Boots_Progressive":
                mario.boots = mario.boots + 1 if mario.boots < 2 else mario.boots
            if item_object == "EQUIPMENT_Hammer_Progressive":
                mario.hammer = mario.hammer + 1 if mario.hammer < 2 else mario.hammer
        elif item_object == "STARSPIRIT":
            mario.starspirits = mario.starspirits + 1 if mario.starspirits < 7 else mario.starspirits
            is_new_pseudoitem = True
        else:
            mario.items.append(item_object)
        
#        print(f"New item: {item_object}")

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


def can_flip_panels():
    """
    Checks if Mario can currently flip hidden panels:
    * Superboots or better, or
    * UltraHammer
    """
    global mario
    return mario.hammer == 2 or mario.boots >= 1


def can_shake_trees():
    """
    Checks if Mario can currently shake trees:
    * Hammer or better, or
    * Bombette
    """
    global mario
    return mario.hammer >= 0 or "Bombette" in mario.partners


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


def saved_all_yoshikids():
    """Checks if Mario has saved all 5 of the Yoshi Kids"""
    global Mario
    count = 0
    for flag_str in mario.flags:
        if flag_str == "RF_SavedYoshiKid":
            count += 1
            if count >= 5:
                return True
    return False


def require(**kwargs):
    def func(kwargs=kwargs):
        global mario
        # Sanity-checking kwargs
        for key in kwargs.keys():
            if key not in ["partner","item","hammer","boots","favor","flag","starspirits"]:
                raise KeyError('Requirement kwargs is not valid', key)

        # Partners
        partners = kwargs.get("partner")
        if type(partners) is not list:
            partners = [partners]
        for partner in partners:
            if partner in mario.partners:
                return True
        # Items
        if item := kwargs.get("item"):
            if item in multiuse_progression_items:
                have_any_req_item = True in (multi_item in mario.items
                                             for multi_item in multiuse_progression_items.get(item))
                if have_any_req_item:
                    # remove single multiuse item #TODO very janky, pls rework
                    for multi_item in multiuse_progression_items.get(item):
                        if multi_item in mario.items:
                            mario.items.remove(multi_item)
                            break
                    return True
            if item in mario.items:
                return True
        # Hammer
        hammer = kwargs.get("hammer")
        if hammer is not None and mario.hammer >= hammer:
            return True
        # Boots
        if boots := kwargs.get("boots"):
            if mario.boots >= boots:
                return True
        # Koopa Koot Favors
        if favor := kwargs.get("favor"):
            if favor in mario.favors:
                return True
        # Flags
        if flag := kwargs.get("flag"):
            if flag in mario.flags:
                return True
        # Star Spirits
        if starspirits := kwargs.get("starspirits"):
            if mario.starspirits >= starspirits:
                return True
                

        return False
    return func
