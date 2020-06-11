def price_difference(a,b,c):
    return b * c - a

i = int(input("What is the price of the product? "))
mp = int(input("What is the monthly payment on the first installment plan? "))
m = int(input("How many months does the first installment plan last? "))
mp2 = int(input("What is the monthly payment on the second installment plan? "))
m2 = int(input("How many months does the second installment plan last? "))

d1 = price_difference(i,mp,m)
d2 = price_difference(i,mp2,m2)

if d1 < d2:
    print("The first installment plan is better!")
elif d1 > d2:
    print("The second installment plan is better!")
else:
    print("No installment plan is better!")