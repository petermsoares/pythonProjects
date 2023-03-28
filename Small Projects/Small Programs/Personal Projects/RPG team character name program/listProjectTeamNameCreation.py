listOfNames = []

print("This is a character creation program. The first stage is to add the names of the characters for your team. Please enter the first team member name below:")


def makeCaracterName():
    newName = input()
    listOfNames.append(newName)
    print("")
    print("Player #" + str(len(listOfNames)) +
          " is " + newName)
    if len(listOfNames) < 5:
        print("Input the name for the next player: ")
        print("")
    else:
        print("")
        return


def replaceName(position):
    # List starts at index 0, so user input will be off by +1. This compensates.
    position = position - 1
    print("Please enter a new name for " +
          str(listOfNames[position]))
    print("")
    # Get the name value stored in the index we are overwriting.
    oldName = listOfNames[position]
    newName = input()  # Get user input of new name.
    listOfNames[position] = newName  # Overwrite the value of the index.
    print("The character " + oldName + " has been renamed " + newName)
    print("")


while len(listOfNames) < 5:
    makeCaracterName()

while True:
    print("Your team member names are: " + str(listOfNames))
    print("Would you like to replace one of your character names with a new name?")
    print("Press y for yes or n for no.")
    print("")
    renameCharacter = input()
    if renameCharacter == "y":
        print("Ok, which character do you want to replace? Select the position of the character on the list below with 1 being the left most name and 5 being the right most name: ")
        print("")
        print(str(listOfNames))
        replacedCharacterIndex = int(input())
        # check to make sure user selects a valid position in the list.
        if replacedCharacterIndex > 0 and replacedCharacterIndex < 6:
            replaceName(replacedCharacterIndex)
        else:  # if user makes invalid selection, restart at top of loop.
            print("You entered an invalid number.")
            print("")
            continue
    elif renameCharacter == "n":  # exits program.
        break
    else:
        print("please enter a valid y or n.")
        print("")
