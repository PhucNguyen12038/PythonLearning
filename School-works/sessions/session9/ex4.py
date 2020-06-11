f1_name = 'first.txt'
f1 = open(f1_name)
l1 = []
l3 = []
for line in f1:
    line = line.replace(" ","")
    line = line.replace("\n","")
    name = line.split(".")[1]
    l1.append(name)
    l3.append(name)
print(l1)

f2_name = 'second.txt'
f2 = open(f2_name)
l2 = []

count = 0
for line in f2:
    order = int(line)
    l2.append(order)
    l3[count] = l1[order-1]
    count +=1
print(l3)
f3_name = 'third.txt'
f3 = open(f3_name,'w+')
count = 0
for i in l3:
    count += 1
    f3.write("{}. {}\n".format(count,i))
f1.close()
f2.close()
f3.close()
