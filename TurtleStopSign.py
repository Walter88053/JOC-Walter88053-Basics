# Using an octagon and a rectangle to show the outline of a stop sign
# John Kowal  -  WALTER$

import turtle

turtle.speed(5)
turtle.color("green")
turtle.pensize(3)

def octagon(length):
    for i in range(8):
        turtle.forward(length)
        turtle.left(45)

def jump1(length):
    turtle.penup()
    turtle.forward(length * .375)
    turtle.pendown()

def rectangle(length):
    for j in range(2):
        turtle.forward(length * .2)
        turtle.right(90)
        turtle.forward(length * 2)
        turtle.right(90)

def jump2(length):
    turtle.penup()
    turtle.forward(length * 3)
    turtle.pendown()

length = 40

for k in range (3):
    octagon(length)
    jump1(length)
    rectangle(length)
    jump2(length)

turtle.Screen().exitonclick()
