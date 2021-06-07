from classes.budget import Budget


class Interface:

    def __init__(self, name, income):
        self.name = name
        self.budget = Budget(income)


    def run(self):
        print(f'Welcome {self.name} how may I assist you?')
        while True:
            mode = int(input(f'1. Update Income\n2. Check monthly income\n3. Expenses\n4. Exit\n'))

            if mode == 1:
                income = int(input('New monthly income :'))
                self.budget.set_monthly_income(income)
                print(f'New income of {income} saved!\n----------\n')
                print('Would you like to do anything else?')

            elif mode == 2:
                self.budget.get_monthly_income()
                print('Would you like to do anything else?')

            elif mode == 3:
                while True:
                    mode2 = int(input(f'What would you like to do {self.name}?\n1. Add expense \n2. Total expenses\n3. View percent breakdown\n4. Add new expense\n5. Go back to previous page\n'))

                    if mode2 == 1:
                        expense = int(input('Expense amount? :'))
                        type = input('Expense category? :')
                        self.budget.add_expense(expense, type)
                        
                    elif mode2 == 2:
                        self.budget.list_expenses()
                    elif mode2 == 3:
                        self.budget.percent_breakdown()
                    elif mode2 == 4:
                        pass
                    elif mode2 == 5:
                        break


            elif mode == 4:
                break
