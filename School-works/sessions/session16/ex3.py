import re

ffile = open("input.txt")
l = []
for line in ffile:
    r1 = re.findall(r'\d+\.\d+',line)
    r2 = re.findall(r'\d+\,\d+',line)
    if len(r1) > 0:
        l.append(r1)
    if len(r2) > 0:
        l.append(r2)

for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")

ffile.close()