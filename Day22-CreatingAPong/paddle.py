from turtle import Turtle

class Paddle(Turtle): #as we're passing argument as turtle,
    # no need to create an object of turtle in the class, 
    # we can directly use the methods of turtle in the class, which can be self.methods of turtle
    
    def __init__(self,position):
        super().__init__() # we've to inherit the properities of turtle
        self.self = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20 #this will move the paddle up by 20 pixels,
        # as ycor() will give the current y coordinate of the paddle
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20 #this will move the paddle down by 20 pixels,
        # as ycor() will give the current y coordinate of the paddle
        self.goto(self.xcor(), new_y)
