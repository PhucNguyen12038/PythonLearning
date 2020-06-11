s = input("Enter month number: ")
x = float(s)
y = x - 1
y = y / 2

if y <= 1: 
    print("Spring")
if y <= 2.5 and y > 1: 
    print("Summer")
if y >= 3 and y <= 4:
    print("Fall")
if y > 4 and y <= 5.5:
    print("Winter")


    