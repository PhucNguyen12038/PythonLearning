import math

d = int(input("Enter the number of student: "))
m = int(input("Enter the number of room: "))
#s = d**2 / 4 * math.pi
if d//m == d/m:
    result = int(d/m)
    print("You will need to put " + str(result) + " in each of " + str(m) + " classes")
else:   
    ns = math.ceil(d/m)
    ns2 = d % m
    a = ns2 * ns
    b = d - a

    e = ns2 * m
    f = d - ns2

    c = f / (ns-1)
    c = m - ns2

    print("You will need to put " + str(ns) + " in each of " + str(ns2) + " classes")
    print("You will need to put " + str(ns-1) + " in each of " + str(c) + " classes")

