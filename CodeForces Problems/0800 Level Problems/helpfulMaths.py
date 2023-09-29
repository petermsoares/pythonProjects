string = input()

# Will return all string values except for the + sign.
# This problem assumes only strings 1, 2, 3, and + are used.
# This solution fails if you use numbers greater than 9. 34+55 will be 3+4+5+5.
addSign = [i for i in string if i != "+"]

# Sort the numbers after removing + signs.
addSign.sort()

for n in range(len(addSign)):

    # for the index values, except the last, concatinate "+"
    if n < len(addSign) - 1:  # makes sure we don't add + to last index
        addSign[n] = str(addSign[n]) + "+"

addSign = "".join(addSign)  # converts List to String

print(addSign)
