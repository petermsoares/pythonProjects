
input1 = input()  # First input is number of people asked.
input2 = input()  # Second is a string of integers.

# I think the spirit of this problem wants me to
# loop through the numbers and check if one of
# them is 1. I think it would be cheating to
# use a count, so let's solve this with a for loop.

# First, get the number of people asked as an integer.
nPeople = int(input1)

# Next, turn the string of 0s and 1s into a List
# so that we can loop through it and check the values.
# Remember this is a list of strings, not ints.
listDifficulty = input2.split()

# Create a loop that will cycle through the list
# for each index value and check whether the value
# is a 0 or a 1.

# Let's assume the string has no 1s and set output to EASY.
output = "EASY"

for i in range(nPeople):

    if listDifficulty[i] == "1":
        output = "HARD"
        break
        # Essentially, if we ever find a 1 in our list
        # we want to change the output to "HARD" and then
        # break out of the loop as there is no need to
        # continue counting.

print(output)
