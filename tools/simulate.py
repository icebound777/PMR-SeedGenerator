from enums import Enums

from db.item import Item, Node
from db.map_area import MapArea


class Mario:
    def __init__(self):
        self.partners = set()
        self.items = set()
        self.boots = 0
        self.hammer = 0
        self.coins = 0
        self.star_pieces = 0
        self.level = 0

    def display(self):
        print("    Items: " + ", ".join([item for item,db_key in self.items]))
        print("    Partners: " + ", ".join(self.partners))
        print(f"    Hammer: {self.hammer}, Boots: {self.boots}, Star Pieces: {self.star_pieces}, Coins: {self.coins}")

    def update(self, node):
        if self.level < node.level:
            self.level = node.level

        if node.remove:
            self.remove_item(node)

        if node.item_received:
            if node.item_received == "StarPiece":
                self.star_pieces += 1
            elif node.item_received == "Coin":
                self.coins += 1
            else:
                self.items.add((node.item_received, node.index))
        
        if node.partner_received:
            self.partners.add(node.partner_received)

    def remove_item(self, node):
        for item,db_key in self.items:
            if item == node.item_required:
                removed_item = (item, db_key)
                break
        self.items.remove(removed_item)

mario = Mario()




# Attempt to run through the game with the current state of item placement
# Return a list of items that are valid to be replaced
def simulate_gameplay(app, **kwargs):
    global mario

    debug = kwargs.get("debug")

    mario.partners = kwargs.get("partners", {"Goombario"})
    mario.items = kwargs.get("items", set())
    mario.boots = kwargs.get("boots", 0)
    mario.hammer = kwargs.get("hammer", 0)
    mario.coins = kwargs.get("coins", 0)
    mario.star_pieces = kwargs.get("star_pieces", 0)
    mario.level = kwargs.get("level", 0)

    nodes = Node.select().order_by(Node.level, Node.id.asc())
    
    activated = set()

    # First pass
    print("First Pass")
    for node in nodes:
        if node.can_activate(mario):
            if node not in activated:
                print("+ " + f"{node}")
                mario.update(node)
            activated.add(node)
        elif node.required and mario.level < node.level:
            print("|| " + f"{node}")
            break
        elif mario.level < node.level:
            pass
    mario.display()

    # Final pass
    print("Final Pass")
    for node in nodes:
        if node.can_activate(mario):
            if node not in activated:
                print("+ " + f"{node}")
                mario.update(node)
            activated.add(node)
        elif node.required and mario.level < node.level:
            print("|| " + f"{node}")
            break
        elif mario.level < node.level:
            pass
    mario.display()

    return mario, activated