from tkinter import *
from tkinter import messagebox

dic = {'hapy':'happy','bob':'bob123'}
 
# This function is executed if the button is pressed
def login():
    
    k = username.get()
    if k in dic:
        p = dic.get(k)
        if p == passwd.get():
            say = "Hello " + k
            messagebox.showinfo(message=say)
        else:
            say = "Password is incorrect"
            messagebox.showinfo(message=say)
    else:
        say = "You need to register"
        messagebox.showinfo(message=say)
# Define the size and the title of the window
def clear():
    username.delete(0, 'end')
    passwd.delete(0, 'end')

window = Tk()
window.title("Login")
window.geometry("300x150")
 
# Label
labelUserName = Label(window, text="Username:")
labelUserName.place(x=5, y=5)

labelUserName = Label(window, text="Password:")
labelUserName.place(x=5, y=35)
 
# Text box
username = Entry(window)
username.place(x=100, y=5, width=150)

passwd = Entry(window)
passwd.place(x=100, y=35, width=150)
 
# Button; function sayHello is associated with a button
but = Button(window, text="Login", command=login)
but.place(x=30, y=70, width=100)

but = Button(window, text="Clear", command=clear)
but.place(x=150, y=70, width=100)
 
# Enter the main event loop
window.mainloop()