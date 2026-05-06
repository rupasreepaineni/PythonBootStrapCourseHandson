from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #when we define in all caps then it's a constant
MOVE_DISTANCE = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #holding the first segment
    def create_snake(self):
        """here we're placing three squared to next to each other
        to look alike a snake"""
        for position in STARTING_POSITIONS:
            self.extend_snake(position)

    def extend_snake(self,position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        #here we're holding last segment and asking to add a new segment to the position of the last segment
        self.extend_snake(self.segments[-1].position())
        #here position is a method from Turtle class


    def move(self):
        """here we're asking the each square to move one after the other position
            the starting position is 3,2,1 which means we've to move -1 step ahead"""

        for seg_num in range(len(self.segments) - 1, 0, -1):  # start,stop,step: -1,0,-1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # asking to move the second square
            # to the position of the previous segment
        self.head.forward(MOVE_DISTANCE)  # moving the head of the snake forward by 20 pixels, first head will be at seg[0],xcor() and seg[0].ycor()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


