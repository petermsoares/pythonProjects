# Problem: https://codeforces.com/problemset/problem/1409/A
# Answer: https://codeforces.com/problemset/submission/1409/228222820

# ***********

# To solve, find the difference between a and b in terms of absolute value. Then, find the smallest number of additions or subtractions needed to make a == b. The number you can add or subtract each turn can be a number between 1 and 10, inclusive. Divide the remainder by 10, and if it is not possible to do so, go down by 1 number until a == b.

# ***********

testCases = int(input())

for x in range(testCases):

    numbers = [int(i) for i in input().split()]
    
    a = numbers[0]
    b = numbers[1]
    counter = 0
    
    if a == b:
        output = 0
    
    if a != b:
        remainder = abs(a - b)
        
        n = 10
        goAhead = True
        while(goAhead):
            
            if remainder // n > 0:
                counter += remainder//n
                remainder -= ((remainder//n)*n)
            
            if remainder == 0:
                goAhead = False
            n -= 1
    print(counter)
