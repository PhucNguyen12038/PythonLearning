a = [['X','X','X',' '],
     ['X','X','X','X'],
     ['X','X','X',' '],
     [' ',' ',' ','O']]

def count_number_row(a,char):
    c = 0
   
    for k in range(4):
        l = []
        for i in range(len(a)):
            if i == k:
                for j in range(len(a[i])):
                    if a[i][j] == char:
                        l.append([i,j])
        
        same_row = 0
        for i in range(len(l) - 1):
            if l[i][0] == l[i+1][0]:
                same_row += 1
        
        consecutive_row = 0
        if same_row >= 2:
            for j in range(len(l)-1):
                if l[j+1][1] - l[j][1]:
                    consecutive_row += 1
            if consecutive_row >= 2:
                c += 1
    return c

def count_number_column(a,char):
    c = 0
    for k in range(4):
        l = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                    if a[i][j] == char and j == k:
                        l.append([i,j])
        
        same_column = 0
        for i in range(len(l) - 1):
            if l[i][1] == l[i+1][1]:
                same_column += 1
        
        consecutive_column = 0
        if same_column >= 2:
            for j in range(len(l)-1):
                if l[j+1][0] - l[j][0]:
                    consecutive_column += 1
            if consecutive_column >= 2:
                c += 1
    return c

def count_number_diagonal(a,char):
    c = 0
    for k in range(len(a)):        
        for i in range(len(a)):
            for j in range(len(a)):
                if 
    return c

def number_of_wins(a):
    return 0

print(count_number_column(a,'X'))