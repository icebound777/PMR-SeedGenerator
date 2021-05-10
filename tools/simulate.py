from enums import Enums

from db.item import Item
from db.node import Node
from db.map_area import MapArea


class Mario:
    instance = None

    def __init__(self):
        self.partners = {"Goombario"}
        self.items = set()
        self.maps = set()
        self.boots = 0
        self.hammer = 0
        self.coins = 0
        self.star_pieces = 0
        self.level = 0
        Mario.instance = self

    def display(self):
        print("    Items: " + ", ".join([item for item,db_key in self.items]))
        print("    Partners: " + ", ".join(self.partners))
        print(f"    Hammer: {self.hammer}, Boots: {self.boots}, Star Pieces: {self.star_pieces}, Coins: {self.coins}")

    def accessible_nodes(self):
        nodes = Node.select()
        return list(filter(lambda node: node.can_activate(self), nodes))

    def traverse_nodes(self, app, update=True):
        iterations = 0
        nodes = self.accessible_nodes()
        accessed_nodes = set()
        item_nodes = set()
        stop_nodes = set()
        while len(nodes) > 0:
            print(f"{len(nodes)} nodes accessed (update={update})")
            app.processEvents()
            iterations += 1
            for node in nodes:
                accessed_nodes.add(node)

                if self.level < node.level and node.sequence:
                    stop_nodes.add(node)

                if node.item_received:
                    item_nodes.add(node)

                if update:
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
            nodes = [node for node in self.accessible_nodes() if node not in accessed_nodes]

        return item_nodes, stop_nodes

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

# Attempt to run through the game with the current state of item placement
# Return a list of items that are valid to be replaced
def simulate_gameplay(app, **kwargs):

    debug = kwargs.get("debug")
    mario = kwargs.get("mario", Mario())

    nodes = Node.select().order_by(Node.level, Node.id.asc())
    activated = set()

    def traverse_nodes():
        for node in nodes:
            if node.can_activate(mario):
                if node not in activated:
                    if debug:
                        print("+ " + f"{node}")
                    mario.update(node)
                activated.add(node)
            elif node.required and mario.level < node.level:
                if debug:
                    print("|| " + f"{node}")
                break
            elif mario.level < node.level:
                pass
        if debug:
            mario.display()

    # Go through twice to pick up any nodes missed in the first pass
    traverse_nodes()
    traverse_nodes()

    return mario, activated