class Budget:

    
    def __init__(self, income):
        self.set_monthly_income(income)
        self.expense_dict = {}
    
    def set_monthly_income(self, income):
        self.monthly_income = income
    
    def get_monthly_income(self):
        print(f'----------\nYour monthly income is :{self.monthly_income}\n----------')
    
    def add_expense(self, expense, type):
        if type in self.expense_dict:
            self.expense_dict[type] = (self.expense_dict[type] + expense)
        else:
            self.expense_dict[type] = expense
    
    def list_expenses(self):
        for entry in self.expense_dict:
            print(entry, self.expense_dict[entry])
    def percent_breakdown(self):
        for entry in self.expense_dict:
            print(f'{entry} {100 * (self.expense_dict[entry] / self.monthly_income)}% of monthly income')
        print('\n')
    