from turtle import Turtle,Screen

tim = Turtle()
screen=Screen()
def move_forwards():
    tim.forward(100)
def move_backwards():
    s = tim.backwards(50)
def counter_clockwise():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
     tim.clear()
     tim.penup()
     tim.home()
     tim.pendown()

#listen function is used to listen for key presses and then call the function when the key is pressed
#onkey,listen are screen functions, not turtle functions
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")


Screen().exitonclick()


# w = forwards
# s = backwards
# a = counter_cloclwise
# d = clockwise
