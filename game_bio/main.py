# 14.09.2022, TheBiochemic
#
# this is the main file
# here is all the stuff that is responsible for the functionality of the game

############################################################################
# imports
############################################################################
import os

############################################################################
# internal variables (denoted by the two underscores)
############################################################################

__terminal_width = os.get_terminal_size().columns

############################################################################
# constants
############################################################################

# these are used with print_fancy(...); constants in general ar written in caps only.
INSET = " " * 8
INSET_1_3 = " " * int(__terminal_width / 3) # creates an inset, that is one third of the screen
INSET_1_4 = " " * int(__terminal_width / 4)
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_BLUE = "\033[36m"
COLOR_RESET = "\033[0m"
SEPARATOR = INSET + "-" * (__terminal_width - len(INSET)*2) + INSET # multiplying a string with a value just repeats it
NEWLINE = "\n"
INPUT_INDICATOR = ">> "

############################################################################
# variables
############################################################################

############################################################################
# helper functions
############################################################################

# this function basically just prints stuff into the console with some better look.
# modifier is one of the constants from this file, that change the behaviour of the output
# message is an optional message, that shall be outputted. the value behind 
# 	the = is the default value
def fancy_out(modifier, message = ""):
	print(modifier + message + COLOR_RESET)

# same as fancy_out, but ontop of that it also centers the text by the with of the terminal
# it only works, when the terminal is bigger than the message
def center_out(modifier, message = ""):
	space_needed = (__terminal_width - len(message))  / 2
	space_printed = " " * int(space_needed)
	fancy_out(modifier + space_printed, message)

# this basically just applies the modifiers in front of the input, before asking
# basically just sugar coating input(...)
def fancy_in(modifier):
	print(modifier, end ="")
	return str(input()).lower().strip()

# simply just clears the terminal, works on windows, linux and osx.
# usually you should avoid using the system(...) command, but since
# it's a learning project, i guess we dont need to look closely to
# secure the software here
def clear():
	os.system('cls||clear')

def exit_game():
	print("\n")
	quit()

# this function drwas a bar of some sort
# modifiers work the same as everywhere else and change the behaviour of the outbut
# the value is the actual value of the bar
# the max value is there to compute, how much the bar is filled
# the width is the width of the bar, it is by default just set on 1/4 of the terminal width
def bar(modifier, value, max_value, width = int(__terminal_width/4)):
	corrected_width = width - 2 # correct width for the square brackets
	ratio = float(value) / float(max_value) # calculate the fill percentate of the bar
	ratio_expanded = int(corrected_width * ratio) # calculate the amount, that is filled

	# finally build the string and draw the bar
	bar_string = "[" + "#" * ratio_expanded + " " * (corrected_width - ratio_expanded) + "] "
	print(modifier + bar_string + str(value) + "/" + str(max_value) + COLOR_RESET)

# this function draws all available options, using a modifier, and attaching an end
# the center will be used between the key and the text
def options(modifier, options, end = "\n", center = " - "):
	#iterating over a dictionary is quite simple, just do
	for key, value in options.items():
		print(modifier + "[" + key + "]" + center + value[0], end = end)
		if not end == "\n":
			modifier = ""

# this function simply draws the title section with custom text
def title(title_text, newlines = 4):
	clear()
	fancy_out(NEWLINE * newlines, SEPARATOR)
	center_out(COLOR_BLUE, title_text)
	fancy_out(SEPARATOR)

############################################################################
# main functions
############################################################################

# this is the entry point of the game, in here basically all other functions are
# the options variable is basically just a dict containing string indices for
# (string, function) pairs
def menu(available_options):

	option = ""

	while True:
		title("Willkommen zu game_bio.")
		options(INSET_1_3, available_options)

		if len(option) > 0:
			fancy_out(NEWLINE + COLOR_RED + INSET_1_3, "Ungültige Option!")
			fancy_out(COLOR_BLUE + INSET_1_3, "Wähle eine Option:")
		else:
			fancy_out(NEWLINE * 2 + COLOR_BLUE + INSET_1_3, "Wähle eine Option:")

		option = fancy_in(INSET_1_3 + INPUT_INDICATOR)
		if option in available_options:	# checks if you can find the option string as an option in the dict
			available_options[option][1]()
			option = ""