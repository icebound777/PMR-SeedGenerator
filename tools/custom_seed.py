import sqlite3
import json


def generate():
    """Generate a custom_seed.json file with default items."""

    custom_seed_dict = {}
    connection = sqlite3.connect("./default_db.sqlite")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    select_statement = ("SELECT node.key_name_item AS key_name_item\
                              , maparea.name       AS map_name\
                              , item.item_name     AS item_name\
                           FROM node\
                          INNER JOIN maparea\
                             ON node.map_area_id = maparea.id\
                          INNER JOIN item\
                             ON node.vanilla_item_id = item.id\
                          WHERE node.key_name_item IS NOT NULL\
                          ORDER BY maparea.area_id ASC, maparea.map_id ASC, node.key_name_item ASC")
    cursor.execute(select_statement)
    tablerows = [row for row in cursor.fetchall()]
    for i,tablerow in enumerate(tablerows):
        key_name = tablerow['key_name_item']
        map_name = tablerow['map_name']
        item_name = tablerow['item_name']

        if custom_seed_dict.get(map_name) is None:
            custom_seed_dict[map_name] = {}
        custom_seed_dict[map_name][key_name] = item_name

    with open("./custom_seed.json", "w") as file:
        json.dump(custom_seed_dict, file, indent=4)

def validate_seed(filepath):
    """
    Analyzes a custom seed file to check for the following:
    * is it a valid JSON
    * are all itemlocations correctly listed
    * is the seed beatable
    """
    #NYI
    return True