


class Mario:
    def __init__(self, **kwargs):
        self.boots = kwargs.get("boots", 0)
        self.hammer = kwargs.get("hammer", 0)
        self.items = kwargs.get("items", [])
        self.partners = kwargs.get("partners", [])
        self.favors = kwargs.get("favors", []) # https://www.mariowiki.com/Koopa_Koot%27s_favors


def flip_panels():
    global mario
    return mario.hammer > 1 or mario.boots > 0

def item(item_str):
    global mario
    return item_str in mario.items

def partner(partner_str):
    global mario
    return partner_str in mario.partners

def parakarry_3_letters():
    global mario
    count = 0
    for item_str in mario.items:
        if item_str.startswith("Letter"):
            count += 1
            if count >= 3:
                return True
    return False

def require(**kwargs):
    def func(kwargs=kwargs):
        global mario
        # Partners
        if partner := kwargs.get("partner"):
            if partner in mario.partners:
                return True
        # Items
        if item := kwargs.get("item"):
            if item in mario.items:
                return True
        # Hammer
        if hammer := kwargs.get("hammer"):
            if mario.hammer >= hammer:
                return True
        # Boots
        if boots := kwargs.get("boots"):
            if mario.boots >= boots:
                return True

        # Koopa Koot Favors
        if favor := kwargs.get("favor"):
            if favor in mario.favors:
                return True
        return False
    return func


# Example
mario = Mario()
"""
mario.partners.append("Kooper")
mario.boots = 0

reqs = [require(partner="Kooper", boots=2)]
if all([r() for r in reqs]):
    print("Accessible")
else:
    print("Not accessible")
"""