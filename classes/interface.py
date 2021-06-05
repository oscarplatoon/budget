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
                sub_mode = input(self.income_menu())
            elif mode == '3':
                sub_mode = input(self.expense_menu())
            elif mode == '4':
                print("Quick Budget: ")
                print(self.budget)
            elif mode == '5':
                print("After witnessing the grim finality your income guarantees you, we hope the rest of your day is EXCELLENT!")
                return


    def main_menu(self):

        return("\nWhat would you like to do?\nOptions:\n1. Budget Menu\n2. Income Menu\n3. Expense Menu\n4. Quick Budget\n5. Quit\n")
    
    def budget_menu(self):
        return

    def income_menu(self):
        pass

    def expense_menu(self):
        pass


