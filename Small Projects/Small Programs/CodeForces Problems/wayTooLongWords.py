l = int(input())
counter = 0
cpuChoice = ""

goAhead = True
while (goAhead):
    cpuChoice = input()

    if len(cpuChoice) > 10:
        fLetter = cpuChoice[0]
        lLetter = cpuChoice[-1]
        distance = str(len(cpuChoice) - 2)
        print(fLetter + distance + lLetter)
    else:
        print(cpuChoice)

    counter = counter + 1
    if counter == l:
        goAhead = False
