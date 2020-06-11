c = 0
def darts(n):
    global c
    
    if n == 0:
        print("Game over!")
        return c
    else:
        print("Your score is {}".format(n))
        p = input("Enter the number of points: ")
        p = int(p)
        c+=1
        if p <= n:     
            return darts(n-p)
        else:
            print("You go broke...")
            return darts(n)
    
print("Number of throws is", darts(301))