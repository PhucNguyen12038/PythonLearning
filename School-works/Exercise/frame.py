fn = input("Enter the first name: ")
ln = input("Enter the last name: ")
bd = input("Enter the birthday: ")
dd = input("Enter the dead day: ")

nameLength = len(fn) + len(ln) + 1
dayLength = len(bd) + len(dd) + 3
maxlength = nameLength
minLength = nameLength
if nameLength > dayLength:
    maxLength = nameLength
    minLength = dayLength
else:
    maxLength = dayLength
    minLength = nameLength
    
distanceToMax = 5
row = 6
a = maxLength + distanceToMax * 2
print("a = ",a)
b = (nameLength - dayLength) // 2
for x in range (0,row+1):
    for y in range (0,a+1):
        
        if x == 0 and y == 0:
            print("+",end='')
        elif x == 0 and y == a:
            print("+",end='')    
        elif x == 6 and y == 0:
            print("+",end='')
        elif x == 6 and y == a:
            print("+",end='')
            
        elif x == 0 and y > 0 and y < a:
            print("-",end='')
        elif x == 6 and y > 0 and y < a:
            print("-",end='')    
            
        elif x > 0 and x < row and y == 0:
            print("|",end='')    
        elif x > 0 and x < row and y == a:
            print("|",end='')
        elif x > 0 and x < row and y > 0 and y < a:
            print(" ",end='')
        if x == 2 and y == distanceToMax:
            print(fn + " " + ln,end='')
        if x == 4 and y == (distanceToMax + b):
            print(bd + " - " + dd,end='')
    
    print('\n')
            

