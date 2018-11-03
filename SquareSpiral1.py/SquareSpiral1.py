"""
SquareSpiral1.py - Draws a square spiral
"""                                                                                                                                                              

import turtle

turtle.bgcolor("black")
TurtlePen = turtle.Pen()

TurtlePen.pencolor("yellow")

for counter in range(100):
    TurtlePen.forward(counter)
    TurtlePen.left(60)
    
    if(counter == 50):
        turtle.bgcolor("blue")
    else:
        turtle.bgcolor("purple")