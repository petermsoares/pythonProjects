# Problem: https://codeforces.com/problemset/problem/510/A
# Answer: https://codeforces.com/problemset/submission/510/227579511

# This is similar to doing the animation in
# automate the boring stuff, except instead of
# doing an animation, we're drawing a picture
# with characters.

# Essentially, we want every even line to be a
# series of periods and #, and every even line
# to be a series of # marks. Note, each even
# line reverses the pattern, and the first
# instance of the pattern always has the #
# marker on the far right. The trick is to use
# a Bool to toggle between the states of the string.

pattern = input().split()

firstValue = int(pattern[0])
secondValue = int(pattern[1])
toggle = False


for x in range(firstValue):

    if x == 0 or x % 2 == 0:
        print("#"*secondValue)
    elif toggle == False:
        print("."*(secondValue-1)+"#")
        toggle = True
    elif toggle == True:
        print("#"+"."*(secondValue-1))
        toggle = False
