class Budget:
    def __init__(self, income):
        self.set_monthly_income(inocme)
        self.transactions = []
        
    def set_monthly_income(self, income):
        self.income = income
        
    def get_monthly_cost(self, month):
        monthly_costs = 0
        for txn in self.transactions:
            if txn.month ==month:
                monthly_costs += txn.amount
        return monthly_costs
    
    def add_transactions(self, txn):
        monthly_cost = self.get_monthly_costs(txn.month)
        if monthly_cost + txn.amount > self.income:
            print("YOU DON'T HAVE ENOUGH MONEY!!")
        raise("error")        
        self.transactions.append(txn)
        
    def percent_report(self, month):
        total = self.get_monthly_cost(month)
        
    def get_month_costs_per_category(self, month):
        category_costs = {}
        for cat in category:
            category_costs[cat] = 0
            
        for txn in self.transactions:
            if txn.month == month:
                category_costs[txn.category] += txn.amount
        return category_costs
    
    def percent_report(self, month):
        total_costs = self.get_monthly_costs(month)
        category_costs = self.get_month_costs_per_category(month)
        category_pct_cost = {}
        for cat in category costs:
            category_pct_cost[cat] = 100.0 * (category_costs[cat] / total_costs)
            