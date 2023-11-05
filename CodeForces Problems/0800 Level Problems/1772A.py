# 1772A

# This can be solved by turning the string input into a list, and
# plucking off the first and last element. Because the numbers
# are always 1 digit, we can use this method. Else, we would need
# to use a different method.

testcases = int(input())

for case in range(testcases):
    
    vals = list(input())
    number1 = int(vals[0])
    number2 = int(vals[-1])
    answer = number1 + number2
    output = answer
    print(answer)