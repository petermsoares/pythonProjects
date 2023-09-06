# Coding out while loop example based on Andy Harris lecture.

# Let's write a program that checks to see if a password is correct. The user will have 3 attempts. If the user guesses correct, they're let into the system. If the user guess is incorrect, they are blocked.


password = "Darrow"  # creating password variable.
attempt = 0  # variable for attempts within loop.

goAhead = True  # variable for condition in while loop.
while (goAhead):

    attempt = attempt + 1  # counter for the loop.
    print("You are on attempt #", attempt, "of 3")

    # get a password from user and assign it to guess.
    guess = input("What is your password? ")

    # if guess is the right password, we let the user in and set the while loop's condition to false so we can exit the loop.
    if guess == password:
        print("That is the correct password. You may enter.")
        goAhead = False

    # if the guess is not the password and the counter is at least 3, then we let the user know they've entered too many attempts and set the condition of the loop to false so that we exit.
    elif attempt >= 3:
        print("Failed. You have made too many attempts. Now exiting")
        goAhead = False

    # note: we need to use elif in this situation so that it alone is guaranteed to fire when we hit attempt number 3. If we use two if statements and if the user guesses the correct password on attempt #3, then the program will still show the message that the user failed.
