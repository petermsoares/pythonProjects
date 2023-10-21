# Problem: 1520A

# The solution to this problem requires us to see
# if letters of a string are repeated after
# a new letter.

# ABA is NO
# AAB is YES
# AAABBBA is NO because A starts after B again.

# To solve scan each letter of the string.
# If a character hasn't been seen before add it to
# a list containing unique characters.
# Scan each letter and determine if it matches the
# previous letter. If it does, we are fine. If it
# does not, we need to check if it's a new unique.
# If it is a new uniuqe, we add it to the uniuqe list.
# If it is in the unique list, we output NO and stop.

# receives number and assigns to testCases
testCases = int(input())

# for the number of test cases we have, examine each:
for t in range(testCases):

    # receives length value and assigns to lenTasks.
    lenTasks = int(input())
    
    # receives the string and assigns it to tasks.
    tasks = list(input())
    
    # Used to check previous unique letters.
    uniqueList = []
    
    output = "YES" # assume output = "yes"
    
    # Always adding first char of string to list.
    uniqueList.append(tasks[0])
    
    # for each letter (l) in our string, compare them:
    for l in range(lenTasks):        
        
        # if we have more than 2 letters, then
        # we compare them.
        if l > 0:
        
            # Two letters differ?
            if tasks[l] != tasks[l-1]:
                # Letter not previously seen?
                if tasks[l] not in uniqueList:
                    # Then add it to uniqueList.
                    uniqueList.append(tasks[l])
                    
                # Seen letter previously...
                elif tasks[l] in uniqueList:
                    output = "NO"
    print(output)
    
# Upon reflection, it's a terrible idea to ever use
# the lowercase character "L" in a loop. It's way
# too similar to the number 1 and it's confusing to
# work with. In the future I'll use something like i,
# or e or n or something. Or maybe even just define
# the looping variable as a full word like "letter"