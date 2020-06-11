import math
import re
def distance(a,b):
    d = (b[0]-a[0]) * (b[0]-a[0]) + (b[1]-a[1]) * (b[1]-a[1])
    d = math.sqrt(d)
    return d

point_dic = {'1':'-5,-5','2': '(3,0)','3': '(0,-2)','4': '(5,9)','5': '(8,3)','6': '(-8,-1)','7': '(-1,-8)','8': '(6,-7)','9': '(-7,4)','10': '(4,9)'}
n = int(input("Please enter the number of points: "))
i = 0
new_dic = dict()
for k,v in point_dic.items():
    #p = input("Please enter the coordinates of point {}: ".format(i+1))
    p = v
    d = re.findall(r'\d+', p)
    for j in range(len(d)):
        d[j] = int(d[j])
    new_dic[i] = d
    i+=1
    if i == 2:
        min_dist = distance(new_dic.get(0),new_dic.get(1))
print(new_dic)
min_point_list = [1,2]
for i in range(len(new_dic)):
    for j in range(len(new_dic)):
        if j > i:
            dist = distance(new_dic.get(i),new_dic.get(j))
            if dist < min_dist:
                min_dist = dist
                min_point_list = [i,j]
min_point_list.sort()
print("Points {} and {} are the closest to each other.".format(min_point_list[0],min_point_list[1]))


