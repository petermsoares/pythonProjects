# Thoughts on solving this problem:
"""
A soldier wants to buy bananas. Each banana
costs n*k. K is the base value and n is the
number of the banana. 

If he wants to buy 3 bananas at $2 each:
Banana 1 = $2 (1*2)
Banana 2 = $4 (2*2)
Banana 3 = $6 (3*2)

num1 = the cost of the 1st banana in dollars.
num2 = the dollars the soldiers has.
num3 = the bananas the solder wants.

To solve, let's count up to the total number
of bananas the solder wants based on the cost,
figure out the cost, and then subtract the
soldier's funds from the cost to get the number
of dollars he needs to borrow to make his purchase.

If he doens't need to borrow money, output nothing.

"""

input = input()  # Gets numbers from judge.

# Turns string of numbers into list of numbers.
list = [int(s) for s in input.split() if s.isdigit()]

cost = list[0]  # Cost of first Banana
money = list[1]  # Money soldier has
goal = list[2]  # Number of bananas soldier wants

thisBanana = 0  # counter for cost of bananas

totalCost = 0  # counter for total cost of bananas
moneyToBorrow = 0  # money solder needs, if applicable

for n in range(goal):
    thisBanana = cost * (n+1)  # cost * nBanana. +1 to offset starting at 0.
    totalCost += thisBanana  # add thisBanana to the totalCost

if money >= totalCost:  # If soldier has enough money.
    print(0)  # Print nothing.
else:  # if soldier needs money.
    # calculate abs value of money needed.
    moneyToBorrow = abs(money-totalCost)
    print(moneyToBorrow)  # print the value of the money needed.
