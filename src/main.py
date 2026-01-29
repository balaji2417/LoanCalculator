def calculate_loan(principal, annual_rate, years):

    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12

    if monthly_rate == 0:
        monthly_payment = principal / num_payments
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / (
                    (1 + monthly_rate) ** num_payments - 1)

    total_paid = monthly_payment * num_payments
    total_interest = total_paid - principal

    return monthly_payment, total_interest, total_paid


def display_amortization(principal, annual_rate, years):

    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12
    monthly_payment, _, _ = calculate_loan(principal, annual_rate, years)

    balance = principal
    print(f"\n{'Month':<8}{'Payment':<12}{'Principal':<12}{'Interest':<12}{'Balance':<12}")
    print("-" * 56)
    for month in range(1, num_payments + 1):
        interest = balance * monthly_rate
        principal_paid = monthly_payment - interest
        balance -= principal_paid

        if month <= 12 or month > num_payments - 3:
            print(
                f"{month:<8}${monthly_payment:<11.2f}${principal_paid:<11.2f}${interest:<11.2f}${max(0, balance):<11.2f}")
        elif month == 13:
            print("... (showing first 12 and last 3 months) ...")


def main():
    print("=" * 40)
    print("       LOAN CALCULATOR")
    print("=" * 40)

    try:
        principal = float(input("\nLoan amount ($): "))
        annual_rate = float(input("Annual interest rate (%): "))
        years = int(input("Loan term (years): "))

        if principal <= 0 or annual_rate < 0 or years <= 0:
            print("Please enter valid positive values.")
            return

        monthly_payment, total_interest, total_paid = calculate_loan(principal, annual_rate, years)

        print("\n" + "=" * 40)
        print("           RESULTS")
        print("=" * 40)
        print(f"Monthly Payment:    ${monthly_payment:,.2f}")
        print(f"Total Interest:     ${total_interest:,.2f}")
        print(f"Total Amount Paid:  ${total_paid:,.2f}")

        show_schedule = input("\nShow amortization schedule? (y/n): ").lower()
        if show_schedule == 'y':
            display_amortization(principal, annual_rate, years)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()