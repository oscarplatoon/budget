import unittest
from classes.interface import BudgetInterface

class TestBudget(unittest.TestCase):
    """
    Does some test stuff
    """
    def test_budget_stuff(self):
        self.assertIsInstance(BudgetInterface('test').name, str)

if __name__ == '__main__':
    unittest.main()
