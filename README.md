# QuickConsole Mods

This repository contains custom command for in-game console for American McGee Presents: Scrapland

## Installation

 - Extract `quickconsole.py` from `data.packed` file to `Bin` folder. You can use [Scrap-Packed-Explorer](https://github.com/ReScrap/Scrap-Packed-Explorer) utitliy
 - Open `quickconsole.py` with notepad and put this line of code to the botton of `quickconsole.py`. Make sure you don't have any spaces at the begining of the line

```python
from QuickConsoleMods import *
```

 - Copy folder `QuickConsoleMods` to `Bin` folder

## How to use QuickConsole

Once ingame and able to move with character

CTRL + ~ (Above TAB) to open up QuickConsole.py - A text console should slide out from the top of the screen

## Mods

Here is list of mods that this repo contains and how to use them

### MaxGPU

Adds command for setting graphic setting to higher values that game allowes

**Usage:**

 - `/GPU.maxgpu 0` - (revert all) Fully revert all to original game values, also restoring testing values to disabled
 - `/GPU.maxgpu 1` - (revert default) Revert to default without removing testing
 - `/GPU.maxgpu 2` - (Improve graphics) Improved graphics
 - `/GPU.maxgpu 3` - (Improve anims) Animation interpolation doubled
 - `/GPU.maxgpu 4` - Enable multiple testing variables

Note: `/GPU.maxgpu 4` enables multiple testing/debug engine variables, which can only be disabled with `/maxgpu 0`

The idea is to go to some graphically interesting location and then do:

 - `/GPU.maxgpu 3` - max graphics variable upgrades
 - `/GPU.maxgpu 1` - default graphic variables

So it can be easily toggled on/off, with mode 0 and 4 being for disable all/enable testing

### EntityUtils

Enables taking control over other Entities in Scrapland.
For example usage see https://www.youtube.com/watch?v=0d1OkaUR5YE

List of commands:

 - `/EntityUtils.unfree` - undoes the `/free` command
 - `/EntityUtils.imyou` - takes over control of the entity that you look at
 - `/EntityUtils.imme` - return control to Di-Tritus
 - `/EntityUtils.makeFriendOrEnemy <entity name> <list>`  Finds the entity with the specified name and adds it to friends/enemies. If <list> is not specified, the entity will be added to the friends list
 - `/EntityUtils.youFriend` - makes the entity that you look at a friend
 - `/EntityUtils.yourName` - prints the name of the entity that you look at
 - `/EntityUtils.createFriendOrEnemy <name> <ship type> <engine type> <AI profile> <list>` - spawns an entity with the specified parameters

Check out some other Scrapland tools and documentation at [https://github.com/ReScrap](https://github.com/ReScrap)

Join to our [Discord server](discord.gg/eBw2Pzpu4w)
