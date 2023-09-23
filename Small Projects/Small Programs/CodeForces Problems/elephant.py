"""
An elephant can move 1-5 units per
step.

Find the min number of steps an elephant
needs to take to reach a specific unit.

Ie: unit is 12, min steps are 3. 2 5-step
steps and 1 2-step step.

I think the way to solve this is to divide
by 5 and then add 1 so long as the number
is bigger than 5. Any number divided by
5 is going to have a remainder less than 5.
so we just add 1 because the specific
number of the remainder doesn't matter.

For numbers of the input that are less
than 5 we can just output 1 because
1, 2, 3, or 4 will be within 1 single
step.
"""

input = int(input())
unitsLeft = input

if input > 5 and input % 5 == 0:
    fiveStepCount = (input // 5)
elif input > 5:
    fiveStepCount = (input // 5) + 1
else:
    fiveStepCount = 1
print(fiveStepCount)
