import math

# First we get the relative positions of dragons that will take damage via input from judge.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

output = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0

# Then we get the total number of dragons from the input of the judge:
total = int(input())

# This solution involves using the inclusion-exclusion principle
# A link to a video explaining this solution is here: https://www.youtube.com/watch?v=szUTQRJU76Q&ab_channel=MathsStatsUNSW
# Note that this solution, as of 2023-10-07 is invalid on codeforces.com because codeforces supports
# Python version 3.8, but the lcm function in the math module wasn't introduced to Python until version 3.9
# So this code, although correct, will cause a run time error on codeforces.com
n1 = (total//a) + (total//b) + (total//c) + (total//d)

n2 = (total//math.lcm(a, b)) + (total//math.lcm(a, c)) + (total//math.lcm(a, d)) + \
    (total//math.lcm(b, c)) + (total//math.lcm(b, d)) + (total//math.lcm(c, d))


n3 = (total//math.lcm(a, b, c)) + (total//math.lcm(a, b, d)) + \
    (total//math.lcm(a, c, d)) + (total//math.lcm(b, c, d))

n4 = (total//math.lcm(a, b, c, d))

output = n1 - n2 + n3 - n4

print(output)
