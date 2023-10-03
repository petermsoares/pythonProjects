# We want to line up n soldiers on parade ground.

# The general thinks its ok if the first solder has the highest height and the last solder has the smallest height.

# The general can swap any two neighboring soldiers. To do the swap it takes 1 second.

# To solve, I think we can use the following rules:
# [1] Need to calculate the total seconds needed to do the swap.
# [2] Count the distance from left to right for the large/small.
# [3] If the two overlap at any point, subtract 1.

input1 = input() # Get first input from judge, total soldiers.

input2 = input().split() # String of the height of each soldier.

soldierHeight = [int(x) for x in input2] # List of height in ints.

soldiersSorted = [int(x) for x in input2] # Make a new list to sort soldiers
soldiersSorted.sort() # Sort the list of soldiers


tallestSoldier = soldiersSorted[-1] # Get the tallets soldier int
shortestSoldier = soldiersSorted[0] # Get the smallest soldier int

# Shows us the first instane of largest soldier.
tallSoldierPosition = soldierHeight.index(tallestSoldier)
# print("tallSoldierPosition",tallSoldierPosition)

# Shows us the right-most first instance of the smallest soldier.
soldierHeight.reverse() # reverse list.
# Get first instance of shortest soldier in reversed list.
shortSoldierPosition = soldierHeight.index(shortestSoldier)
# Get that position in the original list.
listLength = len(soldierHeight) - 1
shortSoldierPosition = listLength - (shortSoldierPosition)
# print("shortSoldierPosition", shortSoldierPosition)

# Calculate the distance the tall soldier needs to move.
distanceTallTravels = abs(tallSoldierPosition - 0)
# print("distance tall travels is:",distanceTallTravels)
# Calculate the distance the short soldier needs to move.
distanceShortTravels = abs(shortSoldierPosition - listLength)
# print("distance short travels is:",distanceShortTravels)

# Add the distances together
secondsCounter = distanceTallTravels + distanceShortTravels

# Subtract 1 if they overlap at anytime. We're allowed to swap only 2 soldiers at once, so if they overlap this means at one point we can swap them both in 1 turn, so we subtract that turn from the secondsCoutner.
if shortSoldierPosition < tallSoldierPosition:
    secondsCounter -= 1
    # print("secondsCounter Activated")
    
print(secondsCounter)


