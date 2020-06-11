#def test(i,j):
#    if i == 0:
#        return j
#    else:
#        return test(i-1,i+j)
#print(test(8,5))


#def a(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return a(n-1) + a(n-2)
#for i in range(0,4):
#    print(a(i),end=" ")

#def fun(n):
#    print(n)
#    if (n > 100):
#        return n - 5
#    return fun(fun(n+11))
#print(fun(45))

#def fun(x):
#    if x == 3:
#        return x + 3
#    if x == 2:
#        return x + 2
#    if x == 1:
#        return x + 1
#    else:
#        return fun(x-1)
#print(fun(15))

#def recursive_count(target, nested_num_list):
#    c = 0
#    for el in nested_num_list:
#        if isinstance(el,list):
#            c+=recursive_count(target,el)
#        elif target == el:
#            c+=1
#    return c
#print(recursive_count(2,[2,9,[2,1,13,2,5],8,[2,6]]))

#import re
#print(re.match(r'.*\?',"test?").group(0))
#print(re.match(r'(very )+(fat )?(tall|ugly) man',"very tall ugly man"))

#n = 19
#while n > 1:
#    if n % 3 == 0:
#        n = n // 3
#    else:
#        n = n + 1
#    print(n)

def a(x,y):
    if y>x and y<2:
        return 1
    elif x<2 and x>y:
        return 2
    elif y<2:
        if x>2 or x<2 and y>2:
            return 3
        else:
            return 4
print(a(3,2))
