# 14.09.2022, TheBiochemic

############################################################################
# imports
############################################################################

import time
import random

import game_bio.main as main

############################################################################
# internal functions
############################################################################

# this function draws the status of all entities in the session,
# it also needs the game_state so we can modify it
def __status(game_state):
	main.fancy_out(main.INSET_1_4, "Du:")
	main.bar(main.INSET_1_4 + main.COLOR_RED, 
		game_state["entities"]["player"]["health"],
		game_state["entities"]["player"]["health_max"])
	main.bar(main.INSET_1_4 + main.COLOR_BLUE, 
		game_state["entities"]["player"]["mana"],
		game_state["entities"]["player"]["mana_max"])
	main.fancy_out(main.NEWLINE)
	main.fancy_out(main.INSET_1_4 * 2, "Gegner:")
	main.bar(main.INSET_1_4 * 2 + main.COLOR_RED, 
		game_state["entities"]["enemy"]["health"],
		game_state["entities"]["enemy"]["health_max"])
	main.bar(main.INSET_1_4 * 2 + main.COLOR_BLUE, 
		game_state["entities"]["enemy"]["mana"],
		game_state["entities"]["enemy"]["mana_max"])
	pass

# thsi function basically just draws the whole top of the screen
def __redraw_header(game_state):
	main.title("Runde " + str(game_state["round"]), 2)
	__status(game_state)
	main.fancy_out(main.SEPARATOR + main.NEWLINE)

# in here the player logic is getting performed, we need the game_state here
# too. it is for resetting some player related things
def __player_logic(game_state):
	game_state["entities"]["player"]["block"] = 0

# in here the enemies logic is getting performed, we need the game_state here
# too
def __enemy_logic(game_state):
	enemy_ref = game_state["entities"]["enemy"]
	player_ref = game_state["entities"]["player"]

	enemy_ref["block"] = 0

	# i gave the enemy a weight system, that basically just adjusts weights
	# of the actions the enemy can do. the more weight a certain action has,
	# the more likely it is, that the enemy will choose this action
	weights = {
		"attack": 3,
		"heal": 3,
		"block": 3,
		"charge": 1
	}

	# defines all the actions, the enemy can do
	actions = {
		"attack": action_attack,
		"heal": action_heal,
		"block": action_block,
		"charge": action_special_attack
	}

	# if low on health, make enemy more likely to heal and block
	if float(enemy_ref["health"]) / float(enemy_ref["health_max"]) < 0.5:
		weights["heal"] = weights["heal"] + 6
		weights["block"] = weights["block"] + 3

	# if the player is low on health, make the enemy more likely to attack
	if float(player_ref["health"]) / float(player_ref["health_max"]) < 0.5:
		weights["attack"] = weights["attack"] + 6

	# if high on health, make enemy more likely to charge
	if float(enemy_ref["health"]) / float(enemy_ref["health_max"]) > 0.75:
		weights["charge"] = weights["charge"] + 4

	# if almost done charging, make enemy more likely to charge
	if float(enemy_ref["mana"]) / float(enemy_ref["mana_max"]) > 0.75:
		weights["charge"] = weights["charge"] + 4

	# if player is done charging, make enemy more likely to block
	if float(player_ref["mana"]) / float(player_ref["mana_max"]) > 0.8:
		weights["block"] = weights["block"] + 8

	# if done charging, let the enemy drop the charging action alltogether
	if enemy_ref["mana"] == enemy_ref["mana_max"]:
		weights["charge"] = 0

	# if max health, let the enemy drop the ehaling action
	if enemy_ref["health"] == enemy_ref["health_max"]:
		weights["heal"] = 0

	# now calculates the weight sum, and executes the randomly chosen action
	weights_sum = 0
	for key, value in weights.items():
		weights_sum = weights_sum + value

	random_action = random.randrange(0, weights_sum)
	action_weight = 0

	for key, value in weights.items():
		action_weight = action_weight + value
		if random_action < action_weight:
			actions[key]("enemy", game_state)
			return


