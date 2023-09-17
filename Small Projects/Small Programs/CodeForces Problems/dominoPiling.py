sample = input()  # Get input from judge.
sample = sample.split(" ")  # split the string into a list based on spaces.
firstNum = int(sample[0])  # Get the first number from the list. Index 0.
lastNum = int(sample[-1])  # Get the last number fromt he list.

totalSquares = firstNum * lastNum
answer = totalSquares // 2
print(answer)
