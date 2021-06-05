from .expense import Expense
from .income import Income

class Budget:
    def __init__(self, name):
        self.name = name
        self.incomes = Income.objects()
        self.expenses = Expense.objects()

    def __str__(self):
        str = f"{self.name}'s budget has {self.total_income()} income and $$$ monthly expenses"
        return (str)

    def total_income(self):
        total_income = 0
        for income in self.incomes:
            total_income += float(income.amount)
        return total_income