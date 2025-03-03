# Changelog

## 0.30.0 (beta)

### Feature Changes

* `Multi Coin Block Shuffle` feature
  * Was formerly called `Shuffle Blocks`.
  * Can now choose between the values `off`, `shuffle` (was formerly `on`), and `anywhere`.
  * The value `shuffle` is no longer biased to be evenly distributed. This now gives the areas with more block locations (like Dry Dry Desert) a higher chance at having more super blocks.
  * If the value `anywhere` is chosen, then Multi Coin Blocks can be shuffled into non-block locations. If this happens, they will instead turn into the new `Coin Bag` item, which gives 10 coins on pick-up.
    * Shoutouts to **typographics** for designing the item sprite for the new `Coin Bag` item!

### Quality of Life

* Made Harry, the shop keeper in southern Toad Town, offer to buy, check, and claim Mario's items without first unlocking his storeroom using the Storeroom Key.

### Miscellaneous

* Modified credits scene
  * Added `typographics` to the in-game credits, for making the `Coin Bag` item sprite.
  * Removed `Jdaster64` from the in-game credits, as he was originally added there due to a misunderstanding. Sorry Jdaster, hope you don't mind too much :)
* RAM locations docs
  * Fix wrong item check collected flag for Boo's Mansion - Super Boots Room - In Big Chest. This should stop auto-trackers marking the item as collected even if the item is never picked up.
* New bomb trigger for Toad Town playroom
  * We originally moved the Bombette bomb trigger for opening the Toad Town playroom over to the tree, because the bomb trigger was on the wrong side of the map. We now moved that bomb trigger back to its original, wrong position, and added a second bomb trigger next to the tree. This way both of these locations work for opening the playroom, so you can show off knowing this obscure bug to your friends again :)

## 0.29.1 (beta)

### Bug Fixes (0.29.1)

* Fixed an issue of `Blue Berry` items not respawning from the replenishible crates in Boo's Mansion.

## 0.29.0a (beta)

### Bug Fixes (0.29.0a)

* Fixed an issue that would rarely cause the `Cake` item to be considered the logical progression for getting past Gourmet Guy, instead of requiring the `CakeMix` item and access to Tayce T.'s cooking

## 0.29.0 (beta)

### Feature Changes (0.29.0)

* `Plandomizer` feature
  * The plandomizer (a portmanteau of "planned" and "randomizer") allows pre-setting different values for the seed, which overrule the changes to be made by the seed generator. This allows for forcing specific changes desired by the player.
  * Currently allows setting the following:
    * Item placement in most item locations
    * Prices in regular shops
    * Chapter difficulty
    * Which bosses appear where
    * BP, FP, and SP costs of badges, moves of Mario and his partners, and the star powers
    * Which spirits to rescue for the `Require Specific Spirits` setting
  * If any changes are made to a seed using the plandomizer, the save select screen will show a `Plando` label to inform the player of this.
  * For more details, please refer to the plandomizer module documentation: <https://github.com/icebound777/PMR-Plando-Validator>
* `Random Starting Stats` option:
  * Allows starting the seed with random amounts of HP, FP, and BP by choosing the level to generate these starting stats for
* `Power Star Hunt` related settings:
  * All three power star hunt settings, `Star Hunt Total`, `Star Way Power Stars Needed`, and `Star Beam Power Stars Needed` can now be set to random. `Star Beam Power Stars Needed` is slightly biased towards rolling higher than the value of `Star Way Power Stars Needed`.
  * The price for power stars sold in shops is now dynamic. The more power stars are in the item pool, the lower the price of power stars becomes.
    * 40 or fewer power stars: random price out of `10,15,20,25,30` coins (same as before)
    * 41 - 80 power stars: random price out of `5,10,15,20` coins
    * 81 or more power stars: random price out of `5,10` coins
* `Dungeon Entrance Shuffle`
  * If combining `Dungeon Entrance Shuffle` and `Limit Chapter Logic`, now only dungeons that are logically required will enter the shuffle, and only shuffle among themselves. This solves the odd case of having to enter logically non-required areas to reach required dungeons.
* `Randomize Puzzles` option:
  * Can now include `Blue Berry`, `Red Berry`, `Yellow Berry`, and `Bubble Berry` items in the Dry Dry Outpost shop code puzzles.
