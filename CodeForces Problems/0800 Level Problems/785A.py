# Solution to CF problem 785A
# https://codeforces.com/problemset/problem/785/A
# Accepted Answer: https://codeforces.com/contest/785/submission/227089176

# Get the number of shapes in the collection:
prettyShapes = int(input())

# Create variable counters for each type of shape:
t = 0
c = 0
o = 0
d = 0
i = 0

# Loop through the list of shapes as they appear.
# Each shape counted will add 1 to that shape's counter.
for x in range(prettyShapes):
    shape = input()

    if shape == "Tetrahedron":
        t += 1
    elif shape == "Cube":
        c += 1
    elif shape == "Octahedron":
        o += 1
    elif shape == "Dodecahedron":
        d += 1
    elif shape == "Icosahedron":
        i += 1

# Calculate the total number of faces by multiplying
# the sides of all represented shapes by respective coutners.
totalShapes = (t*4) + (c*6) + (o*8) + (d*12) + (i*20)

# Output the answer.
print(totalShapes)
