import random

people = ["Alexander", "Ben", "Charlie", "Peter", "Jim"]
newList = [""] * len(people)  # create a new list with empty strings

randomPosition = 0
index = 0

print("Original..:", people)  # prints the original list of people.


def randomNumberCall():  # picks a random index value on the list of people.
    return random.randint(0, (len(people) - 1))


goAhead = True
while (goAhead):

    randomPosition = randomNumberCall()  # Gets a random number.

    if newList[randomPosition] == "":  # if the space is open
        # assign that person to that open spot.
        newList[randomPosition] = people[index]
        index = index + 1  # and then go to the next person.
        # If a space is filled, tell the user and move on. Comment out once program works.

    if index == len(people):
        goAhead = False

print("Randomized:", newList)
