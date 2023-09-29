# Thoughts on solving the problem
"""
The input will have 2 numbers. First is
the starting number. Second is the number
of times we will loop.

Rules are as follows:
- If the last digit of the number is 0,
divide by 10.
- Else, (meaning, the last digit is a
non-zero number), then subtract 1 from
the number.

We can solve this by running a for loop
n number of times, where n is the 2nd
number of our input. During each loop we
analyze what the last digit of the number
is and use one of the two rule statements.
"""

input = input()  # get input from judge.

numlist = input.split()  # takes input and turns into list.

number1 = numlist[0]  # assigns first number in list to number var.
number2 = int(numlist[1])
output = 0  # assigns 0 to output variable.


for n in range(number2):
    # print("loop", n)
    loopNumber = list(number1)  # reassign outpt to a list of number 1
    if loopNumber[-1] == "0":
        # print(number1)
        number1 = int(number1) // 10
    else:
        # print(number1)
        number1 = int(number1) - 1
    number1 = str(number1)


print(number1)
