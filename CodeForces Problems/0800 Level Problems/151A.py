# Problem: https://codeforces.com/problemset/problem/151/A
# Answer: https://codeforces.com/problemset/submission/151/228222163

# ********************

# I had to simplify the variable names down to letters because the answer got too verbose.

# To make a toast, each friend needs:

# - a specified amount to drink: (l*k) // nl
# - a single slice of lime
# - a specified amount of salt: p // np

# ********************

variables = [int(i) for i in input().split()]

n = variables[0]
k = variables[1]
l = variables[2]
c = variables[3]

d = variables[4]
p = variables[5]
nl = variables[6]
np = variables[7]

num1 = (k*l)//nl
num2 = (c*d)
num3 = (p//np)

numbers = [num1, num2, num3]
numbers.sort()
answer = numbers[0] // n

print(answer)
