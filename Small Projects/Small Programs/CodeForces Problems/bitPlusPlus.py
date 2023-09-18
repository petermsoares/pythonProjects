judgeInput = int(input())  # tells us number for loop
counter = 0  # sets counter to zero for looping.

for n in range(judgeInput):
    inputValue = input()  # get input from judge
    if "++" in inputValue:  # if string has ++ add 1
        counter += 1
    if "--" in inputValue:  # if string has -- strct 1
        counter -= 1

print(counter)  # after for loop is done, print coutner.
