#class Menu():

def main():
    signIn()
    stmpMenu()


def stmpMenu():
    print("\nWelcome")
    print("1. Make a budget")
    print("2. ")
    print("3. ")


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

    

if __name__ == "__main__":
    main()