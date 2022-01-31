**This is a living document and will change over time. This document will outline the OpenWorld PM64 Randomizer project itself and is not 100%ly representative of the files or pipeline offered for download to players during releases!**

This document shall describe the general layout of the randomizer and show the sequence of module execution.

## Project Components

The program is divided into the following components:  

1. StarRod modding tool for Paper Mario
2. Randomizer tool written in Python

The randomizer is divided into the following modules:  

1. Graphical User Interface (GUI) in gui.py: Offers user the ability to choose settings for the randomizer
2. Randomizer module: Takes settings given by the GUI or the terminal and creates a randomized ROM.  
The ability to access the randomizer via terminal is useful for automated seed generation (e.g. via web service).

## Randomizer Pipeline

The following steps are taken to create a randomized PM64 ROM within the development project:  
1. Dump the original ROM, copy assets to project root and recompile mod using StarRod.  
(This step is only required to be done once)
2. Create a local SQLite database file representing the ingame world state of the non-randomized, modded ROM to serve as default value repository.  
(This step is only required to be done once)
3. Randomize using given seed and according to chosen settings.
    1. Create World Graph.
        * Either load from defaults DB or
        * randomize in entrance module
    2. Prepare itempool according to chosen settings.
        * Include coins, if set
        * Include shop items, if set
    3. Randomly place progression items into the World Graph.
        1. Create a list of locations that are reachable with Mario's current inventory, are to be randomized according to settings (coins, shops) and don't have an item placed yet
        2. Randomly pick one location from above list
        3. Place a random progression item into the location, removing it from the item pool
        4. Place the same progression item into Mario's inventory
        5. Check if this progression item unlocks the ability to get a new partner, piece of equipment or flag and add these as pseudo-items into Mario's inventory
        6. If shops are randomized and current location is a shop, randomize item price
        7. Repeat until all progression items are placed
    4. Randomly place remaining items into the World Graph
        1. Create a list of locations that are to be randomized according to settings (coins, shops) and don't have an item placed yet
        2. Randomly pick one location from above list
        3. Place a random item into the location, removing it from the item pool
        6. If shops are randomized and current location is a shop, randomize item price
        4. Repeat until all progression items are placed
    5. Randomize Chuck Quizmo questions
    6. Prepare chosen general options (e.g. damage).
4. Write randomized world state into non-randomized, modded ROM.

## World Graph

The World Graph is a series of nodes connected by edges. Nodes depict item locations and distinct entrances of maps, while edges represent the connections between nodes. Edges are used to model connections between entrances, as well as general roadblocks between nodes such as required items or partners.  
Each edge has an origin_node and a target_node, as well as requirements to traverse from the former to the latter. A node is only considered valid if there is an edge with said node as origin_node defined. Otherwise the node cannot be left by Mario and becomes invalid. This however needs only be checked when randomizing entrances.  
While each map in PM's world may have (and often has) multiple nodes associated with itself, each map requires atleast one node. Otherwise the map would have no representation in the World Graph and would be skipped during entrance randomization.  
A node may have an entrance_id, an item, or both. A node with only an entrance_id represents a map entrance. A node with only an item represents an item location. If a map has an item location that can be reached from any entrance without requirements, and said item location can also reach back to the same entrance without requirements, both the entrance and the item may be represented by a single item+entrance_id node to reduce graph complexity (for better understanding, see ./world_graph_visualized/trd.jpg).  
The root of the World Graph is a single edge (with no origin node and no requirements) representing the entrance from which Mario starts his adventure. In the default settings, this edge points towards the green pipe in Toad Town's Gate District.