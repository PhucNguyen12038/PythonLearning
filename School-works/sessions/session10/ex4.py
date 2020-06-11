from turtle import *
def begin():
    setx(0)
    sety(0)
def moveto(x,y):
    penup()
    goto(x,y)
def drawto(x,y):
    pendown()
    goto(x,y)
fname = input("Please enter the file name: ")
 
try:
    ffile = open(fname)
except:
    print("File cannot be opened:", fname)
else:
    begin()
    for line in ffile:
        line = line.strip()
        getPos = line[line.find("(")+1:line.find(")")]
        if len(getPos) > 1:
            list_pos = getPos.split(",")
            x = int(list_pos[0])
            y = int(list_pos[1])
            if line.startswith('moveto'):
                moveto(x,y)
            elif line.startswith('drawto'):
                drawto(x,y)
    ffile.close()