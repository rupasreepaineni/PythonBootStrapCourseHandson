import random
import turtle
import turtle as t
from turtle import Screen
tim = t.Turtle()
colours = ["dark gray","medium aquamarine","navy","green","blue","purple", "dark green", "cyan", "magenta", "brown"]
n = 3
def draw_shape(num_sides):
    angle = 360/num_sides
    tim.width(3)
    tim.color(random.choice(colours))
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shapes in range(3,10):
    draw_shape(shapes)
screen = Screen()
screen.exitonclick()
