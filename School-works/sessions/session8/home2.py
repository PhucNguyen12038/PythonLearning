d = input("Enter distance in kilometers: ")
min_taxi = ""

try:
    ffile = open("taxiprices.txt")
except:
    print("File cannot be opened:", fname)
else:
    for f_line in ffile:
        first = f_line.split(",")
        min_taxi = first[0]
        min_price = float(first[1]) + float(first[2]) * float(d)
        break
    
    for line in ffile:
        strings = line.split(",")
        n = strings[0]
        base_fee = float(strings[1])
        kilo_price = float(strings[2])
        p = base_fee + kilo_price * float(d)
        if p < min_price:
            min_price = p
            min_taxi = n
    
    print("{} is the cheapest.".format(min_taxi))    
    
