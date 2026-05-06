from turtle import Turtle

class Scoreboard(Turtle):

    """making score to the middle of the page"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()
    def update_scoreboard(self): #font of the score and alignment
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self): #game over message
        self.goto(0, 0) #Game over message to the middle of the screen
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))


    def increase_score(self): #increasing the score after eating the food
        self.score += 1
        self.clear() # this will clear the previous score, so that we can update the new score
        self.update_scoreboard()