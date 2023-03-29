
cfInput = int(input())  # get number of words to be entered from CF judge

for i in range(0, cfInput, 1):  # set for loop to run for input from judge

    word = input()
    if len(word) <= 10:  # if word <= 10, print word as normal
        print(word)

    else:  # if word is strictly greater than 10, do the following:
        # get the total number of characters between first and last letter. Or, total minus 2. Remmeber to convert the number to a string for concatination.
        wordLength = str(len(word)-2)
        firstLetter = word[0]  # get first letter of string
        lastLetter = word[-1]  # get last letter of string
        # String concatination for answer.
        print(firstLetter + wordLength + lastLetter)
