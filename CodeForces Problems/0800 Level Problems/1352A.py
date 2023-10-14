# Problem: https://codeforces.com/problemset/problem/1352/A
# Answer: https://codeforces.com/problemset/submission/1352/228094823


# First input is number of cases we have to consider.

# The next inputs will be numbers.

# Your job is to output two lines based on each input:
# First, the number of "round" numbers.
# Second, a string of the list of such numbers.

# Ie: 5009:
# 2
# 5000 9

# Numbers that are one int long are always round and always output to 1.

cases = input()

for n in range(int(cases)):

    number = input()

    # Check if number is 1 digit long. If so, output 1.
    if len(number) == 1:
        print(1)
        print(number)
    # If number is > 1, loop through it as a list.
    else:
        # list of individual digits of our number.
        number = list(number)

        # length of the list
        length = len(number)

        # making an empty list to append to later
        outputList = []

        # counter tracking number of "round" numbers
        roundCounter = 0

        for i in range(length):
            # only do this if the number is not 0
            if number[i] != "0":

                # create the number based on its 10s place.
                # ie, 5 in 532 is 500.
                addNumber = number[i] + ("0"*(length-(i+1)))

                # append this number to the outputList variable.
                outputList.append(addNumber)

                # increase the round counter by 1 if we find one.
                roundCounter += 1

        # After looping, convert List into a string of numbers.
        # separated by spaces.
        outputList = " ".join(outputList)

        # print the count of "round" numbers.
        print(roundCounter)

        # print the string of round numbers separated by spaces.
        print(outputList)
