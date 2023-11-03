# 1472A

# Ok I am a fking idiot. For some reason I thought to include
# a counter for both the cuts to the width and the length(heigh)
# side of the paper. I thought I could keep track of each and
# add them together at the end, but this overcomplicated the
# problem and caused some test cases to fail.

# When I removed the hCoutner from the code and used the wCounter
# to keep track of everything, the problem worked instantly.

# This is a problem that should have taken me maybe 8 minutes, but
# I spent over an hour on it because I didn't properly understand
# how to frame things.

testCases = int(input())

for case in range(testCases):
    
    whn = [int(i) for i in input().split()]
    
    w = whn[0]
    h = whn[1]
    n = whn[2]
    
    wCounter = 1
    #hCounter = 1
    totalCuts = 0
    
        
    while(w % 2 == 0):
        w = w / 2
        wCounter *= 2
    
        
    while(h % 2 == 0):            
        h = h / 2
        wCounter *= 2


    if wCounter == 1:
        totalCuts = 1
    else:
        totalCuts = wCounter #+ hCounter
        
    
    if totalCuts >= n:
        output = "YES"
    else:
        output = "NO"
   
    print(output)