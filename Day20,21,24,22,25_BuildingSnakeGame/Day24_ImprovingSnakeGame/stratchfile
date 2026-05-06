from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""here we're placing three squared to next to each other
to look alike a snake"""
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
"""we're trying to move snake forward by 20 pixels,
and then we will move the last segment to the position of the second last segment,
and so on until we reach the head of the snake, which will move forward by 20 pixels"""


game_is_on = True

while game_is_on:
    screen.update() #updating screen to get the new position of the snake after moving to end
    time.sleep(0.1) # this will make the snake move slower,
    # you can adjust the sleep time to make it faster or slower

    """here we're asking the each square to move one after the other position
    the starting position is 3,2,1 which means we've to move -1 step ahead"""

    for seg_num in range(len(segments) - 1, 0, -1): #start,stop,step: -1,0,-1
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) #asking to move the second square
        # to the position of the previous segment
    segments[0].forward(20) #moving the head of the snake forward by 20 pixels, first head will be at seg[0],xcor() and seg[0].ycor()


screen.exitonclick()