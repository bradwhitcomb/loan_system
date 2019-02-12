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
       

    

# borrower = Customer("best_llc", 4042223344, 30309)
# loan = Loan(500000,0)
# collateral = Accounts_receivable(35000, 3500, .85)
# interest = Interest(.03, .0375)
# print(borrower,'\n',loan,'\n',collateral,'\n',interest)

# print(borrower.name, borrower.email, borrower.city)
# print(collateral.past_dues, collateral.total_aging, collateral.advance_rate)
# print(loan.commitment, loan.loan)
# print(interest.base_rate, interest.margin)

# a = loan.loan_presentments(50)
# b = loan.loan_payment(15)
# print(loan.loan,a,loan.loan,b,loan.loan)


# def create_new_acount():
#     global borrower
#     Customer.dates = []
#     name = input("What is Customer Name?  ")
#     email = int(input("What is Customer email number? "))
#     city = int(input("What is Customer city? "))

#     borrower = Customer(name, email, city)
#     return borrower


# def excess_availability(collateral_object, loan_object):
#     """ Nets the loan against the collateral value to calculate unused availability"""
#     availability = collateral_object.loan_availability()
#     loan_outstanding = loan_object.loan
#     excess_availability = availability - loan_outstanding
#     return excess_availability

# def interest_calculation(yyyy, mm, dd):
    
#     today = date(yyyy, mm, dd)
#     elapsed_days = today - Customer.dates[-1]
#     Customer.dates.append(today)
#     days_interest = elapsed_days.days
#     accrued_interest = days_interest/360 * interest.interest_rate() * loan.loan
#     loan.loan_presentments(accrued_interest)
#     return accrued_interest, loan.loan
# loan.loan

# status = {
#     "Borrower": borrower.name,
#     "Commitment": loan.commitment,
#     "Loan_outstanding": loan.loan,
#     "Collateral_availability": collateral.loan_availability(),
#     "Un-presentmentsn_availability" : collateral.loan_availability() - loan.loan
    
# }

# x = date(2019, 1, 10)
# loan_amount = [0]
# i_rate = [0]
# accrued_interest = [0]


# x =  date(2019, 1, 10)
# day_31 = [1,3,5,7,8,10,12]
date_hist = [0]
loan_hist = [0]
i_rate_hist = [0]
accrued_interest_hist = [0]


# def daily_build(yyyy, mm, dd, loan_object, interest_object):
#     date_hist.append(date(yyyy,mm,dd))
#     loan_hist.append(loan_object.loan)
#     i_rate_hist.append(interest_object.interest_rate())
#     daily_accrued_interest = loan_object.loan * interest_object.interest_rate()/360
#     accrued_interest_hist.append(daily_accrued_interest)


# def interest_calculation(first_yyyy, first_mm, first_dd, end_yyyy, end_mm, end_dd):
#     """ Calculate the total interest between two periods inclusive of the last period.  if you input the first day of the January and the last day of January the function will return 31 days of interest"""
#     first_of_period = date(first_yyyy, first_mm, first_dd)
#     end_of_period = date(end_yyyy, end_mm, end_dd)
#     first = date_hist.index(first_of_period)
#     end = date_hist.index(end_of_period)
#     period_interest = sum(accrued_interest_hist[first:end + 1])
#     return period_interest


    
# def interest_settlement(first_yyyy, first_mm, first_dd, end_yyyy, end_mm, end_dd, loan_object):
#     """ Sum the period's (per month if compounded monthly) interest and add it to the loan """
#     interest_presentments = interest_calculation(first_yyyy, first_mm, first_dd, end_yyyy, end_mm, end_dd)
#     loan_object.loan_presentments(interest_presentments)


# def collections(collateral_object, loan_object, amount):
#     collateral_object.total_aging -= amount
#     loan_object.loan -= amount


# day one!
# loan.loan_presentments(1000)
# daily_build(2019,1,1,loan, interest)
# print(excess_availability(collateral,loan))
# loan.loan_presentments(1000)
# daily_build(2019,1,2,loan, interest)
# excess_availability(collateral, loan)
# loan.loan_presentments(1000)
# daily_build(2019,1,3, loan, interest)
# excess_availability(collateral, loan)
# loan.loan_presentments(1000)
# daily_build(2019,1,4, loan, interest)
# print(excess_availability(collateral, loan))
# loan.loan_presentments(1000)
# daily_build(2019,1,5,loan, interest)

# status = {
#     "Borrower": borrower.name,
#     "Commitment": loan.commitment,
#     "Loan_outstanding": loan.loan,
#     "Collateral_availability": collateral.loan_availability(),
#     "Un-presentmentsn_availability" : collateral.loan_availability() - loan.loan
    
# }

# print(loan.loan)
# print(f'Month of interest {interest_calculation(2019,1,3,2019,1,5)}')
# interest_settlement(2019, 1, 3, 2019, 1, 5, loan)
# print(loan.loan)

# print(accrued_interest_hist)


# collections(collateral, loan, 1000)
# print(loan.loan)

# def loan_advance(collateral_object, loan_object, advance_amount):
#     """ Calculates if the borrower has sufficient excess availability.  If EA can't cover the advance then the transaction is rejected and """
#     if excess_availability(collateral_object, loan_object) > advance_amount:
#         loan_object.loan_presentments(advance_amount)
#     else:
#         print(f'Your advance of ${advance_amount:,.2f} exceeds your excess_availability of ${excess_availability(collateral_object, loan_object):,.2f}.  ADVANCE REJECTED!')
        
        
    
        


# print(loan)  

# loan.loan_presentments(50)

# print(loan)

# loan_advance(collateral, loan, 5000)
# print(loan)
