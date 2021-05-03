class Account():

    def setCustomer(self, details):
        self.email = details[0]
        self.first_name = details[1]
        self.last_name = details[2]
        self.password = details[3]
        self.income = details[4]
        self.expenses = details[5]

    def getCustomer(self):
        return self
    

   
        