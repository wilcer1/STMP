class Budget():
    def __init__(self):
        self.income = 0
        self.variable_expenses = {}
        self.fixed_expenses = {}

    def set_budget(self, income, variable_expenses, fixed_expenses):
       
       
       self.income = income
       self.variable_expenses = variable_expenses
       self.fixed_expenses = fixed_expenses

    def get_total_expenses(self):
        """Add the expenses together and return."""
        for key in self.variable_expenses:
            total_var = 0
            total_var += self.variable_expenses[key]

        for key in self.fixed_expenses:
            total_fix = 0
            total_fix += self.fixed_expenses[key]

        return total_fix, total_var