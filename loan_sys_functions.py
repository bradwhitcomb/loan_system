from datetime import date
from loan_sys_objects import Customer
from loan_sys_objects import Loan
from loan_sys_objects import Accounts_receivable
from loan_sys_objects import Interest
import pandas as pd

date_hist_str = []
loan_hist =[]
i_rate_hist = []
accrued_interest_hist = []
liquidity_hist = []

def excess_availability(collateral_object, loan_object):
    """ Nets the loan against the collateral value to calculate unused availability"""
    availability = collateral_object.loan_availability()
    loan_outstanding = loan_object.loan
    excess_availability = availability - loan_outstanding
    return excess_availability


def daily_build(yyyy, mm, dd, loan_object, interest_object, collateral_object):
    """Calculates end of day loan balance, collateral value and interest accrual"""
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


def fund_presentments(collateral_object, loan_object, presentments):
    if excess_availability(collateral_object, loan_object) > presentments and loan_object.loan + presentments <= loan_object.commitment:
        loan_object.loan_draw(presentments) 
    elif excess_availability(collateral_object, loan_object) > presentments and loan_object.loan + presentments > loan_object.commitment:
        print(f'ADVANCE REJECTED: Borrower may not exceed the loan commitment of ${loan_object.commitment:,.2f}')
    else:
         print(f'Your advance of ${presentments:,.2f} exceeds your excess_availability of ${excess_availability(collateral_object, loan_object):,.2f}:  ADVANCE REJECTED!')
    

df = pd.DataFrame(
    {'loan':loan_hist,
     'Interest Rate': i_rate_hist,
     'Interest Accrual': accrued_interest_hist,
     'Excess Availability': liquidity_hist,
     'Date': date_hist_str
    })




