import json


def convert(filename):
    with open(filename, "r") as file:
        d = json.load(file)

    for map_name,entrance_data in d.items():
        for entrance,data in entrance_data.items():
            d[map_name][entrance]["type"] = "walk"
            d[map_name][entrance]["verbose_name"] = "Exit"
    
    with open(filename, "w") as file:
        json.dump(d, file, indent=4)