num = 0
print("This prgram is an experiment. We find even numbers and divide them by zero to cause an error. The idea is to have all odd numbers printed to the terminal, while all even numbers print an error message instead of causing the program to crash.")
print("")
for number in range(1, 11, 1):

    try:
        if number % 2 == 0:
            # print(str(number)+" Number is Even")
            print(str(number/0))
        else:
            # print(str(number)+" Number is Odd")
            print("The current number is: " + str(number))
    except ZeroDivisionError:
        print("Even number found.")
