# Problem 1676

testCases = int(input())

for case in range(testCases):
    totalBoxes = int(input())
    listofBoxes = [int(i) for i in input().split()]
    
    listofBoxes.sort()
    candiesEaten = 0
    
    for i in range(1, len(listofBoxes)):
        candiesEaten += abs(listofBoxes[i] - listofBoxes[0])
    
    output = candiesEaten
    print(output)