str1 = "Hello"
str2 = "Hi"
f1 = input("Enter source file name: ")
f2 = input("Enter destination file name: ")
 
try:
    ffile1 = open(f1)
    ffile2 = open(f2,'w+')
except:
    print("Files cannot be opened")
else:
    
    count = 0
    for line in ffile1:
        count = count + line.count(str1)
        line2 = line.replace(str1,str2)
        ffile2.write(line2)
    ffile2.close()
    ffile1.close()
    print("{} replacements were made.".format(count))