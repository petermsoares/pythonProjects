
"""
- A and D play chess together.
- Games never end in a draw.

- Games are played in a row:
    - "AADDAA"
    - A won 4
    - D won 2

If A > D, print Anton
If A < D, print Danik
If A == D, print Friendship
"""

# Get input from the judge\
firstInput = input()
inputJ = input()

# Turn string into list so we can count A and D.
gamesList = list(inputJ)

Awins = gamesList.count("A")
Dwins = gamesList.count("D")


def winner():

    if Awins > Dwins:
        return "Anton"
    elif Awins < Dwins:
        return "Danik"
    else:
        return "Friendship"


output = winner()

print(output)
