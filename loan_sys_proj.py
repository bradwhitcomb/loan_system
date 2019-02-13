import random 
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from loan_sys_objects import Customer, Loan, Accounts_receivable, Interest
from loan_sys_functions import excess_availability, sales_collections, fund_presentments, daily_build, interest_calculation
from loan_sys_functions import loan_hist, date_hist_str, i_rate_hist, accrued_interest_hist, liquidity_hist

new_co = Customer('New_Company', 'new@mail', 'roswell')
new_loan = Loan(5000000, 1000000)
new_collateral = Accounts_receivable(6000000, 600000, .85)
new_interest = Interest(.03, .035)

presentments = 125000
sales = 100000
collections = 80000
day = 1

for i in range(31):
    presentments *= random.uniform(1.0, 1.05)
    collections *= random.uniform(1.0, 1.05)
    sales *= random.uniform(1.0, 1.05)

    sales_collections(new_collateral, new_loan, int(collections))
    fund_presentments(new_collateral, new_loan, int(presentments))
    new_collateral.new_sales(int(sales))
    daily_build(2019, 3, day, new_loan, new_interest, new_collateral)
    
    day += 1
    if i > 0 and i % 30 == 0:
        interest_calculation(2019, 3, 1, 2019, 3, i)
        
       
df = pd.DataFrame(
    {'loan':loan_hist,
     'Interest Rate': i_rate_hist,
     'Interest Accrual': accrued_interest_hist,
     'Excess Availability': liquidity_hist,
     'Date': date_hist_str
    })
df.set_index('Date', inplace=True)
df['Cumulative Interest'] = df['Interest Accrual'].cumsum()
print(df)
print(len(date_hist_str), len(loan_hist))
print(df)
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()
