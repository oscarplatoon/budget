class Actions():

    def  add_expense(self):
        re_month = input(f'Enter month(i.e. enter "1" for January):\t')
        re_cost = input(f'Enter cost:\t')
        re_name = input(f'Enter item name:\t')
        re_category = input(f'Enter item category\n(1-Living,2-Food,3-Travel,4-Savings,5-Leisure):\t')
      
        self.transactions.append([re_month,re_cost,re_name,re_category])

    def show_month_costs(self):
        total = 0
        re_month = input(f'Enter month(i.e. enter "1" for January):\t')
        print(f'\n\n\nTransactions for the month of {self.month[int(re_month)]}:')
        for trx in self.transactions:
            if trx[0]== re_month:
                print(f'Cost: {trx[1]}\tName: {trx[2]}')
                total += int(trx[1])
        print(f'\nTotal: {total}\n\n')


    def percent_by_category(self):
        total = 0
        cat_totals = [0,0,0,0,0]
        re_month = input(f'Enter month(i.e. enter "1" for January):\t')
        for trx in self.transactions:
            if trx[0]== re_month:
                total += int(trx[1])
            cat_totals[int(trx[3])-1] += int(trx[1])
        print(f'\n\nReport: Percent of monthly income spent per category\n')
        print(f'Monthly Income: {self.monthly_income}\tTotal Spent: {total}')
        print(f'Living: {(cat_totals[0]/self.monthly_income)*100}%\nFood: {(cat_totals[1]/self.monthly_income)*100}%')
        print(f'Travel: {(cat_totals[2]/self.monthly_income)*100}%\nSavings: {(cat_totals[3]/self.monthly_income)*100}%')
        print(f'Leisure: {(cat_totals[4]/self.monthly_income)*100}%')

    def update_monthly_income(self):
        re_income = input(f'\nEnter new income rounded to the nearest dollar:\t')
        self.monthly_income = int(re_income)
        print(f'\nIncome Updated\n\n')