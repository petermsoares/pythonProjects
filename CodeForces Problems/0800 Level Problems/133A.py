# 133A

# Ok so this is actually a fun take on an old problem where we are
# given a string and we need to check to see if legal characters
# are within the string. If they are, even if we only have one,
# we output "YES". else, we output "NO"

p = "H"
o = "Q"
i = "9"

string = input()

if p in string or o in string or i in string:
    output = "YES"
else:
    output = "NO"

print(output)