* `Cutscene Mode: Minimal`
  * Removed some dialogue from the Toad "inn keeper" in Peach's Castle.

### Logic changes (0.29.0)

* Fixed logic not expecting boots or Kooper for hitting the yellow item block in Tubba's Castle - Stairs to Third Floor
* Fixed logic for the three `Ultra Hammer Skip` glitch settings, and the two `Flarakarry` glitch settings. Formerly these didn't apply properly, so these settings would always count as being turned off

### Quality of Life (0.29.0)

* Entering the toy box in Toad Town will now automatically set the door to the toy box to be open. This is only relevant if you glitched around the toy box door into the toy box.

### Tricks & Glitches (0.29.0)

* New options
  * "Jumpless Dane T. Letters"
  * "Toad Town Sushie Glitch Gearless"
  * "Toad Town Sushie Glitch Full Gear"
  * "Jumpless Summit Climb"
  * "Jumpless Koopa Village Blue Pipe"
  * "Parakarryless Mt. Rugged Seed (Clippy variant)"
  * "Ruins Puzzle Solution Early"
  * "Jumpless Mega Rush"
  * "Raph Skip (Lakilester)"
  * "Bombette Puzzle Skip"
  * "Wattless Dark Basement"
  * "Basement Skip (Parakarry)"
  * "Basement Skip (Lakilester)"
  * "Basement Skip (Hammer)"
  * "Bowsers Castle Hub1 Stair Clip"
  * "Fast Flood Room (Kooperless)"
  * "Cannonless"
* Changed
  * Renamed `Toad Town Sushie Glitch` to `Toad Town Sushie Glitch One Gear`

### Bug Fixes (0.29.0)

* Fixed the vanilla bug of being able to jump into a certain lava loading zone in the basement of Bowser's Castle, possibly causing softlocks or crashes.
* Fixed certain issues with the cutscene of the ravens building the zipline during `Cutscene Mode: Minimal`, which could cause weird behavior or crashes during the cutscene if playing on original hardware.
* Fixed an issue that would sometimes put the menu cursor onto the wrong partner instead of the active partner in the partner menu in battle. This was an edge case that could happen if Bow had not been unlocked yet, and the player was opening the partner menu while having Watt, Sushie, or Lakilester as their active partner.
* Fixed possible buggy behavior and softlock potential when touching an item trap while riding Lakilester. Now item trap knockback is disabled while riding Lakilester.
* Fixed missing star piece "plink" sound effect when a star piece item bounces on the floor. This has been an issue for over three years and apparently nobody noticed :)

### Miscellaneous (0.29.0)

* Entrance randomizer preparations
  * Added a bomb trigger to the uppermost floor of the second Water Puzzle room in Bowser's Castle. This allows blowing up the wall from this side, which is normally not possible
* Spoiler log
  * Moved the item placement areas into their own `items` subcategory.
  * For boss battles, renamed the chapters from just numbers to `chapter #`.
  * Fixed an issue that caused badge BP values to show as vanilla, despite being changed for the seed.
  * Remove the space from partner upgrades for consistency (e.g. `Bombette Upgrade` to `BombetteUpgrade`).
  * Adjust capitalization of star pieces for consistency (`Starpiece` to `StarPiece`).
  * Rename the Super Smash Charge badge from `SSmashChg` to `SSmashCharge` for consistency with the other charge badges.
  * Differentiate the two letters to Goompapa and the two letters to Koover by appending `1` and `2` to the respective item names.
  * If the plandomizer feature is used, the spoiler log will now display that data in a new `plandomizer` subcategory.
  * Renamed the item locations of the beach palm tree that drops two items to make differentiating between the one-time item and the replenishable item easier
    * `Jade Jungle Beach - In Palm Tree 6` to `Jade Jungle Beach - In Palm Tree 6 (one-off)`
    * `Jade Jungle Beach - In Palm Tree 6 2` to `Jade Jungle Beach - In Palm Tree 6 (replenish)`
* RAM locations docs
  * Fix typo in Player Data struct regarding True Max HP and FP
* README file:
  * Added note about needing to clone submodules as well from now on, due to the plandomizer being such a submodule
