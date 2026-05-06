from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.scoreboard() #the updation requires everytime so we've defined it as separate method

    def scoreboard(self):
        self.write(f"Level:{self.level}", align="Left", font=FONT)

    def update_level(self):#increasing the level
        self.level +=1
        self.clear()
        self.scoreboard()

    def Game_over(self):
        self.goto(0, 0)  # Game over message to the middle of the screen
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))





