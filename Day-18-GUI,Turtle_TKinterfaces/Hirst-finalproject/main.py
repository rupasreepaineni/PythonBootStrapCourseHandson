import random
import turtle as t
#screen is also part of turtle module


colours = [(232, 206, 81), (227, 146, 86), (216, 227, 219), (231, 223, 226), (216, 224, 229), (157, 15, 23), (117, 167, 188), (30, 110, 158), (234, 83, 44), (124, 175, 145), (7, 98, 38), (172, 20, 15), (30, 130, 48), (182, 185, 27), (200, 63, 27), (11, 42, 76), (16, 62, 41), (238, 202, 8), (136, 83, 96), (91, 15, 25), (49, 166, 77), (37, 27, 23), (176, 135, 148), (6, 66, 137), (50, 151, 196), (215, 67, 72), (232, 169, 161), (167, 208, 174), (78, 133, 185)]\

tim = t.Turtle()
tim.penup()
tim.speed(0)
tim.setheading(225) #here we're setting the heading of the turtle to 225 degrees,
# so that it starts from the bottom left corner of the screen
tim.forward(300)
tim.setheading(0)
t.Screen().colormode(255) #here changing the colormode to 255, so that we can use the RGB colour values in the colours tuple
number_of_dots = 100
tim.penup()
for dot_count in range(1,number_of_dots+1): #setting the dots count to 100
    tim.dot(20,random.choice(colours))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90) #here we're setting the heading to 90 degrees,
        # so that the turtle moves up after every 10 dots
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


tim.hideturtle()
t.Screen().exitonclick()