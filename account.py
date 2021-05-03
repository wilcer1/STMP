class Account():
    """Constructor that takes the info needed as parameters."""
    def __init__(self, email, firstName, lastName, password, income, expenses):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.income = income
        self.expenses = expenses

    def getCustomer(self):
        return self
    

   
        