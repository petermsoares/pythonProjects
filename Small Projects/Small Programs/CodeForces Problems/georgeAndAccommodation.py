# There are n number of rooms in a building.
# Each room has some number of people in it.
# But every room has some space for at least 1 more person.
# Find the number of rooms that can house at minimum 2 additional guests.

# input1 = the number of rooms available.
# Every other input contains two numbers.
# The first number is the number of people who live in the room.
# The second number is the room's capacity.

input1 = input()  # number of rooms to look through.
nRooms = int(input1)  # converted into number.
roomsAvailable = 0  # counter to keep track of rooms available.

for n in range(nRooms):
    inputPQ = input().split()
    occupants = int(inputPQ[0])
    capacity = int(inputPQ[1])

    if capacity - occupants >= 2:  # if room meets conditions...
        roomsAvailable += 1  # add 1 to available rooms

output = roomsAvailable  # set available rooms to output
print(output)  # print output.
