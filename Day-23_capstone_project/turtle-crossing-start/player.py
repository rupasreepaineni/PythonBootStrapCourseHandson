from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle") #here self refers to the object of the Player class, which is also a turtle
        # ,as we're inheriting the turtle
        # , so we can directly use the methods of turtle in the Player class
        self.color("black")
        self.setheading(90)
        self.penup()
        self.level_up()


    def up(self):
        new_Y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_Y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            #print("Sorry! you haven't reached the winning point"),
            # as the turtle is movement is continuous action better to avoid printing this statement in the console,
            # as it will print this statement in every iteration of the while loop in the canvasandbuttonsstep1.py file, which will clutter the console
            #** always best to use return statements
            return False

    def level_up(self):
        self.goto(STARTING_POSITION)






