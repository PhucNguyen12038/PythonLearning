from turtle import *

def black_square(side):
    fillcolor('black')
    begin_fill()
    for i in range(4):
        forward(side)
        left(90)
    end_fill()

def square(side):
    for i in range(4):
        forward(side)
        left(90)
    
def row(n, side, m):
    for i in range(n):
        #square(side)
        if m % 2 == 0: # index of row
            if i % 2 == 0: # black square
                black_square(side)
            else:
                square(side)
        else:
            if i % 2 != 0: # black square
                black_square(side)
            else:
                square(side)
        forward(side)
    penup()
    left(180)
    forward(n * side)
    left(180)
    pendown()

def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side, i)
        penup()
        left(90)
        forward(side)
        right(90)
        pendown()
    penup()
    right(90)
    forward(m * side)
    left(90)
    pendown()

m = int(input("Enter m: "))
n = int(input("Enter n: "))
row_of_rows(n,m, 40)
