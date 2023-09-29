"""
Calculate the maximum number of people
on the tram between stops. The highest
number is our capacity.

For example, if out of 4 stops the 3rd
stop requires space for 10 people, and 
the third stop has the most people, then
10 is the answer.

This problem requires us to carry over
people from previous stops and analyze
which stop has the most people.

The first input is people getting off
The second input is people getting on.
People who leave always get off before
people enter. 
"""

judgeInput = input()


def maxCapacity():
    capacity = 0
    maxCapacity = 0
    for n in range(int(judgeInput)):
        currentPassengers = input()
        passengerList = currentPassengers.split()
        passengersLeaving = int(passengerList[0])
        passengersEntering = int(passengerList[1])

        capacity -= passengersLeaving
        capacity += passengersEntering

        if capacity > maxCapacity:
            maxCapacity = capacity

    return maxCapacity


output = maxCapacity()

print(output)
