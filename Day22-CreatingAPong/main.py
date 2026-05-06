from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # this will turn off the animation,
# so that we can control when to update the screen[visualize the changes]

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0)) #here (-350, 0) this is a tuple as an argument
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
#to avoid confusion use s- up, w-down for left paddle
screen.onkey(l_paddle.go_up, "s")
screen.onkey(l_paddle.go_down, "w")

game_is_on = True
while game_is_on:
    #time.sleep(0.1) #this will ball movement speed little slower
    #the speed of the ball should be increased each time time you hit the paddle
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall, if it hit the above wall, then it should bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_Y()

    #when hit with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_X()

    #detect if the ball goes out of the right side paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect if the ball goes out of the left side paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()
