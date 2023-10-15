# Problem: https://codeforces.com/problemset/problem/1742/A
# Solution: https://codeforces.com/problemset/submission/1742/228337214

# *

# Determine if one number is the sum of the other two.
# We can sort the numbers from smallest to largest, and then determine if the first two numbers sum to the last number.

# *

cases = int(input())

for x in range(cases):
    numbers = [int(i) for i in input().split()]

    numbers.sort()

    if numbers[0] + numbers[1] == numbers[2]:
        print("YES")
    else:
        print("NO")
