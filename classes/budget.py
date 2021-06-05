from .expense import Expense
from .income import Income
import os
import csv

class Budget:
    def __init__(self, name):
        self.name = name
        self.incomes = Income.objects()
        self.expenses = Expense.objects()

    def __str__(self):
        str = f"{self.name}'s budget has {self.total_income()} income and {self.total_expenses()} monthly expenses"
        return (str)

    def add_income(self, income_data):
        self.incomes.append(Income(**income_data))
        self.save(self.incomes)

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

    def save(self, objects):
        print('saving')
        my_path = os.path.abspath(os.path.dirname(__file__))
        print ("objects matches incomes: " + str(objects == self.incomes))
        if objects == self.incomes:
            print("path set to incomes.csv")
            path = os.path.join(my_path, "../data/incomes.csv")
        if objects == self.expenses:
            path = os.path.join(my_path, "../data/expenses.csv")

        with open(path, 'w') as csvfile:
            print('saving in: ' + path)
            object_csv = csv.writer(csvfile, delimiter=',')
            object_csv.writerow(['name', 'amount', 'category', 'date'])
            if "income" in str(path):
                for objects in self.incomes:
                    print(objects)
                    object_csv.writerow([object.name, object.amount, object.category, object.date])
                    print("saved")
            elif "expense" in str(path):
                for objects in self.expenses:
                    print(objects)
                    object_csv.writerow([object.name, object.amount, object.category, object.date])
                    print("saved")
            
            
