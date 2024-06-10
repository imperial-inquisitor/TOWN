from turtle import *

def stvol(x,y):
    color("brown")
    pensize(20)
    penup()
    goto(x,y)
    pendown()
    left(90)
    forward(200)

def papers():
    color("green")
    pensize(10)
    right(90)
    begin_fill()
    circle(100)
    end_fill()
def derevo(x,y):
    stvol(x,y)
    papers()