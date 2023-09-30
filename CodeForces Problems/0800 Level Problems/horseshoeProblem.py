# Wants to wear all shoes different color. 4 shoes total.
# He has some shoes. We don't know how many.
# He can buy shoes from a store.
# But, he wants to buy as few shoes as possible to save money.

# Colors are represented by numbers, input is given as a string.

input1 = input() # Get input from judge.

shoesOwned = input1.split() # turns input into a List

shoesCounted = [""]*len(shoesOwned) # Make a new list with empty strings equal to the number of items in the shoeOwned List. We will look for duplicates housed in this list.


# Think a way to solve this is to count the number of times each shoe appears in the given list. If the count is greater than 1, we add 1 to the number of shoes that he must purchase.

shoesToBuy = 0

for i in range(len(shoesOwned)):

    # If the index value of shoesOwned at position i exists more than once within the shoesOwned list, then we want to assign that value to the shoesCounted list to keep a record of it.
    
    # Then, if we have at least 2 copies of that shoe color in our shoeCounted list, we add 1 to the shoesToBuy counter. Every time the program picks up on another duplicate copy, maybe a 3rd or 4th pair with the same color, it adds 1 to the counter.
        
    if shoesOwned.count(shoesOwned[i]) > 1:
        shoesCounted[i] = shoesOwned[i]
        if shoesCounted.count(shoesOwned[i]) >= 2:
            shoesToBuy += 1

print(shoesToBuy)
