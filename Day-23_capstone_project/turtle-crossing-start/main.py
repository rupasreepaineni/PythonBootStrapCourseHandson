import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cm = CarManager()
scoreboard = Scoreboard()

#moving the player turtle with the up key
screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #player.up() -- no need to call this function here,
    # as we are calling it in the onkey function, which will be called when the up key is pressed
    cm.create_car()
    cm.move_car()

    #detecting collision with car
    #[every object is a turtle(either car/player[here player is a turtle], so we can use any predefined functions]
    for car in cm.all_cars:
        if car.distance(player) < 20: #if the distance between the car and the player is less than 20,
            # then we consider it a collision, actually the car width is 20 pixels and the player width is 20 pixels,
            # so if the distance between them is less than 20 pixels, then they are colliding
            game_is_on = False
            scoreboard.Game_over()


    #Reaching winning point
    if player.is_at_finish_line():
        #once reaches the end,it should reach to the starting position for another level
        player.level_up()
        # it should start another level
        cm.increase_speed()
        scoreboard.update_level()











screen.exitonclick()