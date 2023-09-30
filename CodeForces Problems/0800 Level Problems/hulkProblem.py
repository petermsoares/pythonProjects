# The string must always end with the word "it"
# The even numbers are "I love"
# The odd numbers are "I hate"
# The space betwee them is the word "that"

# So, 1 = "I hate" + "it" or "I hate it"
# 2 = " I hate that I love it "


input1 = int(input())  # gives us n Number.

ending = " it"  # tack this string onto the end with str-conct.

output = ""  # make the output variable.

if input1 % 2 == 0:  # if the n is even do this:
    output = "I hate that I love that "*(input1//2)
    output = output.split()
    output[-1] = "it"
    output = " ".join(output)
elif input1 == 1:  # if n is 1.
    output = "I hate it"
else:  # n is odd and is not the number 1
    output = ("I hate that I love that "*(input1//2)) + "I hate it"

print(output)
