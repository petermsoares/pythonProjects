input1 = input()
input1 = input1.split()
peopleOnLine = input1[0]
peopleOnLine = int(peopleOnLine)

time = int(input1[1])

input2 = input()

listOfPeople = list(input2)


t = 0

# The first for loop runs for the number equal to time. In this
# problem time is based on a number of seconds. So if the number
# of seconds is 5, then time = 5 and will loop 5 times.

# t = 0 resets the counter that I use to find and replace the letters
# as they appear in the list.
for i in range(time):
    t = 0
    for n in range(peopleOnLine):
        try:
            if listOfPeople[t] == "B" and listOfPeople[t+1] == "G":
                listOfPeople[t] = "G"
                listOfPeople[t+1] = "B"
                t += 1
        # This is the tircky bit. If we have a string BGG and the time
        # value is 1, we loop through 1 time and output GBG. B and G
        # can only switch palces 1 time per loop. So on t = 0, we check
        # and find B. Because the index of 0 = B and the index of 1 = G,
        # the conditions for switching them are met, and we reassign
        # 0 = G and 1 = B. Now the trick is that if we do not increase
        # the value of the integer we use to scan the index values by
        # a value of 1, then we will rescan the B value we just assigned.

        # So without t += 1 at the bottom, our code would run like this:
        # Starting String is "BGG"
        # For t=0: listOfPeople[t]="B" ListOfPeople[t+1]="G". Swap.
        # New String is "GBG" because B moved from 0 to 1.
        # For t=1: listOfPeople[t]="B" ListOfPeople[t+1]="G". Swap.
        # New String is "GGB" because B moved from 1 to 2.

        # This is the problem. If we increase t by 1 for each loop
        # we aren't taking into account the change in position of B.
        # Thus, we can move B back multiple places even though only
        # 1 second of time has passed. To solve this we need to add
        # 1 to t if we do a swap. This way when the counter naturally
        # increases by 1 at the end of the loop, we're beginning our
        # scan of the List in the index value 1 ahead of where the
        # Boy just moved to.

        # Also, we use try and except because there may be an instance
        # where t+1 is outside the range of our list. I'm not sure how
        # to code around this, so I'm just going to use a try and except
        # error handling solution. I know this isn't the best, but it
        # does solve the problem.
        except:
            continue
        t += 1

output = "".join(listOfPeople)
print(output)
