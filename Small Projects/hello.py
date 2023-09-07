# Rock Paper Scissors game against computer, best of 5 or first to 3.

import random
import sys

cpuWins = 0
playerWins = 0

print("Select a choice to play against computer. Press 9 to exit.")
goAhead = True
while (goAhead):

    # Computer picks a number 1 2 or 3 for R, P, S.
    cpuChoice = random.randint(1, 3)
    # Player picks a number.
    playerChoice = int(input("Pick [1] Rock, [2] Paper, or [3] Scissors: "))

    if playerChoice == 9:
        sys.exit()  # Closes program.

    # Program tells player which option he picked.
    if playerChoice == 1:
        print("Player Choice is Rock")
    elif playerChoice == 2:
        print("Player Choice is Paper")
    elif playerChoice == 3:
        print("Player Choice is Scissors")
    elif playerChoice != 9:  # invalid choice will restart current loop.
        print("You made an invalid selection, please select from the options below:")
        continue

    # Program tells player which option CPU picked.
    if cpuChoice == 1:
        print("CPU Choice is Rock")
    elif cpuChoice == 2:
        print("CPU Choice is Paper")
    elif cpuChoice == 3:
        print("CPU Choice is Scissors")

    # Program then compares player choice to cpu choice.
    if playerChoice == cpuChoice:  # if draw, then nothing.
        print("DRAW")
    elif playerChoice == 1 and cpuChoice == 2:  # R v P
        print("CPU wins")
        cpuWins = cpuWins + 1
    elif playerChoice == 1 and cpuChoice == 3:  # R v S
        print("Player wins")
        playerWins = playerWins + 1
    elif playerChoice == 2 and cpuChoice == 1:  # P v R
        print("Player wins")
        playerWins = playerWins + 1
    elif playerChoice == 2 and cpuChoice == 3:  # P v S
        print("CPU wins")
        cpuWins = cpuWins + 1
    elif playerChoice == 3 and cpuChoice == 1:  # S v R
        print("CPU wins")
        cpuWins = cpuWins + 1
    elif playerChoice == 3 and cpuChoice == 2:  # S v P
        print("Player wins")
        playerWins = playerWins + 1

    # Program tells player what current score is.
    print("Current score is PLAYER:", playerWins, "COMPUTER:", cpuWins)

    # Program checks to see if either player has 3/5 wins. If so, ends loop.
    if playerWins >= 3:
        print("Player has won. Games won out of 5:", playerWins)
        goAhead = False
    elif cpuWins >= 3:
        print("CPU has won. Games won", cpuWins)
        goAhead = False
