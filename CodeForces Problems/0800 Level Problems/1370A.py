# 1370A


    
# I think the logic needed to solve this, without modules, is:

# 1: if n is 2 or 3, the gcd is always 1.

# 2: if n is greater than 3 and is even, the gcd is n/2

# 3: if n is greater than 3 and is odd, the gcd is n-1 / 2

# We needed the biggest divisor possible. This means the number
# needs to be divisible by itself, and the number needs to go
# into the largest number possible. By using the rules mentioned
# above, we should be able to retrieve the largest gcd in a list.

# First, get testcases
testCases = int(input())

# Next, run a loop based on the test cases, analyzing each.
for case in range(testCases):
    number = int(input())
    
    if number <= 3:
        output = 1
    elif number % 2 == 0:
        output = number//2
    elif number % 2 != 0:
        output = (number-1)//2
    
    print(output)

# This code worked on the samples given on the website. Now,
# let's submit to the online judge.

# Ok, it worked. This problem took me a little while to understand
# what I was supposed to be doing, but once I understood it
# was straightforward. I enjoyed this one.