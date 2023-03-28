count = 1

while count <= 50:
    if count % 3 == 0 and count % 5 == 0:
        print(str(count) + " Fizz Buzz")
    elif count % 5 == 0:
        print(str(count) + " Buzz")
    elif count % 3 == 0:
        print(str(count) + " Fizz")
    else:
        print(str(count))
    count = count + 1

"""
The trick with this is to trigger the
conditions in the if statement only when
a number is divisible by specific numbers.

First we run a test to see if the number is
divisible by both numbers because if it is
we want to execute code.

Then if it's not divisible by both, we check
each one individually.

Understanding how to create a true condition
is the trick here. We want to say that if
the remainder of the current number is 0 when
divided by a number (3 or 5 or both) then we
run the clause.

I made a mistake and set up my conditions
to be if count % 3 and count % 5: then do
the clause. This is wrong because we're just
making expressions and not comparing them to
anything. count % 3 gives us a remainder number,
not a truth or false value. A clause is only
going to execute when it sees a true value.
"""
