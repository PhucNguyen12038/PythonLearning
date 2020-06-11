import time
def number_of_coins(n):
    if n == 1:
        return 1
    else:
        return ((n-1)+number_of_coins(n-1))



#def number_of_coins(n):
#    s = 0
#    for i in range(n):
#        s = s + i + 1
#    return s - n + 1

time1 = time.time()
number_of_coins(800)
time2 = time.time()
print((time2-time1)*1000.0)