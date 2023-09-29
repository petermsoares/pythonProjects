melon = int(input())
if melon % 2 == 0 and melon != 2:
    print("YES")
else:
    print("NO")

"""
I had to submit this one 6 times.
At first I misread the problem.
I thought so long as the number was
even the output should be YES.

The trick is that the divided pieces
each have to be even, but not
necessarily the same. Thus, 2 is
invalid because it produces 2 units
of 1. 1 is an odd number, so 2 fails.

2 needs to be treated as an exception
to the general rule for the solution
to work.
"""