* Internally reworked how star pieces in non-randomized locations behave (hidden panels and letter rewards). The item pickup for those vanilla star pieces will now look slightly different, but they will still count as regular star pieces.
* Internally reworked how the berry key items work. This was necessary for making the plandomizer implementation of the berries less painful. Ideally, players should not notice any difference to before.

### Additional Technical Changelog (0.29.0)

* Yaml settings changes:
  * Added `RandomStartingStatsLevel`
    * `-1` = Off, `0` - `27` = Level to generate random starting stats for
    * If not turned off, generator will ignore `StartingMaxHP`, `StartingMaxFP`, and `StartingMaxBP`
  * `StarWayPowerStarsNeeded` now accepts `-1` as value (to roll randomly)
  * `StarBeamPowerStarsNeeded` now accepts `-1` as value (to roll randomly)
  * `StarHuntTotal` now accepts `-1` as value (to roll randomly)
  * Added `JumplessDaneTLetters` (bool)
  * Added `ToadTownSushieGlitchGearless` (bool)
  * Renamed `ToadTownSushieGlitch` to `ToadTownSushieGlitchOneGear`
  * Added `ToadTownSushieGlitchFullGear` (bool)
  * Added `JumplessSummitClimb` (bool)
  * Added `JumplessKoopaVillageBluePipe` (bool)
  * Added `ParakarrylessMtRuggedSeedClippy` (bool)
  * Added `RuinsPuzzleSolutionEarly` (bool)
  * Added `JumplessMegaRush` (bool)
  * Added `RaphSkipLakilester` (bool)
  * Added `BombettePuzzleSkip` (bool)
  * Added `WattlessDarkBasement` (bool)
  * Added `BasementSkipParakarry` (bool)
  * Added `BasementSkipLakilester` (bool)
  * Added `BasementSkipHammer` (bool)
  * Added `BowsersCastleHub1StairClip` (bool)
  * Added `FastFloodRoomKooperless` (bool)
  * Added `Cannonless` (bool)
* Changed Item IDs due to internal rework of berry items
  * Items removed:
    * `CakeProxy`, ID 0x25C (always unused)
    * `BlueBerryProxy1`, ID 0x25D (was now unused)
    * `BlueBerryProxy2`, ID 0x25E (was now unused)
    * `RedBerryProxy1`, ID 0x25F (was now unused)
    * `RedBerryProxy2`, ID 0x260 (was now unused)
    * `YellowBerryProxy1`, ID 0x261 (was now unused)
    * `YellowBerryProxy2`, ID 0x262 (was now unused)
    * `BubbleBerryProxy1`, ID 0x263 (was now unused)
    * `BubbleBerryProxy2`, ID 0x264 (was now unused)
  * This change shifts all items beyond item ID 0x264 down by 9 item IDs. The final item in the list is now `Bow` on item ID 0x291

## 0.28.1 (beta)

### Bug Fixes (0.28.1)

* Fix a bug that caused the chapter 3 boss battle's post-battle cutscene to sometimes not play out properly during `Boss Shuffle: On`, causing a softlock
* Fix a bug that caused the seed generator to fail at item placement while `Shuffle Partners` was set to `Shuffle among vanilla locations`, if other settings were very restrictive (like jumpless and hammerless start plus Goombario as only partner)
* Fix a bug that caused the seed generator to fail at item placement while `Seed Goal: Open Starway`, `Dungeon Entrance Shuffle: All + Bowser's Castle`, and `Partner Upgrades: Shuffle among super block locations` were all active
* Stop an uninteractible Bow-NPC from spawning when re-visiting Lady Bow's Room atop Boo's Mansion during `Cutscene Mode: Minimal`
* Fix a crash during the Crystal Palace fake Bombettes puzzle if re-entering the puzzle with a non-Bombette partner out. Fixed by resetting the bombable wall in this niche scenario

## 0.28.0 (beta)

### Feature Changes (0.28.0)

