

# The input has 5 lines, or 5 inputs.
# The first 4 represent a position in a list where a dragon will be hurt.
# Find the number of dragons that are damaged and output it.

# For example and input of 1 2 3 4 12 means that every 1st dragon takes damage, every 2nd dragon takes damage, every 3rd dragon takes damage, and every 4th dragon takes damage. And there are 4 total dragons.

# If the input was 0 0 0 4 12, then only the 4th, 8th, and 12th dragon would take damage.

# A thing to keep in mind when doing this problem is to keep track of duplicates. For example 2 4 0 0 12 would have duplicate damaged dragons because a dragon damaged by 4 would always be damaged by 2.

# d = number of dragons

# To solve I think I want to make a list of dragons and then check the damaged positions of each one. Then tag that dragon in some way--this way if a dragon is damaged twice because he's already tagged he wouldn't get double counted. Then at the end just count the total number of dragons.

damage1 = int(input())
damage2 = int(input())
damage3 = int(input())
damage4 = int(input())
totalDragons = int(input())

# First, let's make a list full of empty strings as long as the totalDragons variable.
damagedDragons = ["O"] * totalDragons  # O will mean a dragon is OK.

# Next, let's make a list of the damaged positions so we can loop through it in a list.
damagedPosition = [damage1, damage2, damage3, damage4]

# Next, we need to loop through each each index value and check whether that position is divisible by the damage type. We will compare the damagedPosition index value at 0 to every damagedDragons index value.

dd = 0  # index value counter for damagedDragons.
dp = 0  # index value counter for damagedPosition List.


goAhead = True
while (goAhead):

    damageType = damagedPosition[dp]

    if (dd + 1) % damageType == 0:
        damagedDragons[dd] = "D"
    dd += 1  # moves on to the next dragon's position

    if dd == len(damagedDragons):
        dd = 0  # reset the dd index counter
        dp += 1  # increase the dp index counter
        # In other words, once we look at all the dragons in the list to see if they are affected by the damage position "DP" value, we move onto the next "DP" value in the loop.

    if dp >= len(damagedPosition):
        goAhead = False
        # If the "DP" counter is equal to the length of the list, or greater, then we have examined all the DP position values against all of the damaged dragon positions and we close the loop.

output = damagedDragons.count("D")  # count the number of damaged dragons.

print(output)  # print the answer.

"""
The first time I submitted this answer was here:
https://codeforces.com/problemset/submission/148/226796658

After analyzing this problem I think there are a few ways to improve performance:

#1, we should have a section that tests whether any of the damagePosition values is = 1. If so, we don't even need to loop through anything because we know every dragon will take damage, so the output is equal to the sum of all dragons.

#2, we should have a section that removes any duplicate damagePosition values, if there are any. This way we aren't doing the same work twice.

#3, it might be faster to make the damagedDragons List into a series of numbers based on the position in the list rather than "O"s and turning them into "D"s. We could cycle through the list and look for values that have a % == 0, and then remove them from the list. This way, each time we loop through the list we're scanning a smaller and smaller set of numbers. For each position we delete, we'd want to add 1 to a counter representing the total number of dragons affected by damage and then output that number. I think this would be much faster, especially if we have a damage type like 2 which is going to remove 1/2 of the dragons anyway.

Instead of doing another problem tomorrow, I think I'll try and redo this problem. The codeforces judge indicated my program's longest run time was 342 ms with a memory of 640 KB.
"""
