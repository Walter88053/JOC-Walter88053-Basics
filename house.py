# Using Turtle to draw a square and a triangle to show the outline of a house
# John Kowal  -  WALTER$

import turtle

# turtle.shape("turtle")
turtle.speed(5)

turtle.color("green")
turtle.pensize(3)


def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

square(100)
triangle(100)

turtle.Screen().exitonclick()
