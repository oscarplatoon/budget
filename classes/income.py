import csv
import os.path

class Income:
    def __init__(self, name, amount, category = "income", date = "1/1/2021"):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    @classmethod
    def objects(cls):
        incomes = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/incomes.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #print(dict(row))
                incomes.append(Income(**dict(row)))
            return incomes
