from random import sample
def bingo():
    c = []
    stop = False
    while stop == False:
        a = sample(range(1,11),3)
        b = sample(range(11,21),2)
        c = a + b
        count = 0
        for i in range (1,4):
            if i in a:
                count += 1
        if count == 3:
            stop = False
        else:
            stop = True
    r_list = list(c)
    return r_list

print(bingo())