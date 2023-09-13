myList = ["Aaron", "John", "Alexander"]

"""
t = "Aaron" in myList
f = "aaron" in myList

print("Is Aaron in my list?")
print(t)
print("Is aaron in my list?")
print(f)
"""

# make a loop that checks whether j is in myList
j = "john"  # changing the case of the "j" will trigger a different outcome of the loop
# starting index at -1 so when counter adds 1 we are at index 0 in loop.
index = -1

lookingForJohn = True
while (lookingForJohn):

    index = index + 1  # counts up from 0 to examine the index position of the list of names

    cap = len(myList)  # cap variable to indicate the end of the list.

    if index == cap:  # first check to see if we're at the end. If we are, then no true values have been found so the output must be false.
        print("John is not on the list")
        lookingForJohn = False

    # if a true value is found, we output the "john is on the list" message.
    elif j == myList[index]:
        print("John is on the list")
        lookingForJohn = False
    # note, you have to check whether the cap is reached before checking the name.
    # this is because the index position starts at 0, but the len function starts counting at 1. So you'll be looking for an index that isn't there and you'll get an error.