* `Boss Shuffle` option:
  * Allows shuffling which boss is encountered at the end of each dungeon area. The map and cutscenes are unaffected by this, but a different boss will load upon fading into the battle.
  * During `Vanilla Difficulty` and `Shuffle Chapter Difficulty` the shuffled boss inherits the difficulty of the chapter it is encountered in (instead of the difficulty assigned to its original chapter)
    * Example: General Guy gets shuffled as the boss within Koopa Bros. Fortress, then General Guy will have the same difficulty as the rest of chapter 1.
  * During `Boss Shuffle` Mario can run away from the seven dungeon boss battles on the very first turn. This will place Mario one room before the boss battle. After the first turn the option to run away will again be disabled.
  * Note: Whichever boss gets shuffled into chapter 3, thus replacing the Tubba's Heart battle, will not give any star points. This is to mimic the original Tubba's Heart battle not giving star points, either. If Tubba's Heart is shuffled into another chapter, then it will now grant star points. That battle is still won by lowering the Heart's HP to 5 or lower.
  * Note: For technical reasons bosses cannot appear in more than one chapter at the moment. So each of the seven main chapter bosses will always be encountered exactly once per seed.
* Changed `Progression On Rowf`:
  * Instead of marking either all or none of Rowf's item sets for holding progression, now allows choosing the maximum number of item sets which may hold progression.
  * Can be turned off, or set a value from 1-5
* Changed `Include Dojo`:
  * Instead of either having the four degree-cards and the diploma being vanilla, or having them all removed and placing other random items as dojo rewards, now allows choosing the maximum number of dojo battles that can hold random items
  * Can be turned off, or set a value from 1-5 (for Chan, Lee, and Master 1-3)
  * The battles that won't hold random items will still keep the original degree-cards / diploma items
  * Any value from 1-5 will count all 5 dojo item locations on the pause menu's map, even if some of them don't hold shuffled items
* Changed `Shuffle Partners` / `Partners In Default Locations`:
  This setting now has three different values:
  * Partners completely vanilla
  * (new) Partners shuffled among vanilla partner locations
  * Partners shuffled anywhere
* Changed `Star Way Spirits Required`:
  * If `Star Way Spirits Required` is set to random, then a number between 1 and 7 spirits will be chosen for opening Star Way (was: a number between 0 and 7)
* Changed `Star Beam Spirits Required`:
  * If `Star Beam Spirits Required` is set to random, then a number between 1 and 7 spirits will be chosen for receiving the Star Beam (was: a number between 0 and 7)
