import time
n = input("Enter positive integer number: ")
time1 = time.time()
try:
    n = int(n)
except:
    n = -1
if n < 0:
    print("Invalid input")
else:
    s = 2
    
    for a in range (1,n+1):
        b = 2 * a / (2 * a - 1)
        c = 2 * a / (2 * a + 1)
        s = s * b * c
    time2 = time.time()
    
    print("Result is ",s)
    t = time2 - time1
    print(t)