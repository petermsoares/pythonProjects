# Problem 1367B

# The list will be of length (1 <= n <- 40).

# First we need to check if each number matches the 
# partify of the index it is in.

# If not, we need to determine if it is possible to
# do a swap--and if so, what the shortest number of
# swaps are.

# To make life easy, as we look through the first list
# to see if it is a "good" list, we should mark the
# index value and number in a separate list. Then
# can can do the swaps based on that list. 

# Note that sometimes we won't be able to make the
# list a "good" list. For example if we have 3 numbers
# that are odd but they're on an even index value, then
# we can never make the list "good" because no matter
# where we swap the values the list values will not
# have parity. In order for a possible arrangement
# to exist, there needs to be the same number of
# even and odd numbers that need to be swapped.

# Ie: 2,4,6,7 is bad because of the 4 value. 4%2=0,
# but 4 is on index value 1, and 1%2 != 0. And because
# all the other numbers on the list are good, we have
# no place to put the 4. However, if we had 3,4,6,7
# we could swap 3 and 4 and it would work.

testcases = int(input())

for t in range(testcases):
    listLength = int(input())
    listItems = [int(i) for i in input().split()]
    
    listGood = True
    
    oddIevenN = []
    evenIoddN = []
    
    
    for i in range(listLength):
        if i % 2 != 0:
            if listItems[i] % 2 == 0:
                listGood = False
                oddIevenN.append([listItems[i],i])
                listGood = False
        elif i % 2 == 0:
            if listItems[i] % 2 != 0:
                listGood = False
                evenIoddN.append([listItems[i],i])
                listGood = False
    
    if len(oddIevenN) != len(evenIoddN):
        output = -1
    else:
        output = len(oddIevenN)
    # print(oddIevenN)
    # print(evenIoddN)
    print(output)    