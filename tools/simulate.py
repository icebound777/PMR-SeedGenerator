


class Mario:
    def __init__(self, **kwargs):
        self.boots = kwargs.get("boots", 0)
        self.hammer = kwargs.get("hammer", 0)
        self.items = kwargs.get("items", [])
        self.partners = kwargs.get("partners", [])


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
            if partner not in mario.partners:
                return False
        # Items
        if item := kwargs.get("item"):
            if item not in mario.items:
                return False
        # Hammer
        if hammer := kwargs.get("hammer"):
            if mario.hammer < hammer:
                return False
        # Boots
        if boots := kwargs.get("boots"):
            if mario.boots < boots:
                return False
        return True
    return func


# Example
"""
mario = Mario()
mario.partners.append("Kooper")
# mario.items.append("Mushroom")

reqs = [require(partner="Kooper", item="Mushroom")]
if all([r() for r in reqs]):
    print("Accessible")
else:
    print("Not accessible")
"""