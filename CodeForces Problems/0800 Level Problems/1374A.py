# Problem 1374A.py

# You get 3 ints: x, y, and n.
# You must find the maximum integer K such that:
    # 0 <= K <= N
    # K % X == Y
    
# X, Y, N
# Find K.

# 7, 5, 12345
# K % 7 == 5, or 

# Let's say K = N

# This will result in 12345 % 7 = 4.
# The 4 is equal to 4/7. # We need to show a 5/7.
# Because we're already at the highest number we can use, we have to go down from 4/7 to 5/7.
# It's like going from floor 10 room 4 to floor 9 room 5. We want to be in a room called 5 at the highest floor possible

# To solve, we need to move a number of steps equal to the mod of k % y, where we set k to n. Then we need to move down another number which is equal to x/x - y/x. Or 7/7 - 5/7. This is 2/7, or 2 steps of a remainder value of 7.

# Thus, for the first example of 7 5 12345, K is 12345 - 6, or 12339

cases = int(input())


for x in range(cases):
    numbers = [int(i) for i in input().split()]
    x = numbers[0]
    y = numbers[1]
    n = numbers[2]
    
    remainder = n % x
    
    # if n % x == y, print n becuase k == n
    if remainder == y:
        output = n
        
    # if remainder less than y, we need to move
    # down "one floor" to the next int that has
    # the remainder value we need. We cannot go
    # up because the remainder is based on the 
    # largest value of n.
    elif remainder < y:
        #print("2")
        distance = abs(x - y)
        output = n - remainder - distance
    # if remainder bigger than y, we need to
    # move down, but not to the next floor, 
    # instead we're going to a lower number room
    # on the same floor (int). So we just move
    # down by a number equal to the distance
    # of n%x and the value of y, or
    # remainder minus y.
    elif remainder > y:
        #print("3")
        distance = abs(remainder-y)
        output = n - distance
    
    print(output)