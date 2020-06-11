import os
kb = 1024
mb = 1024 * kb
gb = 1024 * mb
tb = 1024 * gb

def file_size(fileName):
    size = os.path.getsize(fileName)
    if size != 0:
        return size
    else:
        return 0
def convert(a,b):
    if a == "KB":
        return b / kb
    if a == "MB":
        return b / mb
    if a == "GB":
        return b / gb
    if a == "TB":
        return b / tb
    
def explain(a):
    if a == "KB":
        return kb
    if a == "MB":
        return mb
    if a == "GB":
        return gb
    if a == "TB":
        return tb
currentPath = "/Users/nhp/Desktop/Python_Exercise/session4/"
fileName = input("Enter file name? ")
absolutePath = currentPath + fileName

unit = input("Enter the unit: ")
result = file_size(absolutePath)
c = convert(unit,result)
result = str(c) + " " + str(unit)
print("File size is ",result)
print("Because " + str(unit) + " is equal to "+str(explain(unit)) + " byte")

    