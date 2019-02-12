from datetime import date
from loan_sys_objects import Customer
from loan_sys_objects import Loan
from loan_sys_objects import Accounts_receivable
from loan_sys_objects import Interest
import pandas as pd

date_hist_str = [date(2018,12,31)]
loan_hist =[0]
i_rate_hist = [0]
accrued_interest_hist = [0]
liquidity_hist = [0]

def excess_availability(collateral_object, loan_object):
    """ Nets the loan against the collateral value to calculate unused availability"""
    availability = collateral_object.loan_availability()
    loan_outstanding = loan_object.loan
    excess_availability = availability - loan_outstanding
    return excess_availability


def daily_build(yyyy, mm, dd, loan_object, interest_object, collateral_object):
    date_hist_str.append(date(yyyy,mm,dd))
    loan_hist.append(loan_object.loan)
    liquidity_hist.append(excess_availability(collateral_object, loan_object))
    i_rate_hist.append(interest_object.interest_rate())
    daily_accrued_interest = loan_object.loan * interest_object.interest_rate()/360
    accrued_interest_hist.append(daily_accrued_interest)


def interest_calculation(first_yyyy, first_mm, first_dd, end_yyyy, end_mm, end_dd):
    """ Calculate the total interest between two periods inclusive of the last period.  if you input the first day of the January and the last day of January the function will return 31 days of interest"""
    first_of_period = date(first_yyyy, first_mm, first_dd)
    end_of_period = date(end_yyyy, end_mm, end_dd)
    first = date_hist_str.index(first_of_period)
    end = date_hist_str.index(end_of_period)
    period_interest = sum(accrued_interest_hist[first:end + 1])
    return period_interest


def interest_settlement(first_yyyy, first_mm, first_dd, end_yyyy, end_mm, end_dd, loan_object):
    """ Sum the period's (per month if compounded monthly) interest and add it to the loan """
    interest_draw = interest_calculation(first_yyyy, first_mm, first_dd, end_yyyy, end_mm, end_dd)
    loan_object.loan_draw(interest_draw)


def sales_collections(collateral_object, loan_object, collections):
    """ Sweeps collections against the collateral and the loan """
    collateral_object.total_aging -= collections
    loan_object.loan -= collections


# def loan_advance(collateral_object, loan_object, advance_amount, yyyy, mm, dd, interest_object):
#     """ Calculates if the borrower has sufficient excess availability.  If EA can't cover the advance then the transaction is rejected and """
#     if excess_availability(collateral_object, loan_object) > advance_amount:
#         loan_object.loan_draw(advance_amount)
#         daily_build(yyyy, mm, dd, loan_object, interest_object, collateral_object)
        
#     else:
#         print(f'Your advance of ${advance_amount:,.2f} exceeds your excess_availability of ${excess_availability(collateral_object, loan_object):,.2f}:  ADVANCE REJECTED!')

def fund_presentments(collateral_object, loan_object, presentments):
    """ Calculates if the borrower has sufficient excess availability.  If EA can't cover the advance then the transaction is rejected and """
    if excess_availability(collateral_object, loan_object) > presentments:
        loan_object.loan_draw(presentments)    
    else:
        print(f'Your advance of ${presentments:,.2f} exceeds your excess_availability of ${excess_availability(collateral_object, loan_object):,.2f}:  ADVANCE REJECTED!')


customer = Customer('bradco', 494, 332)
loan = Loan(50000, 1000)
collateral = Accounts_receivable(50000, 5000, .75)
interest = Interest(.03, .07)

# loan_advance(collateral, loan, 5000)
# print(loan)
# loan_advance(collateral, loan, 4000)

# print(loan)
# loan_advance(collateral, loan, 400000)

# print(loan)

daily_build(2019, 1, 4, loan, interest, collateral)
sales_collections(collateral, loan, 500)
loan.loan_draw(500)
daily_build(2019, 1, 5, loan, interest, collateral)
sales_collections(collateral, loan, 500)
loan.loan_draw(5000)
daily_build(2019, 1, 6, loan, interest, collateral)
sales_collections(collateral, loan, 1000)
loan.loan_draw(2000)
daily_build(2019, 1, 6, loan, interest, collateral)


# loan_advance(collateral,loan,5000,2019,1,1,interest)
# loan_advance(collateral,loan,5000,2019,1,2,interest)
# loan_advance(collateral,loan,5000,2019,1,2,interest)
# loan_advance(collateral,loan,5000,2019,1,4,interest)
# loan_advance(collateral,loan,5000,2019,1,5,interest)
# loan_advance(collateral,loan,5000,2019,1,6,interest)
# loan_advance(collateral,loan,5000,2019,1,7,interest)
# loan_advance(collateral,loan,5000,2019,1,8,interest)
# loan_advance(collateral,loan,5000,2019,1,9,interest)
# loan_advance(collateral,loan,5000,2019,1,10,interest)
# loan_advance(collateral,loan,5000,2019,1,11,interest)
# loan_advance(collateral,loan,5000,2019,1,12,interest)

print(loan_hist)
print(liquidity_hist)
df = pd.DataFrame(
    {'loan':loan_hist,
     'Interest Rate': i_rate_hist,
     'Interest Accrual': accrued_interest_hist,
     'Liquidity': liquidity_hist,
     'Date': date_hist_str
    })
print(df)


sales_collections(collateral, loan, 1000)
loan.loan_draw(2000)
daily_build(2019, 1, 6, loan, interest, collateral)


presentments = 1500
collections = 750
growth_rate = 1.02
day = 6

for i in range(20):
    # presentments *= growth_rate
    # collections *= growth_rate
    # day +=1
    sales_collections(collateral, loan, collections)
    loan.loan_draw(presentments)
    daily_build(2019,1,day,loan,interest,collateral)
    presentments *= growth_rate
    collections *= growth_rate

    print(i, int(loan.loan), int(presentments), int(collections))

    
df = pd.DataFrame(
    {'loan':loan_hist,
     'Interest Rate': i_rate_hist,
     'Interest Accrual': accrued_interest_hist,
     'Liquidity': liquidity_hist,
     'Date': date_hist_str
    })

