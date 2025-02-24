# Paper Mario Randomizer - Seed Generator

This python project is the seed generator for the Open World Paper Mario Randomizer mod
for Paper Mario 64.  
This generator runs in the backend of the web generator, but can also be used locally,
although we do not offer support for that.

## Related repositories

* [Web generator repo](https://github.com/Pronyo-Chan/paper-mario-randomizer)
* Base mod repo: (currently private)
* [Plandomizer submodule repo](https://github.com/icebound777/PMR-Plando-Validator)

This repository uses git submodules, so keep that in mind mind when cloning:  
`git clone --recurse-submodules`

## Requirements

This project requires python 3.11+ with a handful of additional dependencies.  
Furthermore a base-modded US-ROM of Paper Mario 64 is required and has to be provided by the user; automatically patching the base mod is not part of the generator.  
For this purpose the patch file for turning the vanilla US ROM into the base mod is
provided within the project's /res folder.

## Running from the command line

Either run a python3 dev container using the provided devcontainer file, or start a python virtual environment (like pipenv).  
Then install the dependencies within `requirements.txt` using `pip`.  

To generate a game with default settings:  
`python3 randomizer.py -t PATH_TO_PREMODDED_ROM`  
To generate a game with custom settings, create or modify a settings yaml file and then:  
`python3 randomizer.py -c PATH_TO_SETTINGS_YAML -t PATH_TO_PREMODDED_ROM`  
For further parameters, see `python3 randomizer.py --help`  
Note that the seed generator writes to the provided file destructively, so make a backup of your pre-modded ROM.

## Code of interest

For curious users, this project can show the internal workings of the generator.  
A few interesting files and directories are:

* `/maps/graph_edges/base_graph`
  The files in here define the item location requirements, as well as requirements
  for traversing the ingame world.
* [Default Settings](presets/default_settings.yaml)
  All options, toggles and their default values that the generator can use
  can be found here.
* [Placement Logic](rando_modules/logic.py)
  This file handles the item placement logic (graph based using DFS).

## Credits

The Paper Mario Randomizer as a whole was built by

* clover
* Icebound777
* Pronyo

with assistance and contributions by

* Jdog
* Quackles
* Rain
* MrN829
* MrCheeze
* AmazingAmpharos
* Boingboingsplat
* Phantom5800
* christianlegge
