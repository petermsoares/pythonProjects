# Problem: https://codeforces.com/problemset/problem/1154/A
# Solution: https://codeforces.com/problemset/submission/1154/228216193



# ******************************

# I had to look at the tutorial for this one, but once it was presented to me it suddenly made sense. I thought there was a relationship between the largest and smallest numbers, but it wasn't until I saw the numbers given as nX = letter + letter that it made sense.

# You're given 4 numbers:
    # n1 = a + b
    # n2 = b + c
    # n3 = c + d
    # n4 = a + b + c
    
# Your job is to output the integer values of a, b, and c.

# To solve, you take the value of a, b, or c located in n4, and
# subtract from it n1, n2, or n3. Note that n4 must always be
# the largest number of the input because it is the sum of all
# 3 integers.

# For 3, 6, 5, 4:

    # To find c, it's n4 - n1.
    # Or: valueC = (a + b + c) - (a + b)
    # Or: valueC = n4 - n1.
    # n4 is 6, because 6 must be equal to a+b+c.
    # n1 can honestly be 3,4,5. It doesn't matter, but you
    # can sort them from smallest to largest.

    # a = 6 - 3, or 3.
    # b = 6 - 4, or 2.
    # c = 6 - 5, or 1.
    
    # Output is 1 2 3. Order doesn't matter.
    
# ******************************

numbers = [int(i) for i in input().split()]

numbers.sort()

valueA = numbers[3] - numbers[0]
valueB = numbers[3] - numbers[1]
valueC = numbers[3] - numbers[2]


print(valueA, valueB, valueC)