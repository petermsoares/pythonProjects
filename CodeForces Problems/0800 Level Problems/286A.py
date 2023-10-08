# Exception: When home team's color matches guest's
# color, the host team will wear its own guest
# uniform instead of its home uniform.

# For each team the color of the home and away
# uniforms are different.

# There a N number of teams.
# There are N*(N-1) games played in the championship.
# Each team invites each other team to its stadium.

# Colors are listed as integers.

# The first line has a number between 2 and 30,
# inclusive, representing the number of teams.

# Every line after N represents the colors of
# uniforms that a team wears. The first is the
# home number and the second is the guest number.

# Question: how many times during the championship
# is a host team going to put on the guest uniform?

# Essentially, if any of the numbers in the first columm match.
numberOfTeams = input()

homeColors = []
awayColors = []


for n in range(int(numberOfTeams)):
    thisTeam = input()
    thisTeam = thisTeam.split()

    homeColors.append(thisTeam[0])
    awayColors.append(thisTeam[1])

awayCounter = 0

for i in range(int(numberOfTeams)):

    # This counts the number of times the number
    # in the left column appears in the right, and
    # then it adds count to the awayCounter.

    awayCounter += awayColors.count(homeColors[i])

    # However, there might be a case where the
    # home and away colors of a team are the same.
    # We check for this below:

    if awayColors[i] == homeColors[i]:
        awayCounter -= 1


print(awayCounter)
