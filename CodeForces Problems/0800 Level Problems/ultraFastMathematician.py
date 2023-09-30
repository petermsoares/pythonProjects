# Each number is made up of 0s and 1s.
# If the index value of the two numbers is the same, the output will be 1.
# If the numbers differ, the output is 0.

string1 = input() # get the first input in form of a string.
firstNumber = list(string1) # String into List.

string2 = input() # get 2nd input in form of a string.
secondNumber = list(string2) # String into List.

outputNumber = [""]*len(string1)


for i in range(len(firstNumber)):
    
    # Get index value of first and second numbers.
    number1 = firstNumber[i]
    number2 = secondNumber[i]
    
    # Compare the two numbers.
    # Assigned values are strings so we can use .join later.
    if number1 == number2:
        outputNumber[i] = "0"
    else:
        outputNumber[i] = "1"

outputNumber = "".join(outputNumber)
    
print(outputNumber)