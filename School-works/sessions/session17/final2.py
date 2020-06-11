fname = 'concert.txt'

#fn = input("Please enter filename: ")
cl = input("What is your class? ")
nt = int(input("How many tickets do you want? "))
dic = {}
array = []

ffile = open("concert.txt")
i = 0
for line in ffile:
    spl = line.strip().split(" ")
    place = spl[0]
    seat = spl[1]
    list_seat = list(seat)
    array.append(list_seat)
    dic.update({place:i})
    i = i + 1
ffile.close()

i = 0
for k,v in dic.items():
    dic[k] = i
    i = i + 1

def find_seat(dic,cl):
    if cl in dic:
        v = dic[cl]
        row = array[v]
        print(row)
        for i in range(len(row)-(nt-1)):
            c = 0
            for j in range(nt-1):
                #print(i,j)
                if row[i+j] == '-' and row[i+j+1] == '-':
                    c += 1
            if c == (nt-1):
                return i
        return -1
    else:
        return -1

if find_seat(dic,cl) == -1:
    print("Sorry but there are no suitable seats available")
else:
    strings = "Your seats are "
    print(strings,end=" ")
    r = dic[cl]
    for i in range(nt):
        s = find_seat(dic,cl) + i
        if i != nt-1:
            st = "(row {}, seat {}),".format(r+1,s+1)
        else:
            st = "(row {}, seat {})".format(r+1,s+1)
        print(st,end=" ")
    

        




