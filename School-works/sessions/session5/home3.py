animalList = ["dragons","snakes","dinosaurs"]
array = []
dra = input("Number of dragons: ")
try:
    dra = int(dra)
except:
    dra = -1
if dra == -1:
    print("Invalid number")
    exit(0)
else:
    array.append(dra)
    
sna = input("Number of snakes: ")
try:
    sna = int(sna)
except:
    sna = -1
if sna == -1:
    print("Invalid number")
    exit(0)
else:
    array.append(sna)
    
    
dino = input("Number of dinosaurs: ")
try:
    dino = int(dino)
except:
    dino = -1
if dino == -1:
    print("Invalid number")
    exit(0)
else:
    array.append(dino)
    
  
stop = False
day = 0
while stop == False:
    a = array[1] - array[0]
    if a <= 0:
        array[1] = 0
    else:
        array[1] = a
        
    b = array[2] - array[1]
    if b <= 0:
        array[2] = 0
    else:
        array[2] = b
        
    c = array[0] - array[2]
    if c <= 0:
        array[0] = 0
    else:
        array[0] = c
    
    day+=1
    check = 0
    #print(array)
    for i in range (0,3):
        if array[i] == 0:
            check = check + 1
    
    if check == 2:
        stop = True
    
    
print("Last meal will be on day " + str(day))
for i in range (0,3):
    if array[i] > 0:
        print("There will be " + str(array[i]) + " " + animalList[i] + " left")