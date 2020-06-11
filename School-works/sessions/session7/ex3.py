s = input("Enter amount: ")
try:
    s = int(s)
except:
    s = -1
if s == -1:
    print("Invalid input")
else:
    if s < 100 and s > 1:
        print("{} cents".format(s))
    elif s == 1:
        print("1 cent")
    else:
        e = s // 100
        c = s % 100
        if e == 1:
            if c == 1:
                print("1 euro and 1 cent")
            else:
                print("1 euro and {} cent".format(c))
        else:
            if c == 1:
                print("{} euros and 1 cent".format(e))
            else:
                print("{} euros and {} cents".format(e,c))