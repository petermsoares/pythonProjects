"""
width of person upright = 1
width of person hunched = 2

Picture:
Fence
|
|
|   IIooIoI (Friends walking upright and hunched)
|
|

Input 1 = the number of friends, the height of fence
Input 2 = the height of each person
"""

input1 = input().split()
friendHeight = input().split()

friends = int(input1[0])
fenceHeight = int(input1[1])

counter = 0

for n in range(friends):

    if int(friendHeight[n]) > fenceHeight:
        counter += 2
    else:
        counter += 1

print(counter)
