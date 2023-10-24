# Problem 1353A

# Ok so I think to answer this problem we need
# to move the smallest numbers from List-A to
# List-B, and the largest numbers from List-B
# to List-A in the swap.

# Note, we shouldn't move anything if the numbers
# in List-A are already larger than List-B, because
# doing so would reduce the maximum sum.

# Also, we have "k" number of swap attempts.

# **********************************************
# Note, our answer is the maximum sum we can get
# based on the number of swaps we can do.
# **********************************************

# The first line is going to be the number of test cases
testCases = int(input())

for case in range(testCases):

    # The next line contains the length of the lists.
    lengthAndSwapVals = [int(i) for i in input().split()]

    # The first number is the length of the lists.
    listLength = lengthAndSwapVals[0]

    # The second number is the number of swaps.
    swaps = lengthAndSwapVals[1]

    # The next input contains the numbers in List-A
    listA = [int(i) for i in input().split()]

    # The next input contains the numbers in List-B
    listB = [int(i) for i in input().split()]

    # Ok now for the logic of winning the game...
    # I think we should sort each list, and reverse
    # list B. Then we can iterate over each list
    # from beginning to end.
    
    # The idea is that if the value in A is less than
    # the value in B, we swap A and B so long as we
    # have swaps available.
    
    # doing a swap will take 1 away from the number
    # of swaps we can do.
    
    # we will keep going until one of these conditions
    # are met:
        # [1] we run out of swaps, and exit the loop.
        # [2] A and B are equal. If so, swapping
        # won't increase the values in A anymore,
        # so we should stop and just do the sum.
        
    # Ok, let's set up the lists for iteration:
    listA.sort()
    listB.sort()
    listB.reverse()
    
    # Now we need to loop through each index and 
    # compare A and B. Let's do this with a while
    # loop.
    
    # Note, we only want to loop if we have swaps
    # available. The rules say that sometimes we
    # might not get a swap counter to use, so we
    # set goAhead to false initially. This is 
    # us assuming that we have zero swaps.
    # however, if the swaps is greater than 0,
    # then we toggle goAhead to true so that
    # the while loop activates.
    
    goAhead = False
    
    if swaps > 0:
        goAhead = True
    
    i = 0
    while(goAhead):
        # at the start, subtract 1 swap to account
        # for this loop's iteration.
        swaps -= 1
        
        # If A[i] < B[i], swap.
        if listA[i] < listB[i]:
            listA[i] = listB[i]
        
        # If not,turn off loop.
        elif listA[i] >= listB[i]:
            goAhead = False
    
        # if all swaps used, turn off loop.
        if swaps <= 0:
            goAhead = False
        
        # failsafe 
        i += 1        
        if i > 50:
            goAhead = False
    
    output = 0
    
    for n in range(listLength):
        output += listA[n]
    
    print(output)

# Ok, this version works on the sample input.
# Let's try it with the online judge.

# It worked. Even though this problem was easy, I feel
# there are a bunch of places where mistakes could
# be made, and I'm happy my first attempt was accepted.