sample = input()  # Get input from judge.
sample = sample.split(" ")  # split the string into a list based on spaces.
firstNum = int(sample[0])  # Get the first number from the list. Index 0.
lastNum = int(sample[-1])  # Get the last number fromt he list.

cList = input()  # Get the string of numbers from the judge.
cList = cList.split(" ")  # Split the string into a List of strings of numbers.

passingNum = int(cList[lastNum - 1])  # Assign the passing score.
passingSum = 0  # Counts number of passing scores.

for i in range(firstNum):
    # converts str to int and compares it to pass.
    if int(cList[i]) >= passingNum:
        # and checks if number is 0. Only positive numbers are added.
        if int(cList[i]) != 0:
            # if all conditions are met, add 1 to the sum of passing socres.
            passingSum += 1
# print out the sum of the passing scores.
print(passingSum)
