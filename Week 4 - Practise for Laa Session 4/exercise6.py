expenditure = float(input("How much the customer has spent?"))
printed_message = "The total checkout with applied discount is"

if expenditure >= 1000:
    discount_apply = 30
    final_expenditure = expenditure - (expenditure / 100 * discount_apply)
    print(printed_message, final_expenditure)
elif expenditure >= 750 and expenditure <= 999:
    discount_apply = 25
    final_expenditure = expenditure - (expenditure / 100 * discount_apply)
    print(printed_message, final_expenditure)
elif expenditure >= 500 and expenditure <= 749:
    discount_apply = 20
    final_expenditure = expenditure - (expenditure / 100 * discount_apply)
    print(printed_message, final_expenditure)
elif expenditure >= 250 and expenditure <= 499:
    discount_apply = 15
    final_expenditure = expenditure - (expenditure / 100 * discount_apply)
    print(printed_message, final_expenditure)
elif expenditure >= 100 and expenditure <= 249:
    discount_apply = 10
    final_expenditure = expenditure - (expenditure / 100 * discount_apply)
    print(printed_message, final_expenditure)
else:
    discount_apply = 5
    final_expenditure = expenditure - (expenditure / 100 * discount_apply)
    print(printed_message, final_expenditure)
