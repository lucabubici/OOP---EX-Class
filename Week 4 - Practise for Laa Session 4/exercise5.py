gross_income = int(input("Insert your gross income."))
tax_threshhold = 18200

if gross_income <= tax_threshhold:
    pay_tax = 0
    print(f"You have ${int(pay_tax)} to pay. Your net income is ${gross_income - pay_tax}.")
elif gross_income >= 18201 and gross_income <= 45000:
    pay_tax = (gross_income - tax_threshhold) / 100 * 19
    print(f"You have ${int(pay_tax)} to pay. Your net income is ${int(gross_income - pay_tax)}.")
elif gross_income >= 45001 and gross_income <= 120000:
    pay_tax = (gross_income - tax_threshhold) / 100 * 32.5
    print(f"You have ${int(pay_tax)} to pay. Your net income is ${int(gross_income - pay_tax)}.")
elif gross_income >= 120001 and gross_income <= 180000:
    pay_tax = (gross_income - tax_threshhold) / 100 * 37
    print(f"You have ${int(pay_tax)} to pay. Your net income is ${int(gross_income - pay_tax)}.")
else:
    pay_tax = (gross_income - tax_threshhold) / 100 * 45
    print(f"You have ${int(pay_tax)} to pay. Your net income is ${int(gross_income - pay_tax)}.")

