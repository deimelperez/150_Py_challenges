import turtle
import random


turtle.shape("turtle")
rn = random.randint(3,10)
for i in range(0,rn):
    turtle.forward(360/rn)
    turtle.right(360/rn)

turtle.exitonclick()
