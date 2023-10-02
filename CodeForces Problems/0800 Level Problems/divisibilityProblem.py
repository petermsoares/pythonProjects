# To solve when A % B == 0
# This outputs to 0.

# To solve when A > B
# 13 // 9 results in an integer value of 1.
# because 9 goes into 13 1 time.
# We then add 1 to the remainder calculation, to get 2.
# And then multiply b times this new number, or 9 times 2 = 18.
# Then we can subtract the A value from this result.
# That is the number of moves up we need.

# To solve when A < B:
# Calculate the difference between B and A. That number
# is the output. Or, the number of times we need to do
# a+1. 



input1 = input() # number of comparisons we must do.

for n in range(int(input1)):
    newInput = input()
    values = newInput.split()
    output = 0
    
    a = int(values[0])
    b = int(values[1])
    
    if a % b == 0:
        output = 0
    
    elif a > b:
        intRemainder = a // b
        intRemainder += 1
        output = (intRemainder * b) - a
    
    elif a < b:
        output = b - a
    
    print(output)
    