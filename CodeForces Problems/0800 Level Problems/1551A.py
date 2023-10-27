# 1551A

# Rules:
    # Must pay with coins valued at 1, or 2.
    # Must pay with equal coins of set 1 and 2:
        # in other words, if he pays with 5 1coin he must pay 5 2coin.
        # Ok ^ is wrong, but it must be as small as possible.
        
# Ie: if he has to pay a bill of $4 he can do:
    # 4 of 1. Abs difference is 4(c1) and 0(c2), or 4
    # 2 of 2 Abs difference is 0(c1) and 2(c2), or 2
    # 1 of 2, and 2 of 1. Abs difference is 1.
    
# This looks like a math/number theory problem.

# I think first we need to divide by 3 in order to get the total times
# coin1 and coin2 go into the number. In other words, because c1 and c2
# sum to 3, when we divide a number by 3 and get an integer returned
# that integer represents the number of 1coin and 2coin we get back.

# Then, we take the remainder after the division by 3 and determine if
# it's divisible by 2 and then 1.

testCases = int(input())

for case in range(testCases):
    thisNumber = int(input())
    
    coin1 = 0
    coin2 = 0
    
    bothCoins = thisNumber // 3
    
    coin1 += bothCoins
    coin2 += bothCoins
    
    remainder = thisNumber - (bothCoins*3)
    
    if remainder == 2:
        coin2 += 1
    elif remainder == 1:
        coin1 += 1
    
    
    output = str(coin1) + " " + str(coin2)
    print(output)
    