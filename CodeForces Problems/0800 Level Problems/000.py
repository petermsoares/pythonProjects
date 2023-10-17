# Problem: https://codeforces.com/problemset/problem/1367/A
# Answer: https://codeforces.com/contest/1367/submission/228610463

# *
# To solve, the answer will be all of the odd
# index values + the last two index values.

cases = int(input())

for x in range(cases):
    
    string = []
    word = list(input())
    # Append the odd letters in the string, or the
    # even numbers of the list because 0 index
    # offsets by 1. 
    for i in range(0, len(word)-2, 2):
        string.append(word[i])
    
    # Append the last 2 letters to the list.
    string.append(word[-2])
    string.append(word[-1])
    
    # turn list into a string.
    string = "".join(string)
    
    # output the answer
    print(string)
   
        
    
    
    
    
    