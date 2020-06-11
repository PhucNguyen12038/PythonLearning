def budget(a):
    return a * 10 + 55


pi = int(input("How many people are invited? "))
an = int(input("How many have answered? "))
maximum = budget(pi)
maximum = str(maximum) + " EUR"
minimum = budget(an)
minimum = str(minimum) + " EUR"
print("Maximum budget size = ", maximum)
print("Minimum budget size = ",minimum)