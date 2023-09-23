string = input()  # get input from judge.

list = list(string)  # convert string into a list

capList = []  # empty list for holding upper letters
lowList = []  # empty list for holding lower letters

for i in range(len(string)):
    if list[i].isupper():  # if letter is capital, add to cap list.
        capList.append(list[i])
    else:  # else, add letter to low list.
        lowList.append(list[i])

if len(capList) > len(lowList):  # if cap list is bigger than low list
    output = string.upper()  # make the input string all caps.
else:  # otherwise make the string lower case.
    output = string.lower()

print(output)  # print the output.