# win and loose conditions are tested here, also other factors, that are
# related to the game itself can go in here
def __game_logic(game_state):
	game_state["round"] = game_state["round"] + 1

	enemy_health = game_state["entities"]["enemy"]["health"]
	player_health = game_state["entities"]["player"]["health"]

	# if both are dead
	if player_health == 0 and enemy_health == 0:
		main.title("Spielergebniss", 4)
		main.fancy_out(main.NEWLINE)
		main.center_out("GLEICHSTAND")
		main.fancy_out(main.NEWLINE)
		main.center_out("Du und der Gegner sind beide tot!")
		game_state["is_running"] = False
		time.sleep(4)
		return

	# if the player is dead
	if player_health == 0:
		main.title("Spielergebniss", 4)
		main.fancy_out(main.NEWLINE)
		main.center_out(main.COLOR_RED, "DU HAST VERLOREN")
		main.fancy_out(main.NEWLINE)
		main.center_out(main.COLOR_RED, "Du wurdest vom Gegner getötet.")
		game_state["is_running"] = False
		time.sleep(4)
		return

	# if the player is dead
	if enemy_health == 0:
		main.title("Spielergebniss", 4)
		main.fancy_out(main.NEWLINE)
		main.center_out(main.COLOR_GREEN, "ERFOLG")
		main.fancy_out(main.NEWLINE)
		main.center_out(main.COLOR_GREEN, "Du hast den Gegner erfolgreich besiegt!")
		game_state["is_running"] = False
		time.sleep(4)
		return


############################################################################
# helper functions
############################################################################

# this function gets executed, if anyone makes an attack order
# the source is just the name of who's attacking
# the game state is needed to advance the game
def action_attack(source, game_state):
	if source == "player":
		# if the player is executing this function
		damage = random.randrange(1,10)

		# if the players special is fully charged
		if game_state["entities"]["player"]["mana"] == game_state["entities"]["player"]["mana_max"]:
			main.fancy_out(main.INSET + main.COLOR_GREEN, "Du holst einen kräftigen Schlag aus.")
			damage = random.randrange(15,20)
			game_state["entities"]["player"]["mana"] = 0
		else:
			main.fancy_out(main.INSET + main.COLOR_GREEN, "Du greifst den Gegner an.")

		time.sleep(1)
		damage_with_block = max(1, damage - game_state["entities"]["enemy"]["block"]) # subtracts the shield block from the damage

		# random.randrange(15,20)

		# if the enemy was blocking
		if game_state["entities"]["enemy"]["block"] > 0:
			main.fancy_out(main.INSET + main.COLOR_RED, "Der Angriff prallt vom Schild des Gegners ab!")

		main.fancy_out(main.INSET + main.COLOR_GREEN, "Gegner nimmt " + str(damage_with_block) + " Schaden.")
		game_state["entities"]["enemy"]["health"] = max(0, game_state["entities"]["enemy"]["health"] - damage)
	else:
		# if the enemy is executing this function
		damage = random.randrange(1,10)

		# if the enemies special is fully charged
		if game_state["entities"]["enemy"]["mana"] == game_state["entities"]["enemy"]["mana_max"]:
			main.fancy_out(main.INSET + main.COLOR_RED, "Der Gegner holt einen kräftigen Schlag aus.")
			damage = random.randrange(15,20)
			game_state["entities"]["enemy"]["mana"] = 0
		else:
			main.fancy_out(main.INSET + main.COLOR_RED, "Der Gegner greift dich an!")

		time.sleep(1)
		damage_with_block = max(1, damage - game_state["entities"]["player"]["block"]) # subtracts the shield block from the damage

		# if the player was blocking
		if game_state["entities"]["enemy"]["block"] > 0:
			main.fancy_out(main.INSET + main.COLOR_GREEN, "Der Angriff prallt vom Schild ab!")

		main.fancy_out(main.INSET + main.COLOR_RED, "Du nimmst " + str(damage_with_block) + " Schaden.")
		game_state["entities"]["player"]["health"] = max(0, game_state["entities"]["player"]["health"] - damage)

# this function gets executes, as soon as someone want to heal themselves
# the source is just the name of who's healing themselves
# the game state is needed to advance the game
def action_heal(source, game_state):
	if source == "player":
		# if the player is executing this function
		main.fancy_out(main.INSET + main.COLOR_GREEN, "Du versuchst, dich zu heilen.")
		time.sleep(1)
		heal = random.randrange(1,7)
		new_health = min(game_state["entities"]["player"]["health_max"], game_state["entities"]["player"]["health"] + heal)

		main.fancy_out(main.INSET + main.COLOR_GREEN, "Du heilst dich um " + str(heal) + " Lebenspunkte.")
		game_state["entities"]["player"]["health"] = new_health
	else:
		# if the enemy is executing this function
		main.fancy_out(main.INSET + main.COLOR_RED, "Der Gegner versuch, sich zu heilen.")
		time.sleep(1)
		heal = random.randrange(1,7)
		new_health = min(game_state["entities"]["enemy"]["health_max"], game_state["entities"]["enemy"]["health"] + heal)
		
		main.fancy_out(main.INSET + main.COLOR_RED, "Der Gegner heilt sich um " + str(heal) + " Lebenspunkte.")
		game_state["entities"]["enemy"]["health"] = new_health

