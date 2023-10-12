# Problem: https://codeforces.com/problemset/problem/155/A
# Answer: https://codeforces.com/problemset/submission/155/227933086

# The first input is the number of contests taken.
# The second input is the list of contests taken.
# The list contains int numbers.

# If the n+1 number is strictly greater than the highest previous number or strictly lower than the lowest previous number, we add 1 to the counter.

# Output the counter.

# Number of rounds
rounds = int(input())

# Scores
scores = [int(i) for i in input().split()]

# Amazing Performances counter
counter = 0
lowestScore = 0
highestScore = 0

# Edge case: if he only takes 1 test we don't need to loop.
if len(scores) == 1:
    print(counter)
    quit()

# Edge case: if he takes only 2 tests and they're different, then he has at least 1 Amazing Score.
if len(scores) ==  2:
    if scores[0] != scores[1]:
        counter += 1
        print(counter)
        quit()
    else:
        print(counter)
        quit()

# While loop checks the first numbers in the list for duplicates. Once it finds a difference, we assign the differing numbers to the highestScore and LowestScore variables. 

# We also keep track of the number of duplicates we've counted. This way, we can begin our comparison loop at that index value instead of having to recount all the numbers again.
dupcounter = 0
goAhead = True
while(goAhead):
    if scores[dupcounter] != scores[dupcounter + 1]:
        if scores[dupcounter] > scores [dupcounter +1]:
            highestScore = scores[dupcounter]
            lowestScore = scores[dupcounter + 1]
            counter += 1 # Add 1 to counter because num differ.
            goAhead = False
        else:
            highestScore = scores[dupcounter + 1]
            lowestScore = scores[dupcounter]
            counter += 1 # Add 1 to counter because num differ.
            goAhead = False
            
    dupcounter += 1
    
    # If none of the numbers are different, we exit the loop.
    if dupcounter >= len(scores)-1:
        goAhead = False

# Here, we begin looping based on where the dupcounter stopped and proceed through the entire list. If a number is greater or less than the prior high/low score, we add 1 to the counter and adjust the highestScore or lowestScore variable.
try:
    for n in range(dupcounter, rounds-1):
    
        if scores[n+1] > scores[n]:
            if scores[n+1] > highestScore:
                counter += 1
                highestScore = scores[n+1]
                
        elif scores[n+1] < scores[n]:
            if scores[n+1] < lowestScore:
                counter += 1
                lowestScore = scores[n+1]
except:
    pass
    
print(counter)
