string = input()
string = list(string)


# Removes characters that are not letters from the list.
n = 0
goAhead = True
while (goAhead):
    value = string[n]

    if value == " " or value == "{" or value == "}" or value == ",":
        del string[n]
    else:
        n += 1

    if n >= len(string):
        n = 0
        goAhead = False


# Sorts list in alpha order.
string.sort()

# Removes duplicate letters from list
goAhead = True
while (goAhead):

    # In situations where we have 0 letters in list, output 0.
    if len(string) == 0:
        output = 0
        break

    # In situations where we have 1 letter in list, output 1.
    if len(string) == 1:
        output = 1
        break

    # In situations where we have multiple letters in list, remove duplicate letters.
    if string[n] == string[n+1]:
        del string[n+1]

    else:
        n += 1

    if n+1 >= len(string):
        output = len(string)
        n = 0
        goAhead = False


print(output)
