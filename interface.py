from actions import Actions
from data import Data

class Interface(Data):

    def run(self):
        while True:
            response = input(f"\nWhat would you like to do?\nOptions:\n1. Input Expense\n2. Show Report: Cost by Month\n3. Show Report: Percent of monthly income spent per category\n4. Update monthly income\n5. Quit\n")
            if response == '1':
                Actions.add_expense(self)
            elif response == '2':
                Actions.show_month_costs(self)
            elif response == '3':
                Actions.percent_by_category(self)
            elif response == '4':
                Actions.update_monthly_income(self)
            elif response == '5':
                break
            else:
                print("\nInvalid input\n")





    

        


