# This is a straightforward problem. Essentially
# we want to take 3 numbers and sort them. Then
# output the second number in the list, because
# that number is the median number.

# We could code a more robust solution and make use
# of the math module to handle test cases greater
# than 3 numbers, but the instructions are to build
# a solution for 3 numbers, so let's not overengineer
# the solution.

# To start, we will import the number of test cases.
testCases = int(input())

# Next, we will loop through all test cases.

for case in range(testCases):
    
    # Next, take the testcase we are examining.
    thisCase = [int(i) for i in input().split()]
    
    # Next, order/sort the list.
    thisCase.sort()
    
    # Next, create an output variable to house
    # the answer, and assign the second index
    # list item to the output variable.
    
    output = thisCase[1]
    
    # Finally, print the output variable as the answer.
    
    print(output)