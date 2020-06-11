import math
import re
def distance(a,b):
    d = (b[0]-a[0]) * (b[0]-a[0]) + (b[1]-a[1]) * (b[1]-a[1])
    d = math.sqrt(d)
    return d

point_dic = dict()
n = int(input("Please enter the number of points: "))

for i in range(n):
    p = input("Please enter the coordinates of point {}: ".format(i+1))
    d = re.findall(r'\d+', p)
    for j in range(len(d)):
        d[j] = int(d[j])
    point_dic[i] = d
    
    if i == 1:
        min_dist = distance(point_dic.get(0),point_dic.get(1))

min_point_list = [0,1]
for i in range(len(point_dic)):
    for j in range(len(point_dic)):
        if i != j:
            dist = distance(point_dic.get(i,0),point_dic.get(j,0))
            if dist < min_dist:
                min_dist = dist
                min_point_list = [i,j]
min_point_list.sort()
print("Points {} and {} are the closest to each other.".format(min_point_list[0]+1,min_point_list[1]+1))

