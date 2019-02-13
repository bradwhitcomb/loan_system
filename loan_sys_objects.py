from datetime import date

class Customer(object):
    """ Creates a customer object that holds general information about the borrower"""
    
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city
        

    def __repr__(self):
        return (f'Customer name: {self.name}\nCustomer email: {self.email}\nCustomer Location: {self.city} ')


class Loan(object):
    """ Creates a revolving loan facility and distinguished between the commitment amount and the loan outstanding"""
    def __init__(self, commitment_amount, loan=0):    
        self.commitment = commitment_amount
        self.loan = loan
        

    def __repr__(self):
        return (f'Commitment:${self.commitment:,}\nLoan: ${self.loan:,}')


    def loan_draw(self, presentments):
        """Creates presentments downs on the credit facility which increase the outstanding loan"""
        self.loan += presentments
        return self.loan


    def loan_payment(self, payment):
        """ Provides for a payment which reduces the outstanding loan """
        self.loan -= payment 
        return self.loan   


class Accounts_receivable(object):
    """ Creates the collateral object """
    def __init__(self, total_aging, past_dues, advance_rate):
        self.total_aging = total_aging 
        self.past_dues = past_dues
        self.advance_rate = advance_rate
       

    def __repr__(self):
        return (f'Total Aging:${self.total_aging:,.0f}\nPast Dues: ${self.past_dues:,.0f}\nAdvance Rate: {self.advance_rate:.2%}')


    def loan_availability(self):
        """ Calculates the total loan availability from the gross aging"""
        availability = (self.total_aging - self.past_dues) * self.advance_rate
        return availability


    def sales_collections(self, collections):
        """ Takes collections and reduces the gross aging"""

        self.total_aging = self.total_aging - collections
        return self.total_aging


    def new_sales(self, sales):
        """ Takes new sales and increases the gross aging """
        self.total_aging = self.total_aging + sales
        return self.total_aging


class Interest(object):
    """ Creates the interest object which tracks earned interest on the loans """
    
    def __init__(self, base_rate, margin):
        self.base_rate = base_rate
        self.margin = margin
        

    def __repr__(self):
        return (f'Base Rate:{self.base_rate:.2%}\nMargin: {self.margin:.2%}')


    def interest_rate(self):
        """ The interest rate is the sum of the base rate plus the margin """
        return self.base_rate + self.margin
       

    
date_hist = [0]
loan_hist = [0]
i_rate_hist = [0]
accrued_interest_hist = [0]






    




