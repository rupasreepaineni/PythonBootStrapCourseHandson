from turtle import Turtle,Screen

tim = Turtle()
screen=Screen()
def move_forwards():
    tim.forward(100)
#listen function is used to listen for key presses and then call the function when the key is pressed
#onkey,listen are screen functions, not turtle functions
screen.listen()
screen.onkey(move_forwards, "space")



Screen().exitonclick()