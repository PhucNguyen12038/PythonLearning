i = input(" Enter your annual income: ")
try:
    income = float(i)
except:
    income = -1
if income > 0:
    if income < 6000:
        tax = income
        print(" Your tax-free income is ",str(tax))
    elif income >= 6000 and income < 14400:
        tax = 6000
        print(" Your tax-free income is ",str(tax))
    elif income >= 14400 and income < 25200:
        tax = 6000 - 6000 / 10800 * (income - 14400)
        tax = round(tax,2)
        print(" Your tax-free income is ",str(tax))
    else:
        tax = 0
        print(" Your tax-free income is ",str(tax))
else:
    print("Input number")