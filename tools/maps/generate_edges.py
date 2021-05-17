import json
from pathlib import Path

for child in Path("./links").iterdir():
    if child.is_file() and child.name != "default_linkages.json":
        with open(child, "r") as file:
            entrance_data = json.load(file)

            edge_list = []
            reqs = ""
            for source_map, entrance_ids in entrance_data.items():
                for entrance_id in entrance_ids.keys():
                    cur_edge_dict = {}
            
                    from_map = {}
            
                    from_map["map"] = source_map
                    from_map["id"] = entrance_id
            
                    cur_edge_dict["from"] = from_map
            
                    to_map = {}
            
                    to_map["map"] = entrance_ids[entrance_id]["dest_map"]
                    to_map["id"] = entrance_ids[entrance_id]["dest_entry"]
            
                    cur_edge_dict["to"] = to_map
            
                    cur_edge_dict["reqs"] = reqs
            
                    edge_list.append(cur_edge_dict)
            
            # print(edge_list)
            with open("./graph_edges/entrance_edges_" + child.name[-8:-5] + ".json", "w") as out_file:
                json.dump(edge_list, out_file, indent=4)