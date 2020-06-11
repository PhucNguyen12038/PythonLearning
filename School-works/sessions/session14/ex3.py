import random
import math

def distance(a,b):
    d = (b[0]-a[0]) * (b[0]-a[0]) + (b[1]-a[1]) * (b[1]-a[1])
    d = math.sqrt(d)
    return d

x = random.randint(0,5)
y = random.randint(0,7)
a = (x,y)
print(a)
c = 0
guess = False
while guess == False:
    x1 = int(input("Enter x: "))
    y1 = int(input("Enter y: "))
    b = (x1,y1)
    c = c + 1
    dis = distance(a,b)
    if dis == 0:
        guess = True
        print("Correctly")
    else:
        print("Distance is {}".format(dis))

print("Number of guess is {}".format(c))
        
