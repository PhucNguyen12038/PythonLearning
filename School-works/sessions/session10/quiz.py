#from easygui import *
#buttons = ["1","2","3"]
#pressed = buttonbox("Choose a number ",choices = buttons)
#msgbox("The result is " + pressed * 10)
#number = integerbox("Enter number:",lowerbound = -5, upperbound = 5)
#print(number)

#from turtle import *
#clr = "green"
##begin_fill()
#circle(50)
#end_fill()
#color(clr)
#exitonclick()

#li = [9,8,7,6,5,4,3,2,1]
#for i in li:
#    print(i)
#    if li.index(i) % 2 == 0:
#        li.remove(i)

#word = "Computer programming"
#print(len(word))
#print(word[-14:])

f = open("input.txt")
for r in f:
    if "wto" in r:
        print(r)