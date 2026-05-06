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
tim.pensize(1)
tim.speed(0)
#or tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading()+10)
        i+=1

draw_spirograph(5)
Screen().exitonclick()