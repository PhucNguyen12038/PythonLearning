import array as arr
month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']

mn = input("Enter month number: ")
try:
    month = int(mn)
except:
    print("Input number")
    
if month <= 0:
    print("Month number must be in range [1-12]")
elif month > 12:
    print("The year has only 12 months")
else:
    print(month_list[month-1])

