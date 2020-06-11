from tkinter import *
 
window = Tk()
window.title("Ship")
area = Canvas(window, width=880, height = 560)
 
area.create_rectangle(0, 0, 800, 600, fill="white", outline="white")
area.create_line(100, 350, 700, 350)
area.create_line(200, 450, 600, 450)
area.create_line(100, 350, 200, 450)
area.create_line(700, 350, 600, 450)

area.create_rectangle(250, 270, 550, 350)
area.create_rectangle(350, 220, 520, 270)

area.create_line(435, 220, 435, 70)
area.create_line(435, 70, 480, 100)
area.create_line(435, 120, 480, 100)
area.pack()

window.mainloop()