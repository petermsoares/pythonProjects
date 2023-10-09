# Problem: https://codeforces.com/problemset/problem/1335/A
# Solution: https://codeforces.com/problemset/submission/1335/227269344

# I starred this problem because I like how it requires
# you to think a little and write out some of the outputs
# in order to find a pattern. I know this isn't the most
# complex problem, but sometimes you won't be able to just
# think of the solution or the steps that you need to do
# in order. Sometimes you need to sit down and write things
# out on paper, or in this case, in the terminal with examples.

# a > b.
# all candles must be given out.
# if there is only 1 or 2 candles, we print 0.
# based on some number of candles, how many ways can we divide?

# if n = 3. a = 2 and b = 1
# if n = 4: a = 3 and b = 1
# if n = 5: a = 3,4 and b = 2,1
# if n = 6: a = 4,5 and b = 2,1
# if n = 7: a = 4,5,6 and b = 3,2,1
# if n = 8: a = 5,6,7 and b = 3,2,1

# Any number smaller than 3: output is 0
# Any number == 3: output is 1
# Any number larger than 3: output = n/2 -1


testCases = input()

for x in range(int(testCases)):
    amountOfCandles = int(input())

    if amountOfCandles < 3:
        print(0)
    elif amountOfCandles == 3:
        print(1)
    else:
        output = (amountOfCandles-1) // 2
        print(output)
