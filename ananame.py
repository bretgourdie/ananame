import csv

lastNamesFileName = "lastNamescsv.csv"
properNamesFileName = "properNamescsv.csv"

def getRemainingLetters(lettersToUse, name):
    newList = lettersToUse[:]

    for letter in name:
        if letter in newList:
            newList.remove(letter)
        else:
            return None

    return newList

def getAllLetters(name):
    return sorted(fullName.replace(" ", "").lower())

def getName(position):
    return input("Please enter your {} name: ".format(position))

def printName(firstName, middleName, lastName):
    print("Your name is {} {} {}".format(firstName, middleName, lastName))

def getGender():
    return input("Please enter \"male\" or \"female\" if you'd like a gendered name; otherwise, enter anything else: ")

firstName = getName("first")
middleName = getName("middle")
lastName = getName("last")

printName(firstName, middleName, lastName)
fullName = firstName + " " + middleName + " " + lastName

gender = getGender()

allLetters = getAllLetters(fullName)

print("These are the letters we have available: \"{}\"".format("".join(allLetters)))

lastNamesToUse = []
with open(lastNamesFileName, "r") as lastNamesFile:
    lastNamesToUse = [lastName.strip() for lastName in lastNamesFile.readlines()]
    lastNamesToUse.remove("lastName")

allProperNames = []
maleProperNames = []
femaleProperNames = []
with open(properNamesFileName, "r") as properNamesFile:
    allProperRows = [properRow.strip() for properRow in properNamesFile.readlines()]
    allProperNames = [properRow.split(",")[0] for properRow in allProperRows]
    allProperNames.remove("name")

    maleProperNames = [properRow.split(",")[0] for properRow in allProperRows if properRow.split(",")[1] == "M"]
    femaleProperNames = [properRow.split(",")[0] for properRow in allProperRows if properRow.split(",")[1] == "F"]

firstNamesToUse = []
if gender == "male":
    firstNamesToUse = maleProperNames
elif gender == "female":
    firstNamesToUse = femaleProperNames
else:
    firstNamesToUse = allProperNames

nameAnagrams = []

for potentialFirstName in firstNamesToUse:
    remainingLettersAfterFirstName = getRemainingLetters(allLetters, potentialFirstName.lower())

    if remainingLettersAfterFirstName is not None:

        for potentialLastName in lastNamesToUse:
            remainingLettersAfterLastName = getRemainingLetters(remainingLettersAfterFirstName, potentialLastName.lower())

            if remainingLettersAfterLastName is not None:
                nameAnagrams.append(potentialFirstName + " " + potentialLastName)

if len(nameAnagrams) > 0:
    print("We found {} anagrams for you!".format(len(nameAnagrams)))

    for nameAnagram in nameAnagrams:
        print("\t{}".format(nameAnagram))
else:
    print("We didn't find any anagrams for you. :(")
