import random

def create_dictionary():
    dic = dict()
    i = input("Enter a word (done to quit): ")
    
    while i != "done":    
        if i in dic:
            print("{} means {}".format(i,dic[i]))
        else:
            print("There is no information for {}".format(i))
            m = input("What does {} mean? ".format(i))
            dic[i] = m
        i = input("Enter a word (done to quit): ")
    print("There are {} entries in the dictionary:".format(len(dic)))
    for k,v in dic.items():
        print("{} - {}".format(k,v))
    return dic

def lookup(dic):
    key = random.choice(list(dic))
    value = dic[key]
    score = 0
    s = input("Enter the translation of word {}".format(key))
    while s != "done":
        if s == value:
            print("correct")
            score = score + 1
            print(score)
            if score == 10:
                print("win")
                break
        else:
            print("incorrect")
            score = score - 1
            if score == -10:
                print("lose")
                break
        s = input("Enter the translation of word {}".format(key))
d = create_dictionary()
g = lookup(d)
