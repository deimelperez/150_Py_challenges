import turtle
import random


turtle.shape("turtle")
for i in range(0,8):
    rn = random.choice(["blue","yellow","red","green","black","pink","brown"])
    turtle.color(rn)
    turtle.forward(100)
    turtle.right(45)

turtle.exitonclick()
