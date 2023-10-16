# Problem: https://codeforces.com/problemset/problem/758/A
# Answer: https://codeforces.com/contest/758/submission/228453123

# *

# The idea is to take the person who has the most money, 
# and make all the people on the list have as much money 
# as he does. Then, calculate the total amount of money needed.

# We can sort the people in order based on how many dollars 
# they have. Then we can .count() the number of people below 
# the highest. Then add the difference between that group of 
# people and the highest group until there are no groups left.

# *

cases = int(input())
people = [int(i) for i in input().split()]

people.sort()

highestPerson = people[-1]
output = 0

# There is an edge case where we only have 1 person in the kingdom.
# In this case, just output 0 and quit the program.

if len(people) == 1:
    print(0)
    quit()

# Ok this didn't work, it took too much time. The reason is that
# I thought each person could only have 100 dollars, but the fact
# pattern said up to 100 people. So I need to go through each index
# Instead. I'm keeping the comment below for reference of what
# not to do in this situation.
    # This takes the highest person's wealth, subtracts 1 from it
    # And counts the number of people who have such wealth.
    # It then multiplies that count by the difference between that
    # person's wealth and the highest person's wealth to get
    # the total number of dollars needed to make that group equal
    # to the highest person. This is inefficient because we are
    # sometimes counting groups that might not exist, but because
    # the cases are small we can use this solution.

n = -1
goAhead = True
while(goAhead):
    n += 1
    person = people[n]
    
    difference = highestPerson - person
    
    output += difference
    
    if person == highestPerson:
        goAhead = False
        
    if n == (len(people)-2):
        goAhead = False
print(output)
    