boy = input("Enter height of boys: ")
girl = input("Enter height of girls: ")s


boy = boy.replace(" ","")


boy_list = boy.split(",")


girl = girl.replace(" ","")
girl_list = girl.split(",")

result_list = []
boy_list.sort(reverse = True)
girl_list.sort(reverse = True)
print(boy_list)
print(girl_list)
if len(boy_list) == len(girl_list):
    for i in range(0,len(girl_list)):
        a = []
        a.append(boy_list[i])
        a.append(girl_list[i])
        result_list.append(a)
else:
    if len(boy_list) > len(girl_list):
        no_partner = []
        a = len(boy_list) - len(girl_list)
        for i in range (0,a):
            no_partner.append(boy_list[i])
        for i in range(0,len(girl_list)):
            t = []
            t.append(boy_list[i+a])
            t.append(girl_list[i])
            result_list.append(t)
    else:
        a = len(girl_list) - len(boy_list)
        for i in range (0,a):
            no_partner.append(boy_list[i])
        for i in range(0,len(boy_list)):
            t = []
            t.append(boy_list[i])
            t.append(girl_list[i+a])
            result_list.append(t)
print("Dancing pairs are ", end = '')
for i in result_list:
    print("({}, {}) ".format(i[0],i[1]), end = '')
print("")
print("There are no dancing partners for boys with heights ", end = '')
for i in range (0,len(no_partner)):
    if i == len(no_partner) - 1:
        print("{}".format(no_partner[i]))
    else:
        print("{}, ".format(no_partner[i]))