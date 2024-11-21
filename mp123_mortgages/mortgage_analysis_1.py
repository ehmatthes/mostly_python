"""Analyze a mortgage loan."""

purchase_price = 500_000
interest_rate = 0.075
loan_term = 360

# Find a monthly payment that pays off the loan.
monthly_payment = 1.00
principal = purchase_price

total_principal = 0
total_interest = 0
while True:
    # Run the life of the loan with the current payment.
    for payment_num in range(loan_term):
        interest = (interest_rate/12) * principal
        toward_principal = monthly_payment - interest
        principal -= toward_principal

        total_interest += interest
        total_principal += toward_principal

    # Exit loop if loan is paid off.
    if principal <= 0:
        break

    # Loan was not paid off. Increase monthly payment, and reset loan.
    monthly_payment += 1.00
    principal = purchase_price

    total_principal = 0
    total_interest = 0

# Summarize loan.
total_paid = total_principal + total_interest
print("Loan summary:")
print(f"  Purchase price: ${purchase_price:,.2f}")
print(f"  Monthly payment: ${monthly_payment:,.2f}")
print(f"  Principal paid: ${total_principal:,.2f}")
print(f"  Total interest paid: ${total_interest:,.2f}")
print(f"  Total paid: ${total_paid:,.2f}")
