def create_dictionary(file_name):
    dic = dict()
    ffile = open(file_name,"r+")
    for line in ffile:
        splits = line.rstrip().split("-")
        dic[splits[0]] = splits[1]
    i = input("Enter a word (done to quit): ")
    
    while i != "done":    
        if i in dic:
            print("{} means {}".format(i,dic[i]))
        else:
            print("There is no information for {}".format(i))
            m = input("What does {} mean? ".format(i))
            dic[i] = m
            ffile.write("{}-{}\n".format(i,m))
            ffile.close()
        i = input("Enter a word (done to quit): ")
    print("There are {} entries in the dictionary:".format(len(dic)))
    for k,v in dic.items():
        print("{} - {}".format(k,v))
    return dic

create_dictionary("dictionary.txt")