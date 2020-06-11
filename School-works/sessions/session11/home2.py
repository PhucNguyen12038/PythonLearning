def more_than_three(a):
    r_list = [0]
    for i in range(1,len(a)):
        count = 0
        for j in range(0,i):
            if a[j] > 3:
                count += 1
        r_list.append(count)
    return r_list

l = [5, 2, 1, 8, 21, 7, 3, 4]
l2 = [4, 4, 4, 4, 4]
print(more_than_three(l2))