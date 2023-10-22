# Problem 1624A

# Given a list of numbers, calculate the number of
# times values can be increased by 1 such that
# all index values are the same.

# The rule here is that we can select any number
# of index values, 0 through all of them, and
# increase them by 1.

# We cannot decrease the value of any integer, and
# because of this rule it makes the problem narrow
# in scope.

# Essentially, the solution involves taking the list
# and sorting it. 

# First we need to check how many numbers the list has.
# If the list only has 1 number, we don't do anythin.

# If the list has more than 2 numbers, we compare
# the smallest and largest numbers. The answer is
# equal to the difference between those two numbers.

# The code below works, but I want to try using a loop.
"""
testCases = int(input())

for case in range(testCases):

    listLength = int(input())
    
    listNumbers = [int(i) for i in input().split()]
    
    listNumbers.sort()
    
    if listLength < 2:
        output = 0
    else:
        output = listNumbers[-1] - listNumbers[0]
    
    print(output)
"""

# Answer 2:
# The answer above worked in 218 ms. I think this
# might be faster...

testCases = int(input())

for case in range(testCases):

    listLength = int(input())
    
    listNumbers = [int(i) for i in input().split()]
    
    smallNumber = listNumbers[0]
    bigNumber = listNumbers[0]
    
    if listLength < 2:
        output = 0
    else:
        
        for n in range(listLength):
            if listNumbers[n] < smallNumber:
                smallNumber = listNumbers[n]
            elif listNumbers[n] > bigNumber:
                bigNumber = listNumbers[n]
                
        output = bigNumber - smallNumber
    print(output)