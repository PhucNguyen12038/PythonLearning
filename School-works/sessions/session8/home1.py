fname = input("Please enter the file name: ")
 
try:
    ffile = open(fname)
except:
    print("File cannot be opened:", fname)
else:
    count = 0
    for line in ffile:
        count += 1
        print("{}. {}".format(count,line))
        
    