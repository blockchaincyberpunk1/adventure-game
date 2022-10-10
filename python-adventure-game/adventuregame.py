import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but "
                "not very effective) dagger.\n")


def first_choice(items, monster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                f"out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    if "sword" in items:
        fight_run(items, monster)
    else:
        print_pause("You feel a bit under-prepared for this, what with "
                    "only having a tiny dagger.")
        fight_run(items, monster)


def second_choice(items, monster):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    "take the sword with you.")
        items.append("sword")
    print_pause("You walk back out to the field.\n")
    choice_option(items, monster)


def choice_option(items, monster):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("Please enter 1 or 2.)\n")
    if choice == '1':
        first_choice(items, monster)
    elif choice == '2':
        second_choice(items, monster)
    else:
        choice_option(items, monster)


def fight_run(items, monster):
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        if "sword" in items:
            print_pause(f"As the {monster} moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause(f"But the {monster} takes one look at your "
                        "shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {monster}. "
                        "You are victorious!")
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {monster}")
            print_pause("You have been defeated!")
        play_again()
    elif choice == '2':
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed.\n")
        choice_option(items, monster)


def play_again():
    choice = input("Would you like to play again? (y/n)").lower()
    if choice == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif choice == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    items = []
    monsters = ["dragon", "gorgon", "wicked fairie", "troll",
                "pirate", "werewolf", "redcap", "basilisk", "imp",
                "ghoul", "ogre", "cyclops", "hydra"]
    monster = random.choice(monsters)
    intro(monster)
    choice_option(items, monster)


play_game()
