# For this problem, case is not taken into consideration.
# Gets user input, converting case.
string1 = input().upper()
string2 = input().upper()
output = 0

# Saves original strings to their original indexes
originalList = [string1, string2]

# The function will take each string from the judge.
# Then convert the string to capital and compare the two
# If they are equal, it returns 0, otherwise nothing.


def alphabetize(position1, position2):

    alphaList = sorted(originalList)  # alphabetizes list.

    # gets index position of str1 in oritinalList
    position1 = originalList.index(string1)
    # gets index position of str1 in alphaList
    position2 = alphaList.index(string1)

    # if position of str1 doesn't change, then original list was alphabetize.
    # if original list is alphabetized, subtract 1 from output.
    # if positions changed, then list was not alphabetized. So we add 1 instead.

    if position1 == position2:
        return -1
    else:
        return 1

# First, check to see if the two strings are equal. If so, we are done.


if string1 == string2:
    output = 0

# If each string is not equal, then we alphabetize.

else:
    isAlphabetical = alphabetize(string1, string2)
    output = isAlphabetical

print(output)
