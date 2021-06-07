from modules import category
from modules.category import Category

# main manager for our budgeting
class Budget:
    def __init__(self):
        self.income = 0
        self.transactions = []

    # Users should be able to update their monthly income.
    def set_monthly_income(self, income):
        self.income = income

    # It should know how much the user's monthly costs are.
    def get_monthly_costs(self, month):
        monthly_costs = 0
        for txn in self.transactions:
            if txn.month == month:
                monthly_costs += txn.amount
        return monthly_costs

    def get_monthly_costs_per_category(self, month):
        category_costs = {}
        for cat in Category:
            category_costs[cat.value] = 0

        for txn in self.transactions:
            if txn.month == month:
                category_costs[txn.category] += txn.amount
        
        return category_costs

    def add_transaction(self, txn):
        monthly_cost = self.get_monthly_costs(txn.month)
        
        # raise an exception if the new transaction will take us over our budget for the month and do not add transaction
        if monthly_cost + txn.amount > self.income:
            raise Exception("This transaction will take you over your budget!")
        
        self.transactions.append(txn)

    def get_monthly_category_spending_pct(self, month):
        total_costs = self.get_monthly_costs(month)
        category_costs = self.get_monthly_costs_per_category(month)
        category_pct_costs = {}

        # calculate percentages for each category spending
        for cat in category_costs:
            category_pct_costs[cat] = round(100.0 * (category_costs[cat] / total_costs), 2)
        
        return category_pct_costs

