
n = 10
x = 100.0

while n >= 0:
    try:
        x = x / n
    except:
        x = x + 1
        print("a")
    n = n-1
    
print(x)    