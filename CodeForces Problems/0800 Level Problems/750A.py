# Problem: https://codeforces.com/problemset/problem/750/A
# Answer: https://codeforces.com/problemset/submission/750/228072549

# ******************************

# time taken to solve each problem is 5*i, where i is the position of the problem. Be careful of 0-index so we don't multiply 5*0.

# he has 4 hours to complete the problems and get to the party. So we should take the total time, subtract the amount of time needed to walk to the party, and the remaining amount of time is the time he has to solve the problems.

# 4 * 60 = 240 minutes.

# Output the number of problems he can solve in the time left over.

# ******************************

# Gets the number of problems[0] and minutes[1] from input. Put them into a list as int values.
startingValues = [int(i) for i in input().split()]

# Create output variable.
output = 0

# Assign the number of problems to the problems variable.
problems = startingValues[0]

# Assign the time needed to get to the party to time variable.
time = startingValues[1]

# Time to do problems is represented in the timeRemaining variable. 4 hours worth of minutes minus the time needed to get to party.
timeRemaining = 240 - time

# Loop through each problem and determine if there is time available to do it. If so, we add that to the output. If not, we do not add it to the output and we stop looping.

for n in range(problems):
    n += 1
    currentProblem = (n*5)
    divisbleCheck = timeRemaining // currentProblem
    
    if divisbleCheck > 0:
        timeRemaining -= currentProblem        
        output += 1
        currentProblem = 0
    else:
        break
        

print(output)










