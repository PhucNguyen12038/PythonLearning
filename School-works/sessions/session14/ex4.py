
#fname = input("Please enter the file name: ")
fname = 'database.txt' 
try:
    ffile = open(fname)
except:
    print("File cannot be opened:", fname)
else:
    for line in ffile:
        l = line.strip().split(";")
        for i in range(len(l)):
            e = l[i].
    ffile.close()