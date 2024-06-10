from turtle import *

def sun(x,y):
    penup()
    goto(x,y)
    pendown()
    color("yellow")
    pensize(8)
    begin_fill()
    for i in range(18):
        forward(150)
        left(100)
    end_fill()
    begin_fill()
    goto(x + 78,y -16)
    circle(83)
    end_fill()