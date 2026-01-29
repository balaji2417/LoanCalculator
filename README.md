# LoanCalculator

A Python-based loan calculator that computes monthly payments, total interest, and amortization schedules for loans.
Features

Calculate monthly loan payments
Compute total interest paid over the loan term
Generate amortization schedules
Support for various loan terms and interest rates

Installation

Clone the repository:

bashgit clone https://github.com/balaji2417/LoanCalculator.git
cd LoanCalculator

Install dependencies:

bashpip install -r requirements.txt
Usage
As a Command Line Application
bashpython src/loan_calculator.py
Example output:
========================================
       LOAN CALCULATOR
========================================

Loan amount ($): 250000
Annual interest rate (%): 6.5
Loan term (years): 30

========================================
           RESULTS
========================================
Monthly Payment:    $1,580.17
Total Interest:     $318,861.23
Total Amount Paid:  $568,861.23
As a Module
pythonfrom src.loan_calculator import calculate_loan

# Calculate loan details
monthly_payment, total_interest, total_paid = calculate_loan(
    principal=250000,    # Loan amount in dollars
    annual_rate=6.5,     # Annual interest rate (%)
    years=30             # Loan term in years
)

print(f"Monthly Payment: ${monthly_payment:,.2f}")
print(f"Total Interest: ${total_interest:,.2f}")
print(f"Total Paid: ${total_paid:,.2f}"
