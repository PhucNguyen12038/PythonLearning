aniver_year = [1,2,3,5]
def has_anniversary(a,b):
    c = b - a
    for i in aniver_year:
        if c == i:
            return True
    if c % 5 == 0:
        return True
    return False
y1 = input("Started working in: ")
y2 = input("First year: ")
y3 = input("Last year: ")

try:
    startY = int(y1)
    firstY = int(y2)
    secondY = int(y3)
except:
    firstY = -1
    secondY = -1
    startY = -1
if firstY != -1 and secondY != -1 and startY != -1:
    for i in range(firstY, secondY+1):
        if has_anniversary(startY,i) == True:
            print(i)
else:
    print("Invalid input")
    
