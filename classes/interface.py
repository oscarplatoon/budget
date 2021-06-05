from .budget import Budget

class BudgetInterface:
    def __init__(self, name):
        self.budget = Budget(name)
        self.name = name

    def run(self):
        print(self.budget)