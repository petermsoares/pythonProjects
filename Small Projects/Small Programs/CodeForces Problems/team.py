codeInput = int(input())
sum = 0
for i in range(codeInput):
    fSolution = input()
    problem = fSolution.count("1")
    if problem >= 2:
        sum += 1
print(sum)

"""
I like this solution instead of hard coding
possible winning solutions. If the team 
gains another memeber and the condition
upon which a problem can be solved is a
3/4 majority vote, then all I need to do
is adjust the if statement to be
problem >= 3. 

The original solution I had was to hard code
out all the possible winning conditions, but
this becomes inflexible for any future changes.

"""
