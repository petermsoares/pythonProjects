"""
The positions in the queue are 
sequentially numbered by integers
from 1 to n.

Person in position 1 is served first.

If at a time X in seconds, a boy
stands on a position I, and a girl
is behind him in position I+1, then
at time X+1, the boy and the girl
switch positions.

input1: number of children
input2: the time interval.

Essentially, the time interval is our
check. We count for i based on t.

So if t is 2 seconds, we count every
other position for the rule.
"""

input1 = input()
input1 = input1.split()
peopleOnLine = input1[0]
peopleOnLine = int(peopleOnLine)
time = int(input1[1])

input2 = input()
listOfPeople = list(input2)

for n in range(peopleOnLine):
    n = n - 1 + time  # offset by -1 because 0 index start

    if listOfPeople[n] == "B" and listOfPeople[n+1] == "G":
        listOfPeople[n] = "g"

        listOfPeople[n+1] = "b"

for n in range(peopleOnLine):
    if listOfPeople[n] == "b":
        listOfPeople[n] = "B"
    else:
        listOfPeople[n] = "G"

output = "".join(listOfPeople)
print(output)
