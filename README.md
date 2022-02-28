# Paper Mario Randomizer - Seed Generator

This python project is the seed generator for the Open World Paper Mario Randomizer mod  
for Paper Mario 64.  
This generator runs in the backend of the web generator, but can also be used locally,  
although we do not offer support for that.

## Related repositories

Web generator repo: https://github.com/Pronyo-Chan/paper-mario-randomizer  
Base mod repo: (currently private)

## Requirements

This project requires python 3.9 with a handful of additional dependencies.  
Furthermore a base-modded US-ROM of Paper Mario 64 is required and has to be  
provided by the user; automatically patching the base mod is not part of the generator.  
For this purpose the patch file for turning the vanilla US ROM into the base mod is  
provided within the project's /res folder.

## Running from the command line

First, install dependencies (or run the project inside of a virtual environment  
like pipenv).  
Then, to generate a game with default settings:  
`py randomizer.py -t PATH_TO_PREMODDED_ROM`  
To generate a game with custom settings, create or modify a settings yaml file and then:  
`py randomizer.py -c PATH_TO_SETTINGS_YAML -t PATH_TO_PREMODDED_ROM`

## Code of interest

For curious users, this project can show the internal workings of the generator.  
A few interesting files and directories are:  
* /maps/graph_edges/  
  The files in here define the item location requirements, as well as requirements  
  for traversing the ingame world.
* /default_settings.yaml  
  All options, toggles and their default values that the generator can use  
  can be found here.
* /rando_modules/logic.py  
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
* Jdaster64
* MrN829