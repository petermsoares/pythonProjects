string = input()  # Get string input from judge.

listOfString = list(string)  # Convert the string to a list.

listOfString[0] = listOfString[0].upper()  # Cap the first value of the list.

stringOfList = "".join(listOfString)  # convert the list back to a string.

print(stringOfList)  # print the string with the first letter capped.
