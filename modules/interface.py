from modules import budget
from modules.budget import Budget
from modules.month import Month
from modules.transaction import Transaction
from modules.category import Category

# REQUIREMENTS:
## It should Keep track of expenses including but not limited to Living, Food, Travel, Savings, and Leisure.
## Users should be able to update their monthly income.
## It should know how much the user's monthly costs are.
## It should be able to create and calculate new expenses.
## It should be able to tell users what percent of their monthly income is being spent in each category.

# main runner for this app
class Interface:

    menu_options = [
        "1. See Total Monthly Expenses",
        "2. See % by Category for a Month",
        "3. Add Transaction",
        "4. Set Monthly Income",
        "5. Quit"
    ]

    def __init__(self):
        self.budget = Budget()

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_user_menu_choice()
            print("")

            if choice == 1:
                self.show_monthly_costs()

            elif choice == 2:
                self.show_monthly_costs_by_category_pct()

            elif choice == 3:
                self.add_transaction()

            elif choice == 4:
                self.set_monthly_income()

            # 0 = force quit
            elif choice == 5 or choice == 0:
                break # quit

            print("")

    def print_menu(self):
        print("----------------")
        print("MAIN MENU:")
        for option in self.menu_options:
            print(option)
        print("----------------")

    def get_user_menu_choice(self):
        num_choices = len(self.menu_options)
        # if no menu options, return 0 (force quit)
        if num_choices == 0:
            return 0

        # prompt user to enter a valid choice (1-num_choices)
        choice = 0
        while choice == 0 or choice > num_choices: 
            choice = int(input(f"...Select choice (1-{num_choices}): "))

        return choice

    def show_monthly_costs(self):
        month = int(input("...Enter a month (0-11): "))
        costs = self.budget.get_monthly_costs(month)
        print(f">>> You spent {costs} dollars in {Month(month).name}!")

    def show_monthly_costs_by_category_pct(self):
        month = int(input("...Enter month: "))

        category_pct_costs = self.budget.get_monthly_category_spending_pct(month)
        for cat in category_pct_costs:
            print(f"{Category(cat).name}: {category_pct_costs[cat]}% of all expenses in {Month(month).name}")

    def add_transaction(self):
        amount = int(input("...Enter amount spent: "))
        category = int(input("...Enter category: "))
        month = int(input("...Enter month: "))
        txn = Transaction(amount, category, month)

        try:
            self.budget.add_transaction(txn)
            print(">>> Transaction added!")
        except Exception as e:
            print(f">>> ERROR: {e}")

    def set_monthly_income(self):
        try:
            income = int(input("...What's your monthly income? "))
            self.budget.set_monthly_income(income)
        except Exception as e:
            print(f">>> ERROR: {e}")

