# 749A

# We are given a prime number.
# We need to determine how many sets of 2 and 3 can sum to that number.
# The answer is the largest set of 2s and 3s.

# For example:
    # input is 6.
    # You can make 6 from:
        # 3 + 3
        # 2 + 2 + 2
    
    # Because 2 + 2 + 2 uses more total numbers, that is our answer.

# I think the solution is as follows:
    # Even numbers: just divide by 2, that's the number of 2s we need.
    # Odd numbers: subtract 3 and then divide by 2.
    
primeNumber = int(input())

numberOfNumbers = 0
outputString = ""

if primeNumber % 2 == 0:
    numberOfNumbers = primeNumber // 2
    outputString = ["2"]*numberOfNumbers
    
else:
    numberOfNumbers = ((primeNumber-3) // 2) + 1
    outputString = ["2"]*(numberOfNumbers-1)
    outputString.append("3")
    
outputString = " ".join(outputString)

print(numberOfNumbers)
print(outputString)
    