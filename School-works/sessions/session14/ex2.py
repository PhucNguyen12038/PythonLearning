def sort_dict_by_value(dates):
    
    key_value ={}     
    ascend_value = []
    for k,v in dates.items():
        key_value[k] = v
    for i in sorted(key_value.values()) :  
        ascend_value.append(i)
    ascend_value.reverse()
    
    new_date = {}
    for i in ascend_value:
        for k,v in dates.items():
            if i == v:
                if k in new_date:
                    continue
                else:
                    new_date.update({k:v})
    
    return new_date

def create_dictionary(file_name):
    ffile = open(file_name)
 
    dates = dict()
     
    for line in ffile:
        splits = line.split("-")
        y = int(splits[0])
        d = int(splits[2])
        m= int(splits[1])
        key = str(y) + "-" + str(m) + "-" + str(d)
        dates[key] = dates.get(key,0) + 1
    
    new_dic = sort_dict_by_value(dates)
       
    ffile.close()
    return new_dic

d = create_dictionary("birthdays.txt")
t = 0
for k,v in d.items():
    if v == 2:
        print(k,v)
    if v == 3:
        t += 1
if t > 0:
    print("file contains three same birthdays")
#print(d)