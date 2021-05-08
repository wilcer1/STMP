class Account:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Account.__instance == None:
            Account()

        return Account.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Account.__instance != None:
            raise Exception("This class is a Account!")
        else:
            Account.__instance = self
            self.email = None
            self.first_name = None
            self.last_name = None
            self.password = None
            self.income = None  # list of tuples
            self.expenses = None  # list of tuples

    def setCustomer(self, details):
        self.email = details[0]
        self.first_name = details[1]
        self.last_name = details[2]
        self.password = details[3]
        self.income = []
        self.expenses = []

    def logOut(self):
        Account.__instance = None
    
