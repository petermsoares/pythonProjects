# 1426A

# Ok the way this problem is written sucks.

# What the problem should say is that x is the number of rooms
# per floor. Only the first floor has 2 rooms. All the other
# floors have x number of rooms.

# The way they wrote (x+3) to (2x + 2) is extremely confusing and
# makes a reader think there is a complex formula to the solution,
# but it's much more simple than that.

# We take the value of n and subtract 2 from it. This accounts for
# the first floor's rooms. We then add 1 to our counter because
# we have counted the first floor.

# Then, we take the new value of n and divide it by x.
# We always round up from a remainder. So if we have 1.0001, that
# counts as 2. 

# Finally, add 1 to the quotnt we got from the prevous calculation,
# that is the answer. For this answer, we will use the math module
# and round the numbers up if there is a remainder.
import math

testCases = int(input())



for case in range(testCases):
    givenValues = [int(i) for i in input().split()]
    
    nthRoom = givenValues[0]
    roomsPerFloor = givenValues[1]
    
    
    
    nthRoom -= 2 # removing floors 1 and 2.
    
    output = math.ceil((nthRoom / roomsPerFloor))

    output += 1 # adding back the first floor.
    
    # Adjusts output if nthRoom is a 1 or 2.
    if output <= 1:
        output = 1
    
    print(output)
    
