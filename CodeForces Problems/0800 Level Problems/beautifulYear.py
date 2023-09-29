input = "1987"
print("Starting year:", input)

startingYear = int(input)
thisYear = startingYear + 1

goAhead = True
while (goAhead):
    # Seting up basic conditions of the loop:
    duplicate = False  # Sets duplicate checker to False at start of loop
    # gets the length of the year we're looping through
    yrLen = len(str(thisYear))
    # turns the int into a string and then into a list.
    thisYear = list(str(thisYear))
    print(thisYear)

    # Code that analyzes whether characters are unique.
    for i in range(yrLen):  # loop through each character of the number
        # if the characters are duplicates
        if thisYear.count(thisYear[i]) > 1:
            duplicate = True  # duplicate variable set to True
            # Turns thisYear from a List to an Int
            thisYear = int("".join(thisYear))
            thisYear += 1  # Add 1 to the current year in the loop.
            break  # break out since we found a duplicate.
    if duplicate == True:  # if no duplicate values are found
        # turn the list to a string and then to an int.
        thisYear = int("".join(thisYear))
        goAhead = False  # turn the loop off since we found a unique number

output = startingYear - thisYear
print("Expected output is 2013")
print(output)
