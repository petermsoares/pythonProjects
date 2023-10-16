# Problem: https://codeforces.com/problemset/problem/432/A
# Answer: https://codeforces.com/problemset/submission/432/228365034

# *

# Each student can compete up to 5 times.
# Each team consists of 3 people. 
# One person may only join one team.

# The first line has two numbers:
    # n = number of people available to pick from.
    # k = number of times we want our teams to compete
# The second line has one number:
    # y = number of times that person has competed already.

# The President wants our school to compete K number of times. Determine based on the candidate list (y) whether we can meet the president's expectations.

# To solve sort the candidates in order of attempts they've made. Then break the candidates into teams of 3 and test how many total attempts each team can make. Note: this number is linked directly to how many attempts the person with the most attempts on the team has made.

# Check to see if the team can make the attempts requested, and if so, add 1 to the output variable. If the team cannot meet the attempts requested, then we don't add that team.

# *

firstInput = [int(i) for i in input().split()]

availablePeople = firstInput[0]
targetAttempts = firstInput[1]

cList = [int(i) for i in input().split()]
cList.sort()



output = 0
def teamChecker(member1, member2, member3):
    attempts = 0 # keeps track of attempts
    output = 0 # keeps track of whether team can meet attempts.
    
    for n in range(targetAttempts):
    
        # This is the team we are currently testing
        team = [member1,member2,member3]
        
        # If the team can compete, add 1 to the attempts that team can make and add 1 to the highest person's attempt count.
        if member3 < 5:
            member3 += 1 
            attempts += 1 
        
        # If we have looped for the number of attempts requested by the President... and
        if n == targetAttempts-1:
            # If attempts == our target, then we add 1 to the output, signifying this team of unique candidates can meet the problem's condition.
            if attempts == targetAttempts:
                output += 1
    
    # Return output, which is either a 1 or a 0            
    return output

# Determine the number of times we should try and loop. If we only have enough to make 1 team of 3 people, we only call our function one time and consider that team.
numberOfTeams = availablePeople // 3

for x in range(numberOfTeams):
    # We do a try/except because sometimes we won't have enough people to fill a team.
    try:
        # call the function to consider whether attempts are met.
        output += teamChecker(cList[0],cList[1],cList[2])
        # Regardless of outcome, delete these candidates from the list and move onto the next candidates.
        del cList[0], cList[1], cList[2]
        
    # If we don't have enough for a team, just continue on. This is going to be for the last iteration of the loop anyway so it will terminate if we trigger the try/except.
    except:
        pass
        
print(output)