# We can solve this problem using ascii character codes for the letters between a and z. Let's convert the entire string one case and then do a comparison.

# first input is number of letters the string contains.
lettersLength = int(input())

# take the string and convert it to lower case.
letters = input().lower()


# Turn the string into a list.
letters = list(letters)

# The ascii values for letters between a and z are 97 through 122
# Loop through the string and look for the ascii code number for each list item


asciiValue = 97  # represents the lower case letter "a"
i = 0  # represents our index counter for our list.

# define condition to keep the loop on
goAhead = True

# go through the loop looking for letter matches
while (goAhead):

    # if we don't find a match, move on to next index
    if asciiValue != ord(letters[i]):

        # Check to see if we have looked at each letter in the string. If we have and still haven't found a match, then the word doesn't contain all letters needed to make a pangram and we exit the loop.

        if i == (lettersLength-1):
            output = "NO"
            goAhead = False

        # After we do the above-mentioned check, we add +1 to i to go to the next index.
        i += 1

    # if we do find a match, reset i counter to loop through the string again, and increase the ascii counter by 1 to check for that ascii character.
    elif asciiValue == ord(letters[i]):
        i = 0
        asciiValue += 1

    # if we have looked at the last ascii value and the goAhead is still True, that means we have found all the characters of the alphbt in our string. Thus, we can make the output a "YES" and break out of the loop.
    if asciiValue == 123 and goAhead == True:
        output = "YES"
        goAhead = False

print(output)
