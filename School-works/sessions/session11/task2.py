from copy import deepcopy
def number_of_wins(list1):
    countx=0
    counto=0
    for i in range(4):     
        for j in range(2):
            if list1[i][j] == 'X' and  list1[i][j+1] == 'X' and list1[i][j+2] == 'X':
                countx = countx + 1
            if  list1[i][j] == 'O' and  list1[i][j+1] == 'O' and list1[i][j+2] == 'O':
                counto = counto + 1
    for i in range(2): 
        for j in range(4):
            if list1[i][j] == 'X' and  list1[i+1][j] == 'X' and list1[i+2][j] == 'X':
                countx = countx + 1
            if list1[i][j] == 'O' and  list1[i+1][j] == 'O' and list1[i+2][j] == 'O':
                counto = counto + 1
    for i in range(2): 
        for j in range(2):                
            if list1[i][j] == 'X' and  list1[i+1][j+1] == 'X' and list1[i+2][j+2] == 'X':
                countx = countx + 1
            if list1[i][j] == 'O' and  list1[i+1][j+1] == 'O' and list1[i+2][j+2] == 'O':
                counto = counto + 1
    for i in range(2): 
        for j in range(2,4):
            if list1[i][j] == 'X' and  list1[i+1][j-1] == 'X' and list1[i+2][j-2] == 'X':
                countx = countx + 1
            if list1[i][j] == 'O' and  list1[i+1][j-1] == 'O' and list1[i+2][j-2] == 'O':
                counto = counto + 1
    results=[]
    results.append(countx)
    results.append(counto)
    return results

def has_won(list1,char):
    countx=0
    counto=0
    for i in range(4):     
        for j in range(2):
            if list1[i][j] == 'X' and  list1[i][j+1] == 'X' and list1[i][j+2] == 'X':
                countx = countx + 1
            if  list1[i][j] == 'O' and  list1[i][j+1] == 'O' and list1[i][j+2] == 'O':
                counto = counto + 1
    for i in range(2): 
        for j in range(4):
            if list1[i][j] == 'X' and  list1[i+1][j] == 'X' and list1[i+2][j] == 'X':
                countx = countx + 1
            if list1[i][j] == 'O' and  list1[i+1][j] == 'O' and list1[i+2][j] == 'O':
                counto = counto + 1
    for i in range(2): 
        for j in range(2):                
            if list1[i][j] == 'X' and  list1[i+1][j+1] == 'X' and list1[i+2][j+2] == 'X':
                countx = countx + 1
            if list1[i][j] == 'O' and  list1[i+1][j+1] == 'O' and list1[i+2][j+2] == 'O':
                counto = counto + 1
    for i in range(2): 
        for j in range(2,4):
            if list1[i][j] == 'X' and  list1[i+1][j-1] == 'X' and list1[i+2][j-2] == 'X':
                countx = countx + 1
            if list1[i][j] == 'O' and  list1[i+1][j-1] == 'O' and list1[i+2][j-2] == 'O':
                counto = counto + 1
    if char == 'X':
        if countx > counto:
            return True
        elif countx <= counto:
            return False
    else:
        if counto > countx:
            return True
        elif counto <= countx:
            return False
def find_win(list1,char):
    list2 = deepcopy(list1)
    for i in range(4):
        for j in range(4):
            if list2[j][i] == ' ':
                list2 = deepcopy(list1)
                list2[j][i] = char
                if has_won(list2,char) == True:
                    print("Play {} can win:".format(char))
                    for i in range(4):
                        for j in range(4):
                            print(list2[j][i] + " ",end="")
                        print("")
                    
                    return 0
    print("Play {} can not win".format(char))
                
matrix = [['O',' ','X','O'],
          ['O',' ',' ','X'],
          ['X',' ',' ',' '],
          ['O','X','X','O']]

find_win(matrix,'X')