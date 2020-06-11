def print_table(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            print("{}{} ".format(a[i],b[j]),end="")
        print("")
a = ["1","2","3"]
b = ["a","b","c"]
print_table(a,b)