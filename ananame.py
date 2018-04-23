
def getName(position):
    return input("Please enter your {} name: ".format(position))

def printName(firstName, middleName, lastName):
    print("Your name is {} {} {}".format(firstName, middleName, lastName))

firstName = getName("first")
middleName = getName("middle")
lastName = getName("last")

printName(firstName, middleName, lastName)
