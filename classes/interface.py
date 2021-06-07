from .budget import Budget


class BudgetInterface:
    def __init__(self, name):
        self.budget = Budget(name)
        self.name = name

    def run(self):
        print(
            f"Welcome, {self.name}, to the nightmarish hellscape that is your personal finances!")
        print("_" * 60)
        while True:
            mode = input(self.main_menu())
            if mode == '1':
                sub_mode = input(self.budget_menu())
            elif mode == '2':
                income_data = {'category': 'income'}
                income_data['name'] = input("Enter income name: \n")
                income_data['amount'] = input("Enter income amount: \n")
                income_data['date'] = input("Enter the income date: \n")
                print(income_data)
                self.budget.add_income(income_data)
                self.budget.save()
            elif mode == '4':
                print("Quick Budget: ")
                print(self.budget)
            elif mode == '5':
                print("After witnessing the grim finality your income guarantees you, we hope the rest of your day is EXCELLENT!")
                return


    def main_menu(self):

        return("\nWhat would you like to do?\nOptions:\n1. Monthly Budget Breakdown \n2. Add income\n3. Add expense\n4. Quick Budget\n5. Quit\n")
    
    def budget_menu(self):
        return

    def income_menu(self):
        pass

    def expense_menu(self):
        pass


