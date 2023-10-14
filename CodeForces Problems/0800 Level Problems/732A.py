# Problem: https://codeforces.com/problemset/problem/732/A
# Answer: https://codeforces.com/problemset/submission/732/228205322

# *************************

# P has two kinds of dollars in his wallet:
    # An unlimited number of 10 bills, and
    # One bill worth between 1 and 9.

# P needs to purchase shovels from a store.
# The first input represents the price of a shovel, followed by the value of P's unique bill worth between 1 and 9.
# 117 3 ==> A shovel costs 173 and he has 1 bill worth $3 in his pocket.

# Output the minimum number of shovels P must buy so that he can pay without receiving any change.

# To solve, we check the following:
    # Is the price of the shovel % 10 == 0?
    # If yes, output that shovel's number.
    
    # If no, is the price of the shovel % 10 minus the unique dollar's value == 0? If yes, output the shovel's number. 
    # If no, go on to the next shovel.

# *************************

startingValues = [int(i) for i in input().split()]

shovelPrice = startingValues[0]
uniqueDollar = startingValues[1]
n = 1
output = 0

goAhead = True
while(goAhead):
    
    if (shovelPrice * n) % 10 == 0:
        output = n
        goAhead = False
    
    if ((shovelPrice * n) % 10) - uniqueDollar == 0:
        output = n
        goAhead = False
    n += 1

print(output)















