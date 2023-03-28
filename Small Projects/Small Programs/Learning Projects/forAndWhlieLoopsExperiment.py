"""
Experiment to make a while loop
do the same task as a for loop to
count all integers within a range
from 0 to n, where n is 100 in this
example.
"""
forTotal = 0
for num in range(101):
    forTotal = forTotal + num
print("For Loop Total: " + str(forTotal))

whileTotal = 0
whileCount = 1
while whileCount < 101:
    whileTotal = whileTotal + whileCount
    whileCount = whileCount + 1
print("While Loop Total: " + str(whileTotal))

if whileTotal == forTotal:
    print("Victory")
else:
    print("Failure")
