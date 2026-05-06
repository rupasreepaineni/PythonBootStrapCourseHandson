import random

import turtle as t
from turtle import Screen
colours = ["dark gray","medium aquamarine","navy","green","blue","purple", "dark green", "cyan", "magenta", "brown"]
directions = [0,90,180,270]
tim = t.Turtle()
tim.pensize(30)
tim.speed(0)
#or tim.speed("fastest")
for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(100)
    tim.right(random.choice(directions))
    i+=1


Screen().exitonclick()