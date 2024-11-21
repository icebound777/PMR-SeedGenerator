# Changelog

## 0.28.1 (beta)

### Bug Fixes

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
