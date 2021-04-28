#class Menu():

def main():
    signIn()
    stmpMenu()


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
        income = input("Enter your monthly income: ")
        expenses = input("Enter your monthly expenses: ")

    else:
        print("That is not valid, enter 1 or 2 \n")
        signIn()


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

    else:
        print("That is not valid, enter 1 or 2 \n")
        stmpMenu()


def budget():
    pass


def saving():
    savingAmount = int(input("How much do you want to save? (In SEK) "))
    savingTime = int(input("Enter when you want to accomplish the saving (Enter in month): "))
    moneyPerMonth = savingAmount / savingTime
    print("To accomplish your goal, you need to save", moneyPerMonth, "SEK in", savingTime, "month!")

def calculateSave():
    pass

if __name__ == "__main__":
    main()
