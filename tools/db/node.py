from db.db import db
from peewee import *
from utility import get_files


# A table that represents all areas of interactivity
class Node(Model):

    # MapArea this node is found in
    map_area = ForeignKeyField(MapArea, backref = "nodes")

    # Entrance ID of the Map if this note represents an entrance
    entrance_id = IntegerField(null = True)

    # Human readable name of item location (eg ItemA)
    key_name = CharField(null = True)

    # reference to item placed here in the unmodified game
    vanilla_item = ForeignKeyField(Item, backref="itemlocation")

    # reference to item placed here during randomization
    current_item = ForeignKeyField(Item, null=True, backref="itemlocation")

    #TODO index?

    def __str__(self):
        """Return string representation of current node"""
        entrance = ("[" + format(self.entrance_id) + "] ") if self.entrance_id else ''
        itemkey = ("[" + format(self.key_name) + "] ") if self.key_name else ''
        item = format(self.current_item.name) if self.current_item else ''

        return f"[{self.map_area.map_id}]{entrance}{itemkey} {item}"

    # def get_key(self):
    #     """Return convention key for location"""
    #     return (Item._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index    

    class Meta:
        database = db


def create_nodes():
    """Rebuild Node table and add nodes"""
    db.drop_tables([Node])
    db.create_tables([Node])

    with open("./debug/keys.json", "r") as file:
        item_keys = json.load(file)["items"]

    with open("./debug/values.json", "r") as file:
        item_values = json.load(file)["items"]
        entrance_values = json.load(file)["entrances"]

    with open("./maps/default_linkages.json", "r") as file:
        entrance_links = json.load(file)

    # Create item only nodes
    for key, data in item_keys.items():
        map_area, created = MapArea.get_or_create(
            area_id = data["area_id"],
            map_id = data["map_id"],
            name = data["map_name"],
            verbose_name = MapArea.get_verbose_name(data["map_name"])
        )

        vanilla_item, created = Item.get_or_create(
            value = item_values[data["map_name"]][data["name"]]
        )

        node, created = Node.get_or_create(
            map_area = map_area,
            key_name = data["name"],
            vanilla_item = vanilla_item,
            current_item = vanilla_item
        )
        print(node, created)

    # Create entrance only nodes
    for key, data in entrance_values.items():

        if data["entrance"] in entrance_links.get(data["name"]).keys():

            map_area, created = MapArea.get_or_create(
                area_id = data["area_id"],
                map_id = data["map_id"],
                name = data["name"],
                verbose_name = MapArea.get_verbose_name(data["name"])
            )

            #TODO makes too few entrances since default_linkages.json isnt complete
            for entrance_id in entrance_links.get(data["name"]).keys():
                node, created = Node.get_or_create(
                    map_area = map_area,
                    entrance_id = entrance_id
                )
    
    # Create item + entrance nodes:
    #TODO ? Might be worth a manual setup