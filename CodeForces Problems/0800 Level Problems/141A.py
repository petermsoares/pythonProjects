# Problem: https://codeforces.com/problemset/problem/141/A
# Answer: https://codeforces.com/problemset/submission/141/227270687

# I think this problem can be solved by combining
# the first two inputs into a list and make the
# third input into a list. Then sort both lists.
# If they're equal, then we print YES. if not, then
# we print NO.

firstLetters = list(input())
secondLetters = list(input())
thirdLetters = list(input())

firstAndSecondLetters = firstLetters + secondLetters
firstAndSecondLetters.sort()

thirdLetters.sort()

if firstAndSecondLetters == thirdLetters:
    print("YES")
else:
    print("NO")

# This program is a little limited because it doesn't
# tell the user why the lists are different when NO is
# printed to the screen. That might be a problem for later.
