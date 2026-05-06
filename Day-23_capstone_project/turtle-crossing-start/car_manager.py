import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  #car movement
MOVE_INCREMENT = 10 #w.r.t speed of cars


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):#generating a random car
        random_chance = random.randint(1, 6)
        if random_chance == 1: #to create a car only when the random chance is 1,
        # so that we don't create a car in every iteration of the while loop in the canvasandbuttonsstep1.py file
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def move_car(self): #moving the cars
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT) #here backward, movement from 300 to -300

    # the cars should increase the speed for upcoming levels
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT




