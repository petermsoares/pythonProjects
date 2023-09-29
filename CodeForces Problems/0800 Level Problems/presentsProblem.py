# The idea behind this problem is as follows:
# Get [1] the index value and [2] the int value of a number.
# Turn the index value into a number.
# Assign the index value to its corrosponding int value in a list.

# Example:
# 2 3 4 1.
# 2 is in position 1. Flip. #1 is assigned to position 2.
# 3 is in position 2. Flip. #2 is assigned to position 3.
# 4 is in position 3. Flip. #3 is assigned to position 4.
# 1 is in position 4. Flip. #3 is assigned to position 1.
# Output:
# 4 1 2 3.

input1 = input() # get the number of people at the party.
input2 = input() # get the list of numbers separated by spaces.

orNumbers = input2 # rename the list of numbers.
orList = orNumbers.split() # length of list of numbers.

reList = [""]*len(orList) # make new list to assign to for output.

# Have a loop that runs through each number on the list.

for n in range(int(input1)):

    # need to get the index value of that number.
    # The index value becomes the assignedNumber.
    # Add 1 to the assignedNumber because indexes are 0-based.
    assignedNumber = n + 1
    

    # need to get the value of that number.
    # The value of the number becomes the index value of assignedNumber
    indexValue = int(orList[n])-1\
    
    
    # Assign our assignedNumbers to their respective indexValues in the reList variable.
    reList[indexValue] = str(assignedNumber) # make str to join later

reList = " ".join(reList) # convert list into string with spaces.

print(reList) # output reordered string.
