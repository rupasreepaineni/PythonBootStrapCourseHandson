import random

import turtle as t
from turtle import Screen
tim = t.Turtle()
Screen().colormode(255)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r,g,b)
    return colour



#colours = ["dark gray","medium aquamarine","navy","green","blue","purple", "dark green", "cyan", "magenta", "brown"]
directions = [0,90,180,270]

tim.pensize(30)
tim.speed(0)
#or tim.speed("fastest")
for i in range(200):
    tim.color(random_colour())
    tim.forward(100)
    tim.right(random.choice(directions))
    i+=1

Screen().exitonclick()