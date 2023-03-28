# Collatz Sequence Problem
import time
import sys

userInput = ""


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        value = 3 * number + 1
        return value


def userInputFunction():
    global userInput
    print("Please enter a number below:")
    userInput = int(input())


while True:
    try:
        userInputFunction()
        break
    except:
        print("You didn't enter a number.")
        continue

try:
    while True:
        if userInput == 1:
            break
        else:
            userInput = collatz(userInput)
            """
            This was tricky. I originally just
            write out collatz(userInput) and
            the program looped forever. Without
            updating the userInput variable's
            value, it just went on forever and
            used the same input.

            Also, I tried to add the global
            keyword before the userInput variable
            because I knew we had to save globally
            but this was illegal because the global
            variables are already referenced in
            a loop. The global keywrod would have
            been applicable if we were altering
            the variable within a function.
            """


except KeyboardInterrupt:
    sys.exit()

print("Sequence complete")
