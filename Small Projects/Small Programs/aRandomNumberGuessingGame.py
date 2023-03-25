import random

computerChoice = random.randint(1, 20)
userGuess = ""

print("The computer is thinking of a number between 1 and 20. Make a guess as to what number the computer has picked.")

while userGuess != computerChoice:
    userGuess = input()
    userGuess = int(userGuess)
    if userGuess == computerChoice:
        print("Your guess of " + str(userGuess) + " is correct! You win.")
    elif userGuess < computerChoice:
        print("Your guess of " + str(userGuess) +
              " is lower than the computer's guess. Guess again!")
    elif userGuess > computerChoice:
        print("Your guess of " + str(userGuess) +
              " is greater than the computer's choice. Guess again!")
print("Thanks for playing! *******")
