# 1742B

# Ok to solve this problem I think we can sort the array and
# then check for duplicates. So long as there are no duplicates
# then the answer should be YES. if not, the answer should be NO.

testCases = int(input())

for case in range(testCases):
    lengthList = int(input())
    thisList = [int(i) for i in input().split()]
    
    thisList.sort()
    
    isIncreasing = False
    # My logic for using a Bool is to toggle the output state.
    # The loop below has a counter. The counter only goes up
    # if there exists more than 1 duplicate value in the list.
    # If there is a duplicate, we keep isIncreasing = False
    # because we are not increasing, but flat lining. Ie:
    # 1 2 2 2 3 is a flatline. So we fail in that case.
    
    # If there are no duplicates, then the counter never goes up.
    # If the counter never goes up, we toggle is Increasing from
    # False to True, which changes the output message.
    counter = 0
    for i in range(lengthList):
        
        if thisList.count(thisList[i]) > 1:
            counter += 1
        
    if counter == 0:
        isIncreasing = True
    
    if isIncreasing == True:
        output = "YES"
    else:
        output = "NO"
    
    print(output)

# Note, if this one works I'm going to be super happy because
# I was able to identify and solve this problem pretty fast.