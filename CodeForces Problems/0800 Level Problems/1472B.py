# 1472B

# I think we can solve this by looking at the length of the string
# and determining how many of 1 and 2 are in the string.

# If the length of the string is 1, the answer is always NO because
# a single candy cannot be divided.

# If the length of the string is 2, the answer is YES if each candy
# is the same. Otherwise the answer is no.

# If the length of the string is greater than 2
    # and if the length of the string is ODD:
        # Yes if the count2 is odd and less than length of string.
        # No otherwise.

# If the length of the string is greater than 2
    # and length of string is EVEN:
        # Yes if count 1 or count 2 == length of string.
        # Yes if count1 or count2 is 1/2 length of string.
        # No otherwise.
        
testCases = int(input())

for case in range(testCases):

    lengthOfList = int(input())
    halfLength = lengthOfList / 2
    
    numbersInList = [int(i) for i in input().split()]
    
    count1 = numbersInList.count(1)
    
    count2 = lengthOfList - count1
    
    output = ""
    
    if lengthOfList == 1:
        output = "NO"
        
    elif lengthOfList == 2:
        if count1 == lengthOfList or count2 == lengthOfList:
            output = "YES"
        else:
            output = "NO"
            
    # For numbers greater than 2 that are ODD:        
    elif lengthOfList % 2 != 0:
        if count2 % 2 != 0 and count1 > 0:
            output = "YES"
        else:
            output = "NO"
    
    # For numbers greater than 2 that are EVEN:
    # Note, I added 2 rules in this code to the above-mentioned
    # notes to make it work.
    elif lengthOfList % 2 == 0:
        if count2 % 2 == 0: # This rule is the first added.
            if count1 == lengthOfList or count2 == lengthOfList:
                output = "YES"
            elif count1 == halfLength or count2 == halfLength:
                output = "YES"
            elif count1 % 2 == 0: # This rule is the second.
                output = "YES"
            else:
                output = "NO"
        else:
            output = "NO"
            
    print(output)