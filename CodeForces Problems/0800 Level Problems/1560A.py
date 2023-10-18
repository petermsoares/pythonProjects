# Problem: https://codeforces.com/problemset/problem/1560/A
# Answer: https://codeforces.com/contest/1560/submission/228630538

# *
# I don't like my answer to this problem. I feel
# like I am mixing up ideas. 

cases = int(input())

for x in range(cases):
    counter = 1
    position = 1
    number = int(input())
    goAhead = True
    while(goAhead):
        sPosition = str(position)
        
        if counter >= number:
            if position % 3 != 0:
                if sPosition[-1] != "3":
                    break
        
        if position % 3 == 0 and position != 0:
            position += 1
            
        elif sPosition[-1] == "3":
            position += 1
            
        else:
            position += 1
            counter += 1 
    print(position)