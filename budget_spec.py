import unittest
from classes.interface import BudgetInterface

class TestBudget(unittest.TestCase):
    """
    Checks that BudgetInterface has a str name.
    """
    def test_basic_budget_functionality(self):
        self.assertIsInstance(BudgetInterface('test').name, str)

    """
    User can track expenses by category
    """
    def test_expense_by_category(self):
    ###WIP
        pass

    """
    User can adjust their monthly income.
    """
    def test_change_monthly_income(self):
        pass

    """
    User can generate monthly costs.
    """
    #Fixed costs, utilities and stuff? Or also non fixed expenses? TBD
    def test_generate_monthly_costs(self):
        pass

    """
    User can create and calculate impacts of new expenses.
    """
    def test_create_new_expense(self):
        pass

    def test_create_new_expense_and_update_budget(self):
        pass

    """
    The budget can calculate what percent of income is spent in a given category
    """
    def test_budget_percents(self):
        pass

if __name__ == '__main__':
    unittest.main()
