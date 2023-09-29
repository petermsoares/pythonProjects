yCounter = 0  # counts y position of where 1 is from center
xCounter = 0  # counts z position of where 1 is from center
move = 0  # sum of moves needed to get 1 in middle.

for n in range(5):
    judgeInput = input()

    if "1" in judgeInput:  # if 1 is in the string
        xCounter = judgeInput.index("1")  # find x position of 1 on index
        # divide by 2 because empty strings add empty index values
        xCounter = (abs(xCounter - 4))/2
        yCounter = abs(n - 2)  # y position away from center.

# add the x and y positions of 1 needed to get to center.
move = int(yCounter + xCounter)
print(move)
