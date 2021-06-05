from .expense import Expense
from .income import Income

class Budget:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        str = f"{self.name}'s budget has $$$$ income and $$$ monthly expenses"
        return (str)