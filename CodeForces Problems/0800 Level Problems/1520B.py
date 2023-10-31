# 1520B

# This question follows a pattern. For every power of 10, we can
# add up to 9 unique numbers.

# Ie: A number that is 10**1:
    # 1, 2, 3, 4, 5, 6, 7, 8, 9
# Ie: A number that is 10**2:
    # We account for numbers in 10**1 and can also have:
    # 11, 22, 33, 44, 55, 66, 77, 88, 99.

# This pattern repeats through 10**9.

# The answer is as follows:
# If the number is less than 10, the output is == the number.
# If the number is == 10, the output is == to 9. (because 1-9 count)

# If the number is greater than 10, we need to take the length
# of the number - 1 and multiply it by 9. This gives is the prior
# sets of ordinary numbers for each power of 10.

# Ie: for a number length 3, such as 111, we have:
# 1-9 (9 numbers) and 11-99 (9 numbers) already counted.
# or 9*(lenNumber - 1), or 9*2, or 18.

# Then we examine the number itself to see whether it is ordinary.
# If it is ordinary (meaning all the digits are the same) then
# we add the first digit to our total. This is because the first
# digit represents the total number of ordinary numbers not yet
# counted. Ie: 111 in the prior example we already counted
# numbers 1-100. But now we need to add 1 more for the 111.

# If the number is not ordinary we need to see whether the
# number that deviates is larger or smaller than the first
# digit. If it is larger, then we know an ordinary number composed
# of the first digit of the number exists. IE: 334 indicates 333
# exists in the range. So we can just add the first digit (3)
# to the total because that first digit signifies 3 ordinary numbers.

# If the number is not ordinary and the number that deviates
# is smaller, then we need to take the first digit and subtract 1.
# This number is the number of ordinary numbers counted.
# ie: 332 means that 333 cannot be counted. So 111 and 222 are the
# only numbers that exist within the 10**3 that are ordinary.

testCases = int(input())

for case in range(testCases):
    number = int(input())
    lenNumber = len(str(number))
    numberList = [int(i) for i in list(str(number))]
    output = 0
    
    if number == 10:
        output = 9
    elif number < 10:
        output = number
    elif number > 10:
        ordinaryNums = (lenNumber-1) * 9
        if numberList.count(numberList[0]) == lenNumber:
            ordinaryNums += numberList[0]
        else:
            for i in range(0, lenNumber-1):
                if numberList[i] > numberList[i+1]:
                    ordinaryNums += numberList[i] - 1
                    break
                elif numberList[i] < numberList[i+1]:
                    ordinaryNums += numberList[i]
                    break
        output = ordinaryNums        
    
    print(output)