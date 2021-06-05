import csv
import os.path

class Income:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @classmethod
    def objects(cls):
        incomes = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/income.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(dict(row))
                incomes.append(Income(**dict(row)))
            return incomes
