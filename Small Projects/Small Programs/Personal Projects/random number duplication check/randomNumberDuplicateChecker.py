# make a simple program that guesses 20 random numbers
# program must not repeat numbers
# a repeated number is counted.
# the output should include a list of random numbers
# and it should have a count of duplicates rolled.
import random

listNumbers = []
duplicateNumbers = []
i = 0


def rollRandom():
    roll = random.randint(1, 100)
    return roll


while i < 20:
    newRoll = rollRandom()
    if newRoll not in listNumbers:
        listNumbers = listNumbers + [newRoll]
    else:
        duplicateNumbers = duplicateNumbers + [newRoll]
        continue
    i = i + 1

print(listNumbers)
print("Duplicate Numbers: " + str(duplicateNumbers))
