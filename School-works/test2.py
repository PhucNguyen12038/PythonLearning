s = input("Enter product: ")
p = input("Enter price: ")
try:
    p = float(p)
except:
    p = -1
total_price = 0
count = 0
max_price = 0

while p != "done":
    
    while p == -1:
        print("Price should be a number")
        try:
            p = float(input("Enter price: "))
        except:
            p = -1
    
    count = count + 1
    total_price = total_price + p
    if p > max_price:
        max_price = p
        max_product = s
    
    s = input("Enter product: ")
   
    if s == "done":
        break
    p = input("Enter price: ")
    try:
        p = float(p)
    except:
        p = -1

print("Number of product is ",count)
print("Total sum of prices is ",total_price)
print("Most expensive product is {}, its price was {}\n".format(max_product,max_price) )