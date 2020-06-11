from turtle import *

def square(side):
    for i in range(4):
        forward(side)
        left(90)

def row(n, side):
    for i in range(n):
        square(side)
        forward(side)
    penup()
    left(180)
    forward(n * side)
    left(180)
    pendown()

def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side)
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