fn = input("Enter filename: ")
print()
f = open(fn)

def prefers_football(l):
    if len(l) > 2:
        if "football" in l[0]:
            return True
        elif "football" in l[1]:
            return True
        else:
            return False
    elif len(l) == 0:
        return False
    else:
        if "football" in l[0]:
            return True
        else:
            return False
fb_grp = []
other_grp = []
for line in f:
    std_name = line.split(":")[0]
    std_spt = line.split(":")[1]
    spt = std_spt.split(",")
    if prefers_football(spt) == True:
        fb_grp.append(std_name)
    else:
        other_grp.append(std_name)
f.close()

first_t = []
second_t = []
for i in range(len(fb_grp)):
    if i % 2 == 0 and i == len(fb_grp) - 1:
        second_t.append(fb_grp[i])
    elif i % 2 == 0:
        first_t.append(fb_grp[i])
    else:
        second_t.append(fb_grp[i])
print("First football team:")
for i in first_t:
    print(i)
print()
print("Second football team:")
for i in second_t:
    print(i)
print()
print("Others:")
for i in other_grp:
    print(i)
        
