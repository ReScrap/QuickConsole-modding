# QuickConsoleGPU-Graphic-Commands


This repository contains the latest versions of:

_QuickConsole.py_ (Extracted + Updated by Earthnuker) - Main game scripting console with Earthnuker's additons

_Scrapland_QuickConsole_plus.py_ (Created by @romibi) - Additional, very useful and interesting scripts.

_QuickConsole_GPU.py_ (Created by @olokos) - adds the /maxgpu command that allows toggling many engine variables with one command ingame.


This repo includes an addition to quickconsole.py - **QuickConsole_GPU.py** that allows to change multiple Scrapland Remastered variables with one short command, only changing the last number at the end.


**Usage:**

Once ingame and able to move with character

CTRL + ~ (Above TAB) to open up QuickConsole.py - A text console should slide out from the top of the screen



then:

`/maxgpu 0` - (revert all) Fully revert all to original game values, also restoring testing values to disabled

`/maxgpu 1` - (revert default) Revert to default without removing testing

`/maxgpu 2` - (Improve graphics) Improved graphics

`/maxgpu 3` - (Improve anims) Animation interpolation doubled

`/maxgpu 4` - Enable multiple testing variables


I went through the list of all engine variables that I considered useful and interesting to change to improve graphics, but I can't see almost any difference.
The only moment I saw a difference was at Rusty's when looking at distant floor, the furthest away ground looks better, but it's very hard to notice.


`/maxgpu 4` enables multiple testing/debug engine variables, which can only be disabled with `/maxgpu 0`

The idea is to go to some graphically interesting location and then do:

`/maxgpu 3` - max graphics variable upgrades

`/maxgpu 1` - default graphic variables


so it can be easily toggled on/off, with mode 0 and 4 being for disable all/enable testing


`QuickConsole_GPU.py` is meant to be a short script to allow for easy experimentation, so that everybody can open it in notepad, replace the variables with different ones or maybe find some different useful variables that arent already there, that might improve graphics ingame. Then testing it with as little user input required as possible.


