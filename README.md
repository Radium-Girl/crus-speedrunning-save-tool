# crus-speedrunning-save-tool
A super simple tkinter gui that's only purpose is to make handing Cruelty Squad save files that bit less laborious between speedruns.

"DELETE SAVE" does exactly what's on the cover, it'll delete specifially your savegame.save and stocks.save, leaving everything else like your settings alone. (This will not warn you, your savegame/stocks.save files will be immediately deleted)
"CREATE PRACTICE SAVE" will create a new savegame.save file with everything unlocked - that includes all weapons, levels, and augments. (This will warn you via popup menu if you wish to overrite your save data)
The folder icon will simply open up your save game directory for if you wish to do anything manually there, like editing specific parameters in your savegame.save file. 

This tool does not do anything that you yourself can't do manually, it just makes it that slight bit quicker for when you're doing many runs back-to-back. 
Before you use this tool be sure that you're okay with potentially losing your save data.
This tool does not interact with the game it's self in any way, just the files inside the Cruelty Squad save directory.

In this repository you will find the .pyw file it's self and an executable for people who don't have python and the required libraries installed to run the python file - most people can just use the .exe in the "dist" folder.
