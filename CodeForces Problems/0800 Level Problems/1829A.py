# 1829A

testCases = int(input())
codeforces = list("codeforces")
thisString = ""


for case in range(testCases):
    counter = 0
    thisString = list(input())
    
    for i in range(10):
        if codeforces[i] != thisString[i]:
            counter += 1
    
    output = counter
    print(output)