# 1872B

# Ok so at first I couldn't think of a way to separate the trap
# locations and the trap timers. For some reason I wanted to 
# sort the traps, but that doesn't work or make sense.

# I think this problem can be solved by using two lists and appending
# values to the end of each list, then referencing them as we
# walk through the hallway.



testCases = int(input()) # get the test cases.

for case in range(testCases):
    trapCount = int(input()) # how many traps we have.
    
    trapLocation = []
    trapTimer = []
    
    for i in range(trapCount):
        trapValues = [int(i) for i in input().split()]
        
        if trapValues[0] not in trapLocation:
            trapLocation.append(trapValues[0])
            trapTimer.append(trapValues[1])
        else:
            indexLocation = trapLocation.index(trapValues[0])
            if trapTimer[indexLocation] > trapValues[1]:
                trapTimer[indexLocation] = trapValues[1]
    

    
    distance = 0
    countDown = 1000000
    areTrapsActive = False
    
    goAhead = True
    while(goAhead):
        
        if countDown > 1:
            distance += 1
            countDown -= 1
            
        else:
            goAhead = False
            
        if distance in trapLocation:
            areTrapsActive = True
            
            indexLocation = trapLocation.index(distance)
            
            if trapTimer[indexLocation] < countDown:
                countDown = trapTimer[indexLocation]
                
        if areTrapsActive == True:
            countDown -= 1
            
    
    
    output = distance

    print(output)
            