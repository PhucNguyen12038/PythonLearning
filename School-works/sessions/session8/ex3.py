import os

def shoe_size(length):
    return round(1.5 * (length + 1.5))
 


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
 
    for foot in ffile:
        try:
            f = float(foot)
            s = shoe_size(f)
            print(s)
        except:
            print("Line cannot be converted")
 
    ffile.close()