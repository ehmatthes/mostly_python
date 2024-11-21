"""Analyze a mortgage loan."""

purchase_price = 500_000
interest_rate = 0.075
loan_term = 360

# Find a monthly payment that pays off the loan.
monthly_payment = 1.00
principal = purchase_price

while True:
    # Run the life of the loan with the current payment.
    for payment_num in range(loan_term):
        interest = (interest_rate/12) * principal
        towards_principal = monthly_payment - interest
        principal -= towards_principal

    # Summarize results.
    print(f"Tried {monthly_payment:,.2f}")
    print(f"  Remaining principal: {principal:,.2f}")

    # Exit loop if loan is paid off.
    if principal <= 0:
        break

    # Loan was not paid off. Increase monthly payment, and reset loan.
    monthly_payment += 1.00
    principal = purchase_price
