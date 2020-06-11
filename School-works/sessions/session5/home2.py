import datetime
now = datetime.datetime.now()

dayInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

def number_of_days(n):
    
    if n > 0 and n <= 12:
        
        if n != 2:
            return dayInMonth[n-1]            
        else:
            y = now.year  
            leapYear = False
            if y % 4 != 0:
                leapYear = False
            elif y % 100 != 0:
                leapYear = True
            elif y % 400 != 0:
                leapYear = False
            else:
                leapYear = True
            
            if leapYear == True:
                return 29
            else:
                return 28
    else:
        return -1
    

while True:
    
    n = input("Enter number of month or 'done': ")
    if n == 'done':
        break
    try:
        n = int(n)
    except:
        n = -1
    if n == -1:
        print("Number of month must be in the range 1-12")
    r = number_of_days(n)
    if r == -1:
        print("Please enter a valid number")    
    else:
        print("This month has " + str(r) + " days")