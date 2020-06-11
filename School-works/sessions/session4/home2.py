c = 299792.458
def sum(a,b):
    u = a + b
    l = 1 + (a * b / (c * c))
    return(u / l)
    
#u = 100000
#v = 200000
#sum(u,v)

s1 = float(input("The speed of the first body with respect to the observer is: "))
s2 = float(input("The speed of the second body with respect to the observer is: "))
s3 = float(input("The speed of the third body with respect to the observer is: "))
s4 = float(input("The speed of the fourth body with respect to the observer is: "))
result = sum(sum(s1,s2),sum(s3,s4))
result = str(result) + " km/s"
print("Sum of speeds is ",result)