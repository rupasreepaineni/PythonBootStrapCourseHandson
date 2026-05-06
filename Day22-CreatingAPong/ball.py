from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.xmove = 10 #this is movement of ball
        self.ymove = 10
        self.move_speed = 0.01

    def move(self):#here we're moving the ball to 10 pixels in x ,
        # and 10 pixels in y direction, so that it will move diagonally
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_Y(self):#when it hits the wall,
        # it should bounce_Y back, so we need to change the direction of the ball
        self.ymove *= -1 #this will change the direction of the ball in y direction

    def bounce_X(self):#when it hits the paddle, it should bounce_X back,
        # so we need to change the direction of the ball
        self.xmove *= -1 #this will change the direction of the ball in x direction
        self.move_speed *= 0.9 #this will increase the speed of the ball each time it hits the paddle

    #when the ball goes out of the right/left side,
    # it should reset to the center and bounce back to the opposite direction
    def reset_position(self):
        self.goto(0, 0)
        #when the ball goes out of the right/left side,
        # it should reset to the center and bounce back to the opposite direction
        self.move_speed = 0.01
        self.bounce_X()