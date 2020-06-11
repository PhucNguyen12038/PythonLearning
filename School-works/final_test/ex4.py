fname = 'carpark.txt'
new_fname = 'new_carpark.txt'
ffile = open(fname)
array = []
for line in ffile:
    l = line.strip()
    list_park = list(l)
    array.append(list_park)
ffile.close()

print(array)
s = int(input("Please select the activity: "))
dic = dict()
while(s >= 1 and s<= 5):
    if s == 1:
        car_name = input("Please enter car owner's name: ")
        coord = input("Please enter the coordinates of parking lot: ")
        coord = coord.replace(" ", "")
        coord = coord.split(",")
        x = int(coord[0])
        y = int(coord[1])
        #print(coord)
        if array[x][y] == '-' or array[x][y] == 'X':
            print("It is not possible to park at that location.")
        else:
            dic.update({car_name:[x,y]})
            array[x][y] = 'X'
            #print(array)
    if s == 2:
        car_name = input("Please enter car owner's name: ")
        s = str(dic[car_name])
        s = s.replace("[","")
        s = s.replace("]","")
        print(s)
    if s == 3:
        car_name = input("Please enter car owner's name: ")
        coord = dic[car_name]
        x = coord[0]
        y = coord[1]
        array[x][y] = 'P'
        del dic[car_name]
        #print(array)
        #print(dic)
    if s == 4:
        print(array)
    if s == 5:
        file_content = ""
        for i in range(len(array)):
            s = ""
            for j in range(len(array[i])):
                s = s + array[i][j]
            s = s+"\n"
            file_content += s
        ffile = open(new_fname,'w+')
        ffile.write(file_content)
        ffile.close()
        print("The program wrote the parking situation to the file and terminated.")
        break
    s = int(input("Please select the activity: "))
    