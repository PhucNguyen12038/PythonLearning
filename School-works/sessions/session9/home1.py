def boys_and_girls(list1):
    count_B = 0
    count_G = 0
    for e in list1:
        gender = e.split()
        if gender[len(gender)-1] == 'B':
            count_B += 1
        elif gender[len(gender)-1] == 'G':
            count_G += 1
    rlist = list([count_B,count_G])
    return rlist

print(boys_and_girls(['Mati B', 'Kati G', 'Siim Aleksander B', 'Ralf B', 'Veronika G']))