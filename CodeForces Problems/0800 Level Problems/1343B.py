# Problem: https://codeforces.com/contest/1343/problem/B
# Solution:

# *

# All the other iterations of even values of n can solve the problem, while the other even iterations fail.

# ie, 2, 6, 10 fail.
# but 4, 8, 12 pass.

# I think the odd section of the array can be found by
# taking the sum of the even array and then subtracting
# smaller values of the odd values starting at n+1.

# *

testCases = int(input().strip())



for x in range(testCases):
    n = int(input())
    buildArray = True
    
    evens = []
    odds = []
    
    # if our even input is in an odd placement, skip.
    if n % 4 > 0:
        output = "NO"
        buildArray = False
    
    # else, find solution
    else:
        for i in range(2, n+1, 2):
            evens.append(i)
    
    if buildArray == True:
        print("YES")
        for i in range(1, n, 2):
            odds.append(i)  
        
        odds[-1] += n // 2    

        output = evens + odds
        
        for x in range(len(output)):
            output[x] = str(output[x])
        output = " ".join(output)        
    
    print(output)
