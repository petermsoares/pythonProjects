# FizzBuzz While Loop Experiment.
# count numbers from 1 through 100 (last number is 100)
# if a number is divisible by 3, print Fizz.
# if a number is divisible by 5, print Buzz.
# if a number is divisible by both 3 and 5, print FizzBuzz.
# Use modulus operator to get remainders to check division of 3 and 5.

# creating a variable called number to hold our counter. Assigning to 0.
number = 0

# Boolean variable used to control while loop
goAhead = True

while (goAhead):

    number = number + 1  # Counter for the loop.

    if number % 3 == 0 and number % 5 == 0:  # if the F and B conditions are met, print FB
        print("FizzBuzz")
    elif number % 3 == 0:  # if the F condition alone is met, print F
        print("Fizz")
    elif number % 5 == 0:  # if the B condition alone is met, print B
        print("Buzz")
    else:  # if no condition is met, print the number based on the current count.
        print(number)

    if number >= 100:  # if count is 100, turn off the loop.
        goAhead = False
