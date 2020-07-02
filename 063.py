import turtle
import random


turtle.shape("turtle")
for i in range(0,3):
    turtle.begin_fill()
    rn = random.choice(["blue","yellow","red","green"])
    turtle.color("black",rn)
    turtle.pendown()
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(150)

turtle.exitonclick()
