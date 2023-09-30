input1 = input() # total number of drinks.
input2 = input() # string containing the fractions of OJ per drink.

# Need to calculate the average volume of OJ based on total n drinks.

percentages = input2.split() # makes list of percentages.
total = 0

for n in range (int(input1)):
    total += int(percentages[n]) # get the total from the list of n
    

output = total/int(input1) # get the average: total count / n drinks
print(output) # print answer

# This solution is correct for this problem.