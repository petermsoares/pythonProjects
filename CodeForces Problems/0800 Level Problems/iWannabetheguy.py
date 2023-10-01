# player X can only pass the P levels. First list of numbers.
# player Y can only pass the Q levels. Second list of numbers.
# I think the first number input represents the number of levels.

# Method one:

# To solve, we can check each list for the number n. Combine each list and then reference that list for the level. If the level isn't in the list, print the fail statement. If the loop never triggers the if statement, just print out the output. Write the output to assume the program will pass.

# If we fail to locate a number, then we print the failure output. If we locate all the numbers we can print the success output.

# I tried submitting this solution on codeforces, but the judge graded my output as incorrect on #27. I am not sure why because the sum of the two lists contain all the numbers needed to reach the last level. This solution does work for the problem.

input1 = input()

pX = input()
pX = pX.split()

pY = input()
pY = pY.split()

pXY = pX + pY # combine both lists of levels that can be solved.

output = "I become the guy." # Assigns the passing string to the output.

for n in range(int(input1)):
    n += 1
    # Here, we just check for the number not being present.
    # If it isn't we reassign the failure string to the output variable and then we break out of the loop.
    
    if str(n) not in pXY :
            output = "Oh, my keyboard!" # If we get a fail condition, reassign the failure string to the output.
            break


print(output)


# Method two:

# Alternatively, there might be a way to solve this problem using lengths of lists. For example, if the game goes to level 5 and the list containing all the unique numbers of each player has a length that is less than 5, then we know one of the levels is missing and the players cannot solve the game.

# Come back to try and solve with this method at a later time.

