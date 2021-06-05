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
        pass