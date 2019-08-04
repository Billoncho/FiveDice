# FiveDice.py
# Billy Ridgeway
# Simulates rolling 5 dice.

import random       # Imports the random library.
keep_going = True   # Set the variable to true.

# Creates a while loop that will simulate rolling 5 dice and showing the
# user the results. The game will continue until the user presses any key
# other than Enter.
while keep_going:
    dice = [0, 0, 0, 0, 0]              # Sets all the dice to zero.
    for i in range(5):                  # Rolls the dice.
        dice[i] = random.randint(1, 6)  # Assigns a random number to each di.
    print("You rolled:", dice, ".")     # Prints the user's dice.
    dice.sort()                         # Sorts the list elements from least to greatest.
    if dice[0] == dice[4]:
        print("Yahtzee!")
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("Four of a kind!")
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("Three of a kind!")
    elif (dice[0] == 1) and (dice[1] == 2) and (dice[2] == 3) and (dice[3] == 4) and (dice[4] == 5):
        print("Large straight!")
    elif ((dice[0] == 1) and (dice[1] == 2) and (dice[2] == 3) and (dice[3] == 4) and (dice[4] != 5)
    or (dice [0] != 1) and (dice[1] == 2) and (dice[2] == 3) and (dice[3] == 4) and (dice[4] == 5)):
        print("Small straight!")
    # Prompts the user to keep playing or quit the game and evaluates the user input.
    keep_going = (input("Hit [Enter] to keep playing, or any key to exit: ") == "")
