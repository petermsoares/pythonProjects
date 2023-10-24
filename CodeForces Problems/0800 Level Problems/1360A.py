# Problem 1360A

# We have two rectangles with lengths a, b.
# The goal is to determine the smallest size square
# plot of land that can house these two rectangles.

# I believe to solve this problem we need to look
# at each side of the rectangle.


# Note, you need to output the AREA of the square,
# which is the length times width.

# After looking at some examples I think we can
# solve with the following rules:

# Rule 1: If all the sides of the rectangles are
# equal, then the answer is (2n)**2 (n being the length
# of the number for the side)

# Rule 2: If the small side * 2 is larger than
# the length of the long side then the answer is 
# (2*smallSide)**2.

# Rule 3: If 2*smallSide is smaller than, or equal to,
# the length of the long side, then the answer is
# the large side squared.

# First, take in the number of test cases:
testCases = int(input())

# Next, loop through each test case:
for case in range(testCases):

    # Get each side as an integer.
    sides = [int(i) for i in input().split()]
    
    # Sort the sides from small to large.
    sides.sort()
    
    # Assign the sides to small and large.
    smallSide = sides[0]
    largeSide = sides[1]
    
    # Next, get the squares of each of the sides.
    ss = smallSide*2
    ll = largeSide*2
    
    # Next, apply one of the three rules based
    # on what is discussed above.
    
    # If both sides are equal.
    if ss == ll:
        output = (2*smallSide)**2
    
    # if sSquare => largeSide.
    elif ss > largeSide:
        output = (ss)**2
        
    elif ss <= largeSide:
        output = largeSide**2
    
    print(output)
    
# Ok this one turned out to be a little tricky. I had
# a bug where I confused squaring the number and
# multiplying by 2. I feel like spacial problems like
# this are best if you solve them first with pen and
# paper and then write out the code. I wouldn't have
# made my mistake and would have gotten to my answer
# faster because my logic for solving the problem
# was correct.