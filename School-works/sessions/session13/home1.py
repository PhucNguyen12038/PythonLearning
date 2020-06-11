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
        dates[y] = dates.get(y,0) + 1
    
    new_dic = sort_dict_by_value(dates)
       
    ffile.close()
    return new_dic

s = input("Enter filename: ")
d = create_dictionary(s)
print("Top 3 years that have the most birthdays are:")
l = list((d.values()))
max_values = []
print(d)
for i in range(3):
    if len(l) > 0:
        max_value = max(l)
        max_values.append(max_value)
        for j in l:
            if j == max_value:
                l.remove(j)
    else:
        break
result = {}
for k,v in d.items():
    if v in max_values:
        result.update({k:v})
        #print("{} - {} birthdays".format(k,v))

i = 3
for k,v in result.items():
    if i > 0:
        print("{} - {} birthdays".format(k,v))
        i -=1
