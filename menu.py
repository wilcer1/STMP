#class Menu():

def main():
    signIn()


def signIn():
    userInput = input("Welcome to STMP" 
    "\n1. Sign in "
    "\n2. Register \n")

    if userInput == "1":
        email = input("Enter your email: ")
        password = input("Enter your password: ")


        # QUERY: "SELECT Account.Email, Account.Password FROM Account WHERE Account.Email =", email, ";"


        stmpMenu()

    elif userInput == "2":
        firstName = input("Enter your firstname: ")
        lastName = input("Enter your lastname: ")
        password = input("Enter a password: ")
        password1 = input("Confirm your password: ")
        email = input("Enter your email: ")
        income = input("Enter your monthly income: ")
        expenses = input("Enter your monthly expenses: ")

        if password == password1:
            print("Test")
            # QUERY: "INSERT INTO Account VALUES("firstName", "lastName", "password", "email", "income", "expenses");"

        else:
            print("\n \nPassword did not match, try again")
            signIn()

        stmpMenu()

    else:
        print("\nThat is not valid, enter 1 or 2")
        signIn()


def stmpMenu():
    userInput = input("\nWelcome"
    "\n1. Make a budget" # budget()
    "\n2. Create long-term savings" # crateSaving()
    "\n3. Sew how much you can save \n") # calculateSave()

    if userInput == "1":
        budget()

    elif userInput == "2":
        createSaving()

    elif userInput == "3":
        calculateSave()

    else:
        print("That is not valid, enter 1 or 2 \n")
        stmpMenu()


def budget():
    pass


def createSaving():
    savingAmount = int(input("How much do you want to save? (In SEK) "))
    savingTime = int(input("Enter when you want to accomplish the saving (Enter in month): "))
    moneyPerMonth = savingAmount / savingTime
    print("To accomplish your goal, you need to save", moneyPerMonth, "SEK in", savingTime, "month!")

def calculateSave():
    pass

if __name__ == "__main__":
    main()
