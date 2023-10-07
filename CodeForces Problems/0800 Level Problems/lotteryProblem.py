# we want to divide the input by the largest number first.
# And if there is a remainder we want to move onto the second
# largest number and so on until we reach one.

withdrawn = int(input())
output = 0   # Number of individual bills.

# If the withdraw request is divisible by 100:
# We add the number of times withdrawn // 100 happens to the output.
# Then we subtract the amount of 100s from the withdrawn amount.
# This way on next pass, we're examining the remainder.
if withdrawn // 100 >= 1:
    output += withdrawn // 100
    withdrawn -= output * 100
if withdrawn // 20 >= 1:
    output += withdrawn // 20
    withdrawn -= (withdrawn//20) * 20
if withdrawn // 10 >= 1:
    output += withdrawn // 10
    withdrawn -= (withdrawn//10) * 10
if withdrawn // 5 >= 1:
    output += withdrawn // 5
    withdrawn -= (withdrawn//5) * 5
if withdrawn // 1 >= 1:
    output += withdrawn
print(output)

