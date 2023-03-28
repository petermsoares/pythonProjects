import random
import sys

# Note, at this point I don't know about arrays and a lot of other helpful things, so most of this is hard coded.

# Game variables to keep track of w,l,t and choices
gameStatus = True
wins = 0
losses = 0
draws = 0
computerChoice = 0
playerChoice = ""

# Pre-Game text before game starts
print("*****")
print("ROCK, PAPER, SCISSORS")
print("*****")

while gameStatus == True:
    print("Current Score: " + str(wins) + " Wins, " + str(losses) +
          " Losses, " + str(draws) + " Draws")
    print("* Player, select (r)ock, (p)aper, or (s)cissors. Press (q) to quit.")

    computerChoice = random.randint(1, 3)
    playerChoice = input()

    # Checks to see if player makes a valid choice.
    # If valid, game begins.
    # If invalid, else condition triggers prompting a valid choice.
    if playerChoice == "r" or "p" or "s" or "q":

        # Logic of comparing player and computer choices is below.
        # Player input dictates game flow.
        if playerChoice == "q":
            print("The game has ended")
            print("*****")
            break

        if playerChoice == "r":
            if computerChoice == 1:
                draws = draws + 1
                print("Player: R, CPU: R. Result: DRAW")
                print("*****")
                continue
            elif computerChoice == 2:
                losses = losses + 1
                print("Player: R, CPU: P. Result: LOSS")
                print("*****")
                continue
            elif computerChoice == 3:
                wins = wins + 1
                print("Player: R, CPU: S. Result: WIN")
                print("*****")
                continue

        if playerChoice == "p":
            if computerChoice == 1:
                wins = wins + 1
                print("Player: P, CPU: R. Result: WIN")
                print("*****")
                continue
            elif computerChoice == 2:
                draws = draws + 1
                print("Player: P, CPU: P. Result: DRAW")
                print("*****")
                continue
            elif computerChoice == 3:
                losses = losses + 1
                print("Player: P, CPU: S. Result: LOSS")
                print("*****")
                continue

        if playerChoice == "s":
            if computerChoice == 1:
                losses = losses + 1
                print("Player: S, CPU: R. Result: LOSS")
                print("*****")
                continue
            elif computerChoice == 2:
                wins = wins + 1
                print("Player: S, CPU: P. Result: WIN")
                print("*****")
                continue
            elif computerChoice == 3:
                draws = draws + 1
                print("Player: S, CPU: S. Result: DRAW")
                print("*****")
                continue
        # Prompts user to input a valid conidtion for the game.
        else:
            print("Player, please pick a valid choice of R, P, S, or Q.")
            print("*****")
            continue

# End game text once game has exited
print("*****")
print("*****")
print("*****")
print("Thanks for playing! Final Scores are:")
print(str(wins) + " Wins, " + str(losses) +
      " Losses, " + str(draws) + " Draws")