# this function gets executed everytime, someone blocks
# the source is just the name of the blocker
# the game state is needed to advance the game
def action_block(source, game_state):
	if source == "player":
		# if the player is executing this function
		main.fancy_out(main.INSET + main.COLOR_GREEN, "Du hebst den Schild.")
		game_state["entities"]["player"]["block"] = random.randrange(1,10)
	else:
		# if the enemy is executing this function
		main.fancy_out(main.INSET + main.COLOR_RED, "Der Gegner hebt den Schild.")
		game_state["entities"]["enemy"]["block"] = random.randrange(1,10)

# this function gets executed everytime, when someone is charging their special attack
# the source is just the name of the charger
# the game state is needed to advance the game
def action_special_attack(source, game_state):
	if source == "player":
		# if the player is executing this function
		main.fancy_out(main.INSET + main.COLOR_GREEN, "Bu bereitest dich für einen starken Angriff vor.")
		new_mana = game_state["entities"]["player"]["mana"] + random.randrange(1,10)
		capped_mana = min(new_mana, game_state["entities"]["player"]["mana_max"])

		if capped_mana == game_state["entities"]["player"]["mana_max"]:
			time.sleep(1)
			main.fancy_out(main.INSET + main.COLOR_GREEN, "Dein nächster Angriff wird deutlich stärker sein.")

		game_state["entities"]["player"]["mana"] = capped_mana
	else:
		# if the enemy is executing this function
		main.fancy_out(main.INSET + main.COLOR_RED, "Der Gegner bereitet sich für einen starken Angriff vor.")
		new_mana = game_state["entities"]["enemy"]["mana"] + random.randrange(1,10)
		capped_mana = min(new_mana, game_state["entities"]["enemy"]["mana_max"])

		if capped_mana == game_state["entities"]["enemy"]["mana_max"]:
			time.sleep(1)
			main.fancy_out(main.INSET + main.COLOR_RED, "Der nächste Angriff des Gegner wird deutlich stärker sein.")

		game_state["entities"]["enemy"]["mana"] = capped_mana


############################################################################
# main functions
############################################################################

# this function just rund the main loop of the game
def start():

	# first we define the gameŝ state. In theory all of that we could do with classes
	# and whatnot, but because there is no reason to over-engineer a working concept
	# we dont do it here. n the end you still can, if you feel like adding new features ;)
	game_state = {
		"is_running": True,
		"round": 1,
		"entities": {
			"player": {
				"health": 50,
				"health_max": 50,
				"mana": 0,
				"mana_max": 20,
				"block": 0
			},
			"enemy": {
				"health": 50,
				"health_max": 50,
				"mana": 0,
				"mana_max": 20,
				"block": 0
			}
		}
	}

	# these are the players options, they are used to determine the possible inputs
	available_options = {
		"a": ("ngreifen", action_attack),
		"b": ("locken", action_block),
		"h": ("eilen", action_heal),
		"v": ("orbereiten", action_special_attack)
	}

	# this is the outer loop, it is running, as long as the game is running
	while game_state["is_running"]:

		# some vars for the inner loop
		successful_option = False
		wrong_input = False

		__player_logic(game_state)

		# the inner loop asks the player for input, until a valid one is given
		while not successful_option:

			__redraw_header(game_state)
			main.options(main.INSET, available_options, ", ", "")

			if wrong_input:
				main.fancy_out(main.NEWLINE + main.COLOR_RED + main.INSET_1_3, "Ungültige Option!")
				main.fancy_out(main.COLOR_BLUE + main.INSET_1_3, "Wähle eine Option:")
			else:
				main.fancy_out(main.NEWLINE * 2 + main.COLOR_BLUE + main.INSET_1_3, "Wähle eine Option:")


			option = main.fancy_in(main.INSET_1_3 + main.INPUT_INDICATOR)


			if option in available_options:
				__redraw_header(game_state)
				successful_option = True
				available_options[option][1]("player", game_state)
				time.sleep(1)
			else: 
				wrong_input = True

		__enemy_logic(game_state)
		time.sleep(1)
		__game_logic(game_state)