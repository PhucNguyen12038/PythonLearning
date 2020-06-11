from easygui import *
from datetime import date 
month = ['January','February,','March','April','May','June','July','August','September','October','November','December']
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 
      
# Driver code  
name = enterbox("Hello stranger, what's your name?")
birth_day = enterbox("What is your birth day?")
birth_day = birth_day.replace(" ","")
day = birth_day.split(",")
birth_date = int(day[0])
birth_month = int(day[1])
birth_month_str = month[birth_month - 1]
birth_year = int(day[2])
age = calculateAge(date(birth_year,birth_month,birth_date))

if name == None or age == None or name == "":
    msgbox("Why do you have to rebel, enter things like a normal human!!")
else:
    a = "Hello, {}!\n".format(name)
    a += "Your birth day is {} {}, {}.\n".format(birth_month_str,birth_date,birth_year)
    a += "Currently you are {} years old.".format(age)
    msgbox(a)