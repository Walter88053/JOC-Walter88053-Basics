# Turtle Square and Rectangle
# John Kowal  -  WALTER$

import turtle

# turtle.shape("turtle")
turtle.speed(5)

turtle.color("green")
turtle.pensize(3)


# STEP 1
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)

# STEPS 2 and 3
# def square(size):
#   for i in range(4):
#       turtle.forward(size)
#       turtle.left(90)

# def back(l):
#   turtle.penup()
#   turtle.backward(l)
#   turtle.pendown()

# square(100),
# back(125)
# square(100)

# STEP 4
def square(size):
        for i in range(0, 4, 1):
            turtle.forward(size)
            turtle.left(90)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

def rectangle(length):
       for i in range(1):
           back(200)
           turtle.forward(length * 1.5)
           turtle.left(90)
           turtle.forward(length)
           turtle.left(90)
           turtle.forward(length * 1.5)
           turtle.left(90)
           turtle.forward(length)
           turtle.left(90)

square(100)
rectangle(100)






turtle.Screen().exitonclick()
