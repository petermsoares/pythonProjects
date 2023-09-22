# Make a program that extracts unique characters from string.

string = input()  # Get string from judge.

startingLetters = list(string)  # turn string into list.
removeLetter = ""  # letter we will remove from startingLetters
uniqueLetters = []  # list we will add unique letters to.
uniqueString = ""  # string we will store unique letters in
uniqueStringLength = 0  # length of string containing unique letters

goAhead1 = True
while (goAhead1):

    removeLetter = startingLetters[0]  # gets letter to be removed
    uniqueLetters.append(removeLetter)  # places that letter in list.

    goAhead2 = True
    while (goAhead2):
        # if the letter is in the list, remove all copies
        if removeLetter in startingLetters:
            startingLetters.remove(removeLetter)
        # if the letter is not in the list, move on.
        else:
            goAhead2 = False
    # if the startingLetters list is empty, stop looping
    if startingLetters == []:
        goAhead1 = False

uniqueString = "".join(uniqueLetters)  # creates a string of unique letters.
uniqueStringLength = len(uniqueString)  # gets length of that string.

if uniqueStringLength % 2 == 0:  # if string is even, print CWH
    print("CHAT WITH HER!")
else:  # if string is odd, print IH.
    print("IGNORE HIM!")
