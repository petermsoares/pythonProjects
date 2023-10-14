# Problem: https://codeforces.com/problemset/problem/723/A
# Answer: https://codeforces.com/problemset/submission/723/228096043

# *********************************

# One of the friends will always remain in his home.
# We want to sort the position of each person and then
# calculate the distance from the ends to the middle.

# *********************************

homePositions = [int(i) for i in input().split()]

homePositions.sort()

distance1 = abs(homePositions[0] - homePositions[1])
distance2 = abs(homePositions[2] - homePositions[1])
output = distance1 + distance2

print(output)
