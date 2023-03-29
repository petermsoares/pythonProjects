judgeInput = int(input())
successfulProblems = 0
rightAnswers = ["1 1 0", "1 0 1", "0 1 1", "1 1 1"]

for i in range(0, judgeInput, 1):
    problemSolve = input()
    if problemSolve in rightAnswers:
        successfulProblems = successfulProblems + 1
    else:
        continue

print(successfulProblems)
