def getAllLetters(name):
    return fullName.replace(" ", "")

def getName(position):
    return input("Please enter your {} name: ".format(position))

def printName(firstName, middleName, lastName):
    print("Your name is {} {} {}".format(firstName, middleName, lastName))

def getGender():
    gender = input("Please enter \"male\" or \"female\" if you'd like a gendered name; otherwise, enter anything else")
    if gender == "male" or gender == "female":
        return gender
    else:
        return None

firstName = getName("first")
middleName = getName("middle")
lastName = getName("last")

printName(firstName, middleName, lastName)
fullName = firstName + " " + middleName + " " + lastName

allLetters = getAllLetters(fullName)

gender = getGender()


