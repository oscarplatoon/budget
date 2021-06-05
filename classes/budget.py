from .expense import Expense
from .income import Income

class Budget:
    def __init__(self, name):
        self.name = name
        self.incomes = Income.objects()
        self.expenses = Expense.objects()

    def __str__(self):
        str = f"{self.name}'s budget has {self.total_income()} income and {self.total_expenses()} monthly expenses"
        return (str)

    def total_income(self):
        total_income = 0
        for income in self.incomes:
            total_income += float(income.amount)
        return total_income

    def total_expenses(self):
        total_expenses = 0
        for expense in self.expenses:
            total_expenses += float(expense.amount)
        return total_expenses
