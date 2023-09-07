# Make a program that checks a user's password input to see if it is correct.
# If the user guesses the correct password, he is let into the system.
# If the user guesses incorrectly 3 times, he is locked out of the system.

# Below are variables for the password and the counter we will use to keep track of user input attempts:
userPassword = "Jackie Chan"
attemptCounter = 0

# Below are the while loop and a boolean variable to control the loop.
# The loop has two conditions that will make it close. Either a correct password OR 3 failed guesses.
goAhead = True
while (goAhead):
    # Increment the counter by 1 for each loop.
    attemptCounter = attemptCounter + 1

    # Message to greet user and show attempts.
    print("Hi, please enter your password below. This is attempt #",
          attemptCounter, "of 3")
    # Capture the input from user and assign it to a variable.
    userGuess = input("Password: ")
    # Compare the user's guess to the correct password. If correct, he enters.
    if userGuess == userPassword:
        print("This is the correct password. You may enter the system")
        goAhead = False
    # If user guessed wrong 3 times, we close him out.
    # Placement of the counter check must be after password check or else on 3rd attempt user locks out even if password is right.
    elif attemptCounter >= 3:
        print("You have made too many attempts. Your account is locked for 10 minutes.")
        goAhead = False
