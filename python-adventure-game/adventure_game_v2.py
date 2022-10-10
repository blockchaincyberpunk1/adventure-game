import time
import random
# import statement


def slight_delay(story):  # create function called slight delay
    print(story)          # print text content from game
    time.sleep(2)         # cause a 2 second delay so player has time to read


# create a function that begins the game with the intro
def game_begin(mythical_creature):  # create function called game begin
    slight_delay("You find yourself standing in an open field, "
                 "filled with grass and yellow wildflowers.")
    slight_delay(f"Rumor has it that a {mythical_creature} is somewhere "
                 "around here, and has been terrifying the nearby village.")
    slight_delay("In front of you is a house.")
    slight_delay("To your right is a dark cave.")
    slight_delay("To your left is the road to the village.")
    slight_delay("In your hand you hold your trusty (but "
                 "not very effective) dagger.\n")


# create function that gives player three different decisions to make
def decisions(weapons, mythical_creature):
    slight_delay("Enter 1 to knock on the door of the house.")
    slight_delay("Enter 2 to peer into the cave.")
    slight_delay("Enter 3 to walk to the village.")
    slight_delay("What would you like to do?")
# example of assignment statement
    decision = input("Please enter 1 or 2 or 3.)\n")  # function call
    if decision == '1':  # decision is the variable that records player input
        house(weapons, mythical_creature)  # sends player to house
    elif decision == '2':
        cave(weapons, mythical_creature)  # sends player to cave
    elif decision == '3':
        village(weapons, mythical_creature)  # sends player to village
    else:  # ensures the player enters valid input - keeps asking them question
        decisions(weapons, mythical_creature)
# decided to add some additional complexity to the game
# create a function that runs through the players decision to go to the house


def house(weapons, mythical_creature):
    slight_delay("You approach the door of the house.")
    slight_delay("You are about to knock when the door opens and "
                 f"out steps a {mythical_creature}.")
    slight_delay(f"Eep! This is the {mythical_creature}'s house!")
    slight_delay(f"The {mythical_creature} attacks you!")
    if "sword" in weapons:  # checks if player has sword then this runs
        decision_fight_or_escape(weapons, mythical_creature)
    else:  # if player does not have sword this runs
        slight_delay("You feel a bit under-prepared for this, what with "
                     "only having a tiny dagger.")
        decision_fight_or_escape(weapons, mythical_creature)


# create a function that give the player the choice to fighht or run
def decision_fight_or_escape(weapons, mythical_creature):
    # function call
    fight_run = input("Would you like to (1) fight or (2) run away?")
    if fight_run == '1':   # gives player option to fight or head back to field
        if "sword" in weapons:   # if player has sword in weapons this runs
            if "army" in weapons:  # player has sword + army this runs
                slight_delay("The townspeople ready themselves for your "
                             "sign to attack.")
                slight_delay("You signal to the townspeople to "
                             f"charge the {mythical_creature}.")
                slight_delay(f"As the {mythical_creature} moves "
                             "to attack, you unsheath your new "
                             "sword.")
                slight_delay("The Sword of Ogoroth shines "
                             "brightly in your hand as you brace "
                             "yourself for the attack.")
                slight_delay(f"But the {mythical_creature} takes "
                             "one look at your shiny new "
                             "toy and the army behind you "
                             "and decides to runs away!")
                slight_delay("You have rid the town of "
                             f"the {mythical_creature}. "
                             "You are victorious!")
                slight_delay("Later, you head back to the village "
                             "for ale and Shepherd's pie.")
            else:  # if player has sword but no army this runs
                slight_delay(f"The {mythical_creature} is bigger "
                             "than you expected.")
                slight_delay("Your too scared to fight the "
                             f"{mythical_creature} all by "
                             "yourself.")
                slight_delay("You walk back out to the field.\n")
                decisions(weapons, mythical_creature)
        else:  # if player does not have sword this runs
            slight_delay("You do your best...")
            slight_delay("but your dagger is no match for "
                         f"the {mythical_creature}")
            slight_delay("You have been defeated!")
        restart_game()  # asks player if they want to play the game again
    elif fight_run == '2':  # give player the option to run away
        slight_delay("You run back into the field. Luckily, you don't "
                     "seem to have been followed.\n")
        decisions(weapons, mythical_creature)
    else:  # ensures player enters valid input
        decision_fight_or_escape(weapons, mythical_creature)
