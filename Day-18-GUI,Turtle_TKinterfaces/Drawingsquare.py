from turtle import Turtle,Screen
square = Turtle()
square.shape("turtle")
square.color("blue")
square.width(3)
square.pos()
for i in range(4):
    square.forward(100)
    square.right(90)
    i =+1

square.circle(100)
square.end_fill()



screen = Screen()
screen.exitonclick()
#***screen.exitonclick(), above two lines or single line can be used to exit the screen on click.
