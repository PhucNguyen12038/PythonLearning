import math
cc = 0.05
sc = 0.04
nc = 0.08

def cake_price(a,b):
    m = 0
    if a == 'Napoleon cake':
        s = b * b
        m = s * nc
    elif a == 'chocolate cake':    
        s = math.pi * b * b
        m = s * cc
    elif a == 'strawberry cake':
        s = math.pi * b * b
        m = s * sc
    
    if m != 0:
        m = round(m,2)    
        return m
    else:
        return -1
