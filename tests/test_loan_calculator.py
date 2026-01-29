import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from test import main as loan_calculator


class TestLoanCalculator(unittest.TestCase):

    def test_calculate_loan_basic(self):
        """Test basic loan calculation"""
        monthly, interest, total = loan_calculator.calculate_loan(10000, 5, 1)
        self.assertAlmostEqual(monthly, 856.07, delta=0.01)
        self.assertAlmostEqual(total, 10272.90, delta=0.01)
        self.assertAlmostEqual(interest, 272.90, delta=0.01)

    def test_calculate_loan_zero_interest(self):
        """Test loan with 0% interest rate"""
        monthly, interest, total = loan_calculator.calculate_loan(12000, 0, 1)
        self.assertEqual(monthly, 1000.0)
        self.assertEqual(interest, 0.0)
        self.assertEqual(total, 12000.0)

    def test_calculate_loan_large_amount(self):
        """Test typical mortgage calculation"""
        monthly, interest, total = loan_calculator.calculate_loan(250000, 6.5, 30)
        self.assertAlmostEqual(monthly, 1580.17, delta=0.01)
        self.assertAlmostEqual(interest, 318861.22, delta=0.01)
        self.assertAlmostEqual(total, 568861.22, delta=0.01)

    def test_calculate_loan_short_term(self):
        """Test short term loan (1 year)"""
        monthly, interest, total = loan_calculator.calculate_loan(5000, 10, 1)
        self.assertAlmostEqual(round(monthly, 2), 439.58)
        self.assertAlmostEqual(round(interest, 2), 274.95)


    def test_calculate_loan_high_interest(self):
        """Test high interest rate loan"""
        monthly, interest, total = loan_calculator.calculate_loan(1000, 24, 1)
        self.assertAlmostEqual(monthly, 94.56, delta=0.01)
        self.assertGreater(interest, 100)  # Interest should be significant

    def test_calculate_loan_long_term(self):
        """Test long term loan (15 years)"""
        monthly, interest, total = loan_calculator.calculate_loan(100000, 4, 15)
        self.assertAlmostEqual(monthly, 739.69, delta=0.01)
        self.assertGreater(total, 100000)

    def test_total_paid_equals_principal_plus_interest(self):
        """Verify total = principal + interest"""
        principal = 50000
        monthly, interest, total = loan_calculator.calculate_loan(principal, 7, 5)
        self.assertAlmostEqual(total, principal + interest, delta=0.01)

    def test_monthly_payment_positive(self):
        """Monthly payment should always be positive"""
        monthly, _, _ = loan_calculator.calculate_loan(10000, 5, 2)
        self.assertGreater(monthly, 0)


if __name__ == '__main__':
    unittest.main()