# Problem: https://codeforces.com/problemset/problem/427/A
# Answer: https://codeforces.com/problemset/submission/427/227736425

# One police officer and respond to one crime.
# If no police officer is available, the crime goes unpunished.
# Find number of unpunished crimes.

# First input is number of events.
# If an integer is -1, a crime happens.
# If an integer is positive, an officer is hired based on that num.

# Note: the police department starts off with 0 officers.
# so if you get  -1 -1 1, then 2 unpunished crimes have
# happened even though one officer was hired.

# The events variable will track the number of events,
# specifically the crimes and the department's ability
# to respond to such crimes.
events = int(input())

# The crimeAndPunishment variable houses a list of the
# various events that will happen as ints.
crimeAndPunishment = [int(i) for i in input().split()]

# To solve this problem I will keep track of a reservoir
# of available officers. If there are none available, we
# will add 1 to the unpunished crime counter. But if there
# is an officer available, we will punish the crime.
availableOfficers = 0
unpunishedCrimes = 0
for n in range(len(crimeAndPunishment)):

    # If the integer is a non-negative number, then the number
    # represents the number of officers we add to the department.
    # We add that number to our available officers.
    if crimeAndPunishment[n] >= 1:
        availableOfficers += crimeAndPunishment[n]

    # If the integer is a negative number, then a crime happened.
    # Only one crime can happen at a time.
    # First we check to see if we have available officers. If we
    # have zero officers, then we add 1 to unpunished crimes. If
    # we have available officers, we subtract one officer from the
    # reserve list so he can investigate the crime.
    if crimeAndPunishment[n] == -1:
        if availableOfficers == 0:
            unpunishedCrimes += 1
        elif availableOfficers > 0:
            availableOfficers -= 1
            # Note: the reason we don't subtract 1 from the reserve
            # is because doing so might create a negative reserve
            # of officers. In this problem the lowest the
            # reserve can go is 0. So first check to see if the
            # reserve has at least 1 person in it (reserve > 0)
            # and if it does, then take that person out because
            # he is responding to the crime. If nobody is in
            # reserve, just keep the availableOfficers number
            # at 0.

# Print the number of unpunished crimes that happen,
# or the crimes that happen where officers aren't
# available to respond.
print(unpunishedCrimes)

# Other possible problems you can make from this one:
# What is the total remaining available reserve of officers?
# What if the reserve is allowed to be negative, how will the
# unpunished crimes number be affected?
# Maybe adding in the random module to see if when an officer
# responds to a crime if he fails?