# player should not be able to fight mythical creature without sword and army


# create a function that runs through the players decision to go to the cave
def cave(weapons, mythical_creature):
    slight_delay("You peer cautiously into the cave.")
    if "sword" in weapons:  # this runs if player already has sword
        slight_delay("You've been here before, and gotten all the good stuff. "
                     "It's just an empty cave now.")
    else:  # this runs if player does not have sword in weapons list
        slight_delay("It turns out to be only a very small cave.")
        slight_delay("Your eye catches a glint of metal behind a rock.")
        slight_delay("You have found the magical Sword of Ogoroth!")
        slight_delay("You discard your silly old dagger and "
                     "take the sword with you.")
        weapons.append("sword")  # this adds sword to weapons list
    slight_delay("You walk back out to the field.\n")
    decisions(weapons, mythical_creature)


# create a function that runs through the players decision to go to the village
def village(weapons, mythical_creature):
    slight_delay("You walk toward the village.")
    if "army" in weapons:  # if player already has army this runs
        slight_delay("The townspeople have already agreed to fight the "
                     f"{mythical_creature}.  They are awaiting your "
                     "instructions.")
    else:
        if "sword" in weapons:  # if player has sword then this runs
            slight_delay("The townspeople celebrate for they were waiting for "
                         "the warrior prophesied of long ago that would "
                         f"defeat the {mythical_creature}.")
            slight_delay("The swordsmen that would wield the magical "
                         "Sword of Ogoroth!")
            slight_delay("They gather their weapons and join you to fight "
                         f"the {mythical_creature}.")
            weapons.append("army")  # adds army to the weapons list

        else:  # this runs if player does not have sword
            slight_delay("The townspeople are disappointed.")
            slight_delay("You are not the warrior they thought would "
                         "save them.")
            slight_delay("You do not have the magical Sword of Ogoroth.")
    slight_delay("You walk back out to the field.\n")
    decisions(weapons, mythical_creature)


# create a function to give player option to play again
def restart_game():  # used .lower to convert user input to lowercase
    decision_restart = input("Would you like to play again? (y/n)").lower()
    if decision_restart == 'y':  # if player enters y this runs
        slight_delay("Excellent! Restarting the game ...")
        adventure_game_v2()  # starts the game all over again
    elif decision_restart == 'n':  # if player enters n this runs
        slight_delay("Thanks for playing! See you next time.")  # program ends
    else:  # ensures player enters correct input and keeps asking til they do
        restart_game()


# create a function called adventure game v2
def adventure_game_v2():    # create empty list called weapons to record when
    weapons = []            # player collects weapons
    mythical_creatures = ["dragon", "gorgon", "wicked fairie", "troll",
                          "pirate", "werewolf", "redcap", "basilisk",
                          "imp", "ghoul", "ogre", "cyclops", "hydra",
                          "yeti", "bai ze", "chimera"]
    mythical_creature = random.choice(mythical_creatures)  # random creatures
    game_begin(mythical_creature)
    decisions(weapons, mythical_creature)
# arguments are weapons and mythical_creature.
# added some additional mythical creatures to my list such as the chimera (a
# chimera is 3 headed mythical monster.
# Another unique add includes the bai ze.
# This is an chinese mythical creature known for having 6 horns and 9 eyes.


adventure_game_v2()
# function call - this makes the function run

# Notes
# I decided to use fstrings instead of the + concatenation.
