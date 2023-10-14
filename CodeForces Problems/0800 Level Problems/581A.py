# Problem: https://codeforces.com/problemset/problem/581/A
# Answer:

# **************************************
# First input is the number of socks V has. Each number is a different color.

# Output the number of days he can wear different socks, and then the number of days he can wear the same socks.

# Note, V throws out worn socks after each day.
# Note, V cannot wear one sock at once.

# To solve, figure out whether a or b is larger. Then subtract the smaller from the larger and divide by 2. This represents the number of days V may wear 2 different socks.

# Then divide the remaining number of socks by 2. This is the number of days V can wear the same color socks. Note, do an integer division by 2, not normal division to avoid the 1-sock issue case.

# **************************************

# Get a list of the numbers of socks available, as ints.
socks = [int(i) for i in input().split()]

# Sort them from smallest to largest
socks.sort()

# If the socks amounts are equal, print the number of socks of either type. This is the number of pairs of different socks available to be used.
if socks[0] == socks[1]:
    print(socks[0], 0)

# If the sock amounts are different, the number in the smaller index[0] will be the number of days different socks can be worn.

# The number of days same socks can be worn is the large group of socks minus the small group of socks divided by 2.
if socks[0] < socks[1]:

    differentSocks = (socks[0])
    sameSocks = str((socks[1] - socks[0]) // 2)
    print(differentSocks, sameSocks)
