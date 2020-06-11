import datetime

def day_of_week(n):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[n]

def create_dictionary(file_name):
    ffile = open(file_name)
 
    dates = dict()
     
    for line in ffile:
        splits = line.split("-")
        y = int(splits[0])
        d = int(splits[2])
        m= int(splits[1])
        try:
            date = datetime.datetime(y,m,d)
            day = day_of_week(date.weekday())
            dates[day] = dates.get(day,0) + 1
        except:
            print("Invalid date")
        
    ffile.close()
    return dates

def sort_dict(dates):
    key_value ={}     
    ascend_value = []
    for k,v in dates.items():
        key_value[k] = v
  
    sum = 0
    for i in sorted(key_value.values()) :  
        ascend_value.append(i)
        sum = sum + int(i)
        
    ascend_value.reverse()
    new_date = {}
    for i in ascend_value:
        for k,v in dates.items():
            if i == v:
                if k in new_date:
                    continue
                else:
                    new_date.update({k:v})
    percentage = {}            
    for k,v in new_date.items():
        p = int(v) / sum * 100
        percentage.update({k:p})
    print(percentage)
d = create_dictionary("birthdays.txt")
sort_dict(d)