import random
charNamesF = ["Alexander", "Billy", "Charlie"]
charNamesL = ["Lecos", "Fields", "Joust"]
charClass = ["Knight", "Cleric", "Mage"]
charInt = 0
charSTR = 0
userChoice = ""

newCharacter = []


def roll3(charInfo):
    info = charInfo[random.randint(0, 2)]
    return info


def rollCharacter():
    newNameF = roll3(charNamesF)
    newNameL = roll3(charNamesL)
    newClass = roll3(charClass)
    newInt = random.randint(50, 100)
    newSTR = random.randint(50, 100)

    character = [newNameF, newNameL, newClass, newInt, newSTR]

    return character


print("Select r to roll a new character or s to save character")
pickingCharacter = True
while (pickingCharacter):
    userChoice = input()
    if userChoice == "r":
        newCharacter = rollCharacter()
        print(newCharacter)
        print("To save this character, press s. To re roll, press r")
    elif userChoice == "s" and newCharacter != []:
        print("Your character has been saved. Now exiting.")
        pickingCharacter = False
    else:
        print("You may have entered an incorrect option. Please pick r to roll a new character or s to save your character. You can only save a character once you've made one.")
