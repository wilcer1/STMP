
class Budget():
    def __init__(self):
        """Declare the attributes needed."""
        self.income = 0
        self.variable_expenses = {}
        self.fixed_expenses = {}
        self.saving_goal = 0
        self.buffert = 0

    def set_budget(self, income, variable_expenses, fixed_expenses):
        """set the attributes."""
        self.income = income
        self.variable_expenses = variable_expenses
        self.fixed_expenses = fixed_expenses


    def get_expenses(self):
        """Add the expenses together and return as string."""
        total_fix = 0
        total_var = 0
     
        for key in self.fixed_expenses:
            total_fix += self.fixed_expenses[key]

        for key in self.variable_expenses:
            total_var += self.variable_expenses[key]

        return str(total_fix), str(total_var)
    
    def get_total_expenses(self):
        total_fix = 0
        total_var = 0
        for key in self.variable_expenses:
            total_var += self.variable_expenses[key]

        for key in self.fixed_expenses:
            total_fix += self.fixed_expenses[key]
        return total_var + total_fix

    def set_saving_goal(self, saving_goal):
        self.saving_goal = saving_goal
    
    def set_buffert(self, buffert):
        self.buffert = buffert