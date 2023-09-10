# Allow a user to add up to 5 cat names to a list.

cats = []
counter = 0

# Function adds punctuation to the list so it doesn't show up with block parens.


def listToWords(list):
    length = len(list)  # Get length of list
    names = ""
    for n in range(length):  # Loop for the length of the list, starting at 0.
        names = names + cats[n]
        if n <= (length - 3):  # So long as a number is less than 2nd from the last, add ,
            names = names + ", "
        elif n == (length - 2):  # if number is the second from the last, add , and
            names = names + ", and "
        elif n == length - 1:  # if number is the last, add .
            names = names + "."
    return names


print("Please make a list of 5 cats.")


goAhead = True
while (goAhead):

    counter = counter + 1  # Tells us which cat we're on

    print("Please name cat", counter)

    newCat = [input()]  # Gets name from user

    cats = cats + newCat  # updates the list with the new cat name

    if len(cats) >= 5:  # turns off loop when designated length of list is reached
        goAhead = False


# converts the list into a puntuated string. Not the best, but I wanted to try doing this.
finalList = listToWords(cats)
# prints final result without the block parens.
print("The names of your cats are:", finalList)
