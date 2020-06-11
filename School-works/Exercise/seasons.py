s = input("Enter month number: ")
x = float(s)
y = x - 1
y = y / 2

if y >= 1 and y <= 2: 
    print("spring")
elif y <= 3.5 and y >= 2.5: 
    print("summer")
elif y >= 4 and y <= 5:
    print("autumn")
else:
    print("winter")


    