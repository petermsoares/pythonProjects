# 1311A

# We can add an odd number to A
# We can subtract an even number from A

# The goal is to turn A into B.

# My intuition is as follows:
# 1. If numbers are equal, output 0.

# 2. If A is bigger than B:
    # A even and B even, then 1 move for the even subtraction.
        # 6 to 2, move 1 unit of 4
    # A even and B odd, then 2 moves.
        # 6 to 1, move 1 unit of 6 down and 1 unit of 1 up.
    # A odd and B even, then 2 moves
        # 5 to 2, move down 1 unit of 2.
    # A odd and b odd, then 1 move.
        # 5 to 3, move down 1 unit of 2.
# If both numbers are odd or both even, total moves == 1
# if both numbers differ, total moves == 2
# if both numbers same, total moves == 0
    
# 3. If A is smaller than B:
    # A even and B even: 2
    # A even and B odd: 1
    # A odd and B odd: 2
    # A odd and B even: 1
# If both numbers are odd or even, total moves == 2
# If both numbers differ, total moves == 1
# If both numbers are the same, total moves == 0

# So, first determine whether numbers are the same or not.
# Then determine whether A is bigger than B.
# Then determine odds vs evens.

testCases = int(input())

for case in range(testCases):
    ab = [int(i) for i in input().split()]
    
    a = ab[0]
    b = ab[1]
    
    aEven = True
    bEven = True
    
    if a % 2 == 0:
        aEven = True
    else:
        aEven = False
    
    if b % 2 == 0:
        bEven = True
    else:
        bEven = False
    
    if a == b:
        totalMoves = 0
    
    elif a > b:
        if aEven != bEven:
            totalMoves = 2
        else:
            totalMoves = 1
    
    elif a < b:
        if aEven != bEven:
            totalMoves = 1
        else:
            totalMoves = 2
    
    output = totalMoves
    
    print(output)
            
    

