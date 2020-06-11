w = int(input("Enter number of week: "))

def new_blossom(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 0
    elif n == 4:
        return 1
    elif n == 5:
        return 2
    
    
    else:
        fibo = 1
        fibo_previous = 1
        for i in range (2, n-2):
            temp = fibo
            fibo = fibo + fibo_previous
            fibo_previous = temp
            #fibo = fibo - 1
            
        return fibo
#if w == 3:
#    print("Number of new blossoms will be 0")
#else:
print("Number of new blossoms will be ",new_blossom(w))