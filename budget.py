class Budget():
    def __init__(self):
        self.income = 0
        self.variable_expenses = None
        self.fixed_expenses = None

    def set_budget(self, income, variable_expenses, fixed_expenses):
       
       
       self.income = income
       self.variable_expenses = variable_expenses
       self.fixed_expenses = fixed_expenses