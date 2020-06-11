from turtle import *
def fractal(order, size):
    if order == 1:
        forward(size)
    else:
        forward(size)
        left(60)
        fractal(order-1, size/3)
        backward(size/3)
        right(60)
        fractal(order-1, size/3)
        backward(size/3)
        right(60)
        fractal(order-1, size/3)
        backward(size/3)
        left(60)
 
left(90)
fractal(5, 100)
exitonclick()