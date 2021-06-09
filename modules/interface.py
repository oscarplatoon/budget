from modules.budget import Budget
from modules.month import Month
from modules.transaction import Transaction
from modules.category import Category

class Interface:
    
    def __init__(self):
        self.budget = Budget()
        
    def run(self):
        while True:
            self.print_menu()
            option = int(input("Select option: "))
            if option == 1:
                month = int(input("Enter a month (0 - 11): "))
                try:
                    costs = self.budget.get_monthly_costs(month)
                    print(f"You spent ${costs} in {Month.get_month_name(month.name)}.")
                except:
                    print("ERROR ADDING TRANSACTION!!")
            elif option == 2:
                month = int(input("Enter Month: "))
                category_pct_costs = self.budget.get_month_costs_per_category(month)
                for cat in category_pct_costs:
                    print(f"{Category(cat).name}: %{category_pct_costs[cat]} of all expenses in the month of {Month(month).name}.")
            elif option == 3:
                amount = int(input("Enter amount spent: "))
                category = int(input("Enter category: "))
                month = int(input("Enter month: "))
                txn = Transaction(amount, category, month)
                
                try:
                    self.budget.add_transaction(txn)
                    print("Transaction added")
                except:
                    print("ERROR ADDING TRANSACTION!!")
            elif option == 5:
                break
            
    def print_menu(self):
        print("1. See Total Monthly Expenses")
        print("2. See Costs by Category (pct)")
        print("3. Add Transaction")
        print("4. Set Monthly Income")
        print("5. Quit")
            