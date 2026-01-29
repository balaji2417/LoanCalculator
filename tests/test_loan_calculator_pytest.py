import pytest
from test import main as loan_calculator

def test_calculate_loan_basic():
    """Test basic loan calculation"""
    monthly, interest, total = loan_calculator.calculate_loan(10000, 5, 1)
    assert round(monthly, 2) == 856.07
    assert round(total, 2) == 10272.89
    assert round(interest, 2) == 272.89

def test_calculate_loan_zero_interest():
    """Test loan with 0% interest rate"""
    monthly, interest, total = loan_calculator.calculate_loan(12000, 0, 1)
    assert monthly == 1000.0
    assert interest == 0.0
    assert total == 12000.0

def test_calculate_loan_large_amount():
    """Test typical mortgage calculation"""
    monthly, interest, total = loan_calculator.calculate_loan(250000, 6.5, 30)
    assert round(monthly, 2) == 1580.17
    assert round(interest, 2) == 318861.22
    assert round(total, 2) == 568861.22

def test_calculate_loan_short_term():
    """Test short term loan (1 year)"""
    monthly, interest, total = loan_calculator.calculate_loan(5000, 10, 1)
    assert round(monthly, 2) == 439.58
    assert round(interest, 2) == 274.92

def test_calculate_loan_high_interest():
    """Test high interest rate loan"""
    monthly, interest, total = loan_calculator.calculate_loan(1000, 24, 1)
    assert round(monthly, 2) == 94.56
    assert interest > 100  # Interest should be significant

def test_calculate_loan_long_term():
    """Test long term loan (15 years)"""
    monthly, interest, total = loan_calculator.calculate_loan(100000, 4, 15)
    assert round(monthly, 2) == 739.69
    assert total > 100000

def test_total_paid_equals_principal_plus_interest():
    """Verify total = principal + interest"""
    principal = 50000
    monthly, interest, total = loan_calculator.calculate_loan(principal, 7, 5)
    assert round(total, 2) == round(principal + interest, 2)

def test_monthly_payment_positive():
    """Monthly payment should always be positive"""
    monthly, _, _ = loan_calculator.calculate_loan(10000, 5, 2)
    assert monthly > 0

@pytest.mark.parametrize("principal,rate,years,expected_monthly", [
    (10000, 5, 1, 856.07),
    (20000, 6, 2, 886.55),
    (50000, 4.5, 5, 931.51),
])
def test_calculate_loan_parametrized(principal, rate, years, expected_monthly):
    """Parametrized test for various loan scenarios"""
    monthly, _, _ = loan_calculator.calculate_loan(principal, rate, years)
    assert round(monthly, 2) == expected_monthly