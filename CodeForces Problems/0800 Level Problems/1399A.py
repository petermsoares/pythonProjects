# Problem: https://codeforces.com/problemset/problem/1399/A
# Solution: https://codeforces.com/problemset/submission/1399/228219198

# *************************

# An array of int values is given.
# If 2 numbers are duplicates, we can remove one of them.
# If 2 numbers differ by 1, we remove the smaller number.
# Determine if we can print an array with 1 element in it.

# To solve, we sort the list in order from small to large.
# Check for duplicate values between numbers, and for absolute
# value differences between numbers. Remove numbers according
# to the rules above. If we get to the end of a list and have
# one element, we print YES. If we have more than 1 element
# we print no--this happens if we cannot continue to destroy
# numbers.


# *************************
cases = int(input())

for n in range(cases):

    ignore = input()
    array = [int(i) for i in input().split()]

    array.sort()

    output = ""

    counter = 0
    goAhead = True
    while (goAhead):

        try:
            if abs(array[0] - array[1]) <= 1:
                del array[0]
            else:
                output = "NO"
                goAhead = False

        except:
            if len(array) == 1:
                output = "YES"
                goAhead = False

    print(output)
