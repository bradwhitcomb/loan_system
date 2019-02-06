import unittest
from loan_sys_functions import excess_availability

customer = Customer('bradco', 494, 332)
loan = Loan(50000, 1000)
collateral = Accounts_receivable(50000, 5000, .75)
interest = Interest(.03, .07)

class TestExcessAvailability(unittest.TestCase):
    def test_excess_availability(self):
        self.assertEquals(excess_availability(collateral, loan),5000)
