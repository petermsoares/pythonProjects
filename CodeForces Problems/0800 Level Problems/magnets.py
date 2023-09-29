# count the number of chains.
# 10-10 form a chain.
# 01-01 form a chain.
# 01-10 breaks the chain.

# Basic idea to solve is to keep count of the number of times the new input deviates from the previous input. Start the counter at 1 because if we get 1 magnet, that's technically 1 group.

input1 = input() # number of magnets
nMagnets = int(input1) # str->int for looping through future inputs.

linkCounter = 1 # set to 1 because if we only get 1 mag we still have 1 chain.

for n in range(nMagnets):
    
    # get the next input:
    thisLink = input()
    
    if n > 0: # this skips the comparison when we get the first magnet.
        if thisLink != previousLink:
            linkCounter += 1
   
    previousLink = thisLink
    
    
print(linkCounter)