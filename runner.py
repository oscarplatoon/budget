# After you write all your classes, use this file to call them all together and run your program
from classes.interface import BudgetInterface

BudgetInterface("Test").run()

# Design plan:
# Runner just fires off the interface, which then creates an instance of Budget
# Budget object will at instance time pull from a csv of expenses and income(s?)
# Borrow the code from school_interface for .csv manipulation, accept the performance hit 
# of rewriting the csv completely for each transaction
# Budget class will be where budget/string formatted output methods happen for the relevant tests.
# 