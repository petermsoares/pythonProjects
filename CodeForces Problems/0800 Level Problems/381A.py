# Problem: https://codeforces.com/problemset/problem/381/A
# Answer: https://codeforces.com/problemset/submission/381/228240295

# This one was a little tricky to understand because of the translation. But essentially 2 players are playing a card game. They each take a turn picking from a list of face-up cards. Cards are shown face-up at all times in a single array.

# Each player will always pick the biggest card possible during his turn.

# A player can only pick one card per turn.

# What is the sum of points each player has at the end of the game based on the cards that they pick?

# *******************

turns = int(input())

player1 = 0   # True's turn
player2 = 0   # False's turn

cards = [int(i) for i in input().split()]

# toggles on and off dependong on which player's turn it is.
toggle = True

for turn in range(turns):

    # If only 1 card left, we can't compare it to another card.
    # So we just give it to the current player drawing from array.
    if len(cards) == 1:
        if toggle == True:
            player1 += cards[0]
        else:
            player2 += cards[0]

    # If we have 2 cards and card [0] is bigger, add it to player's total and delete it from the list.
    elif cards[0] > cards[-1]:
        if toggle == True:
            player1 += cards[0]
            del cards[0]
        else:
            player2 += cards[0]
            del cards[0]

    # Else, add the [-1] card to the player's total and delete it from the list.
    else:
        if toggle == True:
            player1 += cards[-1]
            del cards[-1]
        else:
            player2 += cards[-1]
            del cards[-1]
    if toggle == True:
        toggle = False
    else:
        toggle = True
print(player1, player2)
