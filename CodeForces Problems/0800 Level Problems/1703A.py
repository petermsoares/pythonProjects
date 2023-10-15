# Problem: https://codeforces.com/problemset/problem/1703/A
# Answer: https://codeforces.com/problemset/submission/1703/228354225

# *

# To solve we should take the string, change the case, and then do a comparison to the string "YES". For my solution, i'll convert the string to all upper case letters and then do the comparison.

# *

cases = int(input())

for x in range(cases):

    word = input().upper()

    if word == "YES":
        print("YES")
        
    else:
        print("NO")