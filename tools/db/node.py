from db.db import db
from peewee import *
from utility import get_files


# A table that represents all areas of interactivity
class Node(Model):

    # Things that must be present to activate this node
    partner = CharField(null=True)
    item_required = CharField(null=True)
    hammer = IntegerField(null=True)
    boots = IntegerField(null=True)

    # Used to identify order of key items obtained necessary for progression
    sequence = IntegerField(null=True)

    # Whether or not this node is required to progress further through the list
    required = BooleanField(default=False)

    # Whether the required object is removed
    remove = BooleanField(default=False)

    # Things that are received when this node is activated
    level = IntegerField()
    item_received = CharField(null=True)
    partner_received = CharField(null=True)

    # Misc
    comment = CharField()
    map_name = CharField()
    index = IntegerField(null=True)

    def __str__(self):
        requirements = []
        if self.partner:
            requirements.append(self.partner)
        if self.item_required:
            requirements.append(self.item_required)
        if self.hammer:
            requirements.append(f"Hammer({self.hammer})")
        if self.boots:
            requirements.append(f"Boots({self.boots})")
        requirements = " | ".join(requirements)

        receive = []
        if self.item_received:
            receive.append(self.item_received)
        if self.partner_received:
            receive.append(self.partner_received)
        if self.required:
            receive.append("Progress+")
        receive = ", ".join(receive)

        return f"[{self.map_name}][{self.index if self.index else ''}] Have [{requirements}] -> Receive [{receive}]"

    def can_activate(self, mario):
        if (mario.level + 1) < self.level:
            return False

        if all([self.partner is None, self.item_required is None, self.hammer is None, self.boots is None]):
            return True

        # Check Partners
        if self.partner:
            # Evaluate boolean expressions (lazily)
            if "|" in self.partner:
                p1,p2 = self.partner.replace(" ","").split("|")
                if p1 in mario.partners:
                    return True
                elif p2 in mario.partners:
                    return True
            elif "&" in self.partner:
                pass
                # TODO?
                # p1,p2 = self.partner.replace(" ","").split("&")
            else:
                if self.partner in mario.partners:
                    return True

        # Check Items
        if self.item_required:
            if self.item_required in [item for item,db_key in mario.items]:
                return True
            elif self.item_required == "<Any3Letters>":
                # Parakarry will require 3 of any letter instead of 3 specific ones
                count = 0
                for item,db_key in mario.items:
                    if item.startswith("Letter"):
                        count += 1
                if count >= 3:
                    return True

        # Check Hammer
        if self.hammer and mario.hammer >= self.hammer:
            return True

        # Check Boots
        if self.boots and mario.boots >= self.boots:
            return True

        return False

    class Meta:
        database = db


def create_nodes():
    db.drop_tables([Node])
    db.create_tables([Node])

    for filepath in get_files("./progression/", filetype=".csv"):
        with open(filepath, "r") as file:
            for i,line in enumerate(file.readlines()):
                if i == 0:
                    continue
                comment,partner,item_required,sequence,hammer,boots,item_received,partner_received,required,remove,level,map_name,index = line.strip().split(",")

                # Something is wrong/issing with this entry and needs to be fixed first
                if index == "-1":
                    continue

                node,created = Node.get_or_create(
                    partner=partner if partner else None,
                    item_required=item_required if item_required else None,
                    sequence=None if not sequence else int(sequence),
                    hammer=int(hammer) if hammer else None,
                    boots=int(boots) if boots else None,
                    required=True if required == "1" else False,
                    remove=True if remove == "1" else False,
                    level=int(level),
                    item_received=item_received if item_received else None,
                    partner_received=partner_received if partner_received else None,
                    comment=comment,
                    map_name=map_name,
                    index=int(index) if index else None,
                )

                print(node, created)