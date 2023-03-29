judgeInput = int(input())  # takes input from judge to specify number of loops.
successfulProblems = 0  # sets number of output to 0.
# possible winning combinations
rightAnswers = ["1 1 0", "1 0 1", "0 1 1", "1 1 1"]

for i in range(0, judgeInput, 1):
    problemSolve = input()  # takes input from judge and runs through loop.
    if problemSolve in rightAnswers:  # if input is one of winning combinations move on
        # add one to total winning combination count
        successfulProblems = successfulProblems + 1
    else:
        continue

# print out the total number of winning combinations.
print(successfulProblems)
