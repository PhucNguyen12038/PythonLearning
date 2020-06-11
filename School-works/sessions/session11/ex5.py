import random
matrix = []
def move(x,y,matrix,size,direction):
    pos = []
    for i in range(size):
        if i == x:
            for j in range(size):
                if j == y:
                    if matrix[i][j] == 0:
                        matrix[i][j] = 1
                        if direction == "N":
                            pos.append(i)
                            pos.append(j-1)
                            direction = "S"
                            pos.append(direction)
                        elif direction == "E":
                            pos.append(i-1)
                            pos.append(j)
                            direction = "N"
                            pos.append(direction)
                        elif direction == "W":
                            pos.append(i)
                            pos.append(j+1)
                            direction = "E"
                            pos.append(direction)
                        elif direction == "S":
                            pos.append(i+1)
                            pos.append(j)
                            direction = "W"
                            pos.append(direction)
                    elif matrix[i][j] == 1:
                        matrix[i][j] = 0
                        if direction == "N":
                            pos.append(i)
                            pos.append(j+1)
                            direction = "E"
                            pos.append(direction)
                        elif direction == "E":
                            pos.append(i+1)
                            pos.append(j)
                            direction = "W"
                            pos.append(direction)
                        elif direction == "W":
                            pos.append(i)
                            pos.append(j-1)
                            matrix[i][j] = 1
                            direction = "S"
                            pos.append(direction)
                        elif direction == "S":
                            pos.append(i-1)
                            pos.append(j)
                            direction = "W"
                            pos.append(direction)
            
    return pos

size = int(input("Enter dimension of the matrix: "))
random_place_x = random.randint(0,size)
random_place_y = random.randint(0,size)

for i in range(size):
    l = []
    for j in range(size):
        l.append(0)
    matrix.append(l)


s = 0
pos = move(random_place_x,random_place_y,matrix,size,"N")
while pos[0] >= 0 and pos[0] < size and pos[1] >= 0 and pos[1] < size:
    s = s + 1
    pos = move(pos[0],pos[1],matrix,size,pos[2])

c = 0
for i in range(size):
    for j in range(size):
        if matrix[i][j] == 1:
           c = c + 1
per_1 = c * 100 / (size * size)
print("Average number of steps is [{}]".format(s))
print("Average percent of ones at the end is [{}]".format(per_1))
        

