import os

i = input("Enter filename: ")
if i == "":
    exit()
else:
    exists = os.path.isfile('/Users/nhp/Desktop/Python_Exercise/session8/{}'.format(i))
    while not exists:
        i = input("File doesn't exists, enter new filename: ")
        exists = os.path.isfile('/Users/nhp/Desktop/Python_Exercise/session8/{}'.format(i))
        if exists:
            break
    fn = "/Users/nhp/Desktop/Python_Exercise/session8/{}".format(i)
    ffile = open(fn)
    pos_pp = 0
    min_pp = 0
    total = 0
    for line in ffile:
        total = total + 1
        if line.startswith('+'):
            min_pp = min_pp + 1
        if line.startswith('?'):
            pos_pp = pos_pp + 1

    ffile.close()
    max_pp = int(min_pp)+int(pos_pp)
    print("Total number of people invited is {}".format(total))
    print("Minimum number of people attending is {}".format(min_pp))
    print("Maximum number of people attending is {}".format(max_pp))
    print("Minimum nbudget is {} euros".format(int(min_pp) * 10 + 55))
    print("Maximum nbudget is {} euros".format(max_pp * 10 + 55))