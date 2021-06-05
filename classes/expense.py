import csv
import os.path

class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    @classmethod
    def objects(cls):
        expenses = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/expenses.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #print(dict(row))
                expenses.append(Expense(**dict(row)))
            return expenses
