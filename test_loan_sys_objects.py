import unittest
from loan_sys_objects import Customer, Loan, Accounts_receivable, Interest
from loan_sys_functions import excess_availability

class TestLoanSys(unittest.TestCase):
    def setUp(self):
        self.cust1 = Customer('xyz_co', 'xyz@mail.com', 'Pensacola')
        self.loan1 = Loan(5000, 1000)
        self.ar1 = Accounts_receivable(5500, 500, .75)
        self.interest1 = Interest(.03, .0275)

    def tearDown(self):
        pass

    def test_customer(self):
        

        self.assertEqual(self.cust1.name, 'xyz_co')
        self.assertEqual(self.cust1.email, 'xyz@mail.com')
        self.assertEqual(self.cust1.city, 'Pensacola')

    def test_loan(self):
        

        self.assertEqual(self.loan1.commitment, 5000)
        self.assertEqual(self.loan1.loan, 1000)
        self.assertEqual(self.loan1.loan_draw(0), 1000)
        self.assertEqual(self.loan1.loan_payment(0), 1000)

    def test_accounts_receivable(self):
        
        self.assertEqual(self.ar1.total_aging, 5500)
        self.assertEqual(self.ar1.past_dues, 500)
        self.assertEqual(self.ar1.advance_rate, .75)
        self.assertEqual(self.ar1.loan_availability(), (5500-500)*.75)
        self.assertEqual(self.ar1.sales_collections(0), 5500)
        self.assertEqual(self.ar1.new_sales(0), 5500)
        

    def test_interest(self):

        
        self.assertEqual(self.interest1.base_rate, .03)
        self.assertEqual(self.interest1.margin, .0275)
        self.assertEqual(self.interest1.interest_rate(), .03+.0275)

    def test_excess_availability(self):
        self.assertEqual(excess_availability(self.ar1, self.loan1),2750)

    














if __name__ == "__main__":
    unittest.main()