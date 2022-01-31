Important Files and General Structure:
* The `/db` folder contains all the database models
	* For each model file, there are additional functions for generating a fresh table from the StarRod outputs  in the `/globals` directory of the root folder for this repo
* The `/debug` folder contains some log files, but also some important .json files used by the database generation functions in the `/db` folder. Namely, `keys.json` and `values.json`, which can be generated with `gather_keys()` and `gather_values()` in `parse.py`, respectively.
* The `/progression` folder contains .csv files also used for generating the `Node` table in the database. These files are manually created.
* `logic.py` and `simulate.py` are currently where most of the higher-level randomization logic happens
* `parse.py` is for functions used that parse through files created by StarRod
* `utility.py` is for any functions that provide general utility

Currently, the system works as follows:
* Using the command-line interface, tell StarRod to dump, copy, and compile a mod into an output ROM.
* With the database (that is auto-generated) and other logical datastructures, randomize various elements.
* Then, generate the list of key-value pairs to be written into the output ROM.

The major hurdles on the Python side are currently creating and expanding the .csvs in the `/progression` folder, and working on the key item placement logic. Once we have a fully complete Node table, however, it will be easier to do work on the item logic, so the priority right now is to finish compiling that.