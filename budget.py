class Budget():
    def __init__(self):
        self.income = []
        self.variable_expenses = []
        self.fixed_expenses = []

    def set_budget(self, income, variable_expenses, fixed_expenses):
       
        for name, amount in income:
            self.income.append(name, amount)

        for name, amount in variable_expenses:
            self.variable_expenses.append(name, amount)

        for name, amount in fixed_expenses:
            self.fixed_expenses.append(name, amount)