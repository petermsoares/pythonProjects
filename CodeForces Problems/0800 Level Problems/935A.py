# 935A -- Fafa and his Company

# There must be an equal number of teammembers per team, and
# the sum of team members and team leaders must equal N.

# 



# workers/leaders must have a mod of 0.
# workers + leaders must equal N

# I am going to try and solve with an iteration answer as a hard-math
# solution isn't coming to me at first glance.

numberOfPeople = int(input())
counter = 0

for n in range(1, numberOfPeople):
    leaders = n
    workers = numberOfPeople - n
    
    if (workers % leaders) == 0:
        counter += 1

output = counter
print(counter)