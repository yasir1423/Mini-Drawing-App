from turtle import *
title("Mini Drawing App")
bgcolor("white")
speed(0)
shape("circle")
shapesize(0.5)
pensize(3)
pencolor("black")
penup()
#Functions
def start_drawing(x,y):
    penup()
    goto(x,y)
    pendown()
def draw(x,y):
    goto(x,y)
def stop_drawing(x,y):
    penup()
def clear_screen():
    clear()
#color change functions
def black():
    color("black")
def red():
    color("red")
def blue():
    color("blue")
def green():
    color("green")
def aqua():
    color("aqua")
#Mouse Drawings
onclick(start_drawing)
ondrag(draw)
onrelease(stop_drawing)
listen()
onkey(clear_screen,"c")
onkey(black,"b")
onkey(red,"r")
onkey(blue,"u")
onkey(green,"g")
onkey(aqua,"a")
done()