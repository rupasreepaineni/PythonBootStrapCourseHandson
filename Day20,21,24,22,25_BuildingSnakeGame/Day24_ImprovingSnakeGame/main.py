from turtle import Turtle, Screen
import time

from Pythondaily.Day20_BuildingSnakeGame.food import Food
from Pythondaily.Day20_BuildingSnakeGame.scoreboard import Scoreboard
from Snake import Snake

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
"""making screen to listen to user actions"""
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update() #updating screen to get the new position of the snake after moving to end
    time.sleep(0.1) # this will make the snake move slower,
    # you can adjust the sleep time to make it faster or slower
    snake.move()
    #eating the food
    if snake.head.distance(food) < 15:
        food.refresh() # this will move the food to a new random position
        snake.extend() # this will add a new segment to the snake
        scoreboard.increase_score()
    #detecting collision with wall
    if snake.head.xcor() > 370 or snake.head.xcor() < -370 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
        scoreboard.score_reset()
        game_is_on = False
        scoreboard.game_over()
    #detecting collision with tail
    #for segment in snake.segments: # here we're asking to check the collision
        #if segment == snake.head: # here we're asking to skip the head of the snake, because we don't want to check the collision of the head with itself
            #pass
        #elif snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
    #detecting collision with tail above code without segmentation
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.score_reset()
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()