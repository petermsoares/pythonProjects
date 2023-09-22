# Thoughts on solving this problem:
"""
The weight of the first bear has to be
strictly larger than the second bear.

Bear1's weight goes up 300% each year.
Bear2's weight goes up 200% each year.

The solution should be to increase the
weight of each bear and do a comparison
for each period. When Bear1's weight is
larger than Bear2's weight, that year
number will be the answer to the input.
"""
input = input()  # get judge input.

# returns a list from a string of numbers.
# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
list = [int(s) for s in input.split() if s.isdigit()]

bearL = list[0]  # assign value 1 to bearL
bearB = list[1]  # assign value 2 fo bearB
years = 0  # create a years counter and set to 0

goAhead = True
while (goAhead):

    if bearL <= bearB:
        years += 1  # increase number of years.
        bearL *= 3  # increase bearL weight by 3x
        bearB *= 2  # increase bearB weight by 2x

    if bearL > bearB:  # look to see if bearL is bigger
        goAhead = False  # if so, stop looping

print(years)  # print number of loops (years) it took.
