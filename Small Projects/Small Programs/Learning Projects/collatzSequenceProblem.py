# Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number)
        return 3 * number + 1


goAhead = True
while (goAhead):

    try:
        userNumber = int(input("Please input a number: "))
        goAhead = False
    except:
        print("Please enter a only numbers, not other characters.")

while (userNumber != 1):
    userNumber = collatz(userNumber)

print("End.")
