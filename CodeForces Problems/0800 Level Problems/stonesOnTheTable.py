# Ideas for solving:

"""
First input tells us the number of characters
in the string. The second input is the string.

If any two neighboring letters of the string are
the same, we need to add 1 to a counter. So,
RBB would be 1. BBB would be 2. BBRBB is 2.

I think I want to cycle through the string as
a list and compare the index values to eachother.
If they're the same, add 1 to the counter. Then,
print the counter.
"""
# Gets first input from the judge.
firstInput = int(input())

# Gets input string from the judge.
inputString = input()

# Turns the string into a list of characters
list = list(inputString)

# Create counter
counter = 0

# for index values, except the last one
for i in range(firstInput - 1):
    # if two neighboring index values are the same, add 1
    if list[i] == list[i+1]:
        counter += 1

print(counter)
