# Problem: https://codeforces.com/problemset/problem/1512/A
# Answer: https://codeforces.com/problemset/submission/1512/228229644

# ****************

# Find the index of the number that is unlike the rest.
# To solve this I made a copy of the original list and sort it.
# Sorting the list places the unique number either at the front or back.
# We then check the count of the first and last numbers in the list.
# If the count is == 1, then that's the unique number.
# After we identify the unique number, use .index() to find its index in the original list.
# Add 1 to the index position because lists begin counting at 0, not 1.

# ****************

cases = int(input())

for x in range(cases):

    listLength = int(input())

    originalList = [int(i) for i in input().split()]

    copyList = originalList.copy()
    copyList.sort()

    number1 = copyList[0]
    number2 = copyList[-1]

    number1Count = copyList.count(number1)
    number2Count = copyList.count(number2)

    if number1Count == 1:
        uniqueNumber = number1

    else:
        uniqueNumber = number2

    position = originalList.index(uniqueNumber)+1
    print(position)
