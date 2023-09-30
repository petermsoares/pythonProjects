# f(n) = -1 +2 -3 +4 etc.
# Make a program that does this function for an input.
# ie: input 4 == -1 +2 -3 +4
# ie: input 2 == -1 +2

#Get input string from judge
input1 = input()

# Turn the string into an int and assign it to a readable variable
number = int(input1)

# My original solution was to replicate the function given in
# the problem. But doing this makes the program take too long
# when calculating very large numbers. The answer to this problem
# listed how to solve, and I didn't realize I needed to use math
# to find the answer, so I just implemented the solution given
# in the answer. 

if number % 2 == 0:
    total = number /2
else:
    total = -(number +1)/2

print(int(total))