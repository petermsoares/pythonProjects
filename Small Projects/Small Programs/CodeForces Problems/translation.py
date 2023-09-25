"""
Take a string.
convert it into a list.
Reverse the list.
Turn that string into a list.
Determine if the original string is the same as
the reversed string.
"""
inputString = input()
translationAttempt = input()

myList = list(inputString)

myList.reverse()
newString = "".join(myList)

if newString == translationAttempt:
    print("YES")
else:
    print("NO")
