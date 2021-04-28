#class Menu():

def main():
    signIn()
    stmpMenu()


def stmpMenu():
    userInput = input("\nWelcome"
    "\n1. Make a budget"
    "\n2. Create long-term savings"
    "\n3. Sew how much you can save \n")

    if userInput == "1":
        budget()

    elif userInput == "2":
        saving()

    elif userInput == "3":
        calculateSave()


def signIn():
    userInput = input("Welcome to STMP" 
    "\n1. Sign in "
    "\n2. Register \n")

    if userInput == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

    elif userInput == "2":
        firstName = input("Enter your firstname: ")
        lastName = input("Enter your lastname: ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        password1 = input("Confirm your password: ")

    else:
        print("That is not valid, enter 1 or 2 \n")
        signIn()

def budget():
    pass

def saving():
    pass

def calculateSave():
    pass

if __name__ == "__main__":
    main()
