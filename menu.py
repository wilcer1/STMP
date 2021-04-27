#class Menu():

def main():
    signIn()
    stmpMenu()


def stmpMenu():
    print("Welcome")
    print("1. Make a budget")
    print("2. ")
    print("3. ")


def signIn():
    a = input("Welcome to STMP" 
    "\n1. Sign in "
    "\n2. Register ")
   
    if a == "1":
        username = input("Enter your username ")
        password = input("Enter your password ")

    elif a == "2":
        firstName = input("Enter your firstname ")
        lastName = input("Enter your lastname ")
        username = input("Enter a username ")
        password = input("Enter a password ")
        password1 = input("Confirm your password ")

    

if __name__ == "__main__":
    main()