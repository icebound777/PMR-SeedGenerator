from peewee import *

from db.db import db
from db.node import node

class Edge(Model):
    # Node this edge leads away from
    origin_node = ForeignKeyField(Node, backref = "edges")
    # Node this edge leads towards
    target_node = ForeignKeyField(Node)
    # Requirements for traversing this edge
    #TODO Which Fieldtype to choose here?
    requirements = CharField()

def create_edges():
    """Rebuild Edge table and add edges"""
    db.drop_tables([Edge])
    db.create_tables([Edge])

    #TODO