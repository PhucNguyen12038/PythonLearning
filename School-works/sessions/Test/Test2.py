def binary_paint(filename):
    matrix = []
    f = open(filename)
    for line in f:
        row = []
        number_arr = line.strip().split(" ")
        if len(number_arr) == 0:
            for i in range(8):
                row.append(0)
        for i in range(8):
            row.append(0)
        for j in range(len(number_arr)):
            if number_arr[j] != '':
                row[int(number_arr[j])] = 1
        matrix.append(row)
    f.close()
    return matrix
    
m = binary_paint("painting.txt")
print(m)
#for i in m:
#    print(i)