* Changed `Shuffle Dungeon Entrances`:
  This setting now has three different values:
  * No dungeon shuffle
  * Shuffle spirit dungeons
  * (new) Shuffle spirit dungeons, and include Bowser's Castle  
    (Note: For inclusion of Bowser's Castle, the `Star Way Spirits Needed` setting has to be set to require fewer than 7 star spirits.)
* Changed `Hammerless Start` and `Jumpless Start` item placement logic:
  * Now has a vastly increased chance of placing the first gear item later into the seed progression.
  * It happened quite often during these seeds that the first hammer/boots upgrade (respectively) could be found super early, somewhat defeating the point of these settings. This change tries to combat this. While it will still happen that you find these gear upgrades right away, the chances of that happening should be lower now.
  * Does not affect seeds that are made with neither `Hammerless Start` nor `Jumpless Start` settings.

### Logic changes (0.28.0)

* Reaching the top of Shooting Star Summit now expects having the Boots (formerly expected Boots or Parakarry)
* Fixed logic always expecting Parakarry or Boots for reaching the vanilla location of the Odd Key item
* Fixed logic not requiring being able to climb ledges in Gusty Gulch, while there are very obvious ledges preventing Mario from continuing (only affected glitched logic seeds)

### Quality of Life (0.28.0)

* Adjusted the Pulse Stone key item
  * Beeping now turns off permanently after using tricks to enter the Dry Dry Ruins entrance loading zone without raising the ruins

### Miscellaneous (0.28.0)

* Spoiler log
  * Moved `Ruined Castle Grounds - Muss T. Letter Reward` from the `Peachs Castle Grounds` area to the `Toad Town` area
  * Moved `Hijacked Castle Entrance - Hidden Block` from the `Peachs Castle Grounds` area to the `Peachs Castle` area
  * The `Peachs Castle Grounds` area is a bit weirdly laid out, so these changes were made to make finding these two locations within the spoiler log easier

### Additional Technical Changelog (0.28.0)

* Yaml settings changes:
  * Changed `ProgressionOnRowf`
    * Value data type is now `int` (was `boolean`)
    * `0` = Off, `1`-`5`: 1-5 item sets may hold progression
  * Changed `IncludeDojo`
    * Value data type is now `int` (was `boolean`)
    * `0` = Off, `1`-`5`: 1-5 dojo battles may hold progression
  * `PartnersInDefaultLocations`:
    * Renamed to `PartnerShuffle`
    * Changed: Value data type is now `int` (was `boolean`)
    * `0` = vanilla, `1` = shuffled among vanilla locations, `2` = anywhere
  * Changed `ShuffleDungeonEntrances`
    * Changed: Value data type is now `int` (was `boolean`)
    * `0` = Off, `1` = spirit dungeons, `2` = spirit dungeons + Bowser's Castle
  * Added `BossShuffleMode`
    * `0` = Off, `1` = Shuffle Chapter Bosses
* Misc. generator changes:
  * Fixed broken Python requirements file
  * Added Dockerfile and devcontainer configuration
    * (not sure if the Docker container is set up 100% cleanly, but the devcontainer works)

## 0.27.1a (beta)

### Bug Fixes (0.27.1a)

* Fix a bug that caused the `Star Beam` item to be treated as non-progression, causing issues while generating seeds that had `Limited Chapter Logic` and `Shuffle Star Beam` turned on.

## 0.27.1 (beta)

### Bug Fixes (0.27.1)

* Fix a bug with `Require Specific Spirits` and `Goal: Open Star Way`, where the holograms of the spirits required to rescue don't show up on Shooting Star Summit.

## 0.27.0 (beta)

### Feature Changes (0.27.0)

* Removed `Star Hunt` option and reworked Power Stars:
  * `Star Way Spirits Needed` and `Star Way Power Stars Needed` options now determine how many spirits and power stars are needed to open Star Way. Any combination is valid, like 7 spirits & 0 power stars, 0 spirits & 50 power stars, 4 spirits & 30 power stars etc.
* `Seed Goal` option
  * Select between "Defeat Bowser" and "Open Star Way"
  * "Open Star Way" is basically the old `Star Hunt Ends Game` setting, but can now be used while also requiring star spirits to open the teleporter.
* `Shuffle Star Beam` option
  * Turns the Star Beam into an item and shuffles it into another location
  * Picking up the Star Beam item unlocks the Star Beam ability in battle, but does not increase the star power gauge or unlock any other star power ability
  * The Star Beam cutscene in Star Haven instead offers a different item
  * Hallway Bowser gets dialogue hinting at the location of the Star Beam, if Mario reaches him without having found the Star Beam. This dialogue plays even during `Cutscene Mode: Minimal`
* `Star Beam Spirits Needed` and `Star Beam Power Stars Needed` options
  * Allows setting requirements for getting the item in the Star Beam item location in Star Haven
  * Can be combined with the new `Shuffle Star Beam` option
(Note: The `Require Specific Spirits` and `Limit Chapter Logic` options only affect opening Star Way, not acquiring the Star Beam)
* New sign posts on Shooting Star Summit and in Star Sanctuary will now spell out the requirements. If the unlock is free, that is it needs 0 Star Spirits and 0 Power Stars, the respective sign post will instead not spawn at all
* Reworked the pause menu Power Stars counter
  * This counter is hidden if there are no Power Stars placed in the seed
  * The icon in front of the "\<current> / \<max>" display now shows which unlock is coming up next:
  Either a Shooting Star icon for "Star Way", the Star Beam icon for "Star Beam", and if both of those are already unlocked, a Power Star icon
  * The max value in the "\<current> / \<max>" display now also refers to the unlock that's coming up next
  * Example: Mario needs 10 Power Stars to open Star Way, 20 to get the Star Beam, and 35 total are placed in the seed. Then the Power Star counter will show:
    * "[Shooting Star icon] \<current> / 10", if Mario has less than 10 Power Stars,
    * "[Star Beam icon] \<current> / 20", if Mario has 10 or more, but fewer than 20 Power Stars,
    * "[Power Star icon] \<current> / 35", if Mario has 20 or more Power Stars

### Logic changes (0.27.0)

* While `Keyitems Outside Dungeon` (aka Keysanity) is turned off, the FP Plus chest in the Koopa Bros. Fortress area is no longer a valid location for Koopa Fortress Keys
* Now expects Watt for traversing the dark caves in Bowser's Castle
* Now expects having enough star spirits and power stars to both open Star Way and get the Star Beam, to get past chapter 8 Jr. Troopa and Hallway Bowser (only relevant in prep for entrance rando)

### Tricks & Glitches (0.27.0)

* New options
  * "Volcano Sushie Glitch w/ Goombario save block storage"
  * "Chapter 7 bridge w/ SuperBoots"
  * "Prologue Repel Gel early" (Parakarry-only and Lakilester-only versions)
  * "Sewers Metal Block Room Super Block w/ clippy"
  * "Kooper Puzzle Skip"
  * "Ruins Stones Skip"
  * "Wattless chapter 4 dark room"
  * "Clippy Green Station Multicoin Block"
* Removed options
  * Flarakarry (Bombette) (due to it possibly causing a softlock)

### Bug Fixes (0.27.0)

* Fix a bug that could rarely cause unintended item prices for shop items in Dry Dry Outpost if `Randomize Puzzles` and `Include Shops` were turned on
* Lower logical star piece requirements for some of Merlow's trades (the original calculations were off)
* Fix broken seed generation if both `Mystery Only` and `Random Puzzles` are turned on
* Homeward Shroom now properly reloads the music if the munching SFX is skipped by unpausing manually
* Fix entrance rando issues with having Watt/Sushie/Lakilester active through certain loading zones
* Fix counting star spirits twice during same-seed multiplayer
* Fix Russ T. giving the toy box colored boxes code w/o having handed in the Dictionary first
* (console only) Fix vanilla freeze when trying to Tidal Wave during phase 2 of the Lava Piranha battle if there are Petit Piranhas alive
* Fix Kent C. Koopa breaking the coin cap when handing back the 50 coins when defeated after paying him
* Fix frozen camera during Kooper's Shell turn-in cutscene

### Miscellaneous (0.27.0)

* Renamed some locations in the spoiler log for clarity

### Additional Technical Changelog (0.27.0)

* Added ModFlag `1100` which gets set to True once the current seed goal is reached
* Split up chapter 8 progress byte into flags
* Adding the Star Beam item on item id `0x27F` shifts up all item ids above that by one
* With the Star Beam item a new item type `STARPOWER` is added and referenced within the seed generator
* New DBKey `StarBeamArea`: Has to be set by the generator to the area id of the area the Star Beam gets shuffled to. This is referenced by Hallway Bowser's hint dialogue. If an invalid area id is provided, Bowser will state that the Star Beam can be found in Rogueport.
* Generator will throw a new `ItemPoolTooSmallError` if the settings make it remove more items from the trash item pool (to make place for Power Stars, Pouches etc.) than there are items in the trash item pool to begin with
* To have the generator pick a random number of Magical Seeds to open the Flower Gate, now set `MagicalSeedsRequired` to `-1` (was: set `MagicalSeedsRequired` to `5`)
* Yaml settings changes:
  * Goal Settings
    * Removed `StarHunt`
    * Renamed `StarHuntRequired` to `StarWayPowerStarsNeeded`
    * Removed `StarHuntEndsGame`
    * Added `SeedGoal`
    * Added `StarBeamSpiritsNeeded`
    * Added `StarBeamPowerStarsNeeded`
    * Added `ShuffleStarBeam`
  * Tricks & Glitches
    * Removed `ParakarrylessFlarakarryBombette`
    * Added `ClippySewersUpgradeBlock`
    * Added `Chapter7BridgeWithSuperBoots`
    * Added `RuinsStoneSkip`
    * Added `ClippyGreenStationCoinBlock`
    * Added `WattlessDarkRoom`
    * Added `VolcanoSushieGlitchGoombario`
    * Added `KooperPuzzleSkip`
* Changed logical Star Piece requirements for Merlow rewards:
  * Reward 2 (20sp): `23` is now `22`
  * Reward 4 (40sp): `47` is now `45`
  * Reward 6 (60sp): `68` is now `67`
* Spoiler log location renaming:
  * `Plaza District - Merlon House Stomping` is now `Plaza District - Merlon House Stomp x3`
  * `Plaza District - Rowf's Calculator Reward` is now `Plaza District - Rowf Calculator Reward`
  * `Koopa Village 2 - Koopa Koot Reward 1` is now `Koopa Village 2 - Favor 1 Reward (KoopaLegends)`
  * `Koopa Village 2 - Koopa Koot Reward 2` is now `Koopa Village 2 - Favor 2 Reward 1 (SleepySheep)`
  * `Koopa Village 2 - Koopa Koot Silver Credit` is now `Koopa Village 2 - Favor 2 Reward 2 (SleepySheep)`
  * `Koopa Village 2 - Koopa Koot Reward 3` is now `Koopa Village 2 - Favor 3 Reward (Tape)`
  * `Koopa Village 2 - Koopa Koot Reward 4` is now `Koopa Village 2 - Favor 4 Reward (KoopaTea)`
  * `Koopa Village 2 - Koopa Koot Reward 5` is now `Koopa Village 2 - Favor 5 Reward (LuigiAutograph)`
  * `Koopa Village 2 - Koopa Koot Reward 6` is now `Koopa Village 2 - Favor 6 Reward (Wallet)`
  * `Koopa Village 2 - Koopa Koot Reward 7` is now `Koopa Village 2 - Favor 7 Reward (TastyTonic)`
  * `Koopa Village 2 - Koopa Koot Reward 8` is now `Koopa Village 2 - Favor 8 Reward (MerluvleeAutograph)`
  * `Koopa Village 2 - Koopa Koot Reward 9` is now `Koopa Village 2 - Favor 9 Reward (News)`
  * `Koopa Village 2 - Koopa Koot Reward 10` is now `Koopa Village 2 - Favor 10 Reward 1 (LifeShroom)`
  * `Koopa Village 2 - Koopa Koot Gold Credit` is now `Koopa Village 2 - Favor 10 Reward 2 (LifeShroom)`
  * `Koopa Village 2 - Koopa Koot Reward 11` is now `Koopa Village 2 - Favor 11 Reward (NuttyCake)`
  * `Koopa Village 2 - Koopa Koot Reward 12` is now `Koopa Village 2 - Favor 12 Reward (Bob-ombs)`
  * `Koopa Village 2 - Koopa Koot Reward 13` is now `Koopa Village 2 - Favor 13 Reward (OldPhoto)`
  * `Koopa Village 2 - Koopa Koot Reward 14` is now `Koopa Village 2 - Favor 14 Reward (Koopasta)`
  * `Koopa Village 2 - Koopa Koot Reward 15` is now `Koopa Village 2 - Favor 15 Reward (Glasses)`
  * `Koopa Village 2 - Koopa Koot Reward 16` is now `Koopa Village 2 - Favor 16 Reward (Lime)`
  * `Koopa Village 2 - Koopa Koot Reward 17` is now `Koopa Village 2 - Favor 17 Reward (KookyCookie)`
  * `Koopa Village 2 - Koopa Koot Reward 18` is now `Koopa Village 2 - Favor 18 Reward (Package)`
  * `Koopa Village 2 - Koopa Koot Reward 19` is now `Koopa Village 2 - Favor 19 Reward (Coconut)`
  * `Koopa Village 2 - Koopa Koot Reward 20` is now `Koopa Village 2 - Favor 20 Reward (RedJar)`
  * `Outpost 1 - Store Legend` is now `Outpost 1 - Store Legend (RedJar Code)`
  * `N1W3 Special Block - Hit Block` is now `N1W3 Special Block - Hit Block x1`
  * `N1W3 Special Block - Hit Block Plenty` is now `N1W3 Special Block - Hit Block x5`
  * `N1W3 Special Block - Hit Block Very Much` is now `N1W3 Special Block - Hit Block x10`
  * `Record Room - Beat Boo Game` is now `Record Room - Boo Ring Game`
  * `(East) Old Well - Well Reward` is now `(East) Old Well - Well BlueBerry Reward`
  * `Shiver City Center - Toad House Breakfast` is now `Shiver City Center - Sleep At Toad House`
