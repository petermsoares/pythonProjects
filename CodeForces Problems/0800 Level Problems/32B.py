# Problem: https://codeforces.com/problemset/problem/32/B
# Answer: https://codeforces.com/problemset/submission/32/228366551

# *

# .     == 0
# -.    == 1
# --    == 2

# To solve, I think we can turn the string into a list, and loop through the list for the given characters.

# *


borzeCode = list(input())

lenB = len(borzeCode)
output = []

# Start counter at -1 to start at 0 index at beginning of the loop where we add n += 1. Also, because we are increasing the counter at the beginning of the loop and not the end, we can check n==lenB - 1 at the end of each loop to determine if we should exit.
n = -1
goAhead = True
while(goAhead):
    n += 1
    
    if borzeCode[n] == ".":
        output.append("0")
        
    elif borzeCode[n] == "-":
    
        if borzeCode[n+1] == ".":
            output.append("1")
            n += 1
        else:
            output.append("2")
            n += 1
            
    if n == lenB - 1:
        goAhead = False

output = "".join(output)
print(output)