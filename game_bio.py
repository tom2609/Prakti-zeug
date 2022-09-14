# 14.09.2022, TheBiochemic

############################################################################
# Imports
############################################################################

# this import finds the module/folder and imports the main.py from there.
# i also usually override the default name into something, where i am sure
# it has then as the name, in this case it's main and game respectively

import game_bio.main as main # the same as ./game_bio/main.py
import game_bio.game as game # the same as ./game_bio/game.py

############################################################################
# entry point
############################################################################

# This is the entry point of the game, it is basically just there to make it
# easier to launch from the terminal. You just need to type in
# python ./game_bio.py or python3 ./game_bio.py (or with \ on windows)

# this calls a function from a different file, namely the one i imported as
# main in the imports above
main.menu({
	"n": ("Neues Spiel", game.start),
	"q": ("Spiel beenden", main.exit_game)
	}) # the indentation is sometimes a little weird, when splitting stuff
	   # across multiple lines, just keep that in mind

# you might wonder, why there is no main function; well, it's because we
# call it directly above with main.menu(...)